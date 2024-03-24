# Form implementation generated from reading ui file 'ui/maingui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(916, 685)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(500, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../icon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mainSheetTable = QtWidgets.QTableWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainSheetTable.sizePolicy().hasHeightForWidth())
        self.mainSheetTable.setSizePolicy(sizePolicy)
        self.mainSheetTable.setAutoFillBackground(False)
        self.mainSheetTable.setStyleSheet("/* Table background and borders */\n"
"QTableWidget {\n"
"    background-color: #ffffff; /* Cor de fundo branca */\n"
"    border: 1px solid #000000; /* Borda preta */\n"
"    border-radius: 0px; /* Sem arredondamento de cantos */\n"
"    gridline-color: #d4d4d4; /* Cor das linhas da grade */\n"
"}\n"
"\n"
"/* Styling for table items */\n"
"QTableWidget::item {\n"
"    border: none; /* Sem borda */\n"
"    color: #000000; /* Cor do texto preto */\n"
"    font-size: 10pt; /* Tamanho da fonte */\n"
"}\n"
"\n"
"/* Hover effect on table items */\n"
"QTableWidget::item:hover {\n"
"    background-color: #d9e4f7; /* Cor de fundo azul claro ao passar o mouse */\n"
"}\n"
"\n"
"/* Styling for header sections */\n"
"QHeaderView::section {\n"
"    background-color: #63BE7B ; /* Cor de fundo cinza claro */\n"
"    color: #000000; /* Cor do texto preto */\n"
"    font-weight: bold; /* Texto em negrito */\n"
"    border: 1px solid #82CB95 ; /* Borda cinza */\n"
"    padding: 4px; /* Preenchimento interno */\n"
"}\n"
"\n"
"/* Selected items */\n"
"QTableWidget::item:selected {\n"
"    border: 1px solid #aeaeae; /* Cor de fundo azul escuro para itens selecionados */\n"
"    background-color: #e3e3e3;\n"
"}\n"
"")
        self.mainSheetTable.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.mainSheetTable.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.mainSheetTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.mainSheetTable.setDragDropMode(QtWidgets.QAbstractItemView.DragDropMode.DragDrop)
        self.mainSheetTable.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.mainSheetTable.setRowCount(100)
        self.mainSheetTable.setColumnCount(24)
        self.mainSheetTable.setObjectName("mainSheetTable")
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(23, item)
        self.mainSheetTable.horizontalHeader().setDefaultSectionSize(100)
        self.mainSheetTable.horizontalHeader().setSortIndicatorShown(False)
        self.mainSheetTable.verticalHeader().setDefaultSectionSize(22)
        self.mainSheetTable.verticalHeader().setMinimumSectionSize(22)
        self.mainSheetTable.verticalHeader().setSortIndicatorShown(False)
        self.verticalLayout_3.addWidget(self.mainSheetTable)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.configSheetTable = QtWidgets.QFrame(parent=self.centralwidget)
        self.configSheetTable.setMinimumSize(QtCore.QSize(0, 65))
        self.configSheetTable.setMaximumSize(QtCore.QSize(16777215, 100))
        self.configSheetTable.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.configSheetTable.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.configSheetTable.setObjectName("configSheetTable")
        self.changeTextColorBtn = QtWidgets.QPushButton(parent=self.configSheetTable)
        self.changeTextColorBtn.setGeometry(QtCore.QRect(320, 20, 41, 31))
        self.changeTextColorBtn.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(171, 171, 171);\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"    transition: background-color 0.3s ease; /* Add transition effect */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(253, 253, 253, 255));\n"
"    border: 1px solid rgb(171, 171, 171); /* Optional: Add border color on hover */\n"
"}\n"
"")
        self.changeTextColorBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui\\../img/icons/font_color.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.changeTextColorBtn.setIcon(icon1)
        self.changeTextColorBtn.setObjectName("changeTextColorBtn")
        self.changeCellColorBtn = QtWidgets.QPushButton(parent=self.configSheetTable)
        self.changeCellColorBtn.setGeometry(QtCore.QRect(370, 20, 41, 31))
        self.changeCellColorBtn.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(171, 171, 171);\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(253, 253, 253, 255));\n"
"    border: 1px solid rgb(171, 171, 171); /* Optional: Add border color on hover */\n"
"}")
        self.changeCellColorBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("ui\\../img/icons/fill_color.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.changeCellColorBtn.setIcon(icon2)
        self.changeCellColorBtn.setIconSize(QtCore.QSize(24, 24))
        self.changeCellColorBtn.setObjectName("changeCellColorBtn")
        self.layoutWidget_2 = QtWidgets.QWidget(parent=self.configSheetTable)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 20, 301, 27))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.addRowBtn = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addRowBtn.setFont(font)
        self.addRowBtn.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(171, 171, 171);\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(253, 253, 253, 255));\n"
