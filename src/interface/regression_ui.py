# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'regression.ui'
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
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QStatusBar,
    QTextBrowser, QWidget)
import icons_rc

class Ui_plotTendenciaWindow(object):
    def setupUi(self, plotTendenciaWindow):
        if not plotTendenciaWindow.objectName():
            plotTendenciaWindow.setObjectName(u"plotTendenciaWindow")
        plotTendenciaWindow.resize(668, 730)
        plotTendenciaWindow.setMinimumSize(QSize(668, 720))
        plotTendenciaWindow.setMaximumSize(QSize(668, 730))
        icon = QIcon()
        icon.addFile(u"../icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        plotTendenciaWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(plotTendenciaWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.layoutWidget = QWidget(self.groupBox_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 631, 121))
        self.gridLayout_3 = QGridLayout(self.layoutWidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMouseTracking(True)
        self.label_4.setStyleSheet(u"QLabel {\n"
"	border: None\n"
"}")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.inputPressureUnit = QComboBox(self.layoutWidget)
        self.inputPressureUnit.setObjectName(u"inputPressureUnit")

        self.gridLayout_3.addWidget(self.inputPressureUnit, 0, 1, 1, 2)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 40))
        self.label_6.setMouseTracking(True)
        self.label_6.setStyleSheet(u"QLabel {\n"
"	border: None\n"
"}")

        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 3)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMouseTracking(True)
        self.label_5.setStyleSheet(u"QLabel {\n"
"	border: None\n"
"}")

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.agrupamentoSpinBox = QSpinBox(self.layoutWidget)
        self.agrupamentoSpinBox.setObjectName(u"agrupamentoSpinBox")
        self.agrupamentoSpinBox.setMaximum(5)
        self.agrupamentoSpinBox.setValue(0)

        self.gridLayout_3.addWidget(self.agrupamentoSpinBox, 2, 1, 1, 2)


        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 2)

        self.cotaRadioBtnGroupBox = QGroupBox(self.centralwidget)
        self.cotaRadioBtnGroupBox.setObjectName(u"cotaRadioBtnGroupBox")
        font = QFont()
        font.setPointSize(8)
        self.cotaRadioBtnGroupBox.setFont(font)
        self.cotaRadioBtnGroupBox.setStyleSheet(u"QGroupBox {\n"
"	background-color: #ededed;\n"
"}")
        self.layoutWidget_2 = QWidget(self.cotaRadioBtnGroupBox)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(9, 21, 301, 100))
        self.gridLayout_8 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.layoutWidget_2)
        self.label_18.setObjectName(u"label_18")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_18.setFont(font1)
        self.label_18.setMouseTracking(True)
        self.label_18.setStyleSheet(u"QLabel {\n"
"	border: None\n"
"}")

        self.gridLayout_8.addWidget(self.label_18, 0, 0, 1, 1)

        self.cotaProfSim = QRadioButton(self.layoutWidget_2)
        self.cotaButtonGroup = QButtonGroup(plotTendenciaWindow)
        self.cotaButtonGroup.setObjectName(u"cotaButtonGroup")
        self.cotaButtonGroup.addButton(self.cotaProfSim)
        self.cotaProfSim.setObjectName(u"cotaProfSim")
        self.cotaProfSim.setFont(font1)

        self.gridLayout_8.addWidget(self.cotaProfSim, 0, 1, 1, 1)

        self.cotaProfNao = QRadioButton(self.layoutWidget_2)
        self.cotaButtonGroup.addButton(self.cotaProfNao)
        self.cotaProfNao.setObjectName(u"cotaProfNao")
        self.cotaProfNao.setFont(font1)

        self.gridLayout_8.addWidget(self.cotaProfNao, 0, 2, 1, 1)

        self.labelMesaRotativa = QLabel(self.layoutWidget_2)
        self.labelMesaRotativa.setObjectName(u"labelMesaRotativa")
        self.labelMesaRotativa.setEnabled(False)
        self.labelMesaRotativa.setFont(font1)
        self.labelMesaRotativa.setMouseTracking(True)
        self.labelMesaRotativa.setStyleSheet(u"QLabel {\n"
"	border: None\n"
"}")

        self.gridLayout_8.addWidget(self.labelMesaRotativa, 1, 0, 1, 1)

        self.inputMesaRotativa = QLineEdit(self.layoutWidget_2)
        self.inputMesaRotativa.setObjectName(u"inputMesaRotativa")
        self.inputMesaRotativa.setEnabled(False)

        self.gridLayout_8.addWidget(self.inputMesaRotativa, 1, 1, 1, 2)

        self.label_19 = QLabel(self.layoutWidget_2)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)
        self.label_19.setMouseTracking(True)
        self.label_19.setStyleSheet(u"QLabel {\n"
"	border: None\n"
"}")

        self.gridLayout_8.addWidget(self.label_19, 2, 0, 1, 1)

        self.headerSim = QRadioButton(self.layoutWidget_2)
        self.headerButtonGroup = QButtonGroup(plotTendenciaWindow)
        self.headerButtonGroup.setObjectName(u"headerButtonGroup")
        self.headerButtonGroup.addButton(self.headerSim)
        self.headerSim.setObjectName(u"headerSim")
        self.headerSim.setFont(font1)

        self.gridLayout_8.addWidget(self.headerSim, 2, 1, 1, 1)

        self.headerNao = QRadioButton(self.layoutWidget_2)
        self.headerButtonGroup.addButton(self.headerNao)
        self.headerNao.setObjectName(u"headerNao")
        self.headerNao.setFont(font1)

        self.gridLayout_8.addWidget(self.headerNao, 2, 2, 1, 1)

        self.labelHeaderLines = QLabel(self.layoutWidget_2)
        self.labelHeaderLines.setObjectName(u"labelHeaderLines")
        self.labelHeaderLines.setEnabled(False)
        self.labelHeaderLines.setFont(font1)
        self.labelHeaderLines.setMouseTracking(True)
        self.labelHeaderLines.setStyleSheet(u"QLabel {\n"
"	border: None\n"
"}")

        self.gridLayout_8.addWidget(self.labelHeaderLines, 3, 0, 1, 1)

        self.inputHeaderLines = QLineEdit(self.layoutWidget_2)
        self.inputHeaderLines.setObjectName(u"inputHeaderLines")
        self.inputHeaderLines.setEnabled(False)

        self.gridLayout_8.addWidget(self.inputHeaderLines, 3, 1, 1, 2)


        self.gridLayout.addWidget(self.cotaRadioBtnGroupBox, 1, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMaximumSize(QSize(16777215, 132))
        self.groupBox_5.setStyleSheet(u"QGroupBox {\n"
"	background-color: #ededed;\n"
"}")
        self.layoutWidget_4 = QWidget(self.groupBox_5)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 20, 631, 101))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_8 = QGroupBox(self.layoutWidget_4)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMaximumSize(QSize(250, 16777215))
        self.layoutWidget_5 = QWidget(self.groupBox_8)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(10, 20, 231, 71))
        self.gridLayout_6 = QGridLayout(self.layoutWidget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget_5)
        self.label_11.setObjectName(u"label_11")
        font2 = QFont()
        font2.setPointSize(9)
        self.label_11.setFont(font2)

        self.gridLayout_6.addWidget(self.label_11, 0, 0, 1, 1, Qt.AlignRight)

        self.inputProfMin = QLineEdit(self.layoutWidget_5)
        self.inputProfMin.setObjectName(u"inputProfMin")

        self.gridLayout_6.addWidget(self.inputProfMin, 0, 1, 1, 1)

        self.label_13 = QLabel(self.layoutWidget_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)

        self.gridLayout_6.addWidget(self.label_13, 1, 0, 1, 1, Qt.AlignRight)

        self.inputProfMax = QLineEdit(self.layoutWidget_5)
        self.inputProfMax.setObjectName(u"inputProfMax")

        self.gridLayout_6.addWidget(self.inputProfMax, 1, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.groupBox_8)

        self.groupBox_9 = QGroupBox(self.layoutWidget_4)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.layoutWidget_6 = QWidget(self.groupBox_9)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(10, 20, 360, 74))
        self.gridLayout_7 = QGridLayout(self.layoutWidget_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.layoutWidget_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setEnabled(False)
        self.label_14.setFont(font2)

        self.gridLayout_7.addWidget(self.label_14, 0, 2, 1, 1)

        self.label_15 = QLabel(self.layoutWidget_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font2)

        self.gridLayout_7.addWidget(self.label_15, 2, 0, 1, 1)

        self.inputPlotYAxis = QLineEdit(self.layoutWidget_6)
        self.inputPlotYAxis.setObjectName(u"inputPlotYAxis")

        self.gridLayout_7.addWidget(self.inputPlotYAxis, 2, 1, 1, 4)

        self.label_16 = QLabel(self.layoutWidget_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)

        self.gridLayout_7.addWidget(self.label_16, 0, 0, 1, 1)

        self.inputPlotXAxis = QLineEdit(self.layoutWidget_6)
        self.inputPlotXAxis.setObjectName(u"inputPlotXAxis")

        self.gridLayout_7.addWidget(self.inputPlotXAxis, 1, 1, 1, 4)

        self.inputPlotTitle = QLineEdit(self.layoutWidget_6)
        self.inputPlotTitle.setObjectName(u"inputPlotTitle")
        self.inputPlotTitle.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_7.addWidget(self.inputPlotTitle, 0, 1, 1, 1)

        self.label_17 = QLabel(self.layoutWidget_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)

        self.gridLayout_7.addWidget(self.label_17, 1, 0, 1, 1)

        self.lineColorComboBox = QComboBox(self.layoutWidget_6)
        self.lineColorComboBox.setObjectName(u"lineColorComboBox")
        self.lineColorComboBox.setEnabled(False)

        self.gridLayout_7.addWidget(self.lineColorComboBox, 0, 3, 1, 2)


        self.horizontalLayout_2.addWidget(self.groupBox_9)


        self.gridLayout.addWidget(self.groupBox_5, 3, 0, 1, 2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamilies([u"Roboto"])
        font3.setPointSize(12)
        self.label.setFont(font3)
        self.label.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2)

        self.selectFileGroupBox = QGroupBox(self.centralwidget)
        self.selectFileGroupBox.setObjectName(u"selectFileGroupBox")
        self.selectFileGroupBox.setMinimumSize(QSize(0, 130))
        self.selectFileGroupBox.setMaximumSize(QSize(16777215, 152))
        self.selectFileGroupBox.setStyleSheet(u"QGroupBox {\n"
"	background-color: #ededed;\n"
"}")
        self.selectFileGroupBox.setFlat(False)
        self.selectFileGroupBox.setCheckable(False)
        self.layoutWidget1 = QWidget(self.selectFileGroupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 291, 121))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setMouseTracking(True)
        self.label_3.setStyleSheet(u"QLabel {\n"
"	border: None\n"
"}")

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.txtRadioButton = QRadioButton(self.layoutWidget1)
        self.fileButtonGroup = QButtonGroup(plotTendenciaWindow)
        self.fileButtonGroup.setObjectName(u"fileButtonGroup")
        self.fileButtonGroup.addButton(self.txtRadioButton)
        self.txtRadioButton.setObjectName(u"txtRadioButton")
        self.txtRadioButton.setFont(font1)

        self.gridLayout_2.addWidget(self.txtRadioButton, 1, 2, 1, 1, Qt.AlignHCenter)

        self.xlsxRadioButton = QRadioButton(self.layoutWidget1)
        self.fileButtonGroup.addButton(self.xlsxRadioButton)
        self.xlsxRadioButton.setObjectName(u"xlsxRadioButton")
        self.xlsxRadioButton.setEnabled(True)
        self.xlsxRadioButton.setFont(font1)

        self.gridLayout_2.addWidget(self.xlsxRadioButton, 1, 3, 1, 1, Qt.AlignHCenter)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMouseTracking(True)
        self.label_2.setStyleSheet(u"QLabel {\n"
"	border: None\n"
"}")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.selectFileComboBox = QComboBox(self.layoutWidget1)
        self.selectFileComboBox.setObjectName(u"selectFileComboBox")

        self.gridLayout_2.addWidget(self.selectFileComboBox, 0, 1, 1, 3)

        self.csvRadioButton = QRadioButton(self.layoutWidget1)
        self.fileButtonGroup.addButton(self.csvRadioButton)
        self.csvRadioButton.setObjectName(u"csvRadioButton")
        self.csvRadioButton.setFont(font1)

        self.gridLayout_2.addWidget(self.csvRadioButton, 1, 1, 1, 1, Qt.AlignHCenter)

        self.label_12 = QLabel(self.layoutWidget1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setMouseTracking(True)
        self.label_12.setStyleSheet(u"QLabel {\n"
"	border: None\n"
"}")

        self.gridLayout_2.addWidget(self.label_12, 2, 0, 1, 4)


        self.gridLayout.addWidget(self.selectFileGroupBox, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(100, 50))
        self.frame_4.setMaximumSize(QSize(16777215, 40))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tendenciaPlotBtn = QPushButton(self.frame_4)
        self.tendenciaPlotBtn.setObjectName(u"tendenciaPlotBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tendenciaPlotBtn.sizePolicy().hasHeightForWidth())
        self.tendenciaPlotBtn.setSizePolicy(sizePolicy1)
        self.tendenciaPlotBtn.setMinimumSize(QSize(200, 25))
        self.tendenciaPlotBtn.setMaximumSize(QSize(200, 16777215))
        self.tendenciaPlotBtn.setStyleSheet(u"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(171, 171, 171);\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(253, 253, 253, 255));\n"
"    border: 1px solid rgb(171, 171, 171); /* Optional: Add border color on hover */\n"
"}")

        self.horizontalLayout.addWidget(self.tendenciaPlotBtn)


        self.gridLayout.addWidget(self.frame_4, 4, 0, 1, 2)

        self.outputAfterPlotted = QTextBrowser(self.centralwidget)
        self.outputAfterPlotted.setObjectName(u"outputAfterPlotted")
        self.outputAfterPlotted.setMaximumSize(QSize(16777215, 50))

        self.gridLayout.addWidget(self.outputAfterPlotted, 5, 0, 1, 2)

        plotTendenciaWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(plotTendenciaWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 668, 21))
        plotTendenciaWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(plotTendenciaWindow)
        self.statusbar.setObjectName(u"statusbar")
        plotTendenciaWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.selectFileComboBox, self.csvRadioButton)
        QWidget.setTabOrder(self.csvRadioButton, self.txtRadioButton)
        QWidget.setTabOrder(self.txtRadioButton, self.xlsxRadioButton)
        QWidget.setTabOrder(self.xlsxRadioButton, self.cotaProfSim)
        QWidget.setTabOrder(self.cotaProfSim, self.cotaProfNao)
        QWidget.setTabOrder(self.cotaProfNao, self.inputMesaRotativa)
        QWidget.setTabOrder(self.inputMesaRotativa, self.headerSim)
        QWidget.setTabOrder(self.headerSim, self.headerNao)
        QWidget.setTabOrder(self.headerNao, self.inputHeaderLines)
        QWidget.setTabOrder(self.inputHeaderLines, self.inputPressureUnit)
        QWidget.setTabOrder(self.inputPressureUnit, self.agrupamentoSpinBox)
        QWidget.setTabOrder(self.agrupamentoSpinBox, self.inputProfMin)
        QWidget.setTabOrder(self.inputProfMin, self.inputProfMax)
        QWidget.setTabOrder(self.inputProfMax, self.inputPlotTitle)
        QWidget.setTabOrder(self.inputPlotTitle, self.inputPlotXAxis)
        QWidget.setTabOrder(self.inputPlotXAxis, self.inputPlotYAxis)
        QWidget.setTabOrder(self.inputPlotYAxis, self.lineColorComboBox)
        QWidget.setTabOrder(self.lineColorComboBox, self.tendenciaPlotBtn)
        QWidget.setTabOrder(self.tendenciaPlotBtn, self.outputAfterPlotted)

        self.retranslateUi(plotTendenciaWindow)

        QMetaObject.connectSlotsByName(plotTendenciaWindow)
    # setupUi

    def retranslateUi(self, plotTendenciaWindow):
        plotTendenciaWindow.setWindowTitle(QCoreApplication.translate("plotTendenciaWindow", u"MainWindow", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("plotTendenciaWindow", u"Configura\u00e7\u00f5es das Linhas de T\u00eandencia", None))
        self.label_4.setText(QCoreApplication.translate("plotTendenciaWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Unidade de Press\u00e3o*:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.inputPressureUnit.setToolTip(QCoreApplication.translate("plotTendenciaWindow", u"A unidade de press\u00e3o dos dados carregados.", None))
#endif // QT_CONFIG(tooltip)
        self.label_6.setText(QCoreApplication.translate("plotTendenciaWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Para se realizada o plot das linhas de tend\u00eancia, \u00e9 necess\u00e1rio dividir <br/>o dado em agrupamentos, sendo o padr\u00e3o dividir em 2 agrupamentos.</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("plotTendenciaWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Agrupamento (cluster) dos dados*:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.agrupamentoSpinBox.setToolTip(QCoreApplication.translate("plotTendenciaWindow", u"Agrupamentos (Cluster) dos dados.", None))
#endif // QT_CONFIG(tooltip)
        self.cotaRadioBtnGroupBox.setTitle(QCoreApplication.translate("plotTendenciaWindow", u"Configura\u00e7\u00f5es dos dados", None))
#if QT_CONFIG(statustip)
        self.label_18.setStatusTip(QCoreApplication.translate("plotTendenciaWindow", u"Profundidade em cota \u00e9 igual a mesa rotativa menos a profundidade medida.", None))
#endif // QT_CONFIG(statustip)
        self.label_18.setText(QCoreApplication.translate("plotTendenciaWindow", u"<html><head/><body><p align=\"right\">Profundidade em cota?*:</p></body></html>", None))
        self.cotaProfSim.setText(QCoreApplication.translate("plotTendenciaWindow", u"Sim", None))
        self.cotaProfNao.setText(QCoreApplication.translate("plotTendenciaWindow", u"N\u00e3o", None))
#if QT_CONFIG(statustip)
        self.labelMesaRotativa.setStatusTip(QCoreApplication.translate("plotTendenciaWindow", u"Mesa rotativa \u00e9 a altura da plataforma at\u00e9 a superf\u00edcie do mar/superf\u00edcie terrestre.", None))
#endif // QT_CONFIG(statustip)
        self.labelMesaRotativa.setText(QCoreApplication.translate("plotTendenciaWindow", u"<html><head/><body><p align=\"right\">Mesa Rotativa*:</p></body></html>", None))
#if QT_CONFIG(statustip)
        self.label_19.setStatusTip(QCoreApplication.translate("plotTendenciaWindow", u"Se o arquivo possui cabe\u00e7alho. Comum em arquivos las e csv.", None))
#endif // QT_CONFIG(statustip)
        self.label_19.setText(QCoreApplication.translate("plotTendenciaWindow", u"<html><head/><body><p align=\"right\">Cabe\u00e7alho?*:</p></body></html>", None))
        self.headerSim.setText(QCoreApplication.translate("plotTendenciaWindow", u"Sim", None))
        self.headerNao.setText(QCoreApplication.translate("plotTendenciaWindow", u"N\u00e3o", None))
#if QT_CONFIG(statustip)
        self.labelHeaderLines.setStatusTip(QCoreApplication.translate("plotTendenciaWindow", u"Se houver cabe\u00e7alho, quantas linhas pular?", None))
#endif // QT_CONFIG(statustip)
        self.labelHeaderLines.setText(QCoreApplication.translate("plotTendenciaWindow", u"<html><head/><body><p align=\"right\">Quantas linhas?*:</p></body></html>", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("plotTendenciaWindow", u"Configura\u00e7\u00f5es do Gr\u00e1fico", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("plotTendenciaWindow", u"Limitar a Profundidade", None))
        self.label_11.setText(QCoreApplication.translate("plotTendenciaWindow", u"Profundidade M\u00ednima:", None))
        self.label_13.setText(QCoreApplication.translate("plotTendenciaWindow", u"Profundidade M\u00e1xima:", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("plotTendenciaWindow", u"T\u00edtulo e eixos do gr\u00e1fico", None))
        self.label_14.setText(QCoreApplication.translate("plotTendenciaWindow", u"Cor da Linha", None))
        self.label_15.setText(QCoreApplication.translate("plotTendenciaWindow", u"Eixo y:", None))
        self.label_16.setText(QCoreApplication.translate("plotTendenciaWindow", u"T\u00edtulo:", None))
        self.label_17.setText(QCoreApplication.translate("plotTendenciaWindow", u"Eixo x:", None))
        self.label.setText(QCoreApplication.translate("plotTendenciaWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:696;\">Determina\u00e7\u00e3o do contato de fluidos</span></p><p><span style=\" font-size:10pt;\">Para determina\u00e7\u00e3o do contato entre os fluidos, usou-se de aprendizado de m\u00e1quina para fazer a divis\u00e3o dos dados, e tamb\u00e9m utilizou-se das press\u00f5es de fluido para an\u00e1lise parcial dos tipos de fluidos.</span></p></body></html>", None))
        self.selectFileGroupBox.setTitle(QCoreApplication.translate("plotTendenciaWindow", u"Arquivo", None))
        self.label_3.setText(QCoreApplication.translate("plotTendenciaWindow", u"<html><head/><body><p align=\"right\">Tipo de arquivo:</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.txtRadioButton.setToolTip(QCoreApplication.translate("plotTendenciaWindow", u"<html><head/><body><p>Arquivos de texto no geral. Lembre-se que nesse caso, os valores devem ser separados por tabula\u00e7\u00e3o (tab)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.txtRadioButton.setText(QCoreApplication.translate("plotTendenciaWindow", u"txt", None))
#if QT_CONFIG(tooltip)
        self.xlsxRadioButton.setToolTip(QCoreApplication.translate("plotTendenciaWindow", u"<html><head/><body><p>Um arquivo .xlsx \u00e9 uma planilha eletr\u00f4nica, como no Excel.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.xlsxRadioButton.setText(QCoreApplication.translate("plotTendenciaWindow", u"xlsx", None))
        self.label_2.setText(QCoreApplication.translate("plotTendenciaWindow", u"<html><head/><body><p align=\"right\"><span style=\" font-size:10pt;\">Selecione o arquivo:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.csvRadioButton.setToolTip(QCoreApplication.translate("plotTendenciaWindow", u"<html><head/><body><p>Arquivos <span style=\" font-weight:700;\">C</span>omma <span style=\" font-weight:700;\">S</span>eparated <span style=\" font-weight:700;\">V</span>alues (valores separados por v\u00edrgula) s\u00e3o arquivos comumente utilizados para armazenamento de dados.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.csvRadioButton.setText(QCoreApplication.translate("plotTendenciaWindow", u"csv", None))
        self.label_12.setText(QCoreApplication.translate("plotTendenciaWindow", u"<html><head/><body><p align=\"center\">Arquivos aceitos at\u00e9 agora s\u00e3o o .csv e .txt. <br/>Futuramente h\u00e1 a pretens\u00e3o de colocar <br> suporte a arquivos .xlsx</p></body></html>", None))
        self.tendenciaPlotBtn.setText(QCoreApplication.translate("plotTendenciaWindow", u"Plotar", None))
#if QT_CONFIG(statustip)
        self.outputAfterPlotted.setStatusTip(QCoreApplication.translate("plotTendenciaWindow", u"A profundidade do contato entre os fluidos aparecer\u00e1 nessa \u00e1rea ap\u00f3s o plot.", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.outputAfterPlotted.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.outputAfterPlotted.setHtml(QCoreApplication.translate("plotTendenciaWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.outputAfterPlotted.setPlaceholderText(QCoreApplication.translate("plotTendenciaWindow", u"A profundidade do contato entre os fluidos aparecer\u00e1 nessa \u00e1rea ap\u00f3s o plot.", None))
    # retranslateUi

