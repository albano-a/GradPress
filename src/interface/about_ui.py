# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        if not AboutWindow.objectName():
            AboutWindow.setObjectName(u"AboutWindow")
        AboutWindow.resize(405, 390)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AboutWindow.sizePolicy().hasHeightForWidth())
        AboutWindow.setSizePolicy(sizePolicy)
        AboutWindow.setMinimumSize(QSize(357, 296))
        AboutWindow.setMaximumSize(QSize(405, 390))
        AboutWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u"J:/Universidade/GIECAR/qt_kraken_conversion/about.png", QSize(), QIcon.Normal, QIcon.Off)
        AboutWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(AboutWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 20, 231, 71))
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(20)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 101, 91))
        self.label_2.setPixmap(QPixmap(u"../icon.ico"))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 150, 381, 191))
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.creditsLabel = QLabel(self.groupBox)
        self.creditsLabel.setObjectName(u"creditsLabel")
        self.creditsLabel.setGeometry(QRect(40, 80, 301, 101))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 20, 321, 61))
        self.label_4.setWordWrap(True)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 110, 181, 22))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.giecarBtn = QPushButton(self.widget)
        self.giecarBtn.setObjectName(u"giecarBtn")
        self.giecarBtn.setMinimumSize(QSize(60, 20))
        self.giecarBtn.setMaximumSize(QSize(60, 20))
        font1 = QFont()
        font1.setBold(True)
        self.giecarBtn.setFont(font1)
        self.giecarBtn.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(171, 171, 171);\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"	font-weight: 700; /* Set font weight to 700 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(253, 253, 253, 255));\n"
"    border: 1px solid rgb(171, 171, 171); /* Optional: Add border color on hover */\n"
"}")

        self.horizontalLayout.addWidget(self.giecarBtn)

        self.githubBtn = QPushButton(self.widget)
        self.githubBtn.setObjectName(u"githubBtn")
        self.githubBtn.setMinimumSize(QSize(60, 20))
        self.githubBtn.setMaximumSize(QSize(60, 20))
        self.githubBtn.setFont(font1)
        self.githubBtn.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(171, 171, 171);\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"	font-weight: 700; /* Set font weight to 700 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(253, 253, 253, 255));\n"
"    border: 1px solid rgb(171, 171, 171); /* Optional: Add border color on hover */\n"
"}")

        self.horizontalLayout.addWidget(self.githubBtn)

        AboutWindow.setCentralWidget(self.centralwidget)
        self.groupBox.raise_()
        self.giecarBtn.raise_()
        self.githubBtn.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.menubar = QMenuBar(AboutWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 405, 21))
        AboutWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AboutWindow)
        self.statusbar.setObjectName(u"statusbar")
        AboutWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AboutWindow)

        QMetaObject.connectSlotsByName(AboutWindow)
    # setupUi

    def retranslateUi(self, AboutWindow):
        AboutWindow.setWindowTitle(QCoreApplication.translate("AboutWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">KrakeN Geophysics v0.4.2</span></p></body></html>", None))
        self.label_2.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("AboutWindow", u"GNU General Public License", None))
        self.creditsLabel.setText(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Desenvolvido por Andr\u00e9 Albano</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">GIECAR - UFF</span></p><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">2024</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("AboutWindow", u"<html><head/><body><p align=\"justify\">This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or at your option any later version.</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("AboutWindow", u"Acesse:", None))
#if QT_CONFIG(tooltip)
        self.giecarBtn.setToolTip(QCoreApplication.translate("AboutWindow", u"Acessar o site do Grupo de Interpreta\u00e7\u00e3o Explorat\u00f3ria e Caracteriza\u00e7\u00e3o de Reservat\u00f3rio", None))
#endif // QT_CONFIG(tooltip)
        self.giecarBtn.setText(QCoreApplication.translate("AboutWindow", u"GIECAR", None))
#if QT_CONFIG(tooltip)
        self.githubBtn.setToolTip(QCoreApplication.translate("AboutWindow", u"Acessar o GitHub do projeto", None))
#endif // QT_CONFIG(tooltip)
        self.githubBtn.setText(QCoreApplication.translate("AboutWindow", u"GitHub", None))
    # retranslateUi

