# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainDialogV1.ui'
#
# Created: Thu Jan 11 15:14:28 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1168, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Main/icons/Scratch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("QDialog{\n"
"background-color: qlineargradient(spread:reflect, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(90, 7, 90, 255), stop:0.372881 rgba(26, 23, 99, 252), stop:0.672316 rgba(26, 23, 99, 253), stop:1 rgba(0, 125, 125, 255));\n"
"}\n"
"\n"
"QLabel{\n"
"color: White;\n"
"}\n"
"\n"
"QGroupBox{\n"
"border: 2px solid rgb(190, 190, 190);\n"
"border-radius: 10px;\n"
"margin-top: 3ex\n"
"}\n"
"\n"
"QGroupBox::title{\n"
"subcontrol-origin: margin;\n"
"subcontrol-position: top left;\n"
"padding: 0 3px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QToolButton{\n"
"background-color: Transparent; \n"
"color: White;\n"
"border: 2px ridge White;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QToolButton#arquivoButton{\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QToolButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0.215909 rgba(0, 0, 0, 0), stop:1 rgba(15, 243, 255, 255));\n"
"}\n"
"\n"
"QSpinBox { \n"
"border: 2px solid  white; \n"
"border-radius: 5px; \n"
"color: White;\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QDoubleSpinBox { \n"
"border: 2px solid  white; \n"
"border-radius: 5px; \n"
"color: White;\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button { \n"
"background-color: Transparent;\n"
"width: 14px;\n"
"height: 10px; \n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:pressed{ \n"
"background-color: white;\n"
"width: 14px;\n"
"height: 10px; \n"
"}\n"
"\n"
"QDoubleSpinBox::down-button{ \n"
"background-color: Transparent;\n"
"width: 14px;\n"
"height: 10px; \n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed{ \n"
"background-color: white;\n"
"width: 14px;\n"
"height: 10px; \n"
"}\n"
"\n"
"QDoubleSpinBox::up-arrow{ \n"
"background-color: transparent;\n"
"border-left: 7px solid none;\n"
"border-right: 7px solid none;\n"
"border-bottom: 6px solid white;\n"
"width: 0px; \n"
"height: 0px; \n"
"}\n"
"\n"
"QDoubleSpinBox::down-arrow{ \n"
"border-left: 7px solid none;\n"
"border-right: 7px solid none;\n"
"border-top: 6px solid white;\n"
"width: 0px; \n"
"height: 0px; \n"
"}\n"
"\n"
"\n"
"QSpinBox::up-button { \n"
"background-color: Transparent;\n"
"width: 14px;\n"
"height: 10px; \n"
"}\n"
"\n"
"QSpinBox::up-button:pressed{ \n"
"background-color: white;\n"
"width: 14px;\n"
"height: 10px; \n"
"}\n"
"\n"
"QSpinBox::down-button{ \n"
"background-color: Transparent;\n"
"width: 14px;\n"
"height: 10px; \n"
"}\n"
"\n"
"QSpinBox::down-button:pressed{ \n"
"background-color: white;\n"
"width: 14px;\n"
"height: 10px; \n"
"}\n"
"\n"
"QSpinBox::up-arrow{ \n"
"background-color: transparent;\n"
"border-left: 7px solid none;\n"
"border-right: 7px solid none;\n"
"border-bottom: 6px solid white;\n"
"width: 0px; \n"
"height: 0px; \n"
"}\n"
"\n"
"QSpinBox::down-arrow{ \n"
"border-left: 7px solid none;\n"
"border-right: 7px solid none;\n"
"border-top: 6px solid white;\n"
"width: 0px; \n"
"height: 0px; \n"
"}\n"
"\n"
"\n"
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: qlineargradient(spread:pad, x1:0.988545, y1:1, x2:1, y2:0.455, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(204, 0, 0, 255));\n"
"    width: 10px;\n"
"    margin: 0.5px;\n"
"}")
        self.imageLabel = QtGui.QLabel(Dialog)
        self.imageLabel.setGeometry(QtCore.QRect(0, 60, 541, 400))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.imageLabel.setFont(font)
        self.imageLabel.setFrameShape(QtGui.QFrame.Box)
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.analisarButton = QtGui.QToolButton(Dialog)
        self.analisarButton.setGeometry(QtCore.QRect(770, 480, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.analisarButton.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Main/icons/startB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.analisarButton.setIcon(icon1)
        self.analisarButton.setIconSize(QtCore.QSize(64, 64))
        self.analisarButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.analisarButton.setObjectName("analisarButton")
        self.salvarButton = QtGui.QToolButton(Dialog)
        self.salvarButton.setGeometry(QtCore.QRect(970, 480, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.salvarButton.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Main/icons/salvarB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.salvarButton.setIcon(icon2)
        self.salvarButton.setIconSize(QtCore.QSize(64, 64))
        self.salvarButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.salvarButton.setObjectName("salvarButton")
        self.sairButton = QtGui.QToolButton(Dialog)
        self.sairButton.setGeometry(QtCore.QRect(1070, 480, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.sairButton.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Main/icons/sairB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sairButton.setIcon(icon3)
        self.sairButton.setIconSize(QtCore.QSize(64, 64))
        self.sairButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.sairButton.setObjectName("sairButton")
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(540, 60, 21, 391))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.graficoLabel = QtGui.QLabel(Dialog)
        self.graficoLabel.setGeometry(QtCore.QRect(560, 60, 600, 400))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.graficoLabel.setFont(font)
        self.graficoLabel.setFrameShape(QtGui.QFrame.Box)
        self.graficoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.graficoLabel.setObjectName("graficoLabel")
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(530, 470, 231, 101))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.statusLabel = QtGui.QLabel(self.groupBox)
        self.statusLabel.setGeometry(QtCore.QRect(10, 20, 211, 31))
        self.statusLabel.setObjectName("statusLabel")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 181, 31))
        self.label_5.setObjectName("label_5")
        self.quantidadeLabel = QtGui.QLabel(self.groupBox)
        self.quantidadeLabel.setGeometry(QtCore.QRect(140, 40, 47, 31))
        self.quantidadeLabel.setObjectName("quantidadeLabel")
        self.progressBar = QtGui.QProgressBar(self.groupBox)
        self.progressBar.setGeometry(QtCore.QRect(10, 70, 211, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 470, 511, 101))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.fatorLine = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.fatorLine.setGeometry(QtCore.QRect(110, 70, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.fatorLine.setFont(font)
        self.fatorLine.setDecimals(4)
        self.fatorLine.setSingleStep(0.01)
        self.fatorLine.setProperty("value", 2.0)
        self.fatorLine.setObjectName("fatorLine")
        self.arquivoLine = QtGui.QLineEdit(self.groupBox_2)
        self.arquivoLine.setGeometry(QtCore.QRect(10, 40, 461, 20))
        self.arquivoLine.setObjectName("arquivoLine")
        self.arquivoButton = QtGui.QToolButton(self.groupBox_2)
        self.arquivoButton.setGeometry(QtCore.QRect(480, 40, 25, 21))
        self.arquivoButton.setObjectName("arquivoButton")
        self.tempoLine = QtGui.QSpinBox(self.groupBox_2)
        self.tempoLine.setGeometry(QtCore.QRect(390, 70, 81, 22))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.tempoLine.setFont(font)
        self.tempoLine.setMinimum(1)
        self.tempoLine.setProperty("value", 15)
        self.tempoLine.setObjectName("tempoLine")
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(250, 70, 141, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pararButton = QtGui.QToolButton(Dialog)
        self.pararButton.setGeometry(QtCore.QRect(870, 480, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.pararButton.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Main/icons/stopB.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pararButton.setIcon(icon4)
        self.pararButton.setIconSize(QtCore.QSize(64, 64))
        self.pararButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.pararButton.setObjectName("pararButton")
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(485, 0, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(10, 570, 1141, 21))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 580, 1151, 21))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.imageLabel.setText(QtGui.QApplication.translate("Dialog", "Imagem", None, QtGui.QApplication.UnicodeUTF8))
        self.analisarButton.setText(QtGui.QApplication.translate("Dialog", "Analisar", None, QtGui.QApplication.UnicodeUTF8))
        self.salvarButton.setText(QtGui.QApplication.translate("Dialog", "Salvar", None, QtGui.QApplication.UnicodeUTF8))
        self.sairButton.setText(QtGui.QApplication.translate("Dialog", "Sair", None, QtGui.QApplication.UnicodeUTF8))
        self.graficoLabel.setText(QtGui.QApplication.translate("Dialog", "Gráfico", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.statusLabel.setText(QtGui.QApplication.translate("Dialog", "Em espera", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Quantidade de arquivos:", None, QtGui.QApplication.UnicodeUTF8))
        self.quantidadeLabel.setText(QtGui.QApplication.translate("Dialog", "000", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Configurações", None, QtGui.QApplication.UnicodeUTF8))
        self.arquivoButton.setText(QtGui.QApplication.translate("Dialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.tempoLine.setSuffix(QtGui.QApplication.translate("Dialog", "min", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Arquivo:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Fator mágico:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Tempo entre fotos:", None, QtGui.QApplication.UnicodeUTF8))
        self.pararButton.setText(QtGui.QApplication.translate("Dialog", "Encerrar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "PyScratch", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Escrito e compilado por Vladimir Gaal - Dezembro 2017 - Agradecimento ao site icons8.com por fornecer gratuitamente os ícones utilizados", None, QtGui.QApplication.UnicodeUTF8))

import icones_rc
