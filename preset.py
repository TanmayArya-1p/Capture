from util import *
import json


class NotAPreset(Exception):
    pass


class Preset(AutoRepr):
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

    def getBBOX(preset):
        if(Preset.isValidPreset(preset)):
            j = dict(json.load(open("presets.json","r")))
            if(type(preset) ==str):
                return j[preset]
            else:
                preset.bbox = j[preset.name]
                preset.UpdateBBOX()
                return j[preset.name]

        else:
            raise NotAPreset(f"{preset} is not a valid preset.")
        

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
        
