# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Thermonics3.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLineEdit
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from PyQt5.QtWidgets import QWidget
import PyQt5
import pyvisa
import visa
import time
import sys
import PyQt5
from apscheduler.schedulers.qt import QtScheduler 
from datetime import datetime
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)



class Ui_Read_Window(object):
    def setupUi(self, Read_Window):
        Read_Window.setObjectName("Read_Window")
        Read_Window.resize(334, 226)
        font = QtGui.QFont()
        font.setPointSize(13)
        Read_Window.setFont(font)
        Read_Window.setStyleSheet("background-color: rgb(42, 42, 42);")
        Read_Window.setDocumentMode(False)
        Read_Window.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(Read_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(6, 29, 321, 181))
        self.frame.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(11, 10, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setFrameShape(QtWidgets.QFrame.HLine)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setObjectName("label")
        
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(0)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(5, 5, 101, 80))
        self.groupBox.setMaximumSize(QtCore.QSize(101, 80))
        self.groupBox.setStyleSheet("")
        self.groupBox.setTitle("")
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.AIR_READ = QtWidgets.QLabel(self.groupBox)
        self.AIR_READ.setGeometry(QtCore.QRect(9, 40, 81, 32))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.AIR_READ.setFont(font)
        self.AIR_READ.setStyleSheet("background-color: rgb(45, 45, 45);\n"
"color: rgb(255, 255, 255);")
        self.AIR_READ.setFrameShape(QtWidgets.QFrame.Panel)
        self.AIR_READ.setFrameShadow(QtWidgets.QFrame.Plain)
        self.AIR_READ.setLineWidth(0)
        self.AIR_READ.setText("")
        self.AIR_READ.setWordWrap(True)
        self.AIR_READ.setIndent(5)
        self.AIR_READ.setObjectName("AIR_READ")
        self.AIR_READ.setAlignment(Qt.AlignRight)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 3, 78, 32))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_3.setEnabled(False)
        self.groupBox_3.setGeometry(QtCore.QRect(110, 5, 101, 80))
        self.groupBox_3.setMaximumSize(QtCore.QSize(101, 80))
        self.groupBox_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.DUT_READ = QtWidgets.QLabel(self.groupBox_3)
        self.DUT_READ.setGeometry(QtCore.QRect(9, 40, 81, 32))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.DUT_READ.setFont(font)
        self.DUT_READ.setStyleSheet("background-color: rgb(45, 45, 45);\n"
"color: rgb(255, 255, 255);")
        self.DUT_READ.setFrameShape(QtWidgets.QFrame.Panel)
        self.DUT_READ.setFrameShadow(QtWidgets.QFrame.Plain)
        self.DUT_READ.setLineWidth(0)
        self.DUT_READ.setText("")
        self.DUT_READ.setWordWrap(True)
        self.DUT_READ.setIndent(5)
        self.DUT_READ.setObjectName("DUT_READ")
        self.DUT_READ.setAlignment(Qt.AlignRight)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(9, 3, 91, 32))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(215, 5, 101, 80))
        self.groupBox_2.setMaximumSize(QtCore.QSize(101, 80))
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.SP_READ = QtWidgets.QLabel(self.groupBox_2)
        self.SP_READ.setGeometry(QtCore.QRect(9, 40, 81, 32))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.SP_READ.setFont(font)
        self.SP_READ.setStyleSheet("background-color: rgb(45, 45, 45);\n"
"color: rgb(255, 255, 255);")
        self.SP_READ.setFrameShape(QtWidgets.QFrame.Panel)
        self.SP_READ.setFrameShadow(QtWidgets.QFrame.Plain)
        self.SP_READ.setLineWidth(0)
        self.SP_READ.setText("")
        self.SP_READ.setWordWrap(True)
        self.SP_READ.setIndent(5)
        self.SP_READ.setObjectName("SP_READ")
        self.SP_READ.setAlignment(Qt.AlignRight)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(12, 3, 78, 32))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(13)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBox.setGeometry(QtCore.QRect(120, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(60, 60, 60);\n"
"gridline-color: rgb(43, 43, 43);\n"
"alternate-background-color: rgb(60, 60, 60);\n"
"background-color: rgb(61, 61, 61);")
        self.doubleSpinBox.setWrapping(False)
        self.doubleSpinBox.setReadOnly(False)
        self.doubleSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMinimum(-75.0)
        self.doubleSpinBox.setMaximum(225.0)
        self.doubleSpinBox.setProperty("value", 0.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.SET_B = QtWidgets.QPushButton(self.frame)
        self.SET_B.setGeometry(QtCore.QRect(124, 130, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.SET_B.setFont(font)
        self.SET_B.setStyleSheet("background-color: rgb(150, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.SET_B.setObjectName("SET_B")
        self.EXIT_B = QtWidgets.QPushButton(self.centralwidget)
        self.EXIT_B.setGeometry(QtCore.QRect(282, 8, 41, 23))
        font = QtGui.QFont()
        font.setFamily("Dubai Medium")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.EXIT_B.setFont(font)
        self.EXIT_B.setStyleSheet("background-color: rgb(150, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.EXIT_B.setObjectName("EXIT_B")
        Read_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Read_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 334, 21))
        self.menubar.setObjectName("menubar")
        Read_Window.setMenuBar(self.menubar)

        self.retranslateUi(Read_Window)
        QtCore.QMetaObject.connectSlotsByName(Read_Window)

    def retranslateUi(self, Read_Window):
        _translate = QtCore.QCoreApplication.translate
        Read_Window.setWindowTitle(_translate("Read_Window", "Temperature Controller"))
        self.label_2.setText(_translate("Read_Window", "AIR Temp"))
        self.label_6.setText(_translate("Read_Window", "DUT Temp"))
        self.label_3.setText(_translate("Read_Window", "Set Point"))
        self.SET_B.setText(_translate("Read_Window", "SET"))
        self.EXIT_B.setText(_translate("Read_Window", "Exit"))
        self.label.setText(_translate("Read_Window", "Temperature Controller - Airjet XE"))
        

        scheduler = QtScheduler()
        global Stvjob, rm, instruments, airjet, Set_Temp, Nozzle_Temp, DUT_Temp
        Stvjob = scheduler.add_job(self.SETSP, 'interval', seconds=0.5)
        scheduler.start()
    
        self.SET_B.clicked.connect(self.SET_TEMP)
        self.EXIT_B.clicked.connect(self.CLOSE_JOB)

    def CLOSE_JOB(self):
        Stvjob.remove()
        time.sleep(1)
        Read_Window.close()
        
    def SET_TEMP(self):
        global setpoint_press, NEW
        
        rm = pyvisa.ResourceManager()
        instruments = rm.list_resources()
        airjet = rm.open_resource('GPIB1::15::INSTR')
        SP_VAL =  self.doubleSpinBox.text()
        self.SP_READ.setText(SP_VAL+' '+'°C')
        self.SP_READ.setStyleSheet("background-color: rgb(170, 235, 49);\n"
"color: rgb(255, 0, 0 );")
        NEW2 = self.SP_READ.text()
        A = 'SP'
        NEW = A+SP_VAL
        print (NEW)
        airjet.write(NEW)
        

        
    def SETSP(self):
        global setpoint_press, NEW
        
        rm = pyvisa.ResourceManager()
        instruments = rm.list_resources
        airjet = rm.open_resource('GPIB1::15::INSTR')
        Set_Temp = airjet.query('?SP')
        Nozzle_Temp = airjet.query('?TA')
        DUT_Temp = airjet.query('?TD')
        self.AIR_READ.setText(str(Nozzle_Temp)+'°C')
        self.AIR_READ.setStyleSheet("background-color: rgb(170, 235, 49);\n"
"color: rgb(0, 0,0 );")        
        self.DUT_READ.setText(str(DUT_Temp)+'°C')
        self.DUT_READ.setStyleSheet("background-color: rgb(170, 235, 49);\n"
"color: rgb(0, 0,0 );")
        SP_VAL =  self.doubleSpinBox.text()
        self.SP_READ.setText(SP_VAL+'°C')
        self.SP_READ.setStyleSheet("background-color: rgb(170, 235, 49);\n"
"color: rgb(0, 0,0 );")
        NEW2 = self.SP_READ.text()
        A = 'SP'
        NEW = A+NEW2
        #airjet.write(NEW)
        self.SP_READ.setText(str(Set_Temp+'°C'))
        #print ('Set Point = ' + Set_Temp)
        #print ('Air Temperature = ' + Nozzle_Temp)
        #print ('DUT Temp =' + DUT_Temp)
        #print ('1')
        #print (Stvjob)
        #self.AIR_READ.setText('1')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Read_Window = QtWidgets.QMainWindow()
    ui = Ui_Read_Window()
    ui.setupUi(Read_Window)
    Read_Window.show()
    sys.exit(app.exec_())
    Stvjob.remove()
