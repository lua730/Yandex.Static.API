# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1157, 602)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon_100x100.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget {\n"
"    background-color: #FFF;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_main = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_main.setGeometry(QtCore.QRect(0, 25, 1161, 621))
        self.groupBox_main.setStyleSheet("QGroupBox {\n"
"    color: white;\n"
"    border: 0px;\n"
"    background-color: #FFF;\n"
"\n"
"}")
        self.groupBox_main.setTitle("")
        self.groupBox_main.setObjectName("groupBox_main")
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox_main)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 63, 1141, 451))
        self.stackedWidget.setStyleSheet("QStackedWidget {\n"
"    background-color: #FFF;\n"
"    border: 1px solid black;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.label = QtWidgets.QLabel(self.page1)
        self.label.setGeometry(QtCore.QRect(0, 0, 601, 451))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("sources/map.png"))
        self.label.setObjectName("label")
        self.textEdit_business = QtWidgets.QTextEdit(self.page1)
        self.textEdit_business.setGeometry(QtCore.QRect(610, 10, 521, 431))
        self.textEdit_business.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit_business.setStyleSheet("QTextEdit {\n"
"    border: 0px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    selection-background-color: rgb(212, 212, 255);\n"
"}\n"
"QScrollBar:vertical {\n"
"     border: 2px solid rgba(170, 170, 255, 130);\n"
"     background-color: rgba(255, 255, 255, 0);\n"
"     width: 15px;\n"
"     margin: 0px 0 0px 0;\n"
" }\n"
" QScrollBar::handle:vertical {\n"
"     background: #87a7ff;\n"
"     min-height: 20px;\n"
" }\n"
"\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     border: 0px;\n"
"     background-color: rgba(255, 255, 255, 0);\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: 0px;\n"
"     background-color: rgba(255, 255, 255, 0);\n"
" }\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"")
        self.textEdit_business.setObjectName("textEdit_business")
        self.stackedWidget.addWidget(self.page1)
        self.horizontalSlider_size = QtWidgets.QSlider(self.groupBox_main)
        self.horizontalSlider_size.setEnabled(False)
        self.horizontalSlider_size.setGeometry(QtCore.QRect(90, 10, 160, 22))
        self.horizontalSlider_size.setStyleSheet("")
        self.horizontalSlider_size.setMinimum(0)
        self.horizontalSlider_size.setMaximum(17)
        self.horizontalSlider_size.setPageStep(1)
        self.horizontalSlider_size.setProperty("value", 15)
        self.horizontalSlider_size.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_size.setObjectName("horizontalSlider_size")
        self.label_2 = QtWidgets.QLabel(self.groupBox_main)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label_2.setStyleSheet("QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_main)
        self.label_4.setGeometry(QtCore.QRect(261, 10, 41, 21))
        self.label_4.setStyleSheet("QLabel {\n"
"    color: rgb(0, 0, 0);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.label_4.setObjectName("label_4")
        self.lineEdit_findName = QtWidgets.QLineEdit(self.groupBox_main)
        self.lineEdit_findName.setEnabled(True)
        self.lineEdit_findName.setGeometry(QtCore.QRect(540, 10, 241, 21))
        self.lineEdit_findName.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_findName.setObjectName("lineEdit_findName")
        self.pushButton_find = QtWidgets.QPushButton(self.groupBox_main)
        self.pushButton_find.setGeometry(QtCore.QRect(785, 7, 59, 30))
        self.pushButton_find.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(78, 124, 255);\n"
"    color: white;\n"
"    background-color: rgb(78, 124, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 109, 223);\n"
"}")
        self.pushButton_find.setObjectName("pushButton_find")
        self.pushButton_page1 = QtWidgets.QPushButton(self.groupBox_main)
        self.pushButton_page1.setEnabled(True)
        self.pushButton_page1.setGeometry(QtCore.QRect(300, 10, 73, 27))
        self.pushButton_page1.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(78, 124, 255);\n"
"    color: white;\n"
"    background-color: rgb(78, 124, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 109, 223);\n"
"}")
        self.pushButton_page1.setObjectName("pushButton_page1")
        self.pushButton_page2 = QtWidgets.QPushButton(self.groupBox_main)
        self.pushButton_page2.setGeometry(QtCore.QRect(380, 10, 73, 27))
        self.pushButton_page2.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(78, 124, 255);\n"
"    color: white;\n"
"    background-color: rgb(78, 124, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 109, 223);\n"
"}")
        self.pushButton_page2.setObjectName("pushButton_page2")
        self.pushButton_page3 = QtWidgets.QPushButton(self.groupBox_main)
        self.pushButton_page3.setGeometry(QtCore.QRect(460, 10, 73, 27))
        self.pushButton_page3.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(78, 124, 255);\n"
