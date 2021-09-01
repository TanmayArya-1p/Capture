from PySide6 import QtCore, QtGui, QtWidgets 
from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QAction
from oauth_server import Authorize
import sys
from threading import Thread
from dc_bot import client
import os
from util import *
from config import *
import patoolib
import json
from win32api import GetSystemMetrics

class CaptureTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self,icon,parent=None,app=None):
        super().__init__(icon,parent)
        self.setToolTip("Capture")
        menu = QtWidgets.QMenu(parent)

        OAuth_option = menu.addAction(QtGui.QIcon("static/oauth.ico"), "OAuth2")
        Exit_option = menu.addAction(QtGui.QIcon("static/exit.ico"),"Exit")      

        menu.addSection("Set Presets:")
        preset_1 = menu.addAction(QtGui.QIcon("static/resize.ico"),"Preset 1")     
        preset_2 = menu.addAction(QtGui.QIcon("static/resize.ico"),"Preset 2")    
        preset_3 = menu.addAction(QtGui.QIcon("static/resize.ico"),"Preset 3")
        preset_1.triggered.connect(lambda: os.system("presets.exe -P P1"))
        preset_2.triggered.connect(lambda: os.system("presets.exe -P P2"))
        preset_3.triggered.connect(lambda: os.system("presets.exe -P P3"))
        
        self.setContextMenu(menu)

        OAuth_option.triggered.connect(lambda: Authorize())
        Exit_option.triggered.connect(sys.exit)




if __name__ == "__main__":
    j = json.load(open("presets.json" ,"r"))
    j["D"] = [0, 0, GetSystemMetrics(0), GetSystemMetrics(1)]
    json.dump( j,open("presets.json" , "w"))

    if(not "ffmpeg.exe" in os.listdir()):
        patoolib.extract_archive("ffmpeg.rar", outdir=os.getcwd())
        os.remove("ffmpeg.rar")
    else:
        print("ffmpeg.exe already exists in cwd.")
    try:
        os.remove("write.mp4")
        os.remove("video.mkv")
    except:
        pass
        
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    app.setStyle("Fusion")
    parent = QtWidgets.QWidget()
    icon = QtGui.QIcon("static/ci.ico")
    tray = CaptureTrayIcon(icon,parent,app)
    tray.show()

    bot_thread = Thread(target=client.run , args=(BOT_SECRET,) , daemon=True)
    bot_thread.start()

    sys.exit(app.exec())