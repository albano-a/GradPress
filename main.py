import os
import shutil
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy.linalg import inv
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk
from tkinter import filedialog
from tkinter import ttk
from utilities import create_custom_button

def plot_pressao(x, y, title, xlabel, ylabel, pressao_df, prof_min, prof_max, mesa_rot):
    """
    Função que plota a pressão de formação em função da profundidade (cota)
    """
    ymin = int(prof_min.get()) if prof_min.get() else min(pressao_df['Prof./Intv.(m)'])
    ymax = int(prof_max.get()) if prof_max.get() else max(pressao_df['Prof./Intv.(m)'])

    ymin = int(mesa_rot.get()) - ymin
    ymax = int(mesa_rot.get()) - ymax

    plt.plot(x, y, 'o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.ylim(ymin, ymax)
    plt.gca().invert_yaxis()
    plt.grid()
    plt.show()

class FileUploader:
    def __init__(self, master):
        self.master = master
        self.fname = tk.StringVar(self.master)
        self.fname.set("Selecione um arquivo")
        self.selected_file = tk.StringVar(self.master)

        # Botão para carregar arquivo
        self.upload_button = create_custom_button(self.master,
                                           text="Carregar arquivo",
                                           command=self.upload_file,)
        self.upload_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Label to display messages
        self.message_label = tk.Label(self.master, text="", bg='#ebebeb')
        self.message_label.grid(row=2, column=0, columnspan=2)

        # Dropdown menu to select file
        files = os.listdir("./uploads")
        if not files:
            files = ["Nenhum arquivo encontrado"]

        self.dropdown = tk.OptionMenu(self.master, self.fname, *files)
        self.dropdown.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.fname.trace_add('write', self.update_selected_file)

    def upload_file(self):
        filename = filedialog.askopenfilename()
        print(filename)
        if not os.path.exists("./uploads"):
            os.makedirs("./uploads")
        shutil.copy(filename, "./uploads")
        self.message_label.config(text="Arquivo carregado com sucesso!")

    def update_selected_file(self, *args):
        self.selected_file.set(os.path.join("./uploads", self.fname.get()))

class WellInfoInput:
    def __init__(self, master):
        self.master = master

class ErrorMessage:
    def __init__(self, master):
        self.master = master

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x600")
        self.minsize(575, 600)
        self.title("GradPress")
        self.iconbitmap(default="./icon.ico")  # icone
        self.option_add("*Label.font", "Helvetica 15")  # for the font

        # Determinação de um frame para centralizar o conteúdo da página
        self.frame = tk.Frame(self, bg='#ebebeb')
        ctk.set_appearance_mode("light")
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        # Criação dos frames
        texto_inicial = "Importe e digite as informações do poço nos campos abaixo."
        self.label = tk.Label(self.frame, text=texto_inicial, bg='#ebebeb')
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.file_uploader = FileUploader(self.frame)
        # self.well_info_input = WellInfoInput(self.frame)
        # self.error_message = ErrorMessage(self.frame)

        # Opções do que se fazer com o arquivo
        tk.Label(self.frame, text="Digite o nome do poço: ", bg='#ebebeb') \
            .grid(row=4, columnspan=2, padx=10, pady=10)
        self.nome_entry = tk.Entry(self.frame, borderwidth=2, width=32)
        self.nome_entry.grid(row=5, columnspan=2, padx=10, pady=10)

        # Determinação das profundidades
        tk.Label(self.frame, text="Prof. Inicial", bg='#ebebeb') \
            .grid(row=6, column=0, padx=10, pady=10)
        self.prof_min = tk.Entry(self.frame, borderwidth=2, width=16)
        self.prof_min.grid(row=7, column=0, padx=10, pady=10)

        tk.Label(self.frame, text="Prof. Final", bg='#ebebeb') \
            .grid(row=8, column=0, padx=10, pady=10)
        self.prof_max = tk.Entry(self.frame, borderwidth=2, width=16)
        self.prof_max.grid(row=9, column=0, padx=10, pady=10)

        # Outras opções
        tk.Label(self.frame, text="Mesa Rotativa*", bg='#ebebeb') \
            .grid(row=6, column=1, padx=10, pady=10)
        self.mesa_rot = tk.Entry(self.frame, borderwidth=2, width=16)
        self.mesa_rot.grid(row=7, column=1, padx=10, pady=10)

        # Cria um StringVar para a mensagem de erro
        self.error_message = tk.StringVar(self.frame)

        # Cria um Label para exibir a mensagem de erro
        self.error_label = tk.Label(self.frame, textvariable=self.error_message, fg="red")
        self.error_label.grid(row=11, column=0, columnspan=2, padx=10, pady=10)

        # Butão de plotagem
        create_custom_button(root=self.frame, text="Plotar", command=self.plot_pressure) \
            .grid(row=10, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

    def plot_pressure(self):
        """
        Plota os dados de pressão em relação à profundidade.

        Esta função lê um arquivo CSV contendo dados de pressão e os plota em relação
        aos valores de profundidade (em cota) correspondentes.
        Elimina quaisquer linhas com valores NaN.
        Os valores de profundidade em cota são calculados subtraindo
        os valores de 'Prof./Intv.(m)' do valor de 'mesa_rot'.
        """
        try:
            filename = self.file_uploader.selected_file.get()
            pressao_df = pd.read_csv(filename, delimiter=';')
            pressao_df = pressao_df.dropna(subset=['Prof./Intv.(m)', 'Pressão de Formação (Kgf/cm2)'])
            prof_cota = int(self.mesa_rot.get()) - pressao_df['Prof./Intv.(m)']

            plot_pressao(x=pressao_df['Pressão de Formação (Kgf/cm2)'],
                        y=prof_cota,
                        title=self.nome_entry.get(),
                        xlabel='Pressão de Formação (Kgf/cm2)',
                        ylabel='Profundidade (m)',
                        pressao_df=pressao_df,
                        prof_min=self.prof_min,
                        prof_max=self.prof_max,
                        mesa_rot=self.mesa_rot)
        except Exception as e:
            self.error_message.set(str(e))

if __name__ == "__main__":
    app = App()
    app.mainloop()