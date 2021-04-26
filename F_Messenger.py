# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'мессенджер.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Messenger(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(501, 460)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 481, 401))
        self.tabWidget.setStyleSheet("background-color: rgb(128, 255, 247);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.sendButton = QtWidgets.QPushButton(self.tab)
        self.sendButton.setGeometry(QtCore.QRect(350, 270, 75, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.sendButton.setFont(font)
        self.sendButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sendButton.setObjectName("sendButton")
        self.messages = QtWidgets.QTextBrowser(self.tab)
        self.messages.setGeometry(QtCore.QRect(30, 20, 391, 241))
        self.messages.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.messages.setObjectName("messages")
        self.messageInput = QtWidgets.QTextEdit(self.tab)
        self.messageInput.setGeometry(QtCore.QRect(30, 270, 311, 61))
        self.messageInput.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.messageInput.setObjectName("messageInput")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 0, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(260, 15, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Script")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(320, 5, 161, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(-110, -80, 681, 591))
        self.label_4.setStyleSheet("background-color: rgb(123, 141, 118);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_4.raise_()
        self.tabWidget.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.pushButton.raise_()

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sendButton.setText(_translate("Form", ">"))
        self.messageInput.setPlaceholderText(_translate("Form", "Введите текст..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Общий чат"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))
        self.label.setText(_translate("Form", "Чаты"))
        self.label_2.setText(_translate("Form", "R-Messenger"))
        self.label_3.setText(_translate("Form", "Beta"))
        self.pushButton.setText(_translate("Form", "Найти человека по e-mail"))
