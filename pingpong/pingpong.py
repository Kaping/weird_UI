# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pingpong.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import sys
from time import sleep
import random

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(335, 366)
        Widget.setStyleSheet("background-color: rgb(68, 68, 68);\n"
"\n"
"\n"
"")
        self.horizontalSlider = QtWidgets.QSlider(Widget)
        self.horizontalSlider.setGeometry(QtCore.QRect(10, 270, 311, 22))
        self.horizontalSlider.setStyleSheet("\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: rgb(120, 255, 140);\n"
"    border: 3px solid #4fff6c;\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalSlider = QtWidgets.QSlider(Widget)
        self.verticalSlider.setGeometry(QtCore.QRect(20, 190, 8, 160))
        self.verticalSlider.setStyleSheet("QSlider::groove:vertical {\n"
"    background: white;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 50px;\n"
"    background: rgb(120, 255, 140);\n"
"    color: rgb(120, 255, 140);\n"
"    color: rgb(120, 255, 140);\n"
"\n"
"}")
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.lcdNumber = QtWidgets.QLCDNumber(Widget)
        self.lcdNumber.setGeometry(QtCore.QRect(180, 30, 111, 41))
        self.lcdNumber.setStyleSheet("background-color: rgb(98, 98, 98);\n"
"color: rgb(85, 255, 0);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton = QtWidgets.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(40, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color: rgb(98, 98, 98);\n"
"    color: #78ff8c;\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-color: beige;\n"
"}\n"
"QToolButton:pressed {\n"
"       background-color: rgb(76, 76, 76);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalSlider_2 = QtWidgets.QSlider(Widget)
        self.verticalSlider_2.setGeometry(QtCore.QRect(300, 190, 8, 160))

        self.verticalSlider_2.setStyleSheet("QSlider::groove:vertical {\n"
"    background: white;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 50px;\n"
"    background: rgb(120, 255, 140);\n"
"    color: rgb(120, 255, 140);\n"
"    color: rgb(120, 255, 140);\n"
"\n"
"}")
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.lcdNumber.raise_()
        self.pushButton.raise_()
        self.horizontalSlider.raise_()
        self.verticalSlider.raise_()
        self.verticalSlider_2.raise_()


        self.val = val
        self.n = n
        self.m = m
        self.height = height
        self.isplaying = isplaying
        


        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.pushButton.setText(_translate("Widget", "START"))




class MainWindow(QtWidgets.QMainWindow, Ui_Widget):
        def __init__(self, *args, obj=None, **kwargs):
                super(MainWindow, self).__init__(*args, **kwargs)
                self.setupUi(self)
                self.pushButton.clicked.connect(self.the_button_was_pressed)

                self.timer = QTimer()
                self.segtimer = QTimer()
                self.timer.setInterval(16) # 약 60프레임
                self.segtimer.setInterval(1000)
                self.timer.timeout.connect(self.timerEvent)
                self.verticalSlider.valueChanged.connect(self.the_slider_changed)
                self.segtimer.timeout.connect(self.segtime)
                self.t = 0
                self.my_position = 0
                self.ai_position = 0
                

        def the_button_was_pressed(self):
                
                if self.timer.isActive():
                        self.timer.stop()
                        self.segtimer.stop()
                        self.pushButton.setText('START')
                        
                else:
                        self.t = 0
                        self.lcdNumber.display(self.t)
                        self.timer.start()
                        self.segtimer.start()
                        self.pushButton.setText('STOP')

        def the_slider_changed(self): #100 ~ 0 to 190 ~ 340
                self.my_position = 340 -self.verticalSlider.value()* 1.5
                

        def segtime(self):
                self.t+=1
                self.lcdNumber.display(self.t)


        def timerEvent(self):
                
                if self.n == 1 and self.val <= 5 and self.val >= 2 and self.my_position + 40 >= self.height and self.my_position - 40 <= self.height:
                        self.n = 0
                
                if self.n == 0:
                        if self.val >= 94:
                                self.n = 1
                        else:
                                self.val += 2

                elif self.n == 1:
                        if self.val <= 0:
                                self.timer.stop()
                                self.segtimer.stop()
                                self.n = 0
                                self.pushButton.setText('START')
                        
                        else:
                                self.val -= 2

                if self.m == 0:
                        if self.height >= 340:
                                self.m = 1
                        else:
                                self.height += 4

                elif self.m == 1:
                        if self.height <= 190:
                                self.m = 0
                        else:
                                self.height -= 4

                self.ai_position = 320 - self.height
                self.verticalSlider_2.setValue(self.ai_position)
                self.horizontalSlider.setValue(self.val)
                self.horizontalSlider.setGeometry(QtCore.QRect(10, self.height, 311, 22))

                
                                
            
app = QtWidgets.QApplication(sys.argv)
val = 0
n = 0
m = 0
height = 270
isplaying = False


w = MainWindow()
w.show()

app.exec()