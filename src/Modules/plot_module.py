import pandas as pd
import os
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from Interface.pyInterface.plot_ui import Ui_SimplePlotWindow


class SimplePlotWindow(QMainWindow, Ui_SimplePlotWindow):
    def __init__(self):
        super(SimplePlotWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Plot Simples")
        # Initialize self.selected_file
        self.selected_file = None

        # list of files in the uploads directory - Select the file option
        self.files = os.listdir('uploads')
        self.selectFileComboBox.addItems(self.files)

        # prof cota radio buttons
        # if cotaProfNao is checked, labelMesaRotativa and inputMesaRotativa became enabled
        self.cotaProfNao.toggled.connect(self.on_cotaProfNao_toggled)
        self.headerSim.toggled.connect(self.on_headerSim_toggled)

        self.lineColorComboBox.addItems(['blue', 'red', 'green',
                                         'yellow', 'black', 'purple',
                                         'orange', 'pink', 'brown', 'gray'])

        # plot btn
        self.simplePlotBtn.clicked.connect(self.call_plot_simple)

    def on_cotaProfNao_toggled(self, checked):
        self.labelMesaRotativa.setEnabled(checked)
        self.inputMesaRotativa.setEnabled(checked)

    def on_headerSim_toggled(self, checked):
        self.labelHeaderLines.setEnabled(checked)
        self.inputHeaderLines.setEnabled(checked)

    def open_file_for_simple_plotting(self):
        try:
            self.mesa_rotativa = self.inputMesaRotativa.text()
            self.header_lines = self.inputHeaderLines.text()

            self.selected_file = self.selectFileComboBox.currentText()
            # Verifica se self.header_lines não é uma string vazia
            if self.header_lines != '':
                # Tenta converter self.header_lines para um inteiro
                try:
                    skiprows = int(self.header_lines)
                except ValueError:
                    QMessageBox.critical(self, "Erro",
                                "Número de linhas de cabeçalho inválido.")
                    return pd.DataFrame()
            else:
                skiprows = 0

            # Obtém o texto do botão marcado no fileButtonGroup
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
                    QMessageBox.critical(self, "Erro", f"Ocorreu um erro: {e}")
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
                    QMessageBox.critical(self, "Erro", f"Ocorreu um erro: {e}")
                    return pd.DataFrame()

            elif self.file_type_button_text == 'xlsx':
                try:
                    dataframe = pd.read_excel(f'uploads/{self.selected_file}',
                                                skiprows=skiprows,
                                                names=["prof", "pressao"])
                    return dataframe
                except Exception as e:
                    QMessageBox.critical(self, "Erro",
                                         f"Ocorreu um erro: {e}")
                    return pd.DataFrame()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Ocorreu um erro: {e}")
            return pd.DataFrame()

    def plot_simple(self, x, y, title, xlabel, ylabel, ymin, ymax):
        self.selected_color = self.lineColorComboBox.currentText()

        if self.mesa_rotativa != '':
            try:
                y = int(self.mesa_rotativa) - y
            except ValueError:
                QMessageBox.critical(self, "Erro",
                                     "Valor de mesa rotativa inválido.")
                return
        try:
            ymin = int(self.prof_min) if self.prof_min != '' else None
            ymax = int(self.prof_max) if self.prof_max != '' else None
        except ValueError:
            QMessageBox.critical(self, "Erro",
                                 "Valores de prof min ou prof max inválidos.")
            return

        try:
            # Obtém o texto do botão marcado no cotaButtonGroup
            cota_button_text = self.cotaButtonGroup.checkedButton().text()

            if cota_button_text == "Sim":
                plt.plot(x, y, 'o', color=self.selected_color)
                plt.title(title)
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                if ymin is not None and ymax is not None:
                    plt.ylim(ymin, ymax)
                plt.show()

            elif cota_button_text == "Não":
                plt.plot(x, y, 'o', color=self.selected_color)
                plt.title(title)
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                if ymin is not None and ymax is not None:
                    plt.ylim(ymin, ymax)
                    plt.gca().invert_yaxis()
                plt.show()
        except Exception as e:
            QMessageBox.critical(self, "Erro",
                                 f"Ocorreu um erro ao plotar o gráfico: {e}")

    def call_plot_simple(self):
        self.dataframe = self.open_file_for_simple_plotting()
        self.title = self.inputPlotTitle.text()
        self.x_axis = self.inputPlotXAxis.text()
        self.y_axis = self.inputPlotYAxis.text()
        self.prof_min = self.inputProfMin.text()
        self.prof_max = self.inputProfMax.text()

        if self.dataframe.empty:
            QMessageBox.critical(self, "Error", "O dataframe está vazio.")
        else:
            self.plot_simple(self.dataframe.iloc[:, 1],
                            self.dataframe.iloc[:, 0],
                            self.title,
                            self.x_axis,
                            self.y_axis,
                            self.prof_min,
                            self.prof_max)