import os
import shutil
import sys
import csv
import markdown
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt6.QtCore import Qt, QUrl, QDir, QEvent
from PyQt6.QtGui import (QAction, QKeySequence, QDesktopServices,
                        QFileSystemModel, QStandardItemModel, QStandardItem,
                        QFont, QColor)
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem,
                            QFileDialog, QMessageBox, QColorDialog, QFontDialog,
                            QInputDialog, QMenu)
import PyQt6.Qsci as Qsci
from PyQt6.Qsci import QsciScintilla
from pyui.icons_rc import *
from pyui.maingui import Ui_MainWindow
from pyui.about import Ui_AboutWindow
from pyui.help import Ui_HelpMainWindow
from pyui.manage_files import Ui_ManageFilesWindow
from pyui.simple_plot_window import Ui_SimplePlotWindow
from pyui.plot_tendencia_window import Ui_plotTendenciaWindow
from pyui.gradiente_pressao_window import Ui_gradientePressaoWindow
from pyui.text_editor_window import Ui_textEditorWindow

from app_functions import pressure_gradient_classification

plt.style.use(['bmh'])

class TextEditorWindow(QMainWindow, Ui_textEditorWindow):
    def __init__(self):
        super(TextEditorWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Editor de Texto")
        np.linspace(0, 10, 100)
        # reference the widget here
        self.scintillaWidget.setMarginType(0, QsciScintilla.
                                              MarginType.
                                              NumberMargin)
        self.scintillaWidget.setAutoCompletionSource(QsciScintilla.
                                                     AutoCompletionSource.
                                                     AcsAll)
        self.scintillaWidget.setAutoIndent(True)
        self.scintillaWidget.setBraceMatching(QsciScintilla.
                                              BraceMatch.
                                              StrictBraceMatch)
        self.scintillaWidget.setIndentationWidth(4)
        self.scintillaWidget.setFont(QFont("Consolas", 12))

        # Use QsciLexer for syntax highlighting
        self.python_lexer = Qsci.QsciLexerPython()
        self.python_lexer.setFont(QFont("Consolas", weight=500))
        self.cplusplus_lexer = Qsci.QsciLexerCPP()
        self.cplusplus_lexer.setFont(QFont("Consolas", weight=500))
        self.javascript_lexer = Qsci.QsciLexerJavaScript()
        self.javascript_lexer.setFont(QFont("Consolas", weight=500))
        self.matlab_lexer = Qsci.QsciLexerMatlab()
        self.matlab_lexer.setFont(QFont("Consolas", weight=500))
        self.markdown_lexer = Qsci.QsciLexerMarkdown()
        self.markdown_lexer.setFont(QFont("Consolas", weight=500))

        self.actionNovoArquivoTexto.triggered.connect(self.new_file)
        self.actionAbrirArquivoTexto.triggered.connect(self.open_file)
        self.actionSalvarArquivoTexto.triggered.connect(self.save_file)
        self.actionRecortar.triggered.connect(self.scintillaWidget.cut)
        self.actionCopiar.triggered.connect(self.scintillaWidget.copy)
        self.actionColar.triggered.connect(self.scintillaWidget.paste)
        self.actionDesfazer.triggered.connect(self.scintillaWidget.undo)
        self.actionRefazer.triggered.connect(self.scintillaWidget.redo)
        self.actionApagar.triggered.connect(self.scintillaWidget.clear)
        self.actionSelecionar_tudo.triggered.connect(self.
                                                     scintillaWidget.selectAll)
        self.actionFonte.triggered.connect(self.change_font)
        self.actionPython.triggered.connect(self.python_highlight)
        self.actionC_C.triggered.connect(self.c_c_highlight)
        self.actionC.triggered.connect(self.c_highlight)
        self.actionJavaScript.triggered.connect(self.javascript_highlight)
        self.actionR.triggered.connect(self.r_highlight)
        self.actionMatlab.triggered.connect(self.matlab_highlight)
        self.actionMarkdown.triggered.connect(self.markdown_highlight)

    def python_highlight(self):
        self.scintillaWidget.setLexer(self.python_lexer)

    def c_c_highlight(self):
        self.scintillaWidget.setLexer(self.cplusplus_lexer)

    def c_highlight(self):
        self.scintillaWidget.setLexer(self.cplusplus_lexer)

    def javascript_highlight(self):
        self.scintillaWidget.setLexer(self.javascript_lexer)

    def r_highlight(self):
        return QMessageBox.information(self, "Information",
                                       "R highlighting não foi implementado")

    def matlab_highlight(self):
        self.scintillaWidget.setLexer(self.matlab_lexer)

    def markdown_highlight(self):
        self.scintillaWidget.setLexer(self.markdown_lexer)

    def new_file(self):
        # Clear the current text
        self.scintillaWidget.clear()

        # Reset the current file path
        self.current_file_path = None


    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open File', '',
                                                'All Files (*)')
        if file_name:
            with open(file_name, 'r') as file:
                file_content = file.read()
            self.scintillaWidget.setPlainText(file_content)

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                   "All Files (*)")
        if file_name:
            with open(file_name, 'w') as file:
                file_content = self.scintillaWidget.text()
                file_content = file_content.replace('\n', '\r\n')
                file.write(file_content)

    def change_font(self):
        font, ok = QFontDialog.getFont(self.scintillaWidget.font(), self)
        if ok:
            self.scintillaWidget.setFont(font)

