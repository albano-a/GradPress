import matplotlib.pyplot as plt
import os
import pandas as pd

from Functions import temperature as temp
from Functions.general import timing_function
from Interface.pyInterface.temperatureInterface import Ui_mainWindow
from Interface.pyInterface.temperatureInterfaceDialog import Ui_configurationPlotDialog
from PyQt6.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QVBoxLayout,
    QFileDialog,
    QDialog,
    QApplication,
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure

plt.style.use(["bmh"])


class ConfigurationDialog(QDialog, Ui_configurationPlotDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class TemperatureAnalysis(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)

        self.__plotLayout = QVBoxLayout(self.plotFrame)
        self.__plotLayout.addWidget(self.canvas)

        self.importFileToolBtn.clicked.connect(self.importFile)
        self.plotButtonTemp.clicked.connect(self.plotTemperature)
        self.configurationButton.clicked.connect(self.openPlotConfigurationDialog)

        self.matplotlib_toolbar = NavigationToolbar2QT(self.canvas)

        self.homePlotButton.clicked.connect(self.matplotlib_toolbar.home)
        self.backwardPlotButton.clicked.connect(self.matplotlib_toolbar.back)
        self.forwardPlotButton.clicked.connect(self.matplotlib_toolbar.forward)
        self.panPlotButton.clicked.connect(self.matplotlib_toolbar.pan)
        self.zoomPlotButton.clicked.connect(self.matplotlib_toolbar.zoom)
        self.editPlotButton.clicked.connect(self.matplotlib_toolbar.edit_parameters)
        self.configureSubplotsButton.clicked.connect(
            self.matplotlib_toolbar.configure_subplots
        )
        self.savePlotButton.clicked.connect(self.matplotlib_toolbar.save_figure)

    def importFile(self):
        fileDialog = QFileDialog()
        filePath, _ = fileDialog.getOpenFileName(
            self,
            "Open File",
            "uploads",
            "CSV, TXT, XLSX (*.csv *.txt *.xlsx);;All Files (*)",
        )

        if filePath:
            self.inputFilePath.setText(filePath)

    def openPlotConfigurationDialog(self):
        dialog = ConfigurationDialog()
        dialog.exec()

    def plotTemperature(self):
        # This function has to plot in the `plotFrame` frame the temperature. For that, it
        # needs to run the function `temp.main` and store it's returning values in variables.
        # Then prepare the plot using the matplotlib function
        fname = self.inputFilePath.text()

        temp_top, tvdss_top, y_top, temp_bot, tvdss_bot, y_bot, temp_total, tvdss, predic, a, b = (
            temp.main(fname)
        )
        
        self.figure.clear()
        
        ax = self.canvas.figure.add_subplot(111)
        ax.set_title("Temperature", fontweight="bold", fontsize=14, color="#212121")
        ax.scatter(temp_total, tvdss, label="Corrected")
        ax.plot(temp_total, predic, '--', color="red", label=f"Regression y = {a}x + {b}")
        ax.set_xlabel("Temp")
        ax.set_ylabel("Depth")
        ax.legend(loc="upper right")
        self.canvas.draw()
        
