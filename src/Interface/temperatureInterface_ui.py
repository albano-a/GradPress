# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'temperatureInterface.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QToolButton, QVBoxLayout,
    QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(1049, 762)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.importFileToolBtn = QToolButton(self.centralwidget)
        self.importFileToolBtn.setObjectName(u"importFileToolBtn")

        self.gridLayout.addWidget(self.importFileToolBtn, 0, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.minDepthInput = QLineEdit(self.centralwidget)
        self.minDepthInput.setObjectName(u"minDepthInput")

        self.gridLayout.addWidget(self.minDepthInput, 0, 4, 1, 1)

        self.inputFilePath = QLineEdit(self.centralwidget)
        self.inputFilePath.setObjectName(u"inputFilePath")

        self.gridLayout.addWidget(self.inputFilePath, 0, 2, 1, 1)

        self.maxDepthInput = QLineEdit(self.centralwidget)
        self.maxDepthInput.setObjectName(u"maxDepthInput")

        self.gridLayout.addWidget(self.maxDepthInput, 0, 5, 1, 1)

        self.configurationButton = QPushButton(self.centralwidget)
        self.configurationButton.setObjectName(u"configurationButton")

        self.gridLayout.addWidget(self.configurationButton, 0, 6, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.plotButtonTemp = QPushButton(self.centralwidget)
        self.plotButtonTemp.setObjectName(u"plotButtonTemp")

        self.verticalLayout.addWidget(self.plotButtonTemp)

        self.plotFrame = QFrame(self.centralwidget)
        self.plotFrame.setObjectName(u"plotFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.plotFrame.sizePolicy().hasHeightForWidth())
        self.plotFrame.setSizePolicy(sizePolicy1)
        self.plotFrame.setStyleSheet(u"QFrame {\n"
"	border: 1px solid #212121;\n"
"background-color: #f9f9f9;\n"
"}")
        self.plotFrame.setFrameShape(QFrame.StyledPanel)
        self.plotFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.plotFrame)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.backwardPlotButton = QPushButton(self.centralwidget)
        self.backwardPlotButton.setObjectName(u"backwardPlotButton")

        self.gridLayout_2.addWidget(self.backwardPlotButton, 0, 2, 1, 1)

        self.homePlotButton = QPushButton(self.centralwidget)
        self.homePlotButton.setObjectName(u"homePlotButton")

        self.gridLayout_2.addWidget(self.homePlotButton, 0, 0, 1, 1)

        self.configureSubplotsButton = QPushButton(self.centralwidget)
        self.configureSubplotsButton.setObjectName(u"configureSubplotsButton")

        self.gridLayout_2.addWidget(self.configureSubplotsButton, 1, 2, 1, 1)

        self.forwardPlotButton = QPushButton(self.centralwidget)
        self.forwardPlotButton.setObjectName(u"forwardPlotButton")

        self.gridLayout_2.addWidget(self.forwardPlotButton, 0, 1, 1, 1)

        self.panPlotButton = QPushButton(self.centralwidget)
        self.panPlotButton.setObjectName(u"panPlotButton")

        self.gridLayout_2.addWidget(self.panPlotButton, 1, 0, 1, 1)

        self.zoomPlotButton = QPushButton(self.centralwidget)
        self.zoomPlotButton.setObjectName(u"zoomPlotButton")

        self.gridLayout_2.addWidget(self.zoomPlotButton, 1, 1, 1, 1)

        self.editPlotButton = QPushButton(self.centralwidget)
        self.editPlotButton.setObjectName(u"editPlotButton")

        self.gridLayout_2.addWidget(self.editPlotButton, 0, 3, 1, 1)

        self.savePlotButton = QPushButton(self.centralwidget)
        self.savePlotButton.setObjectName(u"savePlotButton")

        self.gridLayout_2.addWidget(self.savePlotButton, 1, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1049, 22))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"Filename:", None))
        self.importFileToolBtn.setText(QCoreApplication.translate("mainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("mainWindow", u"Depth (Optional):", None))
        self.minDepthInput.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Min. Depth", None))
        self.inputFilePath.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Input file's path or import it...", None))
        self.maxDepthInput.setPlaceholderText(QCoreApplication.translate("mainWindow", u"Max. Depth", None))
        self.configurationButton.setText(QCoreApplication.translate("mainWindow", u"Config...", None))
        self.plotButtonTemp.setText(QCoreApplication.translate("mainWindow", u"Plot", None))
        self.backwardPlotButton.setText(QCoreApplication.translate("mainWindow", u"Backward", None))
        self.homePlotButton.setText(QCoreApplication.translate("mainWindow", u"Home", None))
        self.configureSubplotsButton.setText(QCoreApplication.translate("mainWindow", u"Configure Subplots", None))
        self.forwardPlotButton.setText(QCoreApplication.translate("mainWindow", u"Forward", None))
        self.panPlotButton.setText(QCoreApplication.translate("mainWindow", u"Pan", None))
        self.zoomPlotButton.setText(QCoreApplication.translate("mainWindow", u"Zoom", None))
        self.editPlotButton.setText(QCoreApplication.translate("mainWindow", u"Edit", None))
        self.savePlotButton.setText(QCoreApplication.translate("mainWindow", u"Save", None))
    # retranslateUi

