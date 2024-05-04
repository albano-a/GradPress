import matplotlib.pyplot as plt
import os
import pandas as pd

from Functions import temperature as temp
from Functions.general import timing_function
from Interface.pyInterface.temperatureInterface import Ui_mainWindow
from PyQt6.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QVBoxLayout,
    QFileDialog,
    QApplication,
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure

plt.style.use(["bmh"])


class TemperatureAnalysis(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)

        self.__plotLayout = QVBoxLayout(self.plotFrame)
        self.__plotLayout.addWidget(self.canvas)

        self.importFileToolBtn.clicked.connect(self.importFile)

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
    
    
