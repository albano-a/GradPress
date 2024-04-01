import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt6.QtWidgets import (QApplication, QMainWindow, QMessageBox)
from pyui.plot_tendencia_window import Ui_plotTendenciaWindow


from app_functions import pressure_gradient_classification


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

def main():
    app = QApplication(sys.argv)
    window = PlotTendenciaWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()