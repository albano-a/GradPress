import os
import shutil
import sys
import markdown
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt6 import uic
from PyQt6.QtCore import Qt, QUrl, QResource, QCoreApplication, QDir
from PyQt6.QtGui import (QAction, QKeySequence, QDesktopServices,
                        QFileSystemModel, QStandardItemModel, QStandardItem)
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem,
                            QFileDialog, QMessageBox, QColorDialog, QFontDialog,
                            QInputDialog, QTreeWidgetItem)
from pyui.icons_rc import *
from pyui.maingui import Ui_MainWindow
from pyui.about import Ui_AboutWindow
from pyui.help import Ui_HelpMainWindow
from pyui.manage_files import Ui_ManageFilesWindow
from pyui.simple_plot_window import Ui_SimplePlotWindow
from pyui.plot_tendencia_window import Ui_plotTendenciaWindow
from pyui.gradiente_pressao_window import Ui_gradientePressaoWindow
from app_functions import pressure_gradient_classification

plt.style.use(['bmh'])

class PressureGradientClassificationWindow(QMainWindow, Ui_gradientePressaoWindow):
    def __init__(self):
        super(PressureGradientClassificationWindow, self).__init__()
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

        self.lineColorComboBox.addItems(['blue', 'red', 'green', 'yellow', 'black', \
                                    'purple', 'orange', 'pink', 'brown', 'gray'])

        self.inputPressureUnit.addItems(["psi/ft", "psi/m", "kgf/cm2/m", "bar/m"])

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
                                         self.dataframe, self.kmeansClusters, self.pressure_unit,
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

        self.lineColorComboBox.addItems(['blue', 'red', 'green', 'yellow', 'black', \
                                    'purple', 'orange', 'pink', 'brown', 'gray'])

        # plot btn
        self.simplePlotBtn.clicked.connect(self.call_plot_simple)

    def on_cotaProfNao_toggled(self, checked):
        self.labelMesaRotativa.setEnabled(checked)
        self.inputMesaRotativa.setEnabled(checked)

    def on_headerSim_toggled(self, checked):
        self.labelHeaderLines.setEnabled(checked)
        self.inputHeaderLines.setEnabled(checked)

    def open_file_for_simple_plotting(self):
        self.mesa_rotativa = self.inputMesaRotativa.text()
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

    def plot_simple(self, x, y, title, xlabel, ylabel, ymin, ymax):
        # self.dataframe = self.open_file_for_simple_plotting()
        self.selected_color = self.lineColorComboBox.currentText()

        # Check if self.mesa_rotativa is not an empty string
        if self.mesa_rotativa != '':
            # Convert self.mesa_rotativa to an integer and subtract y
            y = int(self.mesa_rotativa) - y

        # Check if self.prof_min and self.prof_max are not empty strings
        ymin = int(self.prof_min) if self.prof_min != '' else None
        ymax = int(self.prof_max) if self.prof_max != '' else None

        try:
            # Get the text of the checked button in the cotaButtonGroup
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
            QMessageBox.critical(self, "Error", f"Um erro ocorreu: {e}")

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
        # Get the clicked file name
        self.selected_file_path = self.model.filePath(index)
        print(f"You clicked on {self.selected_file_path}")

    def add_file(self):
        # Open a file dialog to select a file to add
        file_path, _ = QFileDialog.getOpenFileName(self, "Abrir arquivo", "", 'CSV, TXT, XLSX (*.csv *.txt *.xlsx)')

        if file_path:
            # Define the destination directory
            dest_path = os.path.join(self.root_path, os.path.basename(file_path))

            # Copy the file to the destination directory
            shutil.copy(file_path, dest_path)

            # Refresh the tree view
            self.manageFilesTreeView.setModel(None)
            self.manageFilesTreeView.setModel(self.model)

            # Set the tree view back to the uploads directory
            self.manageFilesTreeView.setRootIndex(self.model.index(self.root_path))

    def rename_file(self):
        # Get the selected file
        selected_indexes = self.manageFilesTreeView.selectedIndexes()
        if selected_indexes:
            file_path = self.model.filePath(selected_indexes[0])

            # Remember the current directory
            current_directory = os.path.dirname(file_path)

            # Get the new file name from the user
            new_file_name, ok = QInputDialog.getText(self, "Renomear arquivo", "Digite o novo nome do arquivo:")
            if ok and new_file_name:
                # Create the new file path
                new_file_path = os.path.join(os.path.dirname(self.selected_file_path), new_file_name)

                # Rename the file
                os.rename(file_path, new_file_path)

                # Refresh the tree view
                self.manageFilesTreeView.setModel(None)
                self.manageFilesTreeView.setModel(self.model)

                # Set the tree view back to the current directory
                self.manageFilesTreeView.setRootIndex(self.model.index(current_directory))

    def delete_file(self):
        # Get the selected file
        selected_indexes = self.manageFilesTreeView.selectedIndexes()

        if selected_indexes:
            file_path = self.model.filePath(selected_indexes[0])

            # Remember the current directory
            current_directory = os.path.dirname(file_path)

            # Delete the file
            os.remove(file_path)  # Use the file path

            # Refresh the tree view
            self.manageFilesTreeView.setModel(None)
            self.manageFilesTreeView.setModel(self.model)

            # Set the tree view back to the current directory
            self.manageFilesTreeView.setRootIndex(self.model.index(current_directory))

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
        root_path = os.path.dirname(os.path.abspath(__file__)) + '/help'
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

            # Convert markdown to HTML and display the content in the helpTextEdit
            html = markdown.markdown(content)
            self.helpTextEdit.setHtml(html)

