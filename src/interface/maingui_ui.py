# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maingui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QToolBar, QVBoxLayout,
    QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1055, 842)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(500, 500))
        icon = QIcon()
        icon.addFile(u"../icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(True)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        self.actionSalvar = QAction(MainWindow)
        self.actionSalvar.setObjectName(u"actionSalvar")
        self.actionSair = QAction(MainWindow)
        self.actionSair.setObjectName(u"actionSair")
        self.actionGerenciar_Arquivos = QAction(MainWindow)
        self.actionGerenciar_Arquivos.setObjectName(u"actionGerenciar_Arquivos")
        self.actionEditor_de_Texto = QAction(MainWindow)
        self.actionEditor_de_Texto.setObjectName(u"actionEditor_de_Texto")
        self.actionCalculadora = QAction(MainWindow)
        self.actionCalculadora.setObjectName(u"actionCalculadora")
        self.actionTOMI_index = QAction(MainWindow)
        self.actionTOMI_index.setObjectName(u"actionTOMI_index")
        self.actionAjuda = QAction(MainWindow)
        self.actionAjuda.setObjectName(u"actionAjuda")
        self.actionSobre = QAction(MainWindow)
        self.actionSobre.setObjectName(u"actionSobre")
        self.newFileToolbar = QAction(MainWindow)
        self.newFileToolbar.setObjectName(u"newFileToolbar")
        icon1 = QIcon()
        icon1.addFile(u"../img/icons/new_file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.newFileToolbar.setIcon(icon1)
        self.actionAbrirToolbar = QAction(MainWindow)
        self.actionAbrirToolbar.setObjectName(u"actionAbrirToolbar")
        icon2 = QIcon()
        icon2.addFile(u"../img/icons/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbrirToolbar.setIcon(icon2)
        self.actionSaveToolbar = QAction(MainWindow)
        self.actionSaveToolbar.setObjectName(u"actionSaveToolbar")
        icon3 = QIcon()
        icon3.addFile(u"../img/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSaveToolbar.setIcon(icon3)
        self.actionManageFilesToolbar = QAction(MainWindow)
        self.actionManageFilesToolbar.setObjectName(u"actionManageFilesToolbar")
        icon4 = QIcon()
        icon4.addFile(u"../img/icons/inventory.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionManageFilesToolbar.setIcon(icon4)
        self.actionOpenCalculatorToolbar = QAction(MainWindow)
        self.actionOpenCalculatorToolbar.setObjectName(u"actionOpenCalculatorToolbar")
        icon5 = QIcon()
        icon5.addFile(u"../img/icons/scatter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpenCalculatorToolbar.setIcon(icon5)
        self.actionCodeEditorToolbar = QAction(MainWindow)
        self.actionCodeEditorToolbar.setObjectName(u"actionCodeEditorToolbar")
        icon6 = QIcon()
        icon6.addFile(u"../img/icons/code.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCodeEditorToolbar.setIcon(icon6)
        self.actionChangeFontToolbar = QAction(MainWindow)
        self.actionChangeFontToolbar.setObjectName(u"actionChangeFontToolbar")
        icon7 = QIcon()
        icon7.addFile(u"../img/icons/font.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionChangeFontToolbar.setIcon(icon7)
        self.actionTendencyPlotToolbar = QAction(MainWindow)
        self.actionTendencyPlotToolbar.setObjectName(u"actionTendencyPlotToolbar")
        icon8 = QIcon()
        icon8.addFile(u"../img/icons/regression.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionTendencyPlotToolbar.setIcon(icon8)
        self.actionTendencyPlot = QAction(MainWindow)
        self.actionTendencyPlot.setObjectName(u"actionTendencyPlot")
        self.actionClassificacao_de_Fluidos = QAction(MainWindow)
        self.actionClassificacao_de_Fluidos.setObjectName(u"actionClassificacao_de_Fluidos")
        self.actionImportar_Arquivo = QAction(MainWindow)
        self.actionImportar_Arquivo.setObjectName(u"actionImportar_Arquivo")
        self.actionImportar_Arquivo.setEnabled(True)
        self.changeTextColorBtn = QAction(MainWindow)
        self.changeTextColorBtn.setObjectName(u"changeTextColorBtn")
        icon9 = QIcon()
        icon9.addFile(u"../img/icons/font_color.png", QSize(), QIcon.Normal, QIcon.Off)
        self.changeTextColorBtn.setIcon(icon9)
        self.changeCellColorBtn = QAction(MainWindow)
        self.changeCellColorBtn.setObjectName(u"changeCellColorBtn")
        icon10 = QIcon()
        icon10.addFile(u"../img/icons/fill_color.png", QSize(), QIcon.Normal, QIcon.Off)
        self.changeCellColorBtn.setIcon(icon10)
        self.alignLeftButton = QAction(MainWindow)
        self.alignLeftButton.setObjectName(u"alignLeftButton")
        icon11 = QIcon()
        icon11.addFile(u"../img/icons/alignLeft.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.alignLeftButton.setIcon(icon11)
        self.alignCenterButton = QAction(MainWindow)
        self.alignCenterButton.setObjectName(u"alignCenterButton")
        icon12 = QIcon()
        icon12.addFile(u"../img/icons/alignCenter.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.alignCenterButton.setIcon(icon12)
        self.alignRightButton = QAction(MainWindow)
        self.alignRightButton.setObjectName(u"alignRightButton")
        icon13 = QIcon()
        icon13.addFile(u"../img/icons/alignRight.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.alignRightButton.setIcon(icon13)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"QFrame {\n"
"    border: none;  /* Remove qualquer borda */\n"
"    margin: 0px;   /* Define a margem como zero */\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cellNameBox = QComboBox(self.frame)
        self.cellNameBox.setObjectName(u"cellNameBox")
        self.cellNameBox.setMinimumSize(QSize(100, 0))
        self.cellNameBox.setMaximumSize(QSize(150, 16777215))
        self.cellNameBox.setStyleSheet(u"QComboBox {\n"
"	text-align: center;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.cellNameBox)

        self.formulaBar = QLineEdit(self.frame)
        self.formulaBar.setObjectName(u"formulaBar")

        self.horizontalLayout.addWidget(self.formulaBar)


        self.verticalLayout.addWidget(self.frame)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.mainSheetTable = QTableWidget(self.centralwidget)
        if (self.mainSheetTable.columnCount() < 24):
            self.mainSheetTable.setColumnCount(24)
        __qtablewidgetitem = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(20, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(21, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(22, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.mainSheetTable.setHorizontalHeaderItem(23, __qtablewidgetitem23)
        if (self.mainSheetTable.rowCount() < 100):
            self.mainSheetTable.setRowCount(100)
        self.mainSheetTable.setObjectName(u"mainSheetTable")
        sizePolicy.setHeightForWidth(self.mainSheetTable.sizePolicy().hasHeightForWidth())
        self.mainSheetTable.setSizePolicy(sizePolicy)
        self.mainSheetTable.viewport().setProperty("cursor", QCursor(Qt.CrossCursor))
        self.mainSheetTable.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.mainSheetTable.setAutoFillBackground(False)
        self.mainSheetTable.setStyleSheet(u"/* Table background and borders */\n"
"QTableWidget {\n"
"    background-color: #ffffff; /* Cor de fundo branca */\n"
"    border: 1px solid #000000; /* Borda preta */\n"
"    border-radius: 0px; /* Sem arredondamento de cantos */\n"
"    gridline-color: #d4d4d4; /* Cor das linhas da grade */\n"
"	margin: 0;\n"
"}\n"
"\n"
"/* Styling for table items */\n"
"QTableWidget::item {\n"
"    border: none; /* Sem borda */\n"
"    color: #000000; /* Cor do texto preto */\n"
"    font-size: 10pt; /* Tamanho da fonte */\n"
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
""
                        "	background-color: #e6e6e6;\n"
"}\n"
"")
        self.mainSheetTable.setFrameShape(QFrame.StyledPanel)
        self.mainSheetTable.setFrameShadow(QFrame.Sunken)
        self.mainSheetTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.mainSheetTable.setRowCount(100)
        self.mainSheetTable.setColumnCount(24)
        self.mainSheetTable.horizontalHeader().setDefaultSectionSize(100)
        self.mainSheetTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.mainSheetTable.verticalHeader().setMinimumSectionSize(22)
        self.mainSheetTable.verticalHeader().setDefaultSectionSize(22)
        self.mainSheetTable.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_3.addWidget(self.mainSheetTable)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1055, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEditar = QMenu(self.menubar)
        self.menuEditar.setObjectName(u"menuEditar")
        self.menuCalcular = QMenu(self.menubar)
        self.menuCalcular.setObjectName(u"menuCalcular")
        self.menuSobre = QMenu(self.menubar)
        self.menuSobre.setObjectName(u"menuSobre")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QToolBar(MainWindow)
        self.toolBar_2.setObjectName(u"toolBar_2")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_2)
        MainWindow.insertToolBarBreak(self.toolBar_2)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuCalcular.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionAbrir)
        self.menuFile.addAction(self.actionSalvar)
        self.menuFile.addAction(self.actionImportar_Arquivo)
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
        self.toolBar.addAction(self.newFileToolbar)
        self.toolBar.addAction(self.actionAbrirToolbar)
        self.toolBar.addAction(self.actionSaveToolbar)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionManageFilesToolbar)
        self.toolBar.addAction(self.actionOpenCalculatorToolbar)
        self.toolBar.addAction(self.actionTendencyPlotToolbar)
        self.toolBar.addAction(self.actionCodeEditorToolbar)
        self.toolBar.addAction(self.actionChangeFontToolbar)
        self.toolBar.addSeparator()
        self.toolBar_2.addAction(self.changeTextColorBtn)
        self.toolBar_2.addAction(self.changeCellColorBtn)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.alignLeftButton)
        self.toolBar_2.addAction(self.alignCenterButton)
        self.toolBar_2.addAction(self.alignRightButton)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"Novo Arquivo", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir Arquivo", None))
        self.actionSalvar.setText(QCoreApplication.translate("MainWindow", u"Salvar Arquivo", None))
        self.actionSair.setText(QCoreApplication.translate("MainWindow", u"Sair", None))
        self.actionGerenciar_Arquivos.setText(QCoreApplication.translate("MainWindow", u"Gerenciar Arquivos", None))
        self.actionEditor_de_Texto.setText(QCoreApplication.translate("MainWindow", u"Editor de Texto", None))
        self.actionCalculadora.setText(QCoreApplication.translate("MainWindow", u"Gr\u00e1fico Simples", None))
        self.actionTOMI_index.setText(QCoreApplication.translate("MainWindow", u"TOMI Index", None))
        self.actionAjuda.setText(QCoreApplication.translate("MainWindow", u"Manual do usu\u00e1rio", None))
        self.actionSobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.newFileToolbar.setText(QCoreApplication.translate("MainWindow", u"Novo Arquivo", None))
#if QT_CONFIG(tooltip)
        self.newFileToolbar.setToolTip(QCoreApplication.translate("MainWindow", u"Novo Arquivo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.newFileToolbar.setStatusTip(QCoreApplication.translate("MainWindow", u"Abrir um novo arquivo .csv", None))
#endif // QT_CONFIG(statustip)
        self.actionAbrirToolbar.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
#if QT_CONFIG(tooltip)
        self.actionAbrirToolbar.setToolTip(QCoreApplication.translate("MainWindow", u"Abrir arquivo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionAbrirToolbar.setStatusTip(QCoreApplication.translate("MainWindow", u"Abrir um arquivo .csv j\u00e1 existente", None))
#endif // QT_CONFIG(statustip)
        self.actionSaveToolbar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
#if QT_CONFIG(tooltip)
        self.actionSaveToolbar.setToolTip(QCoreApplication.translate("MainWindow", u"Salvar arquivo", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionSaveToolbar.setStatusTip(QCoreApplication.translate("MainWindow", u"Salvar o arquivo", None))
#endif // QT_CONFIG(statustip)
        self.actionManageFilesToolbar.setText(QCoreApplication.translate("MainWindow", u"Gerenciar Arquivos", None))
#if QT_CONFIG(tooltip)
        self.actionManageFilesToolbar.setToolTip(QCoreApplication.translate("MainWindow", u"Gerencie os arquivos carregados", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionManageFilesToolbar.setStatusTip(QCoreApplication.translate("MainWindow", u"Gerencie os arquivos que foram carregados", None))
#endif // QT_CONFIG(statustip)
        self.actionOpenCalculatorToolbar.setText(QCoreApplication.translate("MainWindow", u"Abrir Calculadora", None))
#if QT_CONFIG(tooltip)
        self.actionOpenCalculatorToolbar.setToolTip(QCoreApplication.translate("MainWindow", u"Abra a se\u00e7\u00e3o de calculadoras", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionOpenCalculatorToolbar.setStatusTip(QCoreApplication.translate("MainWindow", u"Abra a se\u00e7\u00e3o de c\u00e1lculos, para calcular gradiente de press\u00e3o e classificar po\u00e7os", None))
#endif // QT_CONFIG(statustip)
        self.actionCodeEditorToolbar.setText(QCoreApplication.translate("MainWindow", u"Editor de Texto", None))
#if QT_CONFIG(tooltip)
        self.actionCodeEditorToolbar.setToolTip(QCoreApplication.translate("MainWindow", u"Abra o editor de texto", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionCodeEditorToolbar.setStatusTip(QCoreApplication.translate("MainWindow", u"Um editor de texto simples", None))
#endif // QT_CONFIG(statustip)
        self.actionChangeFontToolbar.setText(QCoreApplication.translate("MainWindow", u"Fonte", None))
#if QT_CONFIG(tooltip)
        self.actionChangeFontToolbar.setToolTip(QCoreApplication.translate("MainWindow", u"Altere a fonte utilizada", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionChangeFontToolbar.setStatusTip(QCoreApplication.translate("MainWindow", u"Altere a fonte utilizada", None))
#endif // QT_CONFIG(statustip)
        self.actionTendencyPlotToolbar.setText(QCoreApplication.translate("MainWindow", u"Abrir gr\u00e1fico de tendencia", None))
        self.actionTendencyPlot.setText(QCoreApplication.translate("MainWindow", u"Contato de Fluidos", None))
        self.actionClassificacao_de_Fluidos.setText(QCoreApplication.translate("MainWindow", u"Classifica\u00e7\u00e3o de Fluidos", None))
        self.actionImportar_Arquivo.setText(QCoreApplication.translate("MainWindow", u"Importar Dados", None))
        self.changeTextColorBtn.setText(QCoreApplication.translate("MainWindow", u"changeTextColorBtn", None))
#if QT_CONFIG(tooltip)
        self.changeTextColorBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Alterar cor do texto", None))
#endif // QT_CONFIG(tooltip)
        self.changeCellColorBtn.setText(QCoreApplication.translate("MainWindow", u"changeCellColorBtn", None))
#if QT_CONFIG(tooltip)
        self.changeCellColorBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Alterar fundo", None))
#endif // QT_CONFIG(tooltip)
        self.alignLeftButton.setText(QCoreApplication.translate("MainWindow", u"alignLeftButton", None))
#if QT_CONFIG(tooltip)
        self.alignLeftButton.setToolTip(QCoreApplication.translate("MainWindow", u"Alinhar \u00e0 esquerda", None))
#endif // QT_CONFIG(tooltip)
        self.alignCenterButton.setText(QCoreApplication.translate("MainWindow", u"alignCenterButton", None))
#if QT_CONFIG(tooltip)
        self.alignCenterButton.setToolTip(QCoreApplication.translate("MainWindow", u"Alinhar ao centro", None))
#endif // QT_CONFIG(tooltip)
        self.alignRightButton.setText(QCoreApplication.translate("MainWindow", u"alignRightButton", None))
#if QT_CONFIG(tooltip)
        self.alignRightButton.setToolTip(QCoreApplication.translate("MainWindow", u"Alinhar \u00e0 direita", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.formulaBar.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.formulaBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Insira uma fun\u00e7\u00e3o aqui...", None))
        ___qtablewidgetitem = self.mainSheetTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"A", None));
        ___qtablewidgetitem1 = self.mainSheetTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"B", None));
        ___qtablewidgetitem2 = self.mainSheetTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"C", None));
        ___qtablewidgetitem3 = self.mainSheetTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"D", None));
        ___qtablewidgetitem4 = self.mainSheetTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"E", None));
        ___qtablewidgetitem5 = self.mainSheetTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"F", None));
        ___qtablewidgetitem6 = self.mainSheetTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"G", None));
        ___qtablewidgetitem7 = self.mainSheetTable.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"I", None));
        ___qtablewidgetitem8 = self.mainSheetTable.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"J", None));
        ___qtablewidgetitem9 = self.mainSheetTable.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"K", None));
        ___qtablewidgetitem10 = self.mainSheetTable.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"L", None));
        ___qtablewidgetitem11 = self.mainSheetTable.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"M", None));
        ___qtablewidgetitem12 = self.mainSheetTable.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"N", None));
        ___qtablewidgetitem13 = self.mainSheetTable.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"O", None));
        ___qtablewidgetitem14 = self.mainSheetTable.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"P", None));
        ___qtablewidgetitem15 = self.mainSheetTable.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Q", None));
        ___qtablewidgetitem16 = self.mainSheetTable.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"R", None));
        ___qtablewidgetitem17 = self.mainSheetTable.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"S", None));
        ___qtablewidgetitem18 = self.mainSheetTable.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"T", None));
        ___qtablewidgetitem19 = self.mainSheetTable.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"U", None));
        ___qtablewidgetitem20 = self.mainSheetTable.horizontalHeaderItem(20)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"V", None));
        ___qtablewidgetitem21 = self.mainSheetTable.horizontalHeaderItem(21)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"W", None));
        ___qtablewidgetitem22 = self.mainSheetTable.horizontalHeaderItem(22)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"X", None));
        ___qtablewidgetitem23 = self.mainSheetTable.horizontalHeaderItem(23)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Z", None));
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"Arquivo", None))
        self.menuEditar.setTitle(QCoreApplication.translate("MainWindow", u"Gerenciamento", None))
        self.menuCalcular.setTitle(QCoreApplication.translate("MainWindow", u"C\u00e1lculos e Gr\u00e1ficos", None))
        self.menuSobre.setTitle(QCoreApplication.translate("MainWindow", u"Ajuda", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_2.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

