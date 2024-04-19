# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'crud.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSplitter,
    QStatusBar, QTreeView, QWidget)

class Ui_ManageFilesWindow(object):
    def setupUi(self, ManageFilesWindow):
        if not ManageFilesWindow.objectName():
            ManageFilesWindow.setObjectName(u"ManageFilesWindow")
        ManageFilesWindow.resize(650, 500)
        ManageFilesWindow.setMinimumSize(QSize(650, 500))
        ManageFilesWindow.setMaximumSize(QSize(650, 500))
        icon = QIcon()
        icon.addFile(u"../icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        ManageFilesWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(ManageFilesWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 651, 81))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.manageFilesLabel = QLabel(self.frame)
        self.manageFilesLabel.setObjectName(u"manageFilesLabel")
        self.manageFilesLabel.setGeometry(QRect(0, 10, 651, 31))
        font = QFont()
        font.setPointSize(18)
        self.manageFilesLabel.setFont(font)
        self.manageFilesLabel_2 = QLabel(self.frame)
        self.manageFilesLabel_2.setObjectName(u"manageFilesLabel_2")
        self.manageFilesLabel_2.setGeometry(QRect(0, 50, 651, 31))
        self.manageFilesLabel_2.setFont(font)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(70, 110, 521, 301))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.manageFilesTreeView = QTreeView(self.frame_2)
        self.manageFilesTreeView.setObjectName(u"manageFilesTreeView")
        self.manageFilesTreeView.setGeometry(QRect(0, 0, 521, 301))
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(70, 430, 521, 41))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.splitter = QSplitter(self.frame_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 10, 521, 21))
        self.splitter.setOrientation(Qt.Horizontal)
        self.addFileBtn = QPushButton(self.splitter)
        self.addFileBtn.setObjectName(u"addFileBtn")
        self.addFileBtn.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(171, 171, 171);\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(253, 253, 253, 255));\n"
"    border: 1px solid rgb(171, 171, 171); /* Optional: Add border color on hover */\n"
"}")
        self.splitter.addWidget(self.addFileBtn)
        self.renameFileBtn = QPushButton(self.splitter)
        self.renameFileBtn.setObjectName(u"renameFileBtn")
        self.renameFileBtn.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(171, 171, 171);\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(253, 253, 253, 255));\n"
"    border: 1px solid rgb(171, 171, 171); /* Optional: Add border color on hover */\n"
"}")
        self.splitter.addWidget(self.renameFileBtn)
        self.deleteFileBtn = QPushButton(self.splitter)
        self.deleteFileBtn.setObjectName(u"deleteFileBtn")
        self.deleteFileBtn.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(171, 171, 171);\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(253, 253, 253, 255));\n"
"    border: 1px solid rgb(171, 171, 171); /* Optional: Add border color on hover */\n"
"}")
        self.splitter.addWidget(self.deleteFileBtn)
        self.exitManageFilesBtn = QPushButton(self.splitter)
        self.exitManageFilesBtn.setObjectName(u"exitManageFilesBtn")
        self.exitManageFilesBtn.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(171, 171, 171);\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(253, 253, 253, 255));\n"
"    border: 1px solid rgb(171, 171, 171); /* Optional: Add border color on hover */\n"
"}")
        self.splitter.addWidget(self.exitManageFilesBtn)
        ManageFilesWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(ManageFilesWindow)
        self.statusbar.setObjectName(u"statusbar")
        ManageFilesWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ManageFilesWindow)

        QMetaObject.connectSlotsByName(ManageFilesWindow)
    # setupUi

    def retranslateUi(self, ManageFilesWindow):
        ManageFilesWindow.setWindowTitle(QCoreApplication.translate("ManageFilesWindow", u"MainWindow", None))
        self.manageFilesLabel.setText(QCoreApplication.translate("ManageFilesWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Gerenciar Arquivos</span></p></body></html>", None))
        self.manageFilesLabel_2.setText(QCoreApplication.translate("ManageFilesWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Gerencie aqui os arquivos carregados</span></p></body></html>", None))
        self.addFileBtn.setText(QCoreApplication.translate("ManageFilesWindow", u"Adicionar", None))
        self.renameFileBtn.setText(QCoreApplication.translate("ManageFilesWindow", u"Renomear", None))
        self.deleteFileBtn.setText(QCoreApplication.translate("ManageFilesWindow", u"Deletar", None))
        self.exitManageFilesBtn.setText(QCoreApplication.translate("ManageFilesWindow", u"Voltar", None))
    # retranslateUi

