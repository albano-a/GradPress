import csv
import sys

import matplotlib.pyplot as plt
import pandas as pd
from functions.general import uploadFile
from interface.python.maingui_ui import Ui_MainWindow
from main_rc import *
from modules.about_module import AboutWindow
from modules.crud_module import ManageFiles
from modules.gradient_module import GradientClassificationWin
from modules.help_module import HelpWindow
from modules.plot_module import SimplePlotWindow
from modules.regression_module import PlotTendenciaWindow
from modules.temperatureModule import TemperatureAnalysis
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QKeySequence
from PyQt5.QtWidgets import (
    QAction,
    QApplication,
    QColorDialog,
    QFileDialog,
    QFontDialog,
    QMainWindow,
    QMenu,
    QMessageBox,
    QTableWidgetItem,
)

plt.style.use(["bmh"])


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
            "Limpar": self.clear,
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
                "Inserir Coluna à Esquerda": lambda: self.addColumn(left=True),
            },
            "Excluir...": {
                "Excluir Linha Acima": lambda: self.removeRow(above=True),
                "Excluir Linha Abaixo": lambda: self.removeRow(above=False),
                "Excluir Coluna à Direita": lambda: self.removeColumn(left=False),
                "Excluir Coluna à Esquerda": lambda: self.removeColumn(left=True),
            },
        }

        for submenu_text, submenu_actions in submenus.items():
            submenu = contextMenu.addMenu(submenu_text)
            for action_text, action_func in submenu_actions.items():
                submenu.addAction(action_text, action_func)
                actions[action_text] = action_func

        # selected_action = contextMenu.exec(self.table.mapToGlobal(event))

    def updateFormulaBar(self, row, column):
        try:
            if row >= 0 and column >= 0:  # Check that row and column are valid
                currentItem = self.table.item(row, column)
                if (
                    currentItem and currentItem.text()
                ):  # Check that item and its text are not None
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

    def updateCellComboBox(
        self, currentRow, currentColumn, previousRow, previousColumn
    ):
        try:
            if (
                currentRow >= 0 and currentColumn >= 0
            ):  # Check that currentRow and currentColumn are valid
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
        if (
            modifiers == Qt.KeyboardModifier.NoModifier
            and QApplication.mouseButtons() == Qt.MouseButton.LeftButton
        ):
            selected = self.table.selectedRanges()
            if not selected or (
                selected[0].bottomRow() != index.row()
                and selected[0].rightColumn() != index.column()
            ):
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
        rowPosition = self.table.currentRow() if above else self.table.rowCount()
        self.table.insertRow(rowPosition)

    def addColumn(self, left=True):
        colPosition = self.rightClickedColumn
        if not left:
            colPosition += 1
        self.table.insertColumn(colPosition)
        headers = [self.excel_style(i) for i in range(1, self.table.columnCount() + 1)]
        self.table.setHorizontalHeaderLabels(headers)

    def removeRow(self, above=True):
        rowPosition = self.table.currentRow() if above else self.table.rowCount() - 1
        self.table.removeRow(rowPosition)

    def removeColumn(self, left=True):
        colPosition = (
            self.table.currentColumn() if left else self.table.columnCount() - 1
        )
        self.table.removeColumn(colPosition)
        headers = [self.excel_style(i) for i in range(1, self.table.columnCount() + 1)]
        self.table.setHorizontalHeaderLabels(headers)

    def changeFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.table.setFont(font)

    def saveTable(self):
        try:
            filename, _ = QFileDialog.getSaveFileName(
                None, "Save File", "", "CSV (*.csv);;XLSX (*.xlsx)"
            )
            if filename:
                if filename.endswith(".csv"):
                    with open(filename, "w", encoding="UTF-8") as file:
                        for row in range(self.table.rowCount()):
                            row_data = []
                            for column in range(self.table.columnCount()):
                                item = self.table.item(row, column)
                                if item is not None:
                                    row_data.append(item.text())
                            if row_data:
                                file.write(",".join(row_data))
                                file.write("\n")
                elif filename.endswith(".xlsx"):
                    data = []
                    for row in range(self.table.rowCount()):
                        row_data = []
                        for column in range(self.table.columnCount()):
                            item = self.table.item(row, column)
                            if item is not None:
                                row_data.append(item.text())
                        if row_data:
                            data.append(row_data)
                    headers = data[0]
                    data = data[1:]
                    df = pd.DataFrame(data, columns=headers)
                    df.to_excel(filename, index=False)
                QMessageBox.information(None, "Sucesso", "Tabela salva com sucesso!")
            else:
                QMessageBox.warning(None, "Aviso", "Nenhum arquivo selecionado.")
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Um erro ocorreu: {str(e)}")

    # Open csv to QTableWidget
    def openTable(self):
        filename = QFileDialog.getOpenFileName(
            None, "Open File", "", "CSV, TXT, XLSX (*.csv *.txt *.xlsx)"
        )
        if filename[0] != "":
            if filename[0].endswith(".xlsx"):
                dataframe = pd.read_excel(filename[0])
                rowPosition = 0
                # Set the column count and headers
                # Insert the column titles as the first row
                self.table.insertRow(rowPosition)
                for column, title in enumerate(dataframe.columns):
                    item = QTableWidgetItem(str(title))
                    self.table.setItem(rowPosition, column, item)
                rowPosition += 1

                for row in dataframe.values.tolist():
                    self.table.insertRow(rowPosition)
                    self.table.setColumnCount(max(self.table.columnCount(), len(row)))
                    for column, data in enumerate(row):
                        item = QTableWidgetItem(str(data))
                        self.table.setItem(rowPosition, column, item)
                    # Move to the next row
                    rowPosition += 1
                self.table.update()

            else:
                with open(filename[0], "r", encoding="UTF-8") as file:
                    dialect = csv.Sniffer().sniff(file.read(1024))
                    file.seek(0)
                    reader = csv.reader(file, dialect)
                    # self.table.clearContents()

                    rowPosition = 0
                    for row in reader:
                        self.table.insertRow(rowPosition)
                        self.table.setColumnCount(
                            max(self.table.columnCount(), len(row))
                        )
                        for column, data in enumerate(row):
                            item = QTableWidgetItem(str(data))
                            self.table.setItem(rowPosition, column, item)

                        # Move to the next row
                        rowPosition += 1

                    self.table.update()

    def newTable(self):
        try:
            reply = QMessageBox.question(
                self.table,
                "Nova Tabela",
                "Você tem certeza de que deseja criar uma nova tabela? \
                Todo o progresso atual será perdido.",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No,
            )
            if reply == QMessageBox.StandardButton.Yes:
                self.table.setRowCount(0)
                self.table.setColumnCount(0)
                self.table.setRowCount(100)
                self.table.setColumnCount(26)
                headers = [
                    self.excel_style(i) for i in range(1, self.table.columnCount() + 1)
                ]
                self.table.setHorizontalHeaderLabels(headers)
        except Exception as e:
            QMessageBox.critical(
                self.table,
                "Erro",
                f"Ocorreu um erro ao criar uma nova tabela: {str(e)}",
            )

    def textAlignment(self, alignment):
        # left, center, right
        selected_items = self.table.selectedItems()
        if alignment == "left":
            for item in selected_items:
                item.setTextAlignment(Qt.AlignmentFlag.AlignLeft)
        elif alignment == "center":
            for item in selected_items:
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
        elif alignment == "right":
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
                    QMessageBox.warning(None, "Aviso", "Nenhuma célula selecionada.")
            else:
                QMessageBox.warning(None, "Aviso", "Cor inválida selecionada.")
        except Exception as e:
            QMessageBox.critical(
                None, "Erro", f"Ocorreu um erro ao alterar a cor da célula: {str(e)}"
            )

    def changeTextColor(self):
        try:
            color = QColorDialog.getColor()
            if color.isValid():
                for item in self.table.selectedItems():
                    item.setForeground(color)
            else:
                QMessageBox.warning(None, "Aviso", "Cor inválida selecionada.")
        except Exception as e:
            QMessageBox.critical(
                None, "Erro", f"Ocorreu um erro ao alterar a cor do texto: {str(e)}"
            )

    def copy(self):
        selected = self.table.selectedRanges()[0]
        s = ""
        for r in range(selected.rowCount()):
            for c in range(selected.columnCount()):
                item = self.table.item(selected.topRow() + r, selected.leftColumn() + c)
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
                item = self.table.item(selected.topRow() + r, selected.leftColumn() + c)
                if item is None:
                    item = QTableWidgetItem()
                    self.table.setItem(
                        selected.topRow() + r, selected.leftColumn() + c, item
                    )
                item.setText(text)

    def cut(self):
        self.copy()
        for item in self.table.selectedItems():
            if item is not None:
                item.setText("")

    def clear(self):
        for item in self.table.selectedItems():
            if item is not None:
                item.setText("")

    @staticmethod
    def excel_style(col):
        string = ""
        while col > 0:
            col, remainder = divmod(col - 1, 26)
            string = chr(65 + remainder) + string
        return string


