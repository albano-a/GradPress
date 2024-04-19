# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gradient.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QTableView, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_gradientePressaoWindow(object):
    def setupUi(self, gradientePressaoWindow):
        if not gradientePressaoWindow.objectName():
            gradientePressaoWindow.setObjectName(u"gradientePressaoWindow")
        gradientePressaoWindow.resize(690, 619)
        self.centralwidget = QWidget(gradientePressaoWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.fluidClassificationBtn = QPushButton(self.centralwidget)
        self.fluidClassificationBtn.setObjectName(u"fluidClassificationBtn")
        self.fluidClassificationBtn.setMinimumSize(QSize(0, 20))
        self.fluidClassificationBtn.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(171, 171, 171);\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(253, 253, 253, 255));\n"
"    border: 1px solid rgb(171, 171, 171); /* Optional: Add border color on hover */\n"
"}")

        self.gridLayout.addWidget(self.fluidClassificationBtn, 3, 0, 1, 1)

        self.fluidPressureResults = QTextBrowser(self.centralwidget)
        self.fluidPressureResults.setObjectName(u"fluidPressureResults")
        self.fluidPressureResults.setMaximumSize(QSize(16777215, 80))

        self.gridLayout.addWidget(self.fluidPressureResults, 4, 0, 1, 1)

        self.saveOutputContent = QPushButton(self.centralwidget)
        self.saveOutputContent.setObjectName(u"saveOutputContent")
        self.saveOutputContent.setMinimumSize(QSize(150, 20))
        self.saveOutputContent.setMaximumSize(QSize(150, 16777215))
        self.saveOutputContent.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(171, 171, 171);\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(253, 253, 253, 255));\n"
