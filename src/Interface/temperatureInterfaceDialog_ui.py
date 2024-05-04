# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'temperatureInterfaceDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_configurationPlotDialog(object):
    def setupUi(self, configurationPlotDialog):
        if not configurationPlotDialog.objectName():
            configurationPlotDialog.setObjectName(u"configurationPlotDialog")
        configurationPlotDialog.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(configurationPlotDialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(configurationPlotDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 8, 0, 1, 1)

        self.plotTitleInputTemp = QLineEdit(self.groupBox)
        self.plotTitleInputTemp.setObjectName(u"plotTitleInputTemp")

        self.gridLayout_2.addWidget(self.plotTitleInputTemp, 3, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 2, 1, 1, 1)

        self.plotStyleBox = QComboBox(self.groupBox)
        self.plotStyleBox.addItem("")
        self.plotStyleBox.addItem("")
        self.plotStyleBox.addItem("")
        self.plotStyleBox.addItem("")
        self.plotStyleBox.addItem("")
        self.plotStyleBox.addItem("")
        self.plotStyleBox.setObjectName(u"plotStyleBox")

        self.gridLayout_2.addWidget(self.plotStyleBox, 1, 0, 1, 2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)

        self.axisXInputTemp = QLineEdit(self.groupBox)
        self.axisXInputTemp.setObjectName(u"axisXInputTemp")

        self.gridLayout_2.addWidget(self.axisXInputTemp, 5, 0, 1, 2)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 2)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 6, 0, 1, 2)

        self.axisYInputTemp = QLineEdit(self.groupBox)
        self.axisYInputTemp.setObjectName(u"axisYInputTemp")

        self.gridLayout_2.addWidget(self.axisYInputTemp, 7, 0, 1, 2)

        self.fontsizeInputTemp = QLineEdit(self.groupBox)
        self.fontsizeInputTemp.setObjectName(u"fontsizeInputTemp")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontsizeInputTemp.sizePolicy().hasHeightForWidth())
        self.fontsizeInputTemp.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.fontsizeInputTemp, 3, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.tempDialogButtonBox = QDialogButtonBox(configurationPlotDialog)
        self.tempDialogButtonBox.setObjectName(u"tempDialogButtonBox")
        self.tempDialogButtonBox.setOrientation(Qt.Vertical)
        self.tempDialogButtonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.tempDialogButtonBox)


        self.retranslateUi(configurationPlotDialog)
        self.tempDialogButtonBox.accepted.connect(configurationPlotDialog.accept)
        self.tempDialogButtonBox.rejected.connect(configurationPlotDialog.reject)

        QMetaObject.connectSlotsByName(configurationPlotDialog)
    # setupUi

    def retranslateUi(self, configurationPlotDialog):
        configurationPlotDialog.setWindowTitle(QCoreApplication.translate("configurationPlotDialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("configurationPlotDialog", u"Configure", None))
        self.label_2.setText(QCoreApplication.translate("configurationPlotDialog", u"Plot Title", None))
        self.label_5.setText(QCoreApplication.translate("configurationPlotDialog", u"Fontsize", None))
        self.plotStyleBox.setItemText(0, QCoreApplication.translate("configurationPlotDialog", u"default", None))
        self.plotStyleBox.setItemText(1, QCoreApplication.translate("configurationPlotDialog", u"classic", None))
        self.plotStyleBox.setItemText(2, QCoreApplication.translate("configurationPlotDialog", u"bmh", None))
        self.plotStyleBox.setItemText(3, QCoreApplication.translate("configurationPlotDialog", u"ggplot", None))
        self.plotStyleBox.setItemText(4, QCoreApplication.translate("configurationPlotDialog", u"fivethirtyeight", None))
        self.plotStyleBox.setItemText(5, QCoreApplication.translate("configurationPlotDialog", u"seaborn-v0_8", None))

        self.label.setText(QCoreApplication.translate("configurationPlotDialog", u"Plot Style", None))
        self.axisXInputTemp.setPlaceholderText(QCoreApplication.translate("configurationPlotDialog", u"Temperatura (F/C)", None))
        self.label_3.setText(QCoreApplication.translate("configurationPlotDialog", u"X Axis Label", None))
        self.label_4.setText(QCoreApplication.translate("configurationPlotDialog", u"Y Axis Label", None))
        self.axisYInputTemp.setPlaceholderText(QCoreApplication.translate("configurationPlotDialog", u"TVDSS (m)", None))
        self.fontsizeInputTemp.setPlaceholderText(QCoreApplication.translate("configurationPlotDialog", u"11, 12, ...", None))
    # retranslateUi

