from PyQt6.QtWidgets import QMainWindow 
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from pyui.gradiente_pressao_window import Ui_gradientePressaoWindow
import os


class GradientClassificationWin(QMainWindow,
                                Ui_gradientePressaoWindow):
    # TODO: fully implement this function
    def __init__(self):
        super(GradientClassificationWin, self).__init__()
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

    def save_output_content(self):
        pass