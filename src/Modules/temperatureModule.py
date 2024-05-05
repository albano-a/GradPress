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
            fileDirName = os.path.dirname(filePath)
            self.inputFilePath.setText(fileDirName)

        return fileDirName

    def openPlotConfigurationDialog(self):
        dialog = ConfigurationDialog()
        dialog.exec()

    def plotTemperature(self):
        pass
