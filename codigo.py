import random
import sys
from tkinter import CENTER
from unicodedata import name
import requests
from PyQt5 import uic, QtGui ,QtCore
from PyQt5.QtCore import QDate, QTime, Qt, QTimer, QEvent
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QCheckBox, QListWidget, QPushButton, QWidget,
                             QHBoxLayout, QApplication, QVBoxLayout, QMessageBox)

bloqueo = 0 
class ejemplo_GUI(QMainWindow):
 
    def __init__(self):
        
        super().__init__()
        uic.loadUi("gui_app.ui",self)
        self.setWindowTitle("Postulante para ROBOTILSA S.A")
        self.boton.clicked.connect(self.fn_activar)
        self.boton.setIcon(QtGui.QIcon('logo.png'))
        self.boton.setIconSize(QtCore.QSize(50,50))
    
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lista.setFont(font)
        self.lista = QtWidgets.QListWidget(self.lista)
        self.lista.setGeometry(QtCore.QRect(0, 0, 331, 481))
        self.lista.installEventFilter(self)
    
    def eventFilter(self, source, event):
        if event.type() == QEvent.ContextMenu and source is self.lista:
            menu = QMenu()
            menu.addAction('Informacion del personaje')
            

            if menu.exec_(event.globalPos()):
                item = source.itemAt(event.pos())
                print(item.text())
                dlg = QDialog(self)
                dlg.setWindowTitle("Informacion del personaje")
                dlg.exec()
            return True

        return super().eventFilter(source, event)

    def showTime(self):
        self.date = QDate.currentDate()
        self.time = QTime.currentTime()

        self.fecha.setText(self.date.toString('dd/MM/yyyy'))
        self.hora.setText(self.time.toString(Qt.DefaultLocaleLongDate))

    def fn_activar(self):
        global bloqueo
        if bloqueo == 1:
            self.lista.clear()
            bloqueo = 0
        
        randomlist = random.sample(range(1, 83), 10)   
        for i in range (10):
            bloqueo = 1
            name1 = 'https://swapi.dev/api/people/{}'.format(randomlist[i])
            name1 = requests.get(name1)
            resp = name1.json()
            self.lista.setItemAlignment(Qt.AlignCenter)
            self.lista.addItem(resp['name'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = ejemplo_GUI()
    GUI.show()



    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing window...')