"    border: 1px solid rgb(171, 171, 171); /* Optional: Add border color on hover */\n"
"}")
        self.addRowBtn.setObjectName("addRowBtn")
        self.horizontalLayout_3.addWidget(self.addRowBtn)
        self.row_label_2 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.row_label_2.setFont(font)
        self.row_label_2.setObjectName("row_label_2")
        self.horizontalLayout_3.addWidget(self.row_label_2)
        self.rmRowBtn = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rmRowBtn.setFont(font)
        self.rmRowBtn.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(171, 171, 171);\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(253, 253, 253, 255));\n"
"    border: 1px solid rgb(171, 171, 171); /* Optional: Add border color on hover */\n"
"}")
        self.rmRowBtn.setObjectName("rmRowBtn")
        self.horizontalLayout_3.addWidget(self.rmRowBtn)
        self.addColBtn = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.addColBtn.setFont(font)
        self.addColBtn.setStyleSheet("QPushButton {\n"
"    border-radius:15px;\n"
"    border: 1px solid rgb(171, 171, 171);\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(253, 253, 253, 255));\n"
"    border: 1px solid rgb(171, 171, 171); /* Optional: Add border color on hover */\n"
"}")
        self.addColBtn.setObjectName("addColBtn")
        self.horizontalLayout_3.addWidget(self.addColBtn)
        self.col_label_2 = QtWidgets.QLabel(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.col_label_2.setFont(font)
        self.col_label_2.setObjectName("col_label_2")
        self.horizontalLayout_3.addWidget(self.col_label_2)
        self.rmColBtn = QtWidgets.QPushButton(parent=self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.rmColBtn.setFont(font)
        self.rmColBtn.setStyleSheet("QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(171, 171, 171);\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(253, 253, 253, 255), stop:1 rgba(239, 239, 239, 255));\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(239, 239, 239, 255), stop:1 rgba(253, 253, 253, 255));\n"
"    border: 1px solid rgb(171, 171, 171); /* Optional: Add border color on hover */\n"
"}")
        self.rmColBtn.setObjectName("rmColBtn")
        self.horizontalLayout_3.addWidget(self.rmColBtn)
        self.verticalLayout.addWidget(self.configSheetTable)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEditar = QtWidgets.QMenu(parent=self.menubar)
        self.menuEditar.setObjectName("menuEditar")
        self.menuCalcular = QtWidgets.QMenu(parent=self.menubar)
        self.menuCalcular.setObjectName("menuCalcular")
        self.menuSobre = QtWidgets.QMenu(parent=self.menubar)
        self.menuSobre.setObjectName("menuSobre")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(parent=MainWindow)
        self.toolBar_2.setStyleSheet("QToolBar {\n"
"    icon-size: 32px; /* Set the icon size */\n"
"    spacing: 10px; /* Set the spacing between items */\n"
"}")
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar_2)
        self.actionNew = QtGui.QAction(parent=MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionAbrir = QtGui.QAction(parent=MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionSalvar = QtGui.QAction(parent=MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionSair = QtGui.QAction(parent=MainWindow)
        self.actionSair.setObjectName("actionSair")
        self.actionGerenciar_Arquivos = QtGui.QAction(parent=MainWindow)
        self.actionGerenciar_Arquivos.setObjectName("actionGerenciar_Arquivos")
        self.actionEditor_de_Texto = QtGui.QAction(parent=MainWindow)
        self.actionEditor_de_Texto.setObjectName("actionEditor_de_Texto")
        self.actionCalculadora = QtGui.QAction(parent=MainWindow)
        self.actionCalculadora.setObjectName("actionCalculadora")
        self.actionTOMI_index = QtGui.QAction(parent=MainWindow)
        self.actionTOMI_index.setObjectName("actionTOMI_index")
        self.actionAjuda = QtGui.QAction(parent=MainWindow)
        self.actionAjuda.setObjectName("actionAjuda")
        self.actionSobre = QtGui.QAction(parent=MainWindow)
        self.actionSobre.setObjectName("actionSobre")
        self.newFileToolbar = QtGui.QAction(parent=MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("ui\\../img/icons/new_file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.newFileToolbar.setIcon(icon3)
        self.newFileToolbar.setObjectName("newFileToolbar")
        self.actionAbrirToolbar = QtGui.QAction(parent=MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("ui\\../img/icons/folder.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionAbrirToolbar.setIcon(icon4)
        self.actionAbrirToolbar.setObjectName("actionAbrirToolbar")
        self.actionSaveToolbar = QtGui.QAction(parent=MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("ui\\../img/icons/save.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionSaveToolbar.setIcon(icon5)
        self.actionSaveToolbar.setObjectName("actionSaveToolbar")
        self.actionManageFilesToolbar = QtGui.QAction(parent=MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("ui\\../img/icons/inventory.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionManageFilesToolbar.setIcon(icon6)
        self.actionManageFilesToolbar.setObjectName("actionManageFilesToolbar")
        self.actionOpenCalculatorToolbar = QtGui.QAction(parent=MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("ui\\../img/icons/scatter.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpenCalculatorToolbar.setIcon(icon7)
        self.actionOpenCalculatorToolbar.setObjectName("actionOpenCalculatorToolbar")
        self.actionCodeEditorToolbar = QtGui.QAction(parent=MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("ui\\../img/icons/code.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionCodeEditorToolbar.setIcon(icon8)
        self.actionCodeEditorToolbar.setObjectName("actionCodeEditorToolbar")
        self.actionChangeFontToolbar = QtGui.QAction(parent=MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("ui\\../img/icons/font.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionChangeFontToolbar.setIcon(icon9)
        self.actionChangeFontToolbar.setObjectName("actionChangeFontToolbar")
        self.actionTendencyPlotToolbar = QtGui.QAction(parent=MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("ui\\../img/icons/regression.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionTendencyPlotToolbar.setIcon(icon10)
        self.actionTendencyPlotToolbar.setObjectName("actionTendencyPlotToolbar")
        self.actionTendencyPlot = QtGui.QAction(parent=MainWindow)
        self.actionTendencyPlot.setObjectName("actionTendencyPlot")
        self.actionClassificacao_de_Fluidos = QtGui.QAction(parent=MainWindow)
        self.actionClassificacao_de_Fluidos.setObjectName("actionClassificacao_de_Fluidos")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionAbrir)
        self.menuFile.addAction(self.actionSalvar)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSair)
        self.menuEditar.addAction(self.actionGerenciar_Arquivos)
        self.menuEditar.addAction(self.actionEditor_de_Texto)
        self.menuCalcular.addAction(self.actionCalculadora)
        self.menuCalcular.addAction(self.actionTendencyPlot)
        self.menuCalcular.addAction(self.actionClassificacao_de_Fluidos)
        self.menuCalcular.addAction(self.actionTOMI_index)
        self.menuSobre.addAction(self.actionAjuda)
        self.menuSobre.addAction(self.actionSobre)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuCalcular.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())
        self.toolBar.addAction(self.newFileToolbar)
        self.toolBar.addAction(self.actionAbrirToolbar)
        self.toolBar.addAction(self.actionSaveToolbar)
        self.toolBar_2.addAction(self.actionManageFilesToolbar)
        self.toolBar_2.addAction(self.actionOpenCalculatorToolbar)
        self.toolBar_2.addAction(self.actionTendencyPlotToolbar)
        self.toolBar_2.addAction(self.actionCodeEditorToolbar)
        self.toolBar_2.addAction(self.actionChangeFontToolbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.mainSheetTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "A"))
        item = self.mainSheetTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "B"))
        item = self.mainSheetTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "C"))
        item = self.mainSheetTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "D"))
        item = self.mainSheetTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "E"))
        item = self.mainSheetTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "F"))
        item = self.mainSheetTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "G"))
        item = self.mainSheetTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "I"))
        item = self.mainSheetTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "J"))
        item = self.mainSheetTable.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "K"))
        item = self.mainSheetTable.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "L"))
        item = self.mainSheetTable.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "M"))
        item = self.mainSheetTable.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "N"))
        item = self.mainSheetTable.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "O"))
        item = self.mainSheetTable.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "P"))
        item = self.mainSheetTable.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Q"))
        item = self.mainSheetTable.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "R"))
        item = self.mainSheetTable.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "S"))
        item = self.mainSheetTable.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "T"))
        item = self.mainSheetTable.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "U"))
        item = self.mainSheetTable.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "V"))
        item = self.mainSheetTable.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "W"))
        item = self.mainSheetTable.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "X"))
        item = self.mainSheetTable.horizontalHeaderItem(23)
        item.setText(_translate("MainWindow", "Z"))
        self.addRowBtn.setStatusTip(_translate("MainWindow", "Adicionar linha à planilha"))
        self.addRowBtn.setText(_translate("MainWindow", "+"))
        self.row_label_2.setText(_translate("MainWindow", "Linhas"))
        self.rmRowBtn.setStatusTip(_translate("MainWindow", "Remover linha da planilha"))
        self.rmRowBtn.setText(_translate("MainWindow", "-"))
        self.addColBtn.setStatusTip(_translate("MainWindow", "Adicionar coluna à planilha"))
        self.addColBtn.setText(_translate("MainWindow", "+"))
        self.col_label_2.setText(_translate("MainWindow", "Colunas"))
        self.rmColBtn.setStatusTip(_translate("MainWindow", "Remover coluna da planilha"))
        self.rmColBtn.setText(_translate("MainWindow", "-"))
        self.menuFile.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuEditar.setTitle(_translate("MainWindow", "Editar"))
        self.menuCalcular.setTitle(_translate("MainWindow", "Calcular"))
        self.menuSobre.setTitle(_translate("MainWindow", "Sobre"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.actionNew.setText(_translate("MainWindow", "Novo"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar"))
        self.actionSair.setText(_translate("MainWindow", "Sair"))
        self.actionGerenciar_Arquivos.setText(_translate("MainWindow", "Gerenciar Arquivos"))
        self.actionEditor_de_Texto.setText(_translate("MainWindow", "Editor de Texto"))
        self.actionCalculadora.setText(_translate("MainWindow", "Gráfico Simples"))
        self.actionTOMI_index.setText(_translate("MainWindow", "TOMI Index"))
        self.actionAjuda.setText(_translate("MainWindow", "Ajuda"))
        self.actionSobre.setText(_translate("MainWindow", "Sobre"))
        self.newFileToolbar.setText(_translate("MainWindow", "Novo Arquivo"))
        self.newFileToolbar.setToolTip(_translate("MainWindow", "Novo Arquivo"))
        self.newFileToolbar.setStatusTip(_translate("MainWindow", "Abrir um novo arquivo .csv"))
        self.actionAbrirToolbar.setText(_translate("MainWindow", "Abrir"))
        self.actionAbrirToolbar.setToolTip(_translate("MainWindow", "Abrir arquivo"))
        self.actionAbrirToolbar.setStatusTip(_translate("MainWindow", "Abrir um arquivo .csv já existente"))
        self.actionSaveToolbar.setText(_translate("MainWindow", "Salvar"))
        self.actionSaveToolbar.setToolTip(_translate("MainWindow", "Salvar arquivo"))
        self.actionSaveToolbar.setStatusTip(_translate("MainWindow", "Salvar o arquivo"))
        self.actionManageFilesToolbar.setText(_translate("MainWindow", "Gerenciar Arquivos"))
        self.actionManageFilesToolbar.setToolTip(_translate("MainWindow", "Gerencie os arquivos carregados"))
        self.actionManageFilesToolbar.setStatusTip(_translate("MainWindow", "Gerencie os arquivos que foram carregados"))
        self.actionOpenCalculatorToolbar.setText(_translate("MainWindow", "Abrir Calculadora"))
        self.actionOpenCalculatorToolbar.setToolTip(_translate("MainWindow", "Abra a seção de calculadoras"))
        self.actionOpenCalculatorToolbar.setStatusTip(_translate("MainWindow", "Abra a seção de cálculos, para calcular gradiente de pressão e classificar poços"))
        self.actionCodeEditorToolbar.setText(_translate("MainWindow", "Editor de Texto"))
        self.actionCodeEditorToolbar.setToolTip(_translate("MainWindow", "Abra o editor de texto"))
        self.actionCodeEditorToolbar.setStatusTip(_translate("MainWindow", "Um editor de texto simples"))
        self.actionChangeFontToolbar.setText(_translate("MainWindow", "Fonte"))
        self.actionChangeFontToolbar.setToolTip(_translate("MainWindow", "Altere a fonte utilizada"))
        self.actionChangeFontToolbar.setStatusTip(_translate("MainWindow", "Altere a fonte utilizada"))
        self.actionTendencyPlotToolbar.setText(_translate("MainWindow", "Abrir gráfico de tendencia"))
        self.actionTendencyPlot.setText(_translate("MainWindow", "Contato de Fluidos"))
        self.actionClassificacao_de_Fluidos.setText(_translate("MainWindow", "Classificação de Fluidos"))
