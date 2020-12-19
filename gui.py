import sys
import numpy as np
import os
import datetime as dt

from PyQt5.QtWidgets import QMainWindow, QCheckBox,  QApplication, QWidget, \
QSizePolicy, QPushButton, QAction, QLineEdit, QMessageBox, QInputDialog, \
QLabel, QComboBox
from PyQt5.QtGui import *  
from PyQt5.QtCore import QSize 
from PyQt5.QtGui import QIcon

# =============================================================================
# This py file creates a gui that will take inputs from a connected BNC-2120 to
# Lock-in Amplifiers. It also automatically updates the values given to it and
# save them to a file in the same directory as this program.
# =============================================================================

def Start():
    m = GUI()
    m.show()
    return m     

class GUI(QWidget):
    '''This is the actual class that makes the GUI itself'''
    def __init__(self):
        super().__init__()
        self.title = 'Super Awesome Temperature Probe Program'
        self.left = 0
        self.top = 50
        self.width = 480
        self.height = 220
        self.button_count=0
        self.label_count=0
        self.initUI()
        
    def initUI(self):
        '''Sets up the layout of the GUI'''
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        #Quit Button
        self.button = QPushButton('Quit',self)
        self.button.move(10,10)
        self.button.clicked.connect(self.exiting)
        
        #Plot Button
        self.button = QPushButton('Plot',self)
        self.button.move(90,10)
        self.button.clicked.connect(self.start_plotting)
        
        #Samples/second Label
        label=QLabel('Samples/sec:',self)
        label.move(10,55)
        
        #Textbox for Samples/second
        self.sampsec = QLineEdit(self,text='1')
        self.sampsec.move(90,50)
        self.sampsec.resize(100,25)
        
        #Project name Label
        label=QLabel('Project Name:',self)
        label.move(10,94)
        
        #Textbox for Project name
        self.projname = QLineEdit(self)
        self.projname.move(90,90)
        self.projname.resize(100,25)
        
        #Checkbox for Temp vs Time viewer
        self.b1 = QCheckBox('Temp vs Time',self)
        self.b1.move(220,0)
        self.b1.resize(320,40)
        
        #Checkbox for Signalx vs Temp viewer
        self.b2 = QCheckBox('Signalx vs Temp',self)
        self.b2.move(220,20)
        self.b2.resize(320,40)
        
        #Checkbox for Signaly vs Temp viewer
        self.b3 = QCheckBox('Signaly vs Temp',self)
        self.b3.move(220,40)
        self.b3.resize(320,40)
        
        #Checkbox for Signaly vs Signalx viewer
        self.b4 = QCheckBox('Signaly vs Signalx',self)
        self.b4.move(220,60)
        self.b4.resize(320,40)
        
        #Dropdown list of possible resistors
        self.resistor = QComboBox(self)
        self.resistor.addItem("Platinum")
        self.resistor.addItem("RuO")
        self.resistor.addItem("Raw_Temp.")
        self.resistor.addItem("resistance")
        self.resistor.addItem("Thermocouple")
        self.resistor.move(220,95)
        
        #Comments Label
        label=QLabel('Comments:',self)
        label.move(10,134)
        
        #Textbox for Comments
        self.comment = QLineEdit(self)
        self.comment.move(90,130)
        self.comment.resize(200,25)
        
        #Voltage Sweep Label
        label=QLabel('Voltage Sweep:',self)
        label.move(10,184)
        
        #Min Voltage Sweep Label
        label=QLabel('Start',self)
        label.move(100,165)
        
        #Max Voltage Sweep Label
        label=QLabel('End',self)
        label.move(175,165)
        
        #Voltage Sweep Incriment Label
        label=QLabel('Incriments/10min',self)
        label.move(250,165)
        
        #Textbox for min voltage sweep
        self.min_volt = QLineEdit(self)
        self.min_volt.move(90,180)
        self.min_volt.resize(80,25)
        self.min_volt.setText('0')
        
        #Texbox for max voltage sweep
        self.max_volt = QLineEdit(self)
        self.max_volt.move(160,180)
        self.max_volt.resize(80,25)
        self.max_volt.setText('0')
        
        #Texbox for voltage sweep incriments
        self.inc_volt = QLineEdit(self)
        self.inc_volt.move(240,180)
        self.inc_volt.resize(80,25)
        self.inc_volt.setText('0')
        
        #Checkbox for collecting magnetic interference
        self.mag_inter = QCheckBox('Magnetic interferece',self)
        self.mag_inter.move(350,0)
        self.mag_inter.resize(320,40)
        
    def exiting(self):
        '''Used only by the quit button to exit the program "gracefully"'''
        sys.exit()
        
    def write_header_file(self):
        '''This files just stores some information specific to this run and 
        saves the file to the current directory for future reference'''
        
        directory='../{}'.format(self.projname.text())
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        if os.path.isfile('{}/header.txt'.format(directory)):
            return 
        
        f = open('{}/header.txt'.format(directory),'w')
        
        line = 'Project Name: {}\n'.format(self.projname.text())
        f.write(line)
        
        line = 'Start Date: {}\n'.format(dt.datetime.now().date())
        f.write(line)
        
        line = 'Start Time: {}\n'.format(dt.datetime.now().time())
        f.write(line)
        
        line = 'Resistor Type: {}\n'.format(self.resistor.currentText())
        f.write(line)
        
        line = 'Comments: {}\n'.format(self.comment.text())
        f.write(line)
        
        f.close()
        
    def start_plotting(self):
        '''Calls another python file that shows the automatic updates of 
        whatever values the user wants'''
        
        self.write_header_file()
        
        directory = '../{}'.format(self.projname.text())
        if not os.path.exists(directory):
            os.makedirs(directory)
            
        state1 = self.b1.isChecked()
        state2 = self.b2.isChecked()
        state3 = self.b3.isChecked()
        state4 = self.b4.isChecked()
        
        if self.mag_inter.isChecked():
            interference = 1
        else:
            interference = 0
        
        states_l = [state1,state2,state3,state4]
        commands = ['Temp','Signalx vs Temp','Signaly vs Temp',\
                    'Signaly vs Signalx']
        to_be_used_commands = []
        
        for i in range(0,len(states_l)):
            if states_l[i]:
                to_be_used_commands.append(commands[i])
                
        str_used = ' ; '.join(to_be_used_commands) 
        resist = str(self.resistor.currentText())
        
        cmd = 'python viewer.py {} {} {} {} {} {} {} {}'.format(str_used,\
                                self.projname.text(),self.sampsec.text()\
                                ,resist,self.min_volt.text(),\
                                self.max_volt.text(),self.inc_volt.text(),\
                                interference)
        print(cmd)
        os.system(cmd)  
        #This is to get around a problem when a file is first being created
        cmd = 'python viewer.py {} {} {} {} {} {} {} {}'.format(str_used,\
                                self.projname.text(),self.sampsec.text(),\
                                resist,self.min_volt.text(),\
                                self.max_volt.text(),self.inc_volt.text(),\
                                interference)
        os.system(cmd)
    
if __name__ == '__main__':
    #Stars by calling the application and initiate the start process
    app = QApplication(sys.argv)
    window = Start()
    app.exec_()
    
    