class MainProgram(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainProgram, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Kraken Geophysics")

        self.actionSair.triggered.connect(QApplication.instance().quit)

        # Create a TableManager for the mainSheetTable
        self.tableManager = TableManager(
            self.mainSheetTable, self.formulaBar, self.cellNameBox
        )

        # new file
        self.newFileToolbar.triggered.connect(self.tableManager.newTable)
        self.actionNew.triggered.connect(self.tableManager.newTable)

        # Menubar

        self.actionAbrir.triggered.connect(self.tableManager.openTable)
        self.actionImportar_Arquivo.triggered.connect(uploadFile)
        self.actionSalvar.triggered.connect(self.tableManager.saveTable)
        self.actionSobre.triggered.connect(self.openAboutWindow)
        self.actionAjuda.triggered.connect(self.openHelpWindow)
        self.actionGerenciar_Arquivos.triggered.connect(self.openManageFilesWindow)
        self.actionCalculadora.triggered.connect(self.openSimplePlotWindow)
        self.actionFluidContact.triggered.connect(self.openPlotTendenciaWindow)
        self.actionTemperatureGradient.triggered.connect(self.openTemperatureWindow)
        self.actionFluidClassification.triggered.connect(
            self.openGradientClassificationWindow
        )

        # Toolbar
        self.actionAbrirToolbar.triggered.connect(self.tableManager.openTable)
        self.actionSaveToolbar.triggered.connect(self.tableManager.saveTable)
        self.actionChangeFontToolbar.triggered.connect(self.tableManager.changeFont)
        self.changeTextColorBtn.triggered.connect(self.tableManager.changeTextColor)
        self.changeCellColorBtn.triggered.connect(self.tableManager.changeCellColor)
        self.actionManageFilesToolbar.triggered.connect(self.openManageFilesWindow)
        self.actionOpenPlotWindowToolbar.triggered.connect(self.openSimplePlotWindow)
        self.actionRegressionPlotToolbar.triggered.connect(self.openPlotTendenciaWindow)
        self.alignLeftButton.triggered.connect(
            lambda: self.tableManager.textAlignment("left")
        )
        self.alignCenterButton.triggered.connect(
            lambda: self.tableManager.textAlignment("center")
        )
        self.alignRightButton.triggered.connect(
            lambda: self.tableManager.textAlignment("right")
        )

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
        try:
            self.aboutWindow = AboutWindow()
            self.aboutWindow.show()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def openHelpWindow(self):
        try:
            self.helpWindow = HelpWindow()
            self.helpWindow.show()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def openManageFilesWindow(self):
        try:
            self.manageFiles = ManageFiles()
            self.manageFiles.show()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def openSimplePlotWindow(self):
        try:
            self.simplePlotWindow = SimplePlotWindow()
            self.simplePlotWindow.show()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def openPlotTendenciaWindow(self):
        try:
            self.plotTendenciaWindow = PlotTendenciaWindow()
            self.plotTendenciaWindow.show()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def openGradientClassificationWindow(self):
        try:
            self.gradientClassificationWindow = GradientClassificationWin()
            self.gradientClassificationWindow.show()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def openTemperatureWindow(self):
        try:
            self.openTemperatureWin = TemperatureAnalysis()
            self.openTemperatureWin.show()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


def main():
    app = QApplication([])
    window = MainProgram()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
