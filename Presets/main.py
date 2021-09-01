from shiboken6.Shiboken import isValid
from ui import Ui_MainWindow
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QPixmap
from PIL import ImageGrab,Image
import sys
from win32api import GetSystemMetrics
import os
import json
import click

def pil2pixmap(im):
    r, g, b = im.split()
    im = Image.merge("RGB", (b, g, r))
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)
    pixmap = QtGui.QPixmap.fromImage(qim)
    return pixmap


import json


class NotAPreset(Exception):
    pass


class Preset:
    def __init__(self,name , bbox=None):
        self.name = name
        self.bbox = bbox

        if bbox:
            self.left= bbox[0]
            self.right = bbox[2]
            self.top = bbox[1]
            self.bottom = bbox[3]

    def GetResolution(self):
        return((int(self.bbox[2]-self.bbox[0]) , int(self.bbox[3]-self.bbox[1])))

    def getBBOX(self):
        if(Preset.isValidPreset(self)):
            j = dict(json.load(open("presets.json","r")))
            if(type(self) ==str):
                return j[self]
            else:
                self.bbox = j[self.name]
                self.UpdateBBOX()
                return j[self.name]

        else:
            raise NotAPreset(f"{self} is not a valid preset.")
        

    def UpdateBBOX(self):
        if self.bbox:
            self.left= self.bbox[0]
            self.right = self.bbox[2]
            self.top = self.bbox[1]
            self.bottom = self.bbox[3]

    @staticmethod
    def PresetInstance(preset_name:str):
        p = Preset(name=preset_name)
        p.getBBOX()
        return p

    @staticmethod
    def isValidPreset(preset_name):
        j = dict(json.load(open("presets.json","r")))

        if(type(preset_name)==str and preset_name in j.keys()):
            return True
        elif(type(preset_name)==Preset and preset_name.name in j.keys()):
            return True
        else:
            return False
    
    @staticmethod
    def GetPresets():
        j = dict(json.load(open("presets.json","r")))
        return list(j.keys())
        
class Preset_Window(QtWidgets.QMainWindow):
    def __init__(self,*args,**kwargs):
        temp = kwargs.copy()
        temp.pop("preset_name")
        super().__init__(*args,**temp)

        self.preset_name = kwargs["preset_name"]
        self.pre = Preset.PresetInstance(self.preset_name)
        preset_reference = {"P1" : "Preset 1" , "P2" :"Preset 2" , "P3" : "Preset 3"}

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self ,preset_reference.get(self.preset_name))
        self.setWindowIcon(QtGui.QIcon('static/resize.ico'))

        self.right = self.pre.right
        self.bottom = self.pre.bottom
        self.top = self.pre.top
        self.left = self.pre.left
        self.bbox = [self.left,self.top,self.right,self.bottom]

        self.ScreenshotRefresh()

        self.ui.Refresh.clicked.connect(self.ScreenshotRefresh)
        self.ui.Reset.clicked.connect(self.ResetPreview)
        self.ui.Screen_Preview.setAlignment(QtCore.Qt.AlignCenter)

        #Set Up Sliders
        self.ui.Ax_Slider.setMaximum(GetSystemMetrics(0))
        self.ui.Ax_Slider.setMinimum(0)
        self.ui.Ax_Slider.setSingleStep(1)
        self.ui.Ax_Slider.setValue(self.left)
        self.ui.Ax_Slider.valueChanged.connect(self.SliderRefresh)

        self.ui.Ay_Slider.setMaximum(GetSystemMetrics(1))
        self.ui.Ay_Slider.setMinimum(0)
        self.ui.Ay_Slider.setSingleStep(1)
        self.ui.Ay_Slider.setValue(self.bottom)
        self.ui.Ay_Slider.valueChanged.connect(self.SliderRefresh)

        self.ui.Bx_Slider.setMaximum(GetSystemMetrics(0))
        self.ui.Bx_Slider.setSingleStep(1)
        self.ui.Bx_Slider.setMinimum(0)
        self.ui.Bx_Slider.setValue(self.right)
        self.ui.Bx_Slider.valueChanged.connect(self.SliderRefresh)

        self.ui.By_Slider.setMaximum(GetSystemMetrics(1))
        self.ui.By_Slider.setMinimum(0)
        self.ui.By_Slider.setSingleStep(1)
        self.ui.By_Slider.setValue(0)
        self.ui.By_Slider.setValue(self.top)
        self.ui.By_Slider.valueChanged.connect(self.SliderRefresh)

    def SliderRefresh(self):
        self.ui.Ax_Slider.setMaximum(self.ui.Bx_Slider.value()-10)
        self.ui.Bx_Slider.setMinimum(self.ui.Ax_Slider.value()+10)
        self.ui.Ay_Slider.setMinimum(self.ui.By_Slider.value()+10)
        self.ui.By_Slider.setMaximum(self.ui.Ay_Slider.value()-10)

        self.left = self.ui.Ax_Slider.value()
        self.bottom = self.ui.Ay_Slider.value()
        self.right = self.ui.Bx_Slider.value()
        self.top = self.ui.By_Slider.value()
        self.bbox = [self.left,self.top,self.right,self.bottom]
        self.CropRefresh()

    def ResetPreview(self):
        self.right = GetSystemMetrics(0)
        self.bottom = GetSystemMetrics(1)
        self.top = 0
        self.left = 0
        self.ui.Ay_Slider.setValue(self.bottom)
        self.ui.Ax_Slider.setValue(0)
        self.ui.Bx_Slider.setValue(self.right)
        self.ui.By_Slider.setValue(0)
        self.bbox = [self.left,self.top,self.right,self.bottom]

    
    def CropRefresh(self):
        im = self.ss.crop((self.left,self.top,self.right,self.bottom))
        self.ui.Screen_Preview.setPixmap(pil2pixmap(im).scaled(self.ui.Screen_Preview.size() , QtCore.Qt.KeepAspectRatio , QtCore.Qt.SmoothTransformation))

    def ScreenshotRefresh(self):    
        self.ss = ImageGrab.grab()
        self.CropRefresh()

class InvalidPreset(Exception):
    pass

@click.command()
@click.option('--preset_name', '-P')
def SetPreset(preset_name:str,):
    if(Preset.isValidPreset(preset_name)):
    
        if not QtWidgets.QApplication.instance():
            app = QtWidgets.QApplication(sys.argv)
        else:
            app = QtWidgets.QApplication.instance()

        app.setStyle("Fusion")
        ui = Preset_Window(preset_name=preset_name)
        ui.show()
        app.exec()
        j = json.load(open("presets.json" ,"r"))
        j[preset_name] = ui.bbox
        json.dump( j,open("presets.json" , "w"))
    else:
        raise InvalidPreset(f"'{preset_name}' is not a valid preset.")
SetPreset()