class AboutWindow(QMainWindow, Ui_AboutWindow):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sobre")

        # Connect the buttons to the openUrl method
        self.giecarBtn.clicked.connect(lambda: self.openUrl('http://gcr.sites.uff.br/'))
        self.githubBtn.clicked.connect(lambda: self.openUrl('https://github.com'))

    def openUrl(self, url):
        QDesktopServices.openUrl(QUrl(url))

class TableManager:
    def __init__(self, table):
        self.table = table

    def addRow(self):
        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)

    def removeRow(self):
        rowPosition = self.table.rowCount()
        if rowPosition > 0:
            self.table.removeRow(rowPosition - 1)

    def addColumn(self):
        colPosition = self.table.columnCount()
        self.table.insertColumn(colPosition)
        headers = [self.excel_style(i) for i in range(1, self.table.columnCount() + 1)]
        self.table.setHorizontalHeaderLabels(headers)

    def removeColumn(self):
        colPosition = self.table.columnCount()
        if colPosition > 0:
            self.table.removeColumn(colPosition - 1)

    def changeFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.table.setFont(font)

    def saveTable(self):
        filename = QFileDialog.getSaveFileName(None, 'Save File', '', 'CSV(*.csv)')
        if filename[0] != '':
            with open(filename[0], 'w', encoding='UTF-8') as file:
                for row in range(self.table.rowCount()):
                    row_data = []
                    for column in range(self.table.columnCount()):
                        item = self.table.item(row, column)
                        if item is not None:
                            row_data.append(item.text())
                    if row_data:  # Check if row_data is not empty
                        file.write(','.join(row_data))
                        file.write('\n')

    def openCSV(self):
        try:
            filename = QFileDialog.getOpenFileName(None, 'Open File', '', 'CSV, TXT, XLSX (*.csv *.txt *.xlsx)')
            if filename[0] != '':
                dest_path = os.path.join('uploads', os.path.basename(filename[0]))
                # Check if the file already exists in the uploads directory
                if os.path.exists(dest_path):
                    QMessageBox.warning(None, "Arquivo já existente", "Esse arquivo já foi carregado anteriormente.")
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
                                self.table.setItem(rowPosition, column, QTableWidgetItem(str(data)))
                            else:
                                print(f"Warning: Trying to add None value at row {rowPosition}, column {column}")
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
                            self.table.setColumnCount(max(self.table.columnCount(), len(row)))
                            # Add the data to the table
                            for column, data in enumerate(row):
                                if data is not None:
                                    self.table.setItem(rowPosition, column, QTableWidgetItem(str(data)))
                                else:
                                    print(f"Warning: Trying to add None value at row {rowPosition}, column {column}")
                                self.table.update()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Um erro ocorreu: {e}")

    def newTable(self):
        reply = QMessageBox.question(self.table, 'Nova Tabela',
                                     "Você tem certeza de que deseja criar uma nova tabela? Todo o progresso atual será perdido.",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            self.table.setRowCount(0)
            self.table.setColumnCount(0)
            self.table.setRowCount(100)
            self.table.setColumnCount(26)
            headers = [self.excel_style(i) for i in range(1, self.table.columnCount() + 1)]
            self.table.setHorizontalHeaderLabels(headers)

    def changeCellColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            for item in self.table.selectedItems():
                item.setBackground(color)

    def changeTextColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            for item in self.table.selectedItems():
                item.setForeground(color)

    def copy(self):
        selected = self.table.selectedRanges()[0]
        s = ""
        for r in range(selected.rowCount()):
            for c in range(selected.columnCount()):
                s += self.table.item(selected.topRow() + r, selected.leftColumn() + c).text() + "\t"
            s = s[:-1] + "\n"  # remove last '\t'
        QApplication.clipboard().setText(s)

    def paste(self):
        selected = self.table.selectedRanges()[0]
        s = QApplication.clipboard().text()
        for r, line in enumerate(s.split("\n")[:-1]):  # remove last '\n'
            for c, text in enumerate(line.split("\t")):
                self.table.setItem(selected.topRow() + r, selected.leftColumn() + c, QTableWidgetItem(text))

    def cut(self):
        self.copy()
        for item in self.table.selectedItems():
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

        self.actionSair.triggered.connect(exit)

        # Create a TableManager for the mainSheetTable
        self.tableManager = TableManager(self.mainSheetTable)

        #row btns
        self.addRowBtn.clicked.connect(self.tableManager.addRow)
        self.rmRowBtn.clicked.connect(self.tableManager.removeRow)
        # col btns
        self.addColBtn.clicked.connect(self.tableManager.addColumn)
        self.rmColBtn.clicked.connect(self.tableManager.removeColumn)
        #new file
        self.newFileToolbar.triggered.connect(self.tableManager.newTable)
        self.actionNew.triggered.connect(self.tableManager.newTable)

        #opening
        self.actionAbrirToolbar.triggered.connect(self.tableManager.openCSV)
        self.actionAbrir.triggered.connect(self.tableManager.openCSV)
        # saving
        self.actionSaveToolbar.triggered.connect(self.tableManager.saveTable)
        self.actionSalvar.triggered.connect(self.tableManager.saveTable)
        # font
        self.actionChangeFontToolbar.triggered.connect(self.tableManager.changeFont)

        self.changeTextColorBtn.clicked.connect(self.tableManager.changeTextColor)
        self.changeCellColorBtn.clicked.connect(self.tableManager.changeCellColor)
        self.actionSobre.triggered.connect(self.openAboutWindow)
        self.actionAjuda.triggered.connect(self.openHelpWindow)
        self.actionGerenciar_Arquivos.triggered.connect(self.openManageFilesWindow)
        self.actionManageFilesToolbar.triggered.connect(self.openManageFilesWindow)
        self.actionCalculadora.triggered.connect(self.openSimplePlotWindow)
        self.actionOpenCalculatorToolbar.triggered.connect(self.openSimplePlotWindow)
        self.actionTendencyPlot.triggered.connect(self.openPlotTendenciaWindow)
        self.actionTendencyPlotToolbar.triggered.connect(self.openPlotTendenciaWindow)
        self.actionClassificacao_de_Fluidos.triggered.connect(self.openPressureGradientClassificationWindow)
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

    def openPressureGradientClassificationWindow(self):
        self.pressureGradientClassificationWindow = PressureGradientClassificationWindow()
        self.pressureGradientClassificationWindow.show()




def main():
    app = QApplication(sys.argv)
    window = MyGUI()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()