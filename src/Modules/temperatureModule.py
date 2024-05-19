import matplotlib.pyplot as plt

from functions import temperature as temp
from interface.python.temperatureInterface import Ui_mainWindow
from interface.python.temperatureInterfaceDialog import Ui_configurationPlotDialog
from PyQt5.QtWidgets import (
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
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.tempDialogButtonBox.accepted.connect(self.exportChoices)
        self.tempDialogButtonBox.rejected.connect(self.reject)
        self.parent = parent

    def exportChoices(self):
        style = self.plotStyleBox.currentText()
        plotTitle = self.plotTitleInputTemp.text()
        fontSize = int(self.fontsizeInputTemp.text())
        axisX = self.axisXInputTemp.text()
        axisY = self.axisYInputTemp.text()

        if isinstance(self.parent, TemperatureAnalysis):
            self.parent.plotTemperature(plotTitle, fontSize, axisX, axisY, style)

        print(style, plotTitle, fontSize, axisX, axisY)


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
        dialog = ConfigurationDialog(self)
        dialog.exec()

    def plotTemperature(
        self,
        title="Gradiente de Temperatura",
        font_size=12,
        axis_x="Temperature",
        axis_y="TVDSS",
        style="bmh",
    ):
        self.figure.clear()
        # This function has to plot in the `plotFrame` frame the temperature. For that, it
        # needs to run the function `temp.main` and store it's returning values in variables.
        # Then prepare the plot using the matplotlib function
        plt.style.use([style])

        fname = self.inputFilePath.text()
        bot_lim = self.minDepthInput.text()
        top_lim = self.maxDepthInput.text()

        if bot_lim == "" and top_lim == "":
            bot_lim = None
            top_lim = None
        else:
            bot_lim = int(bot_lim)
            top_lim = int(top_lim)

        (
            temp_top,
            tvdss_top,
            y_top,
            temp_bot,
            tvdss_bot,
            y_bot,
            temp_total,
            tvdss,
            predic,
            a,
            b,
        ) = temp.main(fname)

        ax = self.canvas.figure.add_subplot(111)
        ax.set_title(title, fontweight="bold", fontsize=font_size, color="#212121")
        ax.scatter(temp_total, tvdss, label="Corrected")
        ax.plot(
            temp_total, predic, "--", color="red", label=f"Regression y = {a}x + {b}"
        )
        if bot_lim is not None and top_lim is not None:
            plt.ylim(bot_lim, top_lim)
        ax.set_xlabel(axis_x)
        ax.set_ylabel(axis_y)
        ax.legend(loc="upper right")
        self.canvas.draw()
