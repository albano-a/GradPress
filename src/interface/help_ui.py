# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QTextEdit,
    QTreeView, QWidget)

class Ui_HelpMainWindow(object):
    def setupUi(self, HelpMainWindow):
        if not HelpMainWindow.objectName():
            HelpMainWindow.setObjectName(u"HelpMainWindow")
        HelpMainWindow.resize(800, 600)
        HelpMainWindow.setMaximumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u"../help.png", QSize(), QIcon.Normal, QIcon.Off)
        HelpMainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(HelpMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(260, 10, 521, 531))
        self.frame.setStyleSheet(u"QFrame {\n"
"	border: 1px solid #212121\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.helpTextEdit = QTextEdit(self.frame)
        self.helpTextEdit.setObjectName(u"helpTextEdit")
        self.helpTextEdit.setGeometry(QRect(0, 0, 521, 531))
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 241, 531))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	border: 1px solid #212121\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.helpTreeView = QTreeView(self.frame_2)
        self.helpTreeView.setObjectName(u"helpTreeView")
        self.helpTreeView.setGeometry(QRect(0, 0, 241, 531))
        HelpMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(HelpMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        HelpMainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(HelpMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        HelpMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HelpMainWindow)

        QMetaObject.connectSlotsByName(HelpMainWindow)
    # setupUi

    def retranslateUi(self, HelpMainWindow):
        HelpMainWindow.setWindowTitle(QCoreApplication.translate("HelpMainWindow", u"MainWindow", None))
        self.helpTextEdit.setHtml(QCoreApplication.translate("HelpMainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Seja bem vindo ao guia de uso do Kraken Software v0.4.2</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Este software foi desenvolvido com o pr"
                        "op\u00f3sito de auxiliar os estudantes da gradua\u00e7\u00e3o de Geof\u00edsica e pesquisadores do GIECAR a realizar suas pesquisas de forma r\u00e1pida e direta. Neste guia, voc\u00ea encontrar\u00e1 tudo necess\u00e1rio para realizar todas as funcionalidades do programa.</span></p></body></html>", None))
    # retranslateUi

