# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 600)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.boton = QtWidgets.QPushButton(self.centralwidget)
        self.boton.setGeometry(QtCore.QRect(520, 400, 131, 61))
        self.boton.setObjectName("boton")
        self.fecha = QtWidgets.QLabel(self.centralwidget)
        self.fecha.setGeometry(QtCore.QRect(470, 110, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.fecha.setFont(font)
        self.fecha.setText("")
        self.fecha.setObjectName("fecha")
        self.hora = QtWidgets.QLabel(self.centralwidget)
        self.hora.setGeometry(QtCore.QRect(470, 240, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.hora.setFont(font)
        self.hora.setText("")
        self.hora.setObjectName("hora")
        self.lista = QtWidgets.QListWidget(self.centralwidget)
        self.lista.setGeometry(QtCore.QRect(40, 50, 331, 481))
        self.lista.setObjectName("lista")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton.setText(_translate("MainWindow", "REQUEST"))
