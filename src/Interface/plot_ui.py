# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plot.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QToolBar, QWidget)

class Ui_SimplePlotWindow(object):
    def setupUi(self, SimplePlotWindow):
        if not SimplePlotWindow.objectName():
            SimplePlotWindow.setObjectName(u"SimplePlotWindow")
        SimplePlotWindow.resize(670, 530)
        SimplePlotWindow.setMinimumSize(QSize(670, 530))
        SimplePlotWindow.setMaximumSize(QSize(670, 530))
        icon = QIcon()
        icon.addFile(u"../icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        SimplePlotWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(SimplePlotWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.titleFrame = QFrame(self.centralwidget)
        self.titleFrame.setObjectName(u"titleFrame")
        self.titleFrame.setMaximumSize(QSize(16777215, 90))
        self.titleFrame.setAutoFillBackground(False)
        self.titleFrame.setStyleSheet(u"")
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.titleFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 631, 71))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.titleFrame, 0, 0, 1, 2)

        self.selectFileGroupBox = QGroupBox(self.centralwidget)
        self.selectFileGroupBox.setObjectName(u"selectFileGroupBox")
        self.selectFileGroupBox.setMaximumSize(QSize(16777215, 152))
        self.selectFileGroupBox.setFlat(False)
        self.selectFileGroupBox.setCheckable(False)
        self.layoutWidget = QWidget(self.selectFileGroupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 301, 121))
        self.gridLayout_2 = QGridLayout(self.layoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.selectFileComboBox = QComboBox(self.layoutWidget)
        self.selectFileComboBox.setObjectName(u"selectFileComboBox")

        self.gridLayout_2.addWidget(self.selectFileComboBox, 0, 1, 1, 3)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMouseTracking(True)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	border: None\n"
"}")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.csvRadioButton = QRadioButton(self.layoutWidget)
        self.fileButtonGroup = QButtonGroup(SimplePlotWindow)
        self.fileButtonGroup.setObjectName(u"fileButtonGroup")
        self.fileButtonGroup.addButton(self.csvRadioButton)
        self.csvRadioButton.setObjectName(u"csvRadioButton")
        font = QFont()
        font.setPointSize(10)
        self.csvRadioButton.setFont(font)

        self.gridLayout_2.addWidget(self.csvRadioButton, 1, 1, 1, 1, Qt.AlignHCenter)

        self.txtRadioButton = QRadioButton(self.layoutWidget)
        self.fileButtonGroup.addButton(self.txtRadioButton)
        self.txtRadioButton.setObjectName(u"txtRadioButton")
        self.txtRadioButton.setFont(font)

        self.gridLayout_2.addWidget(self.txtRadioButton, 1, 2, 1, 1, Qt.AlignHCenter)

        self.xlsxRadioButton = QRadioButton(self.layoutWidget)
        self.fileButtonGroup.addButton(self.xlsxRadioButton)
        self.xlsxRadioButton.setObjectName(u"xlsxRadioButton")
        self.xlsxRadioButton.setEnabled(True)
        self.xlsxRadioButton.setFont(font)

        self.gridLayout_2.addWidget(self.xlsxRadioButton, 1, 3, 1, 1, Qt.AlignHCenter)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(250, 0))
        self.label_11.setFont(font)
        self.label_11.setMouseTracking(True)
        self.label_11.setStyleSheet(u"QLabel {\n"
"	border: None\n"
"}")
        self.label_11.setWordWrap(True)

        self.gridLayout_2.addWidget(self.label_11, 2, 0, 1, 4, Qt.AlignHCenter)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(True)
        self.label_3.setStyleSheet(u"QLabel {\n"
"	border: None\n"
"}")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.selectFileGroupBox, 2, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(16777215, 132))
        self.layoutWidget1 = QWidget(self.groupBox_5)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 631, 101))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.layoutWidget1)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(250, 16777215))
        self.groupBox.setFlat(True)
        self.layoutWidget2 = QWidget(self.groupBox)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 20, 231, 71))
        self.gridLayout_4 = QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.layoutWidget2)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setPointSize(9)
        self.label_6.setFont(font1)

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1, Qt.AlignRight)

        self.inputProfMin = QLineEdit(self.layoutWidget2)
        self.inputProfMin.setObjectName(u"inputProfMin")

        self.gridLayout_4.addWidget(self.inputProfMin, 0, 1, 1, 1)

        self.label_7 = QLabel(self.layoutWidget2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1, Qt.AlignRight)

        self.inputProfMax = QLineEdit(self.layoutWidget2)
        self.inputProfMax.setObjectName(u"inputProfMax")

        self.gridLayout_4.addWidget(self.inputProfMax, 1, 1, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.layoutWidget1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFlat(True)
        self.layoutWidget3 = QWidget(self.groupBox_2)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 20, 360, 74))
        self.gridLayout_5 = QGridLayout(self.layoutWidget3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.layoutWidget3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.gridLayout_5.addWidget(self.label_12, 0, 2, 1, 1)

        self.label_10 = QLabel(self.layoutWidget3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout_5.addWidget(self.label_10, 2, 0, 1, 1)

        self.inputPlotYAxis = QLineEdit(self.layoutWidget3)
        self.inputPlotYAxis.setObjectName(u"inputPlotYAxis")

        self.gridLayout_5.addWidget(self.inputPlotYAxis, 2, 1, 1, 4)

        self.label_8 = QLabel(self.layoutWidget3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout_5.addWidget(self.label_8, 0, 0, 1, 1)

        self.inputPlotXAxis = QLineEdit(self.layoutWidget3)
        self.inputPlotXAxis.setObjectName(u"inputPlotXAxis")

        self.gridLayout_5.addWidget(self.inputPlotXAxis, 1, 1, 1, 4)

        self.inputPlotTitle = QLineEdit(self.layoutWidget3)
        self.inputPlotTitle.setObjectName(u"inputPlotTitle")
        self.inputPlotTitle.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_5.addWidget(self.inputPlotTitle, 0, 1, 1, 1)

        self.label_9 = QLabel(self.layoutWidget3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout_5.addWidget(self.label_9, 1, 0, 1, 1)

        self.lineColorComboBox = QComboBox(self.layoutWidget3)
        self.lineColorComboBox.setObjectName(u"lineColorComboBox")

        self.gridLayout_5.addWidget(self.lineColorComboBox, 0, 3, 1, 2)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.gridLayout.addWidget(self.groupBox_5, 3, 0, 1, 2)

        self.cotaRadioBtnGroupBox = QGroupBox(self.centralwidget)
        self.cotaRadioBtnGroupBox.setObjectName(u"cotaRadioBtnGroupBox")
        font2 = QFont()
        font2.setPointSize(8)
        self.cotaRadioBtnGroupBox.setFont(font2)
        self.layoutWidget4 = QWidget(self.cotaRadioBtnGroupBox)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(9, 21, 301, 121))
        self.gridLayout_3 = QGridLayout(self.layoutWidget4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.headerNao = QRadioButton(self.layoutWidget4)
        self.headerButtonGroup = QButtonGroup(SimplePlotWindow)
        self.headerButtonGroup.setObjectName(u"headerButtonGroup")
        self.headerButtonGroup.addButton(self.headerNao)
        self.headerNao.setObjectName(u"headerNao")
        self.headerNao.setFont(font)

        self.gridLayout_3.addWidget(self.headerNao, 2, 2, 1, 1)

        self.labelHeaderLines = QLabel(self.layoutWidget4)
        self.labelHeaderLines.setObjectName(u"labelHeaderLines")
        self.labelHeaderLines.setEnabled(False)
        self.labelHeaderLines.setFont(font)
        self.labelHeaderLines.setMouseTracking(True)
        self.labelHeaderLines.setStyleSheet(u"QLabel {\n"
"	border: None\n"
"}")

        self.gridLayout_3.addWidget(self.labelHeaderLines, 3, 0, 1, 1)

        self.inputHeaderLines = QLineEdit(self.layoutWidget4)
        self.inputHeaderLines.setObjectName(u"inputHeaderLines")
        self.inputHeaderLines.setEnabled(False)

        self.gridLayout_3.addWidget(self.inputHeaderLines, 3, 1, 1, 2)

        self.cotaProfSim = QRadioButton(self.layoutWidget4)
        self.cotaButtonGroup = QButtonGroup(SimplePlotWindow)
        self.cotaButtonGroup.setObjectName(u"cotaButtonGroup")
        self.cotaButtonGroup.addButton(self.cotaProfSim)
        self.cotaProfSim.setObjectName(u"cotaProfSim")
        self.cotaProfSim.setFont(font)

        self.gridLayout_3.addWidget(self.cotaProfSim, 0, 1, 1, 1)

        self.cotaProfNao = QRadioButton(self.layoutWidget4)
        self.cotaButtonGroup.addButton(self.cotaProfNao)
        self.cotaProfNao.setObjectName(u"cotaProfNao")
        self.cotaProfNao.setFont(font)

        self.gridLayout_3.addWidget(self.cotaProfNao, 0, 2, 1, 1)

        self.label_4 = QLabel(self.layoutWidget4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setMouseTracking(True)
        self.label_4.setStyleSheet(u"QLabel {\n"
"	border: None\n"
"}")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.labelMesaRotativa = QLabel(self.layoutWidget4)
        self.labelMesaRotativa.setObjectName(u"labelMesaRotativa")
        self.labelMesaRotativa.setEnabled(False)
        self.labelMesaRotativa.setFont(font)
        self.labelMesaRotativa.setMouseTracking(True)
        self.labelMesaRotativa.setStyleSheet(u"QLabel {\n"
"	border: None\n"
"}")

        self.gridLayout_3.addWidget(self.labelMesaRotativa, 1, 0, 1, 1)

        self.inputMesaRotativa = QLineEdit(self.layoutWidget4)
        self.inputMesaRotativa.setObjectName(u"inputMesaRotativa")
        self.inputMesaRotativa.setEnabled(False)

        self.gridLayout_3.addWidget(self.inputMesaRotativa, 1, 1, 1, 2)

        self.headerSim = QRadioButton(self.layoutWidget4)
        self.headerButtonGroup.addButton(self.headerSim)
        self.headerSim.setObjectName(u"headerSim")
        self.headerSim.setFont(font)

        self.gridLayout_3.addWidget(self.headerSim, 2, 1, 1, 1)

        self.label_5 = QLabel(self.layoutWidget4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setMouseTracking(True)
        self.label_5.setStyleSheet(u"QLabel {\n"
"	border: None\n"
"}")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.cotaRadioBtnGroupBox, 2, 1, 1, 1)

        self.simplePlotBtn = QPushButton(self.centralwidget)
        self.simplePlotBtn.setObjectName(u"simplePlotBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.simplePlotBtn.sizePolicy().hasHeightForWidth())
        self.simplePlotBtn.setSizePolicy(sizePolicy1)
        self.simplePlotBtn.setMinimumSize(QSize(200, 25))
        self.simplePlotBtn.setMaximumSize(QSize(16777215, 16777215))
        self.simplePlotBtn.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(171, 171, 171);\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(253, 253, 253, 255));\n"
"    border: 1px solid rgb(171, 171, 171); /* Optional: Add border color on hover */\n"
"}")

        self.gridLayout.addWidget(self.simplePlotBtn, 6, 0, 1, 2, Qt.AlignHCenter)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 5, 0, 1, 2)

        SimplePlotWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(SimplePlotWindow)
        self.statusbar.setObjectName(u"statusbar")
        SimplePlotWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(SimplePlotWindow)
        self.toolBar.setObjectName(u"toolBar")
        SimplePlotWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        QWidget.setTabOrder(self.selectFileComboBox, self.csvRadioButton)
        QWidget.setTabOrder(self.csvRadioButton, self.txtRadioButton)
        QWidget.setTabOrder(self.txtRadioButton, self.xlsxRadioButton)
        QWidget.setTabOrder(self.xlsxRadioButton, self.cotaProfSim)
        QWidget.setTabOrder(self.cotaProfSim, self.cotaProfNao)
        QWidget.setTabOrder(self.cotaProfNao, self.inputMesaRotativa)
        QWidget.setTabOrder(self.inputMesaRotativa, self.headerSim)
        QWidget.setTabOrder(self.headerSim, self.headerNao)
        QWidget.setTabOrder(self.headerNao, self.inputHeaderLines)
        QWidget.setTabOrder(self.inputHeaderLines, self.inputProfMin)
        QWidget.setTabOrder(self.inputProfMin, self.inputProfMax)
        QWidget.setTabOrder(self.inputProfMax, self.inputPlotTitle)
        QWidget.setTabOrder(self.inputPlotTitle, self.lineColorComboBox)
        QWidget.setTabOrder(self.lineColorComboBox, self.inputPlotXAxis)
        QWidget.setTabOrder(self.inputPlotXAxis, self.inputPlotYAxis)
        QWidget.setTabOrder(self.inputPlotYAxis, self.simplePlotBtn)

        self.retranslateUi(SimplePlotWindow)

        QMetaObject.connectSlotsByName(SimplePlotWindow)
    # setupUi

    def retranslateUi(self, SimplePlotWindow):
        SimplePlotWindow.setWindowTitle(QCoreApplication.translate("SimplePlotWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("SimplePlotWindow", u"<html><head/><body><p><span style=\"font-size:12pt; font-weight:600;\">Simple Plot</span></p><p><span style=\"font-size:12pt;\">Fill in the fields below to generate a simple graph, <br/>just plotting the x-axis and the y-axis</span></p><p><br/></p></body></html>", None))
        self.selectFileGroupBox.setTitle(QCoreApplication.translate("SimplePlotWindow", u"File", None))
        self.label_2.setText(QCoreApplication.translate("SimplePlotWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Select the file:</span></p></body></html>", None))
        self.csvRadioButton.setText(QCoreApplication.translate("SimplePlotWindow", u"csv", None))
        self.txtRadioButton.setText(QCoreApplication.translate("SimplePlotWindow", u"txt", None))
        self.xlsxRadioButton.setText(QCoreApplication.translate("SimplePlotWindow", u"xlsx", None))
        self.label_11.setText(QCoreApplication.translate("SimplePlotWindow", u"<html><head/><body><p align=\"center\">The accepted file formats so far are .csv and .txt. In the future, there is an intention to add support for .xlsx files.</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("SimplePlotWindow", u"<html><head/><body><p align=\"right\">File type:</p></body></html>", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("SimplePlotWindow", u"Plot Settings", None))
        self.groupBox.setTitle(QCoreApplication.translate("SimplePlotWindow", u"Depth limit", None))
        self.label_6.setText(QCoreApplication.translate("SimplePlotWindow", u"Minimum Depth:", None))
        self.label_7.setText(QCoreApplication.translate("SimplePlotWindow", u"Maximum Depth:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SimplePlotWindow", u"Title and Axis", None))
        self.label_12.setText(QCoreApplication.translate("SimplePlotWindow", u"Line color", None))
        self.label_10.setText(QCoreApplication.translate("SimplePlotWindow", u"Y axis:", None))
        self.label_8.setText(QCoreApplication.translate("SimplePlotWindow", u"Title:", None))
        self.label_9.setText(QCoreApplication.translate("SimplePlotWindow", u"X axis:", None))
        self.cotaRadioBtnGroupBox.setTitle(QCoreApplication.translate("SimplePlotWindow", u"File Settings", None))
        self.headerNao.setText(QCoreApplication.translate("SimplePlotWindow", u"No", None))
#if QT_CONFIG(statustip)
        self.labelHeaderLines.setStatusTip(QCoreApplication.translate("SimplePlotWindow", u"Se houver cabe\u00e7alho, quantas linhas pular?", None))
#endif // QT_CONFIG(statustip)
        self.labelHeaderLines.setText(QCoreApplication.translate("SimplePlotWindow", u"<html><head/><body><p align=\"right\">How many lines?:</p></body></html>", None))
        self.cotaProfSim.setText(QCoreApplication.translate("SimplePlotWindow", u"Yes", None))
        self.cotaProfNao.setText(QCoreApplication.translate("SimplePlotWindow", u"No", None))
#if QT_CONFIG(statustip)
        self.label_4.setStatusTip(QCoreApplication.translate("SimplePlotWindow", u"Profundidade em cota \u00e9 igual a mesa rotativa menos a profundidade medida.", None))
#endif // QT_CONFIG(statustip)
        self.label_4.setText(QCoreApplication.translate("SimplePlotWindow", u"<html><head/><body><p align=\"right\">TVDSS?*:</p></body></html>", None))
#if QT_CONFIG(statustip)
        self.labelMesaRotativa.setStatusTip(QCoreApplication.translate("SimplePlotWindow", u"Mesa rotativa \u00e9 a altura da plataforma at\u00e9 a superf\u00edcie do mar/superf\u00edcie terrestre.", None))
#endif // QT_CONFIG(statustip)
        self.labelMesaRotativa.setText(QCoreApplication.translate("SimplePlotWindow", u"<html><head/><body><p align=\"right\">Rotary table:</p></body></html>", None))
        self.headerSim.setText(QCoreApplication.translate("SimplePlotWindow", u"Yes", None))
#if QT_CONFIG(statustip)
        self.label_5.setStatusTip(QCoreApplication.translate("SimplePlotWindow", u"Se o arquivo possui cabe\u00e7alho. Comum em arquivos las e csv.", None))
#endif // QT_CONFIG(statustip)
        self.label_5.setText(QCoreApplication.translate("SimplePlotWindow", u"<html><head/><body><p align=\"right\">Header?:</p></body></html>", None))
        self.simplePlotBtn.setText(QCoreApplication.translate("SimplePlotWindow", u"Plot", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("SimplePlotWindow", u"toolBar", None))
    # retranslateUi

