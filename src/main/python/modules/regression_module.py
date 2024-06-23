import pandas as pd
import os
import matplotlib.pyplot as plt
from PyQt5 import uic
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog
from functions.general import pressure_gradient_classification
from functions.uic import import_ui


class PlotTendenciaWindow(QMainWindow):
    def __init__(self):
        super(PlotTendenciaWindow, self).__init__()

        # import uic file

        import_ui(self, "regression")
        self.setWindowIcon(QIcon("src/main/icons/Icon.ico"))

        # self.setupUi(self)
        self.setWindowTitle("Plot de Tendência")

        self.selected_file = None

        # prof cota radio buttons
        # if cotaProfNao is checked, labelMesaRotativa and inputMesaRotativa became enabled
        self.cotaProfNao.toggled.connect(self.on_cotaProfNao_toggled)
        self.headerSim.toggled.connect(self.on_headerSim_toggled)
        self.filepathButton.clicked.connect(self.copy_file_path)
        self.cancelButton.clicked.connect(self.close)

        self.inputPressureUnit.addItems(["psi/ft", "psi/m", "kgf/cm2/m", "bar/m"])

        # plot btn
        self.tendenciaPlotBtn.clicked.connect(self.call_plot_trends)

    def copy_file_path(self):
        """Open file dialog for copying file path"""
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self,
            "Open File",
            "uploads",
            "All Files (*)",
        )

        if file_path:
            self.fileLineEdit.setText(file_path)

    def on_cotaProfNao_toggled(self, checked):
        self.labelMesaRotativa.setEnabled(checked)
        self.inputMesaRotativa.setEnabled(checked)

    def on_headerSim_toggled(self, checked):
        self.labelHeaderLines.setEnabled(checked)
        self.inputHeaderLines.setEnabled(checked)

    def open_file_for_trend_plotting(self):

        self.header_lines = self.inputHeaderLines.text()

        self.selected_file = self.fileLineEdit.text()
        # Check if self.header_lines is not an empty string
        if self.header_lines != "":
            # Convert self.header_lines to an integer
            skiprows = int(self.header_lines)
        else:
            skiprows = 0

        # Get the text of the checked button in the fileButtonGroup
        self.file_type_button_text = self.fileComboBox.currentText()

        if self.file_type_button_text == ".csv":
            try:
                dataframe = pd.read_csv(
                    self.selected_file,
                    delimiter="[;,]",
                    names=["prof", "pressao"],
                    engine="python",
                    skiprows=skiprows,
                )
                return dataframe
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Um erro ocorreu: {e}")
                return pd.DataFrame()

        elif self.file_type_button_text == ".txt":
            try:
                dataframe = pd.read_csv(
                    self.selected_file,
                    skiprows=skiprows,
                    delimiter="\t",
                    names=["prof", "pressao"],
                    engine="python",
                )
                return dataframe
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Um erro ocorreu: {e}")
                return pd.DataFrame()

        elif self.file_type_button_text == ".xlsx":
            try:
                dataframe = pd.read_excel(
                    self.selected_file,
                    skiprows=skiprows,
                    names=["prof", "pressao"],
                )
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
        if self.mesa_rotativa != "":
            # Convert self.mesa_rotativa to an integer and subtract y
            y = int(self.mesa_rotativa) - y

        try:
            fig, axs, messages = pressure_gradient_classification(
                self.dataframe,
                self.kmeansClusters,
                self.pressure_unit,
                self.title,
                self.x_axis,
                self.y_axis,
            )
            plt.show()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Um erro ocorreu: {e}")
            return

    def call_plot_trends(self):
        self.plot_trends()
