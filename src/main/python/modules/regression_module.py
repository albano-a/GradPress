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

        # prof cota radio buttons
        # if cotaProfNao is checked, labelMesaRotativa and inputMesaRotativa became enabled
        self.cotaProfNao.toggled.connect(self.on_cotaProfNao_toggled)
        self.filepathButton.clicked.connect(self.copy_file_path)
        self.cancelButton.clicked.connect(self.close)
        self.customRadioButton.toggled.connect(self.on_customRadioButton_toggled)
        self.refreshPushButton.clicked.connect(self.refresh_combobox)

        self.inputPressureUnit.addItems(["psi/ft", "psi/m", "kgf/cm2/m", "bar/m"])

        # plot btn
        self.tendenciaPlotBtn.clicked.connect(self.call_plot_trends)

    def on_customRadioButton_toggled(self, checked):
        """Slot to handle the toggling of customRadioButton."""
        self.depth_limit_groupbox.setEnabled(checked)
        self.title_axis_groupbox.setEnabled(checked)

    def copy_file_path(self):
        """Open file dialog for copying file path"""
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            self,
            "Open File",
            "uploads",
            "Excel Files (*.xlsx *.xls);;All Files (*)",
        )

        if file_path:
            self.fileLineEdit.setText(file_path)

    def on_cotaProfNao_toggled(self, checked):
        self.labelMesaRotativa.setEnabled(checked)
        self.inputMesaRotativa.setEnabled(checked)

    def read_file(self):
        self.selected_file = self.fileLineEdit.text()
        sheetTab = self.workbookComboBox.currentText()
        try:
            dataframe = pd.read_excel(
                self.selected_file,
                skiprows=1,
                decimal=",",
                sheet_name=sheetTab,
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            dataframe = pd.DataFrame()
        return dataframe

    def refresh_combobox(self):
        file_path = self.fileLineEdit.text()
        if file_path:
            try:
                workbooks = pd.ExcelFile(file_path).sheet_names
                print(workbooks)
                self.workbookComboBox.clear()
                self.workbookComboBox.addItems(workbooks)
            except Exception as e:
                QMessageBox.critical(
                    self, "Error", f"Failed to load Excel file: {str(e)}"
                )
        else:
            QMessageBox.warning(self, "Warning", "Please select an Excel file first.")

    def process_data_for_trends(self):
        self.dataframe = self.read_file()
        self.kmeans_clusters = self.agrupamentoSpinBox.value()

        title = self.inputPlotTitle.text()
        x_axis = self.inputPlotXAxis.text()
        y_axis = self.inputPlotYAxis.text()
        pressure_unit = self.inputPressureUnit.currentText()
        try:
            return pressure_gradient_classification(
                self.dataframe,
                self.kmeans_clusters,
                pressure_unit,
                title,
                x_axis,
                y_axis,
            )
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")
            return None

    def plot_trends(self):
        (
            top_pressao,
            top_prof,
            bottom_pressao,
            bottom_prof,
            extended_pressure_top,
            extended_cota_top,
            extended_pressure_bot,
            extended_cota_bot,
            y_intercept,
            x_intercept,
            top_fluid_color,
            top_fluid_name,
            bottom_fluid_name,
            bottom_fluid_color,
            slope_top,
            slope_bottom,
        ) = self.process_data_for_trends()

        plt.figure(figsize=(10, 6))

        plt.plot(top_pressao, top_prof, "o", c=top_fluid_color, label=top_fluid_name)
        plt.plot(
            bottom_pressao,
            bottom_prof,
            "o",
            c=bottom_fluid_color,
            label=bottom_fluid_name,
        )
        plt.plot(
            extended_pressure_top,
            extended_cota_top,
            c=top_fluid_color,
            label=top_fluid_name + " " + str(round(slope_top, 4)),
        )
        plt.plot(
            extended_pressure_bot,
            extended_cota_bot,
            "-",
            c=bottom_fluid_color,
            label=bottom_fluid_name + " " + str(round(slope_bottom, 4)),
        )
        plt.plot(
            y_intercept,
            x_intercept,
            "s",
            c="k",
            label="Intersection " + str(round(x_intercept, 2)),
        )

        plt.title(self.inputPlotTitle.text())
        plt.legend(fontsize="small")
        plt.xlabel(self.inputPlotXAxis.text())
        plt.ylabel(self.inputPlotYAxis.text())
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def call_plot_trends(self):
        self.plot_trends()