class GradientClassificationWin(QMainWindow,
                                Ui_gradientePressaoWindow):
    # TODO: fully implement this function
    def __init__(self):
        super(GradientClassificationWin, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Classificação do Gradiente de Pressão")

        model = QStandardItemModel(10, 5, self)
        model.setHorizontalHeaderLabels(['Fluido', 'Gradiente (psi/ft)',
                                         'Gradiente (psi/m)', 'Gradiente (kgf/cm2/m)',
                                         'Gradiente (bar/m)'])

        data = [
            ["Dry Gas Zero", 0.000, 0.000, 0.000, 0.000],
            ["Dry Gas", 0.000, 0.000, 0.000, 0.000],
            ["Wet Gas", 0.140, 0.459, 0.030, 0.032],
            ["Oil limit", 0.300, 0.984, 0.069, 0.069],
            ["Oil 60º", 0.387, 1.270, 0.089, 0.087],
            ["Oil 20º (Heavy)", 0.404, 1.325, 0.093, 0.091],
            ["Fresh Water", 0.433, 1.421, 0.100, 0.098],
            ["Sea Water", 0.444, 1.457, 0.102, 0.101],
            ["Salt sat. Water", 0.520, 1.706, 0.120, 0.118],
            ["Salt sat. Water Max", 100.000, 100.000, 100.000, 100.000]
        ]

        for row in range(len(data)):
            for column in range(len(data[0])):
                item = QStandardItem(str(data[row][column]))
                model.setItem(row, column, item)

        self.fluidPressureTableView.setModel(model)

        self.selected_file = None

        # list of files in the uploads directory - Select the file option
        self.files = os.listdir('uploads')
        self.fileComboBox.addItems(self.files)

        self.pressureComboBox.addItems(["psi/ft", "psi/m", "kgf/cm2/m", "bar/m"])

        self.fluidClassificationBtn.clicked.connect(self.classify_fluid)
        self.saveOutputContent.clicked.connect(self.save_output_content)

    def classify_fluid(self):
        pass

    def save_output_content(self):
        pass

class PlotTendenciaWindow(QMainWindow, Ui_plotTendenciaWindow):
    def __init__(self):
        super(PlotTendenciaWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Plot de Tendência")

        self.selected_file = None

        # list of files in the uploads directory - Select the file option
        self.files = os.listdir('uploads')
        self.selectFileComboBox.addItems(self.files)

        # prof cota radio buttons
        # if cotaProfNao is checked, labelMesaRotativa and inputMesaRotativa became enabled
        self.cotaProfNao.toggled.connect(self.on_cotaProfNao_toggled)
        self.headerSim.toggled.connect(self.on_headerSim_toggled)

        self.lineColorComboBox.addItems(['blue', 'red', 'green',
                                         'yellow', 'black', 'purple',
                                         'orange', 'pink', 'brown', 'gray'])

        self.inputPressureUnit.addItems(["psi/ft", "psi/m",
                                         "kgf/cm2/m", "bar/m"])

        # plot btn
        self.tendenciaPlotBtn.clicked.connect(self.call_plot_trends)

    def on_cotaProfNao_toggled(self, checked):
        self.labelMesaRotativa.setEnabled(checked)
        self.inputMesaRotativa.setEnabled(checked)

    def on_headerSim_toggled(self, checked):
        self.labelHeaderLines.setEnabled(checked)
        self.inputHeaderLines.setEnabled(checked)

    def open_file_for_trend_plotting(self):

        self.header_lines = self.inputHeaderLines.text()

        self.selected_file = self.selectFileComboBox.currentText()
        # Check if self.header_lines is not an empty string
        if self.header_lines != '':
            # Convert self.header_lines to an integer
            skiprows = int(self.header_lines)
        else:
            skiprows = 0

        # Get the text of the checked button in the fileButtonGroup
        self.file_type_button_text = self.fileButtonGroup.checkedButton().text()

        if self.file_type_button_text == 'csv':
            try:
                dataframe = pd.read_csv(f'uploads/{self.selected_file}',
                                delimiter='[;,]',
                                names=["prof", "pressao"],
                                engine='python',
                                skiprows=skiprows)
                return dataframe
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Um erro ocorreu: {e}")
                return pd.DataFrame()

        elif self.file_type_button_text == 'txt':
            try:
                dataframe = pd.read_csv(f'uploads/{self.selected_file}',
                                skiprows=skiprows,
                                delimiter='\t',
                                names=["prof", "pressao"],
                                engine='python')
                return dataframe
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Um erro ocorreu: {e}")
                return pd.DataFrame()

        elif self.file_type_button_text == 'xlsx':
            try:
                dataframe = pd.read_excel(f'uploads/{self.selected_file}',
                                            skiprows=skiprows,
                                            names=["prof", "pressao"])
                return dataframe
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Um erro ocorreu: {e}")
                return pd.DataFrame()

    def plot_trends(self):
        self.dataframe = self.open_file_for_trend_plotting()
        self.kmeansClusters = self.agrupamentoSpinBox.value()
        self.mesa_rotativa = self.inputMesaRotativa.text()

        self.title = self.inputPlotTitle.text()
        self.x_axis = self.inputPlotXAxis.text()
        self.y_axis = self.inputPlotYAxis.text()
        self.pressure_unit = self.inputPressureUnit.currentText()
        # self.prof_min = self.inputProfMin.text()
        # self.prof_max = self.inputProfMax.text()

        # Check if self.mesa_rotativa is not an empty string
        if self.mesa_rotativa != '':
            # Convert self.mesa_rotativa to an integer and subtract y
            y = int(self.mesa_rotativa) - y

        fig, axs, messages = pressure_gradient_classification(
                                         self.dataframe, self.kmeansClusters,
                                         self.pressure_unit,
                                         self.title, self.x_axis, self.y_axis)
        for message in messages:
            self.outputAfterPlotted.append(message)
        plt.show()

    def call_plot_trends(self):
        self.plot_trends()

class SimplePlotWindow(QMainWindow, Ui_SimplePlotWindow):
    def __init__(self):
        super(SimplePlotWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Plot Simples")
        # Initialize self.selected_file
        self.selected_file = None

        # list of files in the uploads directory - Select the file option
        self.files = os.listdir('uploads')
        self.selectFileComboBox.addItems(self.files)

        # prof cota radio buttons
        # if cotaProfNao is checked, labelMesaRotativa and inputMesaRotativa became enabled
        self.cotaProfNao.toggled.connect(self.on_cotaProfNao_toggled)
        self.headerSim.toggled.connect(self.on_headerSim_toggled)

        self.lineColorComboBox.addItems(['blue', 'red', 'green',
                                         'yellow', 'black', 'purple',
                                         'orange', 'pink', 'brown', 'gray'])

        # plot btn
        self.simplePlotBtn.clicked.connect(self.call_plot_simple)

    def on_cotaProfNao_toggled(self, checked):
        self.labelMesaRotativa.setEnabled(checked)
        self.inputMesaRotativa.setEnabled(checked)

    def on_headerSim_toggled(self, checked):
        self.labelHeaderLines.setEnabled(checked)
        self.inputHeaderLines.setEnabled(checked)

    def open_file_for_simple_plotting(self):
        try:
            self.mesa_rotativa = self.inputMesaRotativa.text()
            self.header_lines = self.inputHeaderLines.text()

            self.selected_file = self.selectFileComboBox.currentText()
            # Verifica se self.header_lines não é uma string vazia
            if self.header_lines != '':
                # Tenta converter self.header_lines para um inteiro
                try:
                    skiprows = int(self.header_lines)
                except ValueError:
                    QMessageBox.critical(self, "Erro",
                                "Número de linhas de cabeçalho inválido.")
                    return pd.DataFrame()
            else:
                skiprows = 0

            # Obtém o texto do botão marcado no fileButtonGroup
            self.file_type_button_text = self.fileButtonGroup.checkedButton().text()

            if self.file_type_button_text == 'csv':
                try:
                    dataframe = pd.read_csv(f'uploads/{self.selected_file}',
                                    delimiter='[;,]',
                                    names=["prof", "pressao"],
                                    engine='python',
                                    skiprows=skiprows)
                    return dataframe
                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Ocorreu um erro: {e}")
                    return pd.DataFrame()

            elif self.file_type_button_text == 'txt':
                try:
                    dataframe = pd.read_csv(f'uploads/{self.selected_file}',
                                    skiprows=skiprows,
                                    delimiter='\t',
                                    names=["prof", "pressao"],
                                    engine='python')
                    return dataframe
                except Exception as e:
                    QMessageBox.critical(self, "Erro", f"Ocorreu um erro: {e}")
                    return pd.DataFrame()

            elif self.file_type_button_text == 'xlsx':
                try:
                    dataframe = pd.read_excel(f'uploads/{self.selected_file}',
                                                skiprows=skiprows,
                                                names=["prof", "pressao"])
                    return dataframe
                except Exception as e:
                    QMessageBox.critical(self, "Erro",
                                         f"Ocorreu um erro: {e}")
                    return pd.DataFrame()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro: {e}")
            return pd.DataFrame()

    def plot_simple(self, x, y, title, xlabel, ylabel, ymin, ymax):
        self.selected_color = self.lineColorComboBox.currentText()

        if self.mesa_rotativa != '':
            try:
                y = int(self.mesa_rotativa) - y
            except ValueError:
                QMessageBox.critical(self, "Erro",
                                     "Valor de mesa rotativa inválido.")
                return
        try:
            ymin = int(self.prof_min) if self.prof_min != '' else None
            ymax = int(self.prof_max) if self.prof_max != '' else None
        except ValueError:
            QMessageBox.critical(self, "Erro",
                                 "Valores de prof min ou prof max inválidos.")
            return

        try:
            # Obtém o texto do botão marcado no cotaButtonGroup
            cota_button_text = self.cotaButtonGroup.checkedButton().text()

            if cota_button_text == "Sim":
                plt.plot(x, y, 'o', color=self.selected_color)
                plt.title(title)
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                if ymin is not None and ymax is not None:
                    plt.ylim(ymin, ymax)
                plt.show()

            elif cota_button_text == "Não":
                plt.plot(x, y, 'o', color=self.selected_color)
                plt.title(title)
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                if ymin is not None and ymax is not None:
                    plt.ylim(ymin, ymax)
                    plt.gca().invert_yaxis()
                plt.show()
        except Exception as e:
            QMessageBox.critical(self, "Erro",
                                 f"Ocorreu um erro ao plotar o gráfico: {e}")

    def call_plot_simple(self):
        self.dataframe = self.open_file_for_simple_plotting()
        self.title = self.inputPlotTitle.text()
        self.x_axis = self.inputPlotXAxis.text()
        self.y_axis = self.inputPlotYAxis.text()
        self.prof_min = self.inputProfMin.text()
        self.prof_max = self.inputProfMax.text()

        if self.dataframe.empty:
            QMessageBox.critical(self, "Error", "O dataframe está vazio.")
        else:
            self.plot_simple(self.dataframe.iloc[:, 1],
                            self.dataframe.iloc[:, 0],
                            self.title,
                            self.x_axis,
                            self.y_axis,
                            self.prof_min,
                            self.prof_max)

class ManageFiles(QMainWindow, Ui_ManageFilesWindow):
    def __init__(self):
        super(ManageFiles, self).__init__()
        self.setupUi(self)

        self.selected_file_path = None

         # Create a QFileSystemModel
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())

        # Set the model for manageFilesTreeView
        self.manageFilesTreeView.setModel(self.model)

        # Set the root index for manageFilesTreeView
        self.root_path = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
        self.manageFilesTreeView.setRootIndex(self.model.index(self.root_path))

        # Connect the clicked signal to our custom slot
        self.manageFilesTreeView.clicked.connect(self.on_manageFilesTreeView_clicked)

        # Connect buttons to their respective methods
        self.addFileBtn.clicked.connect(self.add_file)
        self.renameFileBtn.clicked.connect(self.rename_file)
        self.deleteFileBtn.clicked.connect(self.delete_file)
        self.exitManageFilesBtn.clicked.connect(self.close)

        # self.show()

    def on_manageFilesTreeView_clicked(self, index):
        try:
            # Get the clicked file name
            self.selected_file_path = self.model.filePath(index)
            if self.selected_file_path:
                print(f"Você clicou em {self.selected_file_path}")
            else:
                print("Nenhum arquivo selecionado.")
        except Exception as e:
            print(f"Erro ao acessor o arquivo: {e}")

    def add_file(self):
        try:
            # Abre um diálogo de arquivo para selecionar um arquivo para adicionar
            file_path, _ = QFileDialog.getOpenFileName(self, "Abrir arquivo", "", 'CSV, TXT, XLSX (*.csv *.txt *.xlsx)')

            if file_path:
                # Define o diretório de destino
                dest_path = os.path.join(self.root_path, os.path.basename(file_path))

                # Tenta copiar o arquivo para o diretório de destino
                try:
                    shutil.copy(file_path, dest_path)
                except Exception as e:
                    print(f"Erro ao copiar o arquivo: {e}")
                    return

                # Tenta atualizar a visualização em árvore
                try:
                    self.manageFilesTreeView.setModel(None)
                    self.manageFilesTreeView.setModel(self.model)

                    # Define a visualização em árvore de volta para o diretório de uploads
                    self.manageFilesTreeView.setRootIndex(self.model.index(self.root_path))
                except Exception as e:
                    print(f"Erro ao atualizar a visualização em árvore: {e}")
        except Exception as e:
            print(f"Erro ao abrir o diálogo de arquivo: {e}")

    def rename_file(self):
        try:
            # Obtém o arquivo selecionado
            selected_indexes = self.manageFilesTreeView.selectedIndexes()
            if selected_indexes:
                file_path = self.model.filePath(selected_indexes[0])

                # Lembra o diretório atual
                current_directory = os.path.dirname(file_path)

                # Obtém o novo nome do arquivo do usuário
                new_file_name, ok = QInputDialog.getText(self, "Renomear arquivo", "Digite o novo nome do arquivo:")
                if ok and new_file_name:
                    # Cria o novo caminho do arquivo
                    new_file_path = os.path.join(os.path.dirname(self.selected_file_path), new_file_name)

                    # Tenta renomear o arquivo
                    try:
                        os.rename(file_path, new_file_path)
                    except Exception as e:
                        print(f"Erro ao renomear o arquivo: {e}")
                        return

                    # Tenta atualizar a visualização em árvore
                    try:
                        self.manageFilesTreeView.setModel(None)
                        self.manageFilesTreeView.setModel(self.model)

                        # Define a visualização em árvore de volta para o diretório atual
                        self.manageFilesTreeView.setRootIndex(self.model.index(current_directory))
                    except Exception as e:
                        print(f"Erro ao atualizar a visualização em árvore: {e}")
        except Exception as e:
            print(f"Erro ao acessar o caminho do arquivo: {e}")

    def delete_file(self):
        try:
            # Obtém o arquivo selecionado
            selected_indexes = self.manageFilesTreeView.selectedIndexes()
            if selected_indexes:
                file_path = self.model.filePath(selected_indexes[0])

                # Lembra o diretório atual
                current_directory = os.path.dirname(file_path)

                # Tenta excluir o arquivo
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(f"Erro ao excluir o arquivo: {e}")
                    return

                # Tenta atualizar a visualização em árvore
                try:
                    self.manageFilesTreeView.setModel(None)
                    self.manageFilesTreeView.setModel(self.model)

                    # Define a visualização em árvore de volta para o diretório atual
                    self.manageFilesTreeView.setRootIndex(self.model.index(current_directory))
                except Exception as e:
                    print(f"Erro ao atualizar a visualização em árvore: {e}")
        except Exception as e:
            print(f"Erro ao acessar o caminho do arquivo: {e}")

class HelpWindow(QMainWindow, Ui_HelpMainWindow):
    def __init__(self):
        super(HelpWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Ajuda")

        # Create a QFileSystemModel
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())

        # Set the model for helpTreeView
        self.helpTreeView.setModel(self.model)

        # Set the root index for helpTreeView
        root_path = os.path.dirname(os.path.abspath(__file__)) + '/docs'
        self.helpTreeView.setRootIndex(self.model.index(root_path))

        # Hide the "Size" and "Type" columns
        self.helpTreeView.hideColumn(1)
        self.helpTreeView.hideColumn(2)
        self.helpTreeView.hideColumn(3)

        # Connect the clicked signal to our custom slot
        self.helpTreeView.clicked.connect(self.on_helpTreeView_clicked)

        self.show()

    def on_helpTreeView_clicked(self, index):
        # Get the full file path of the clicked item
        file_path = self.helpTreeView.model().filePath(index)

        # Check if it's a markdown file
        if os.path.isfile(file_path) and file_path.endswith('.md'):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            # Convert markdown to HTML and display the
            # content in the helpTextEdit
            html = markdown.markdown(content)
            self.helpTextEdit.setHtml(html)

class AboutWindow(QMainWindow, Ui_AboutWindow):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sobre")

        # Connect the buttons to the openUrl method
        self.giecarBtn.clicked.connect(lambda: self.openUrl
                                       ('http://gcr.sites.uff.br/'))
        self.githubBtn.clicked.connect(lambda: self.openUrl
                                       ('https://github.com'))

    def openUrl(self, url):
        QDesktopServices.openUrl(QUrl(url))

class TableManager:
    def __init__(self, table, formulaBar, cellNameBox):
        self.table = table
        self.formulaBar = formulaBar
        self.cellNameBox = cellNameBox
        self.start_cell = None

        self.table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)

        self.table.pressed.connect(self.onCellPressed)
        self.table.entered.connect(self.onCellEntered)
        self.table.currentCellChanged.connect(self.updateCellComboBox)
        self.table.cellClicked.connect(self.updateFormulaBar)
        self.formulaBar.textChanged.connect(self.updateCurrentItem)
        self.table.customContextMenuRequested.connect(self.contextMenuEvent)


    def contextMenuEvent(self, event):
        contextMenu = QMenu()
        self.rightClickedColumn = self.table.columnAt(event.x())

        actions = {
            "Copiar": self.copy,
            "Colar": self.paste,
            "Recortar": self.cut,
            "Limpar": self.clear
        }

        for action_text, action_func in actions.items():
            contextMenu.addAction(action_text, action_func)

        contextMenu.addSeparator()

        # Create submenus and their actions
        submenus = {
            "Inserir...": {
                "Inserir Linha Acima": lambda: self.addRow(above=True),
                "Inserir Linha Abaixo": lambda: self.addRow(above=False),
                "Inserir Coluna à Direita": lambda: self.addColumn(left=False),
                "Inserir Coluna à Esquerda": lambda: self.addColumn(left=True)
            },
            "Excluir...": {
                "Excluir Linha Acima": lambda: self.removeRow(above=True),
                "Excluir Linha Abaixo": lambda: self.removeRow(above=False),
                "Excluir Coluna à Direita": lambda: self.removeColumn(left=False),
                "Excluir Coluna à Esquerda": lambda: self.removeColumn(left=True)
            }
        }

        for submenu_text, submenu_actions in submenus.items():
            submenu = contextMenu.addMenu(submenu_text)
            for action_text, action_func in submenu_actions.items():
                submenu.addAction(action_text, action_func)
                actions[action_text] = action_func

        selected_action = contextMenu.exec(self.table.mapToGlobal(event))

        if selected_action:
            action_text = selected_action.text()
            if action_text in actions:
                actions[action_text]()


    def updateFormulaBar(self, row, column):
        try:
            if row >= 0 and column >= 0:  # Check that row and column are valid
                currentItem = self.table.item(row, column)
                if currentItem and currentItem.text():  # Check that item and its text are not None
                    self.formulaBar.blockSignals(True)
                    self.formulaBar.setText(currentItem.text())
                    self.formulaBar.blockSignals(False)
                else:
                    self.formulaBar.clear()
            else:
                self.formulaBar.clear()
        except Exception as e:
            print(f"Erro ao atualizar a barra de fórmulas: {e}")
            self.formulaBar.clear()

    def updateCurrentItem(self, text):
        try:
            if text is not None:  # Check that text is not None
                currentItem = self.table.currentItem()
                if currentItem:  # Check that currentItem is not None
                    currentItem.setText(text)
        except Exception as e:
            print(f"Error ao atualizar o item atual: {e}")

    def updateCellComboBox(self, currentRow, currentColumn,
                           previousRow, previousColumn):
        try:
            if currentRow >= 0 and currentColumn >= 0:  # Check that currentRow and currentColumn are valid
                # Convert column number to letter and add 1 to row number
                cellName = f"{chr(65 + currentColumn)}{currentRow + 1}"
                if cellName:  # Check that cellName is not None
                    self.cellNameBox.clear()
                    self.cellNameBox.addItem(cellName)
        except Exception as e:
            print(f"Erro ao atualizar a NameBox: {e}")

    def onCellPressed(self, index):
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.KeyboardModifier.ControlModifier:
            item = self.table.itemFromIndex(index)
            if item is not None:
                item.setSelected(not item.isSelected())
        elif modifiers == Qt.KeyboardModifier.ShiftModifier:
            if self.start_cell is None:
                self.start_cell = index
            else:
                self.selectRange(self.start_cell, index)

    def onCellEntered(self, index):
        modifiers = QApplication.keyboardModifiers()
        if modifiers == Qt.KeyboardModifier.NoModifier \
            and QApplication.mouseButtons() == Qt.MouseButton.LeftButton:
            selected = self.table.selectedRanges()
            if not selected or (selected[0].bottomRow() != index.row() and \
                selected[0].rightColumn() != index.column()):
                self.table.clearSelection()
                self.table.setCurrentCell(index.row(), index.column())
                item = self.table.itemFromIndex(index)
                if item is not None:
                    item.setSelected(True)

    def selectRange(self, start_index, end_index):
        start_row, end_row = sorted([start_index.row(), end_index.row()])
        start_col, end_col = sorted([start_index.column(), end_index.column()])
        for r in range(start_row, end_row + 1):
            for c in range(start_col, end_col + 1):
                item = self.table.item(r, c)
                if item is not None:
                    item.setSelected(True)

    def addRow(self, above=True):
        rowPosition = self.table.currentRow() \
                        if above else self.table.rowCount()
        self.table.insertRow(rowPosition)

    def addColumn(self, left=True):
        colPosition = self.rightClickedColumn
        if not left:
            colPosition += 1
        self.table.insertColumn(colPosition)
        headers = [self.excel_style(i)
                   for i in range(1, self.table.columnCount() + 1)]
        self.table.setHorizontalHeaderLabels(headers)

    def removeRow(self, above=True):
        rowPosition = self.table.currentRow() \
                        if above else self.table.rowCount() - 1
        self.table.removeRow(rowPosition)

    def removeColumn(self, left=True):
        colPosition = self.table.currentColumn() \
                        if left else self.table.columnCount() - 1
        self.table.removeColumn(colPosition)
        headers = [self.excel_style(i)
                   for i in range(1, self.table.columnCount() + 1)]
        self.table.setHorizontalHeaderLabels(headers)

    def changeFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.table.setFont(font)

    def saveTable(self):
        try:
            options = QFileDialog.Options()
            filename, _ = QFileDialog.getSaveFileName(None,
                                                      'Save File', '',
                                                      'CSV (*.csv)',
                                                      options=options)
            if filename:
                with open(filename, 'w', encoding='UTF-8') as file:
                    for row in range(self.table.rowCount()):
                        row_data = []
                        for column in range(self.table.columnCount()):
                            item = self.table.item(row, column)
                            if item is not None:
                                row_data.append(item.text())
                        if row_data:
                            file.write(','.join(row_data))
                            file.write('\n')
                QMessageBox.information(None, 'Sucesso',
                                        'Tabela salva com sucesso!')
            else:
                QMessageBox.warning(None, 'Aviso',
                                    'Nenhum arquivo selecionado.')
        except Exception as e:
            QMessageBox.critical(None, 'Error', f'Um erro ocorreu: {str(e)}')

    def openCSV(self):
        try:
            filename = QFileDialog.getOpenFileName(None, 'Open File', '',
                                        'CSV, TXT, XLSX (*.csv *.txt *.xlsx)')
            if filename[0] != '':
                dest_path = os.path.join('uploads', os.path.basename(filename[0]))
                # Check if the file already exists in the uploads directory
                if os.path.exists(dest_path):
                    QMessageBox.warning(None, "Arquivo já existente",
                        "Esse arquivo já foi carregado anteriormente.")
                    return
                # Copy the file to the uploads folder
                shutil.copy(filename[0], dest_path)
                if filename[0].endswith('.xlsx'):
                    # Read the XLSX file with pandas
                    dataframe = pd.read_excel(filename[0])
                    # Convert the dataframe to a list of lists and iterate over the rows
                    for row in dataframe.values.tolist():
                        rowPosition = self.table.rowCount()
                        self.table.insertRow(rowPosition)
                        # Ensure the table has enough columns
                        self.table.setColumnCount(max(self.table.columnCount(), len(row)))
                        # Add the data to the table
                        for column, data in enumerate(row):
                            if data is not None:
                                self.table.setItem(rowPosition, column,
                                                   QTableWidgetItem(str(data)))
                            else:
                                print(f"Warning:
                                      Trying to add None value at row
                                      {rowPosition}, column {column}")
                            self.table.update()
                else:
                    with open(filename[0], 'r', encoding='UTF-8') as file:
                        dialect = csv.Sniffer().sniff(file.read(1024))
                        file.seek(0)
                        reader = csv.reader(file, dialect)
                        for row in reader:
                            rowPosition = self.table.rowCount()
                            self.table.insertRow(rowPosition)
                            # Ensure the table has enough columns
                            self.table.setColumnCount(
                                max(self.table.columnCount(), len(row)))
                            # Add the data to the table
                            for column, data in enumerate(row):
                                if data is not None:
                                    self.table.setItem(rowPosition, column, QTableWidgetItem(str(data)))
                                else:
                                    print(f"Warning: Trying to add None
                                          value at row {rowPosition},
                                          column {column}")
                                self.table.update()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Um erro ocorreu: {e}")

    def newTable(self):
        try:
            reply = QMessageBox.question(self.table, 'Nova Tabela',
            "Você tem certeza de que deseja criar uma nova tabela? \
                Todo o progresso atual será perdido.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No)
            if reply == QMessageBox.StandardButton.Yes:
                self.table.setRowCount(0)
                self.table.setColumnCount(0)
                self.table.setRowCount(100)
                self.table.setColumnCount(26)
                headers = [self.excel_style(i)
                           for i in range(1, self.table.columnCount() + 1)]
                self.table.setHorizontalHeaderLabels(headers)
        except Exception as e:
            QMessageBox.critical(self.table, 'Erro',
                f'Ocorreu um erro ao criar uma nova tabela: {str(e)}')

    def textAlignment(self, alignment):
        # left, center, right
        selected_items = self.table.selectedItems()
        if alignment == 'left':
            for item in selected_items:
                item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
        elif alignment == 'center':
            for item in selected_items:
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        elif alignment == 'right':
            for item in selected_items:
                item.setTextAlignment(Qt.AlignmentFlag.AlignRight)

    def changeCellColor(self):
        try:
            color = QColorDialog.getColor()
            if color.isValid():
                selected_items = self.table.selectedItems()
                if selected_items:
                    for item in selected_items:
                        item.setBackground(QColor(color))
                else:
                    QMessageBox.warning(None, 'Aviso',
                                        'Nenhuma célula selecionada.')
            else:
                QMessageBox.warning(None, 'Aviso', 'Cor inválida selecionada.')
        except Exception as e:
            QMessageBox.critical(None, 'Erro',
            f'Ocorreu um erro ao alterar a cor da célula: {str(e)}')

    def changeTextColor(self):
        try:
            color = QColorDialog.getColor()
            if color.isValid():
                for item in self.table.selectedItems():
                    item.setForeground(color)
            else:
                QMessageBox.warning(None, 'Aviso', 'Cor inválida selecionada.')
        except Exception as e:
            QMessageBox.critical(None, 'Erro',
            f'Ocorreu um erro ao alterar a cor do texto: {str(e)}')

    def copy(self):
        selected = self.table.selectedRanges()[0]
        s = ""
        for r in range(selected.rowCount()):
            for c in range(selected.columnCount()):
                item = self.table.item(selected.topRow() + r,
                                       selected.leftColumn() + c)
                if item is not None:
                    s += item.text() + "\t"
                else:
                    s += "\t"
            s = s[:-1] + "\n"  # remove last '\t'
        QApplication.clipboard().setText(s)

    def paste(self):
        selected = self.table.selectedRanges()[0]
        s = QApplication.clipboard().text()
        for r, line in enumerate(s.split("\n")[:-1]):  # remove last '\n'
            for c, text in enumerate(line.split("\t")):
                item = self.table.item(selected.topRow() + r,
                                       selected.leftColumn() + c)
                if item is None:
                    item = QTableWidgetItem()
                    self.table.setItem(selected.topRow() + r,
                                       selected.leftColumn() + c, item)
                item.setText(text)

    def cut(self):
        self.copy()
        for item in self.table.selectedItems():
            if item is not None:
                item.setText('')

    def clear(self):
        for item in self.table.selectedItems():
            if item is not None:
                item.setText('')

    @staticmethod
    def excel_style(col):
        string = ""
        while col > 0:
            col, remainder = divmod(col - 1, 26)
            string = chr(65 + remainder) + string
        return string

class MyGUI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        # uic.loadUi('maingui.ui', self)

        self.setupUi(self)
        self.setWindowTitle("Kraken Geophysics")

        self.actionSair.triggered.connect(QApplication.instance().quit)

        # Create a TableManager for the mainSheetTable
        self.tableManager = TableManager(self.mainSheetTable,
                                         self.formulaBar,
                                         self.cellNameBox)

        #new file
        self.newFileToolbar.triggered.connect(self.tableManager.newTable)
        self.actionNew.triggered.connect(self.tableManager.newTable)

        #opening
        self.actionAbrirToolbar.triggered.connect(
            self.tableManager.openCSV)
        self.actionAbrir.triggered.connect(
            self.tableManager.openCSV)
        self.actionImportar_Arquivo.triggered.connect(
            self.tableManager.openCSV)
        # saving
        self.actionSaveToolbar.triggered.connect(
            self.tableManager.saveTable)
        self.actionSalvar.triggered.connect(
            self.tableManager.saveTable)
        # font
        self.actionChangeFontToolbar.triggered.connect(
            self.tableManager.changeFont)

        self.changeTextColorBtn.triggered.connect(
            self.tableManager.changeTextColor)
        self.changeCellColorBtn.triggered.connect(
            self.tableManager.changeCellColor)
        self.actionSobre.triggered.connect(
            self.openAboutWindow)
        self.actionAjuda.triggered.connect(
            self.openHelpWindow)
        self.actionGerenciar_Arquivos.triggered.connect(
            self.openManageFilesWindow)
        self.actionManageFilesToolbar.triggered.connect(
            self.openManageFilesWindow)
        self.actionCalculadora.triggered.connect(
            self.openSimplePlotWindow)
        self.actionOpenCalculatorToolbar.triggered.connect(
            self.openSimplePlotWindow)
        self.actionTendencyPlot.triggered.connect(
            self.openPlotTendenciaWindow)
        self.actionTendencyPlotToolbar.triggered.connect(
            self.openPlotTendenciaWindow)
        self.actionClassificacao_de_Fluidos.triggered.connect(
            self.openGradientClassificationWindow)
        self.actionEditor_de_Texto.triggered.connect(
            self.openTextEditorWindow)
        self.actionCodeEditorToolbar.triggered.connect(
            self.openTextEditorWindow)

        self.alignLeftButton.triggered.connect(
            lambda: self.tableManager.textAlignment('left'))
        self.alignCenterButton.triggered.connect(
            lambda: self.tableManager.textAlignment('center'))
        self.alignRightButton.triggered.connect(
            lambda: self.tableManager.textAlignment('right'))

        # Create actions
        copyAction = QAction(self)
        copyAction.setShortcut(QKeySequence("Ctrl+C"))

        pasteAction = QAction(self)
        pasteAction.setShortcut(QKeySequence("Ctrl+V"))

        cutAction = QAction(self)
        cutAction.setShortcut(QKeySequence("Ctrl+X"))

        # Add actions to the widget
        self.addAction(copyAction)
        self.addAction(pasteAction)
        self.addAction(cutAction)

        # Connect actions to your methods
        copyAction.triggered.connect(self.tableManager.copy)
        pasteAction.triggered.connect(self.tableManager.paste)
        cutAction.triggered.connect(self.tableManager.cut)

        self.show()

    def openAboutWindow(self):
        self.aboutWindow = AboutWindow()
        self.aboutWindow.show()

    def openHelpWindow(self):
        self.helpWindow = HelpWindow()
        self.helpWindow.show()

    def openManageFilesWindow(self):
        self.manageFiles = ManageFiles()
        self.manageFiles.show()

    def openSimplePlotWindow(self):
        self.simplePlotWindow = SimplePlotWindow()
        self.simplePlotWindow.show()

    def openPlotTendenciaWindow(self):
        self.plotTendenciaWindow = PlotTendenciaWindow()
        self.plotTendenciaWindow.show()

    def openGradientClassificationWindow(self):
        self.gradientClassificationWindow = GradientClassificationWin()
        self.gradientClassificationWindow.show()

    def openTextEditorWindow(self):
        self.textEditorWindow = TextEditorWindow()
        self.textEditorWindow.show()

def main():
    app = QApplication(sys.argv)
    window = MyGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()