from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QMessageBox,QAction
from oauth_server import Authorize
import sys
from threading import Thread
from dc_bot import client
import os
from util import *
from config import *
import patoolib


class CaptureTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self,icon,parent=None):
        super().__init__(icon,parent)
        self.setToolTip("Capture")
        menu = QtWidgets.QMenu(parent)

        OAuth_option = menu.addAction(QtGui.QIcon("static/oauth.ico"), "OAuth2")
        Exit_option = menu.addAction(QtGui.QIcon("static/exit.ico"),"Exit")        

        self.setContextMenu(menu)

        OAuth_option.triggered.connect(lambda: Authorize())
        Exit_option.triggered.connect(sys.exit)




if __name__ == "__main__":
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

    app = QtWidgets.QApplication(sys.argv)
    parent = QtWidgets.QWidget()
    icon = QtGui.QIcon("static/ci.ico")
    tray = CaptureTrayIcon(icon,parent)
    tray.show()

    bot_thread = Thread(target=client.run , args=(BOT_SECRET,) , daemon=True)
    bot_thread.start()

    sys.exit(app.exec_())   