from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import au_coordinates

class UI_MainWindow(QtWidgets.QWidget):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(600,500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("\n"
            "background:url(resources/images/background2.png);\n"
            "color:white;\n"
            "")

        # image label
        self.img_label1 = QtWidgets.QLabel(self.centralwidget)
        self.img_label1.setGeometry(QtCore.QRect(15,15,100,100))
        self.img_label1.setText("")
        self.img_label1.setPixmap(QtGui.QPixmap("resources/images/ceg_logo_bw.jpg"))
        self.img_label1.setScaledContents(True)
        self.img_label1.setObjectName("img_label1")

        # image label
        self.img_label2 = QtWidgets.QLabel(self.centralwidget)
        self.img_label2.setGeometry(QtCore.QRect(480,15,100,100))
        self.img_label2.setText("")
        self.img_label2.setPixmap(QtGui.QPixmap("resources/images/rceg.jpeg"))
        self.img_label2.setScaledContents(True)
        self.img_label2.setObjectName("img_label2")

        # label1 properties
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(155, 15, 280, 50))
        font = QtGui.QFont("Libeartion serif",11)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(
            "background:rgba(200,200,200,20);\n"
            "border-radius : 5px;\n"
            "")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")

        # label 2 properties
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(205, 70, 200, 30))
        font = QtGui.QFont("Times New Roman",11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("text-align:center;\n"
            "background:rbg(0,0,0,180);\n"
            "border-radius : 10px;\n"
            "")
        self.label_2.setObjectName("label_2")

        # label 3 properties
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 150, 200, 30))
        font = QtGui.QFont("Sans-serif",12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("text-align:center;\n"
            "background:rbg(0,0,0,180);\n"
            "border-radius : 10px;\n"
            "")
        self.label_3.setObjectName("label_3")

        # label 4 properties
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 250, 200, 30))
        font = QtGui.QFont("Sans-serif",12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("text-align:center;\n"
            "background:rbg(0,0,0,180);\n"
            "border-radius : 10px;\n"
            "")
        self.label_4.setObjectName("label_4")

        # run button properties       
        self.centralwidget.setObjectName("centralwidget")
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(400, 400, 70, 35))
        font = QtGui.QFont('Sans-serif', 12)
        self.runButton.setFont(font)
        self.runButton.setStyleSheet(
            "QPushButton:hover{\n"
            "background:rgb(15,15,15);\n"
            "\n"
            "}")
        self.runButton.setObjectName("runButton")

        # eStop button properties       
        self.centralwidget.setObjectName("centralwidget")
        self.eStopButton = QtWidgets.QPushButton(self.centralwidget)
        self.eStopButton.setGeometry(QtCore.QRect(110, 400, 70, 35))
        font = QtGui.QFont('Sans-serif', 12)
        self.eStopButton.setFont(font)
        self.eStopButton.setStyleSheet(
            "QPushButton:hover{\n"
            "background:rgb(15,15,15);\n"
            "\n"
            "}")
        self.eStopButton.setObjectName("eStopButton")

        # Drop Down menu for pickup
        self.centralwidget.setObjectName("centralwidget")
        self.pickUp_dropdown = QtWidgets.QComboBox(self.centralwidget)
        self.pickUp_dropdown.setGeometry(QtCore.QRect(210,150,340,30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pickUp_dropdown.setFont(font)
        self.pickUp_dropdown.setStyleSheet(
            "QComboBox::editable"
            "{"
            "background: rgba(255,255,255,100)"
            "}\n"
            "QComboBox"
            "{"
            "combobox-popup:0;\n"
            "color:rgba(0,0,0,20);\n"
            "selection-background-color: lightgrey;\n"
            
            "}\n"

        )
        self.pickUp_dropdown.setObjectName("pickUp_dropdown")
        
        self.pickUp_dropdown.addItem("")
        self.pickUp_dropdown.addItem("")
        self.pickUp_dropdown.addItem("")
        self.pickUp_dropdown.addItem("")
        self.pickUp_dropdown.addItem("")
        self.pickUp_dropdown.addItem("")
        self.pickUp_dropdown.addItem("")
        self.pickUp_dropdown.addItem("")
        self.pickUp_dropdown.addItem("")
        self.pickUp_dropdown.addItem("")
        self.pickUp_dropdown.addItem("")
        self.pickUp_dropdown.addItem("")
        self.pickUp_dropdown.addItem("")
        self.pickUp_dropdown.addItem("")
        self.pickUp_dropdown.addItem("")
        self.pickUp_dropdown.addItem("")
        self.pickUp_dropdown.addItem("")
        self.pickUp_dropdown.addItem("")
        self.pickUp_dropdown.addItem("")
        self.pickUp_dropdown.addItem("")
    
        # Drop Down menu for drop
        self.centralwidget.setObjectName("centralwidget")
        self.drop_dropdown = QtWidgets.QComboBox(self.centralwidget)
        self.drop_dropdown.setGeometry(QtCore.QRect(210,250,340,30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.drop_dropdown.setFont(font)
        self.drop_dropdown.setStyleSheet(
            "QComboBox::editable"
            "{"
            "background: rgba(255,255,255,100)"
            "}\n"
            "QComboBox"
            "{"
            "combobox-popup:0;\n"
            "color:rgba(0,0,0,20);\n"
            "selection-background-color: lightgrey;\n"
            "}\n"

        )
        self.drop_dropdown.setObjectName("drop_dropdown")
        
        self.drop_dropdown.addItem("")
        self.drop_dropdown.addItem("")
        self.drop_dropdown.addItem("")
        self.drop_dropdown.addItem("")
        self.drop_dropdown.addItem("")
        self.drop_dropdown.addItem("")
        self.drop_dropdown.addItem("")
        self.drop_dropdown.addItem("")
        self.drop_dropdown.addItem("")
        self.drop_dropdown.addItem("")
        self.drop_dropdown.addItem("")
        self.drop_dropdown.addItem("")
        self.drop_dropdown.addItem("")
        self.drop_dropdown.addItem("")
        self.drop_dropdown.addItem("")
        self.drop_dropdown.addItem("")
        self.drop_dropdown.addItem("")
        self.drop_dropdown.addItem("")
        self.drop_dropdown.addItem("")
        self.drop_dropdown.addItem("")


        ### Main Window
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Window"))
        self.label_1.setText(_translate("MainWindow", "College of Engineering Guindy\nAnna University"))
        self.label_2.setText(_translate("MainWindow", "ROBOTICS CLUB OF CEG"))
        self.label_3.setText(_translate("MainWindow", "Pick Up From     : "))
        self.label_4.setText(_translate("MainWindow", "Deliver At          : "))
    
        self.pickUp_dropdown.setItemText(0,_translate("MainWindow", "~select"))
        for i in range(1,20):
            self.pickUp_dropdown.setItemText(i,_translate("MainWindow", au_coordinates.impCoordinates[i-1]['name']))

        self.drop_dropdown.setItemText(0,_translate("MainWindow", "~select"))
        for i in range(1,20):
            self.drop_dropdown.setItemText(i,_translate("MainWindow", au_coordinates.impCoordinates[i-1]['name']))

        self.runButton.setText(_translate("MainWindow", "Fly"))
        self.runButton.clicked.connect(self.run_ros)
        self.eStopButton.setText(_translate("MainWindow", "E-Stop"))
        self.eStopButton.clicked.connect(self.stop_ros)
    
    def stop_ros(self):
        os.system('^Z')
        
    def run_ros(self):
        # store the corrdinates
        pickUp_loc = self.pickUp_dropdown.currentText()
        drop_loc = self.drop_dropdown.currentText()
        print(pickUp_loc)
        print(drop_loc)

        for ind in range(0,19):
            if(au_coordinates.impCoordinates[ind]['name'] == pickUp_loc):
                pickUp_lat = au_coordinates.impCoordinates[ind]['lat']
                pickUp_long = au_coordinates.impCoordinates[ind]['long']
            if(au_coordinates.impCoordinates[ind]['name'] == drop_loc):
                drop_lat = au_coordinates.impCoordinates[ind]['lat']
                drop_long = au_coordinates.impCoordinates[ind]['long']

        with open('location.txt','w') as fwrite:
            fwrite.write(str(pickUp_lat)+'\n')
            fwrite.write(str(pickUp_long)+'\n')
            fwrite.write(str(drop_lat)+'\n')
            fwrite.write(str(drop_long)+'\n')
        fwrite.close()
        """
        with open('location.txt','r') as fread:
        temp = fread.readline()
        pick_up_lat = float(temp[:len(temp)-1])
        temp = fread.readline()
        pick_up_long = float(temp[:len(temp)-1])
        temp = fread.readline()
        drop_lat = float(temp[:len(temp)-1])
        temp = fread.readline()
        drop_long = float(temp[:len(temp)-1])
        """

        os.system("python3 off_board_global.py")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UI_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
