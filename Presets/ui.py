# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preset_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow , preset_name):
        MainWindow.setObjectName(preset_name)
        MainWindow.setFixedSize(736, 468)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Screen_Preview = QtWidgets.QLabel(self.centralwidget)
        self.Screen_Preview.setGeometry(QtCore.QRect(20, 30, 691, 341))
        self.Screen_Preview.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Screen_Preview.setText("")
        self.Screen_Preview.setScaledContents(False)
        self.Screen_Preview.setObjectName("Screen_Preview")
        self.A_Label = QtWidgets.QLabel(self.centralwidget)
        self.A_Label.setGeometry(QtCore.QRect(10, 370, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(16)
        self.A_Label.setFont(font)
        self.A_Label.setTextFormat(QtCore.Qt.PlainText)
        self.A_Label.setObjectName("A_Label")
        self.B_Label = QtWidgets.QLabel(self.centralwidget)
        self.B_Label.setGeometry(QtCore.QRect(710, 0, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(16)
        self.B_Label.setFont(font)
        self.B_Label.setObjectName("B_Label")
        self.Ax_Label = QtWidgets.QLabel(self.centralwidget)
        self.Ax_Label.setGeometry(QtCore.QRect(55, 380, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(16)
        self.Ax_Label.setFont(font)
        self.Ax_Label.setTextFormat(QtCore.Qt.MarkdownText)
        self.Ax_Label.setObjectName("Ax_Label")
        self.Bx_Label = QtWidgets.QLabel(self.centralwidget)
        self.Bx_Label.setGeometry(QtCore.QRect(245, 380, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(16)
        self.Bx_Label.setFont(font)
        self.Bx_Label.setTextFormat(QtCore.Qt.MarkdownText)
        self.Bx_Label.setObjectName("Bx_Label")
        self.Refresh = QtWidgets.QPushButton(self.centralwidget)
        self.Refresh.setGeometry(QtCore.QRect(620, 390, 75, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(10)
        self.Refresh.setFont(font)
        self.Refresh.setObjectName("Refresh")
        self.Ay_Label = QtWidgets.QLabel(self.centralwidget)
        self.Ay_Label.setGeometry(QtCore.QRect(50, 420, 31, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(16)
        self.Ay_Label.setFont(font)
        self.Ay_Label.setTextFormat(QtCore.Qt.MarkdownText)
        self.Ay_Label.setObjectName("Ay_Label")
        self.By_Label_ = QtWidgets.QLabel(self.centralwidget)
        self.By_Label_.setGeometry(QtCore.QRect(245, 420, 21, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(16)
        self.By_Label_.setFont(font)
        self.By_Label_.setTextFormat(QtCore.Qt.MarkdownText)
        self.By_Label_.setObjectName("By_Label_")
        self.Ax_Slider = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Ax_Slider.setGeometry(QtCore.QRect(90, 390, 121, 22))
        self.Ax_Slider.setObjectName("Ax_Slider")
        self.Ay_Slider = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Ay_Slider.setGeometry(QtCore.QRect(90, 430, 121, 22))
        self.Ay_Slider.setObjectName("Ay_Slider")
        self.Bx_Slider = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Bx_Slider.setGeometry(QtCore.QRect(280, 390, 121, 22))
        self.Bx_Slider.setObjectName("Bx_Slider")
        self.By_Slider = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.By_Slider.setGeometry(QtCore.QRect(280, 430, 121, 22))
        self.By_Slider.setObjectName("By_Slider")
        self.Reset = QtWidgets.QPushButton(self.centralwidget)
        self.Reset.setGeometry(QtCore.QRect(540, 390, 75, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(10)
        self.Reset.setFont(font)
        self.Reset.setObjectName("Reset")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow , preset_name)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow , preset_name):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(preset_name, preset_name))
        self.A_Label.setText(_translate("MainWindow", "A"))
        self.B_Label.setText(_translate("MainWindow", "B"))
        self.Ax_Label.setText(_translate("MainWindow", "A<sub>x</sub>"))
        self.Bx_Label.setText(_translate("MainWindow", "B<sub>x</sub>"))
        self.Refresh.setText(_translate("MainWindow", "Refresh"))
        self.Ay_Label.setText(_translate("MainWindow", "A<sub>y</sub>"))
        self.By_Label_.setText(_translate("MainWindow", "B<sub>y</sub>"))
        self.Reset.setText(_translate("MainWindow", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())