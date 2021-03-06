# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'help.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(337, 300)
        self.groupBox_title = QtWidgets.QGroupBox(Dialog)
        self.groupBox_title.setGeometry(QtCore.QRect(0, 0, 341, 25))
        self.groupBox_title.setStyleSheet("QGroupBox {\n"
"    color: white;\n"
"    border: 0px;\n"
"    background-color:rgb(78, 124, 255)\n"
"}")
        self.groupBox_title.setTitle("")
        self.groupBox_title.setObjectName("groupBox_title")
        self.label_name = QtWidgets.QLabel(self.groupBox_title)
        self.label_name.setGeometry(QtCore.QRect(5, 3, 81, 21))
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
        self.pushButton_page3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_page3.setGeometry(QtCore.QRect(120, 270, 73, 27))
        self.pushButton_page3.setStyleSheet("QPushButton {\n"
"    border: 2px solid rgb(78, 124, 255);\n"
"    color: white;\n"
"    background-color: rgb(78, 124, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(68, 109, 223);\n"
"}")
        self.pushButton_page3.setObjectName("pushButton_page3")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 321, 231))
        self.textEdit.setMouseTracking(False)
        self.textEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.textEdit.setStyleSheet("QTextEdit {\n"
"    border: 0px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
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
        self.textEdit.setObjectName("textEdit")
        self.label_secret = QtWidgets.QLabel(Dialog)
        self.label_secret.setEnabled(True)
        self.label_secret.setGeometry(QtCore.QRect(400, 70, 301, 141))
        self.label_secret.setText("")
        self.label_secret.setPixmap(QtGui.QPixmap("sources/test.png"))
        self.label_secret.setScaledContents(True)
        self.label_secret.setObjectName("label_secret")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Help"))
        self.label_name.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">СПРАВКА</span></p></body></html>"))
        self.pushButton_page3.setText(_translate("Dialog", "ОК"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Небольшой учебный проект, демонстрирующий возможности yandex.api</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Функции:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Переключение режима отображения карты (схема, спутник, гибрид)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Изменение масштаба карты (Клавиши: PgUp, PgDown)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Перещение по карте (Клавиши: LeftArrow, RightArrow, DownArrow, UpArrow)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Поиск объектов</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Выбор объектов курсором</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Просмотр данных об организациях на выбранном объекте</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- Просмотр полного адрес и почтового индекса выбранного объекта</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Created by lua730</p></body></html>"))