"    border: 1px solid rgb(171, 171, 171); /* Optional: Add border color on hover */\n"
"}")

        self.gridLayout.addWidget(self.saveOutputContent, 5, 0, 1, 1, Qt.AlignHCenter)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.fluidPressureTableView = QTableView(self.centralwidget)
        self.fluidPressureTableView.setObjectName(u"fluidPressureTableView")
        self.fluidPressureTableView.setMaximumSize(QSize(16777215, 200))

        self.gridLayout.addWidget(self.fluidPressureTableView, 1, 0, 1, 2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 100))
        self.groupBox.setMaximumSize(QSize(16777215, 120))
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(338, 23, 322, 87))
        self.groupBox_2.setMaximumSize(QSize(16777215, 90))
        self.widget = QWidget(self.groupBox_2)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 20, 281, 61))
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_4.setFont(font1)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.profMinInput = QLineEdit(self.widget)
        self.profMinInput.setObjectName(u"profMinInput")

        self.gridLayout_2.addWidget(self.profMinInput, 0, 1, 1, 1)

        self.profMaxInput = QLineEdit(self.widget)
        self.profMaxInput.setObjectName(u"profMaxInput")

        self.gridLayout_2.addWidget(self.profMaxInput, 1, 1, 1, 1)

        self.widget1 = QWidget(self.groupBox)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(11, 24, 311, 81))
        self.gridLayout_3 = QGridLayout(self.widget1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.widget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setMouseTracking(True)
        self.label_6.setStyleSheet(u"QLabel {\n"
"	border: None\n"
"}")

        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)

        self.csvRadioButton = QRadioButton(self.widget1)
        self.csvRadioButton.setObjectName(u"csvRadioButton")
        self.csvRadioButton.setFont(font1)

        self.gridLayout_3.addWidget(self.csvRadioButton, 2, 1, 1, 1, Qt.AlignHCenter)

        self.txtRadioButton = QRadioButton(self.widget1)
        self.txtRadioButton.setObjectName(u"txtRadioButton")
        self.txtRadioButton.setFont(font1)

        self.gridLayout_3.addWidget(self.txtRadioButton, 2, 2, 1, 1, Qt.AlignHCenter)

        self.xlsxRadioButton = QRadioButton(self.widget1)
        self.xlsxRadioButton.setObjectName(u"xlsxRadioButton")
        self.xlsxRadioButton.setEnabled(True)
        self.xlsxRadioButton.setFont(font1)

        self.gridLayout_3.addWidget(self.xlsxRadioButton, 2, 3, 1, 1, Qt.AlignHCenter)

        self.pressureComboBox = QComboBox(self.widget1)
        self.pressureComboBox.setObjectName(u"pressureComboBox")
        self.pressureComboBox.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.pressureComboBox, 1, 1, 1, 3)

        self.fileComboBox = QComboBox(self.widget1)
        self.fileComboBox.setObjectName(u"fileComboBox")
        self.fileComboBox.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.fileComboBox, 0, 1, 1, 3)


        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout)

        gradientePressaoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(gradientePressaoWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 690, 21))
        gradientePressaoWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(gradientePressaoWindow)
        self.statusbar.setObjectName(u"statusbar")
        gradientePressaoWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.fluidPressureTableView, self.fileComboBox)
        QWidget.setTabOrder(self.fileComboBox, self.pressureComboBox)
        QWidget.setTabOrder(self.pressureComboBox, self.csvRadioButton)
        QWidget.setTabOrder(self.csvRadioButton, self.txtRadioButton)
        QWidget.setTabOrder(self.txtRadioButton, self.xlsxRadioButton)
        QWidget.setTabOrder(self.xlsxRadioButton, self.profMinInput)
        QWidget.setTabOrder(self.profMinInput, self.profMaxInput)
        QWidget.setTabOrder(self.profMaxInput, self.fluidClassificationBtn)
        QWidget.setTabOrder(self.fluidClassificationBtn, self.fluidPressureResults)
        QWidget.setTabOrder(self.fluidPressureResults, self.saveOutputContent)

        self.retranslateUi(gradientePressaoWindow)

        QMetaObject.connectSlotsByName(gradientePressaoWindow)
    # setupUi

    def retranslateUi(self, gradientePressaoWindow):
        gradientePressaoWindow.setWindowTitle(QCoreApplication.translate("gradientePressaoWindow", u"MainWindow", None))
        self.fluidClassificationBtn.setText(QCoreApplication.translate("gradientePressaoWindow", u"Classificar Fluidos", None))
        self.saveOutputContent.setText(QCoreApplication.translate("gradientePressaoWindow", u"Salvar output", None))
        self.label.setText(QCoreApplication.translate("gradientePressaoWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Tabela de Gradiente de Press\u00e3o</span></p></body></html>", None))
        self.groupBox.setTitle(QCoreApplication.translate("gradientePressaoWindow", u"Importa\u00e7\u00e3o do arquivo", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("gradientePressaoWindow", u"Intervalo (opcional)", None))
        self.label_4.setText(QCoreApplication.translate("gradientePressaoWindow", u"<html><head/><body><p align=\"right\">Prof. M\u00edn:</p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("gradientePressaoWindow", u"<html><head/><body><p align=\"right\">Prof. M\u00e1x:</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("gradientePressaoWindow", u"<html><head/><body><p align=\"right\">Arquivo:</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("gradientePressaoWindow", u"<html><head/><body><p align=\"right\">Unidade de press\u00e3o:</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("gradientePressaoWindow", u"<html><head/><body><p align=\"right\">Tipo de arquivo:</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.csvRadioButton.setToolTip(QCoreApplication.translate("gradientePressaoWindow", u"<html><head/><body><p>Arquivos <span style=\" font-weight:700;\">C</span>omma <span style=\" font-weight:700;\">S</span>eparated <span style=\" font-weight:700;\">V</span>alues (valores separados por v\u00edrgula) s\u00e3o arquivos comumente utilizados para armazenamento de dados.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.csvRadioButton.setText(QCoreApplication.translate("gradientePressaoWindow", u"csv", None))
#if QT_CONFIG(tooltip)
        self.txtRadioButton.setToolTip(QCoreApplication.translate("gradientePressaoWindow", u"<html><head/><body><p>Arquivos de texto no geral. Lembre-se que nesse caso, os valores devem ser separados por tabula\u00e7\u00e3o (tab)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.txtRadioButton.setText(QCoreApplication.translate("gradientePressaoWindow", u"txt", None))
#if QT_CONFIG(tooltip)
        self.xlsxRadioButton.setToolTip(QCoreApplication.translate("gradientePressaoWindow", u"<html><head/><body><p>Um arquivo .xlsx \u00e9 uma planilha eletr\u00f4nica, como no Excel.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.xlsxRadioButton.setText(QCoreApplication.translate("gradientePressaoWindow", u"xlsx", None))
    # retranslateUi

