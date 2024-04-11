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
from PyQt6.QtCore import Qt, QDir
from PyQt6.QtGui import (QAction, QKeySequence,
                        QFileSystemModel, QStandardItemModel, QStandardItem,
                        QFont, QColor)
from PyQt6.QtWidgets import (QApplication, QMainWindow, QTableWidgetItem,
                            QFileDialog, QMessageBox, QColorDialog, QFontDialog,
                            QInputDialog, QMenu)

from pyui.icons_rc import *
from pyui.maingui import Ui_MainWindow
from pyui.simple_plot_window import Ui_SimplePlotWindow
from pyui.plot_tendencia_window import Ui_plotTendenciaWindow
from pyui.gradiente_pressao_window import Ui_gradientePressaoWindow
from pyui.text_editor_window import Ui_textEditorWindow

# Software modules
from modules.about_module import AboutWindow
from modules.help_module import HelpWindow
from modules.manage_files_module import ManageFiles
from modules.simple_plot_module import SimplePlotWindow
from modules.plot_tendencia_module import PlotTendenciaWindow
from modules.gradient_classification_module import GradientClassificationWin
from modules.text_editor_module import TextEditorWindow


from app_functions import pressure_gradient_classification

plt.style.use(['bmh'])

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
                                print(f"Warning:\
                                      Trying to add None value at row\
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
                                    print(f"Warning: Trying to add None\
                                          value at row {rowPosition},\
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