"    color: white;\n"
"    background-color: rgb(78, 124, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 109, 223);\n"
"}")
        self.pushButton_page3.setObjectName("pushButton_page3")
        self.lineEdit_fullAddress = QtWidgets.QLineEdit(self.groupBox_main)
        self.lineEdit_fullAddress.setEnabled(True)
        self.lineEdit_fullAddress.setGeometry(QtCore.QRect(10, 543, 961, 20))
        self.lineEdit_fullAddress.setReadOnly(True)
        self.lineEdit_fullAddress.setObjectName("lineEdit_fullAddress")
        self.label_3 = QtWidgets.QLabel(self.groupBox_main)
        self.label_3.setGeometry(QtCore.QRect(10, 520, 161, 16))
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_main)
        self.checkBox.setEnabled(True)
        self.checkBox.setGeometry(QtCore.QRect(700, 520, 261, 20))
        self.checkBox.setObjectName("checkBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox_main)
        self.label_5.setGeometry(QtCore.QRect(990, 520, 71, 16))
        self.label_5.setObjectName("label_5")
        self.lineEdit_index = QtWidgets.QLineEdit(self.groupBox_main)
        self.lineEdit_index.setEnabled(True)
        self.lineEdit_index.setGeometry(QtCore.QRect(990, 543, 161, 20))
        self.lineEdit_index.setReadOnly(True)
        self.lineEdit_index.setObjectName("lineEdit_index")
        self.pushButton_delete = QtWidgets.QPushButton(self.groupBox_main)
        self.pushButton_delete.setGeometry(QtCore.QRect(849, 7, 59, 30))
        self.pushButton_delete.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(78, 124, 255);\n"
"    color: white;\n"
"    background-color: rgb(78, 124, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 109, 223);\n"
"}")
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.label_error = QtWidgets.QLabel(self.groupBox_main)
        self.label_error.setGeometry(QtCore.QRect(950, 10, 151, 21))
        self.label_error.setStyleSheet("QLabel:{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    alternate-background-color:  rgba(255, 255, 255, 0);\n"
"}")
        self.label_error.setObjectName("label_error")
        self.label_buisness = QtWidgets.QLabel(self.groupBox_main)
        self.label_buisness.setGeometry(QtCore.QRect(810, 40, 171, 21))
        self.label_buisness.setStyleSheet("QLavel{\n"
"    background: rgba(255, 255, 255, 0);\n"
"}")
        self.label_buisness.setObjectName("label_buisness")
        self.groupBox_title = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_title.setGeometry(QtCore.QRect(0, 0, 1161, 25))
        self.groupBox_title.setStyleSheet("QGroupBox {\n"
"    color: white;\n"
"    border: 0px;\n"
"    background-color:rgb(78, 124, 255)\n"
"}")
        self.groupBox_title.setTitle("")
        self.groupBox_title.setObjectName("groupBox_title")
        self.label_name = QtWidgets.QLabel(self.groupBox_title)
        self.label_name.setGeometry(QtCore.QRect(5, 3, 341, 21))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("QLabel {\n"
"    color: #FFF;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.label_name.setObjectName("label_name")
        self.exitAppButton = QtWidgets.QPushButton(self.groupBox_title)
        self.exitAppButton.setGeometry(QtCore.QRect(1130, 0, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.exitAppButton.setFont(font)
        self.exitAppButton.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    border-radius: 20px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: #FFF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(69, 69, 106);\n"
"}")
        self.exitAppButton.setObjectName("exitAppButton")
        self.minimizeButton = QtWidgets.QPushButton(self.groupBox_title)
        self.minimizeButton.setGeometry(QtCore.QRect(1110, 0, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Proxima Nova")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.minimizeButton.setFont(font)
        self.minimizeButton.setStyleSheet("QPushButton {\n"
"    border: 0px;\n"
"    border-radius: 20px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    color: #FFF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(69, 69, 106);\n"
"}")
        self.minimizeButton.setObjectName("minimizeButton")
        self.pushButton_help = QtWidgets.QPushButton(self.groupBox_title)
        self.pushButton_help.setEnabled(True)
        self.pushButton_help.setGeometry(QtCore.QRect(350, 3, 91, 21))
        self.pushButton_help.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(78, 124, 255);\n"
"    color: white;\n"
"    background-color: #7398ff;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 109, 223);\n"
"}")
        self.pushButton_help.setObjectName("pushButton_help")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Yandex.api Map"))
        self.textEdit_business.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Масштаб:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Тип:</span></p></body></html>"))
        self.pushButton_find.setText(_translate("MainWindow", "Поиск"))
        self.pushButton_page1.setText(_translate("MainWindow", "Карта"))
        self.pushButton_page2.setText(_translate("MainWindow", "Спутник"))
        self.pushButton_page3.setText(_translate("MainWindow", "Гибрид"))
        self.label_3.setText(_translate("MainWindow", "Полный адрес:"))
        self.checkBox.setText(_translate("MainWindow", "Показывать почтовый индекс, если имеется"))
        self.label_5.setText(_translate("MainWindow", "Индекс:"))
        self.pushButton_delete.setText(_translate("MainWindow", "Сброс"))
        self.label_error.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_buisness.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Организации:</span></p></body></html>"))
        self.label_name.setText(_translate("MainWindow", "<html><head/><body><p>КАРТА С ИСПОЛЬЗОВАНИЕМ ЯНДЕКС.API</p></body></html>"))
        self.exitAppButton.setText(_translate("MainWindow", "X"))
        self.minimizeButton.setText(_translate("MainWindow", "_"))
        self.pushButton_help.setText(_translate("MainWindow", "Справка"))