# Form implementation generated from reading ui file 'src/Interface/gradient.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_gradientePressaoWindow(object):
    def setupUi(self, gradientePressaoWindow):
        gradientePressaoWindow.setObjectName("gradientePressaoWindow")
        gradientePressaoWindow.resize(690, 636)
        self.centralwidget = QtWidgets.QWidget(parent=gradientePressaoWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.fluidClassificationBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.fluidClassificationBtn.setMinimumSize(QtCore.QSize(0, 20))
        self.fluidClassificationBtn.setObjectName("fluidClassificationBtn")
        self.gridLayout.addWidget(self.fluidClassificationBtn, 3, 0, 1, 1)
        self.fluidPressureResults = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.fluidPressureResults.setMaximumSize(QtCore.QSize(16777215, 80))
        self.fluidPressureResults.setObjectName("fluidPressureResults")
        self.gridLayout.addWidget(self.fluidPressureResults, 4, 0, 1, 1)
        self.saveOutputContent = QtWidgets.QPushButton(parent=self.centralwidget)
        self.saveOutputContent.setMinimumSize(QtCore.QSize(150, 20))
        self.saveOutputContent.setMaximumSize(QtCore.QSize(150, 16777215))
        self.saveOutputContent.setObjectName("saveOutputContent")
        self.gridLayout.addWidget(self.saveOutputContent, 5, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.fluidPressureTableView = QtWidgets.QTableView(parent=self.centralwidget)
        self.fluidPressureTableView.setMaximumSize(QtCore.QSize(16777215, 200))
        self.fluidPressureTableView.setObjectName("fluidPressureTableView")
        self.gridLayout.addWidget(self.fluidPressureTableView, 1, 0, 1, 2)
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 100))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setMouseTracking(True)
        self.label_6.setStyleSheet("QLabel {\n"
"    border: None\n"
"}")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.csvRadioButton = QtWidgets.QRadioButton(parent=self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.csvRadioButton.setFont(font)
        self.csvRadioButton.setObjectName("csvRadioButton")
        self.gridLayout_3.addWidget(self.csvRadioButton, 2, 1, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.txtRadioButton = QtWidgets.QRadioButton(parent=self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.txtRadioButton.setFont(font)
        self.txtRadioButton.setObjectName("txtRadioButton")
        self.gridLayout_3.addWidget(self.txtRadioButton, 2, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.xlsxRadioButton = QtWidgets.QRadioButton(parent=self.groupBox)
        self.xlsxRadioButton.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.xlsxRadioButton.setFont(font)
        self.xlsxRadioButton.setObjectName("xlsxRadioButton")
        self.gridLayout_3.addWidget(self.xlsxRadioButton, 2, 3, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.pressureComboBox = QtWidgets.QComboBox(parent=self.groupBox)
        self.pressureComboBox.setStyleSheet("")
        self.pressureComboBox.setObjectName("pressureComboBox")
        self.gridLayout_3.addWidget(self.pressureComboBox, 1, 1, 1, 3)
        self.fileComboBox = QtWidgets.QComboBox(parent=self.groupBox)
        self.fileComboBox.setStyleSheet("")
        self.fileComboBox.setObjectName("fileComboBox")
        self.gridLayout_3.addWidget(self.fileComboBox, 0, 1, 1, 3)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.profMinInput = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.profMinInput.setObjectName("profMinInput")
        self.gridLayout_2.addWidget(self.profMinInput, 0, 1, 1, 1)
        self.profMaxInput = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.profMaxInput.setObjectName("profMaxInput")
        self.gridLayout_2.addWidget(self.profMaxInput, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.gridLayout.addWidget(self.groupBox, 2, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        gradientePressaoWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=gradientePressaoWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 26))
        self.menubar.setObjectName("menubar")
        gradientePressaoWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=gradientePressaoWindow)
        self.statusbar.setObjectName("statusbar")
        gradientePressaoWindow.setStatusBar(self.statusbar)

        self.retranslateUi(gradientePressaoWindow)
        QtCore.QMetaObject.connectSlotsByName(gradientePressaoWindow)
        gradientePressaoWindow.setTabOrder(self.fluidPressureTableView, self.fileComboBox)
        gradientePressaoWindow.setTabOrder(self.fileComboBox, self.pressureComboBox)
        gradientePressaoWindow.setTabOrder(self.pressureComboBox, self.csvRadioButton)
        gradientePressaoWindow.setTabOrder(self.csvRadioButton, self.txtRadioButton)
        gradientePressaoWindow.setTabOrder(self.txtRadioButton, self.xlsxRadioButton)
        gradientePressaoWindow.setTabOrder(self.xlsxRadioButton, self.profMinInput)
        gradientePressaoWindow.setTabOrder(self.profMinInput, self.profMaxInput)
        gradientePressaoWindow.setTabOrder(self.profMaxInput, self.fluidClassificationBtn)
        gradientePressaoWindow.setTabOrder(self.fluidClassificationBtn, self.fluidPressureResults)
        gradientePressaoWindow.setTabOrder(self.fluidPressureResults, self.saveOutputContent)

    def retranslateUi(self, gradientePressaoWindow):
        _translate = QtCore.QCoreApplication.translate
        gradientePressaoWindow.setWindowTitle(_translate("gradientePressaoWindow", "MainWindow"))
        self.fluidClassificationBtn.setText(_translate("gradientePressaoWindow", "Classify"))
        self.saveOutputContent.setText(_translate("gradientePressaoWindow", "Save output"))
        self.label.setText(_translate("gradientePressaoWindow", "<html><head/><body><p align=\"center\"><span style=\"font-weight:600; text-decoration:underline;\">Pressure Gradient Table</span></p></body></html>"))
        self.groupBox.setTitle(_translate("gradientePressaoWindow", "File import"))
        self.label_2.setText(_translate("gradientePressaoWindow", "<html><head/><body><p align=\"right\">File:</p></body></html>"))
        self.label_3.setText(_translate("gradientePressaoWindow", "<html><head/><body><p align=\"right\">Pressure unit:</p></body></html>"))
        self.label_6.setText(_translate("gradientePressaoWindow", "<html><head/><body><p align=\"right\">File type:</p></body></html>"))
        self.csvRadioButton.setToolTip(_translate("gradientePressaoWindow", "<html><head/><body><p>Arquivos <span style=\" font-weight:700;\">C</span>omma <span style=\" font-weight:700;\">S</span>eparated <span style=\" font-weight:700;\">V</span>alues (valores separados por vírgula) são arquivos comumente utilizados para armazenamento de dados.</p></body></html>"))
        self.csvRadioButton.setText(_translate("gradientePressaoWindow", "csv"))
        self.txtRadioButton.setToolTip(_translate("gradientePressaoWindow", "<html><head/><body><p>Arquivos de texto no geral. Lembre-se que nesse caso, os valores devem ser separados por tabulação (tab)</p></body></html>"))
        self.txtRadioButton.setText(_translate("gradientePressaoWindow", "txt"))
        self.xlsxRadioButton.setToolTip(_translate("gradientePressaoWindow", "<html><head/><body><p>Um arquivo .xlsx é uma planilha eletrônica, como no Excel.</p></body></html>"))
        self.xlsxRadioButton.setText(_translate("gradientePressaoWindow", "xlsx"))
        self.groupBox_2.setTitle(_translate("gradientePressaoWindow", "Depth (optional)"))
        self.label_4.setText(_translate("gradientePressaoWindow", "<html><head/><body><p align=\"right\">Min. Depth:</p></body></html>"))
        self.label_5.setText(_translate("gradientePressaoWindow", "<html><head/><body><p align=\"right\">Máx. Depth:</p></body></html>"))
