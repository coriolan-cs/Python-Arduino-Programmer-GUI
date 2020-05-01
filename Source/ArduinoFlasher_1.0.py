# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ArduinoFlasher.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import subprocess
import os
import sys
import glob
import serial
import os.path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon

#Below definitions
node_ID_string = '#define NODE_ID'
program_path = 'Arduino-Flasher-Project/Firmware_V4/'

compiler = 'arduino-cli'
flag1_compile = 'compile'
flag2_boardname1 = '-b'
flag3_boardname2 = 'arduino:avr:uno'
flag4_program_path = 'program_path'
flag5_verbose = '-v'

flag1_upload = 'upload'
flag2_portname1 = '-p'

#testComPort = 'COM6'

def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
            #numberOfPortsFound = numberOfPortsFound + 1
        except (OSError, serial.SerialException):
            #print("ERRORS")
            pass
    return result

class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        #begining of QT-designer generated code
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(550, 590)
        MainWindow.setMinimumSize(QtCore.QSize(550, 590))
        MainWindow.setMaximumSize(QtCore.QSize(550, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.pushButton_installTool = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_installTool.setObjectName("pushButton_installTool")
        self.verticalLayout.addWidget(self.pushButton_installTool)
        spacerItem = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.toolButton_selectFile = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_selectFile.setObjectName("toolButton_selectFile")
        self.verticalLayout.addWidget(self.toolButton_selectFile)
        self.label_fileChosen = QtWidgets.QLabel(self.centralwidget)
        self.label_fileChosen.setText("")
        self.label_fileChosen.setObjectName("label_fileChosen")
        self.verticalLayout.addWidget(self.label_fileChosen)
        spacerItem1 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.spinBox_ID = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_ID.setMinimum(1)
        self.spinBox_ID.setMaximum(999)
        self.spinBox_ID.setObjectName("spinBox_ID")
        self.verticalLayout.addWidget(self.spinBox_ID)
        spacerItem2 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton_RefreshCOM = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_RefreshCOM.setObjectName("pushButton_RefreshCOM")
        self.verticalLayout.addWidget(self.pushButton_RefreshCOM)
        self.comboBox_COMPORTS = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_COMPORTS.setCurrentText("")
        self.comboBox_COMPORTS.setObjectName("comboBox_COMPORTS")
        self.verticalLayout.addWidget(self.comboBox_COMPORTS)
        spacerItem3 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.pushButton_Flash = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Flash.setObjectName("pushButton_Flash")
        self.verticalLayout.addWidget(self.pushButton_Flash)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 550, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #enf of Qt Generated layout


        #begining of my code
        self.pushButton_Flash.clicked.connect(self.FlashButtonPressed)

        self.pushButton_RefreshCOM.clicked.connect(self.refreshComPortPressed)

        self.comboBox_COMPORTS.setCurrentText("")
        self.comboBox_COMPORTS.setObjectName("comboBox_COMPORTS")

        self.refreshComPortPressed()
        
        self.toolButton_selectFile.clicked.connect(self.openFileNameDialog)

        self.pushButton_installTool.clicked.connect(self.installTool)

        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.spinBox_ID.valueChanged.connect(self.valueIDchange)

        #Check file, then define ID 1 when program starts
        if os.path.isfile(program_path + '_ID.h'):
            print ("File exist")
            with open((program_path + '_ID.h'), "w") as file1:
                file1.write(node_ID_string + ' ' + str(self.spinBox_ID.value()))
                print("#define ID ", str(self.spinBox_ID.value()))
        else:
            print ("File not exist")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 852, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Install arduino-cli
    def installTool(self):
        print("Checking if Tool is installed")
        self.updateLabel("TO PRINT NOW")
        self.textEdit.setText("Checking if Tool is installed")

        try: 
            p = Popen(["ipconfig"], stdout=PIPE, bufsize=1)
            with p.stdout:
                for line in iter(p.stdout.readline, b''):
                    print(line)
                    self.textEdit.setText(line)
            p.wait() # wait for the subprocess to exit
            
            
        except: 
            print("Not installed. Installing now")

            try:
                result = subprocess.run(['curl', '-fsSL', 'https://raw.githubusercontent.com/arduino/arduino-cli/master/install.sh', '|', 'sh'])
                #result = subprocess.run(['avrdude'], stdout=subprocess.PIPE)
                resultstring = result.stdout.decode('utf-8')
                self.textEdit.setText(resultstring)
                print(resultstring)
            except:
                print("Except")


    #Browse button    
    def openFileNameDialog(self):
        print("Opening Window")
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.rootPath() , '*.ino') #works
        if fileName:
            print(fileName)
            self.label_fileChosen.setText(fileName)


    # If change ID, write ID in file
    def valueIDchange(self):
        print("current value:"+str(self.spinBox_ID.value()))   
        #file = open(“/Firmware_V4/_ID.h”,”w”)
        cwd = os.getcwd()
        files = os.listdir(cwd)  # Get all the files in that directory
        print("Files in %r: %s" % (cwd, files))
        #file1 = open('Arduino-Flasher-Project/Firmware_V4/_ID.h', 'w')

        if os.path.isfile(program_path + '_ID.h'):
            print ("File exist")
            with open((program_path + '_ID.h'), "w") as file1:
                file1.write(node_ID_string + ' ' + str(self.spinBox_ID.value()))
                print("#define ID ", str(self.spinBox_ID.value()))
                self.textEdit.setText("Wrote in file #define ID " + str(self.spinBox_ID.value()))
        else:
            print ("File do not exist")
            self.textEdit.setText("File do not exist. Will not write ID")


    

    # Refresh com ports when hit refresh
    def refreshComPortPressed(self):
        listReturned = serial_ports()   

        if(len(listReturned) == 0):
            print("No COM port found")
            self.textEdit.setText("No COM port foud!")
        else:
            print("Found", len(listReturned), "COM ports")
            print(listReturned)
            for comPort in range(len(listReturned)):
                print(comPort+1)
                self.comboBox_COMPORTS.addItem(listReturned[comPort])
                
                #If the item is already on the list, delete it
                if self.comboBox_COMPORTS.count() > len(listReturned):
                    self.comboBox_COMPORTS.removeItem(len(listReturned))

            
    #Start compilation and flashing process
    def FlashButtonPressed(self):
        print("FLASH button pressed")

        if(len(listReturned) == 0):
            print("No COM port found")
            self.textEdit.setText("No COM port foud!")
            return
            
        self.textEdit.setText("Compiling...")
        #compiling process
        subprocess.call([compiler, flag1_compile, flag2_boardname1, flag3_boardname2, program_path, flag5_verbose])
        
        self.textEdit.setText("Compiling done. Flashing...")
        #flashign process
        subprocess.call([compiler, flag1_upload, flag2_boardname1, flag3_boardname2, flag2_portname1, self.comboBox_COMPORTS.currentText(), program_path, flag5_verbose])
        
        self.textEdit.setText("Flashing done!")


    # PyQT5 requirement
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_Flash.setText(_translate("MainWindow", "FLASH!"))
        self.label.setText(_translate("MainWindow", "COM port"))
        self.toolButton_selectFile.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "Select HEX file"))
        self.label_3.setText(_translate("MainWindow", "Target ID (1-999)"))
        self.label_4.setText(_translate("MainWindow", "ATMEGA328p ARDUINO COMPILER AND FLASHER"))
        self.label_5.setText(_translate("MainWindow", "Debug output:"))
        self.pushButton_installTool.setText(_translate("MainWindow", "Install arduino-cli Tool"))
        self.pushButton_RefreshCOM.setText(_translate("MainWindow", "Refresh COM ports"))

    

    # test function
    def updateLabel(self, textToUpdate):
        self.textEdit.setText(textToUpdate)

    #def pressed(self):
    #    print("Browse button pressed")

    

    
        



if __name__ == "__main__":
    import sys

    #check if COM ports are connected
    listReturned = serial_ports()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
