## This Application was Designed and Coded by : Abdulrahman Almajayda
## Since : 7/7/2021
## GitHub : GitHub.com/itsDaRKSAMA 

# a.almajayda : importing pyQt5 modules
from sys import path
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from functions import CaloriesCalculator as calc

# a.almajayda : importing sys and os 
import sys
import os
from os import path

# a.almajayda : declaring UI files
MAIN_CLASS,_=loadUiType(path.join(path.dirname(__file__),"main.ui"))
ABOUT_CLASS,_=loadUiType(path.join(path.dirname(__file__),"about.ui"))


# a.almajayda : Main Window Class
class MainApp(QtWidgets.QMainWindow,MAIN_CLASS):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handling_UI()
        self.Handling_Button()

    # a.almajayda : handling main window
    def Handling_UI(self):
        # a.almajayda : remove window frames
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # a.almajayda : center window on screen
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        
    # a.almajayda : handling all buttons and connect with functions
    def Handling_Button(self):
        self.calcBtn.clicked.connect(self.Handling_Calculate)
        self.clearBtn.clicked.connect(self.ClearAll)
        self.exitButton.clicked.connect(self.Handling_Exit_Button)
        self.aboutButton.clicked.connect(self.Handling_About_Button)

    # a.almajayda : handling Calculate button     
    def Handling_Calculate(self):
        activity = self.activityCombo.currentText().split()[1]
        height = self.hightInput.text()
        weight = self.weightInput.text()
        age = self.ageInput.text()
        # print(activity)
        if(height != "" and weight != "" and age != ""):
            try:
                height_m = float(height) / 100
                cal = calc()
                if(self.maleRB.isChecked()):
                    total = cal.menCalc(float(height),float(weight),float(age),activity)
                else:
                    total = cal.womenCalc(float(height),float(weight),float(age),activity)

                gain = cal.get_ToGain(total)
                lose = cal.get_ToLose(total)
                self.SetLabels(Calories=total,ToGain=gain,ToLoss=lose)
                self.SetBMILabel(height_m,float(weight))
                self.LabelMessage(message="")
            except ValueError:
                self.ClearAll()
                self.LabelMessage(message="You can only use numbers")
        else:
            self.LabelMessage(message="You must enter all fields")

    # a.almajayda : reset and clear all fields
    def ClearAll(self):
        self.hightInput.setText("")
        self.weightInput.setText("")
        self.ageInput.setText("")
        self.activityCombo.setCurrentIndex(0)
        self.femaleRB.setChecked(False)
        self.maleRB.setChecked(True)
        self.LabelMessage(message="")

    # a.almajayda : set Result labels 
    def SetLabels(self,Calories = "",ToGain = "",ToLoss = ""):
        self.resultLabel1.setText(f"Calories : {Calories}")
        self.resultLabel2.setText(f"To Gain : {ToGain}")
        self.resultLabel3.setText(f"To Lose : {ToLoss}")

    # a.almajayda : set BMI label 
    def SetBMILabel(self,height_m = 1, weight = 1):
        BMI,shape = calc.get_BMI(self,height_m,weight)
        self.resultLabel4.setText(BMI)
        if shape in ("Overweight","Mild"):self.resultLabel4.setStyleSheet("color: #F2C94C")
        elif shape in ("Moderate","ObeseI") :self.resultLabel4.setStyleSheet("color: #F6D777")
        elif shape in ("ObeseII","Severe"):self.resultLabel4.setStyleSheet("color: #EB5757")
        elif shape == "ObeseIII" : self.resultLabel4.setStyleSheet("color: #ED2C2C")
        else:self.resultLabel4.setStyleSheet("color: #27AE60")
        print(shape)

    # a.almajayda : set Errors label 
    def LabelMessage(self,message = ""):
        self.errorMessage.setText(message)
        self.errorMessage.setStyleSheet("color: #FF5656; font-weight: bold;")

    # a.almajayda : handling exit and about buttons
    def Handling_Exit_Button(self):
        self.close()

    def Handling_About_Button(self):
        # about()
        self.about_app = AboutApp()
        # self.close()
        self.about_app.show()
        


# a.almajayda : About window class
class AboutApp(QtWidgets.QMainWindow,ABOUT_CLASS):
    def __init__(self,parent=None):
        
        super(AboutApp,self).__init__(parent)
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.exitButton.clicked.connect(self.Handling_Exit_Button)
        # a.almajayda : remove window frames
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)

        # a.almajayda : center window on screen
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())


    # a.almajayda : handling exit and about buttons
    def Handling_Exit_Button(self):
        self.close()

        

        

# a.almajayda : handling Main window
def main():
    main_app = QtWidgets.QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    # main_app.exec_()
    sys.exit(main_app.exec_())

# a.almajayda : handling About window
# def about():
#     about_app = QtWidgets.QApplication(sys.argv)
#     about_window = AboutApp()
#     about_window.show()
#     # about_app.exec_()
#     sys.exit(about_app.exec_())


# a.almajayda : Start The Application
if __name__ == '__main__':
    # print(MAIN_CLASS)
    main()