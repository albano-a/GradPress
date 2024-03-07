# Standard library imports
import os
import shutil
from os.path import normpath
import csv
import io
# Related third party imports
from click import command
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import pandas as pd
from tksheet import Sheet
from tkinter import filedialog, ttk, Label
import tkinter as tk
from PIL import Image, ImageTk
import pygments.lexers
from pygments.styles import get_style_by_name
import pandasgui as pg
from numpy.linalg import inv
from CTkMenuBar import *
from ttkwidgets.font import *
# Local application/library specific imports
from utility.utilities import create_custom_button, custom_dropdown, centralize_window, create_custom_entry
from utility.fluid_pressure import fluid_pressure
from chlorophyll import CodeView
from utility.icons import add_img, remove_img, font_img



class NewWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.menu_bar = MenuBar(self)
        self.config(menu=self.menu_bar.menu_bar)

class AboutPage:
    def __init__(self, master):
        import webbrowser
        self.master = master
        self.about_window = tk.Toplevel(self.master)
        self.about_window.title("Sobre o GradPress")

        # Função que centraliza a janela
        centralize_window(self.about_window, 300, 200)

        self.about_window.minsize(300, 200)
        self.about_window.maxsize(300, 200)
        self.about_window.option_add("*Label.font", "Segoe\\ UI 15")

        self.about_frame = tk.Frame(self.about_window)
        self.about_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.about_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.giecar_link = create_custom_button(self.about_frame,
                                                text="GIECAR",
                                                command=lambda: \
                                                webbrowser.open("http://gcr.sites.uff.br/"),
                                                width=100,
                                                fg_color="#840000",
                                                hover_color="#a50000")
        self.giecar_link.grid(row=1, column=0, padx=10, pady=10)

        self.github_link = create_custom_button(self.about_frame,
                                                text="GitHub",
                                                command=lambda: \
                                                webbrowser.open("https://github.com/albano-a/GradPress"),
                                                width=100)
        self.github_link.grid(row=1, column=1, padx=10, pady=10)

        texto_inicial = "Desenvolvido por André Albano\nGIECAR - UFF\n2024"
        self.label = tk.Label(self.about_frame, text=texto_inicial, font=("Segoe UI", 10, "bold"))
        self.label.grid(row=2, column=0, columnspan=2, padx=15, pady=10)

class FilesFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # List all files in ./uploads
        self.files = os.listdir("./uploads")

        listbox_frame = tk.Frame(self, bg='#ebebeb')
        listbox_frame.grid(row=0, column=0, padx=10, pady=10)

        self.listbox = tk.Listbox(listbox_frame, width=400, height=200)
        self.listbox.grid(row=0, column=0, sticky='nsew')  # Use grid instead of pack
        for file in self.files:
            self.listbox.insert(tk.END, file)

        # Create a scrollbar and attach it to the listbox
        scrollbar = tk.Scrollbar(listbox_frame, command=self.listbox.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')  # Use grid instead of pack
        self.listbox.config(yscrollcommand=scrollbar.set)

        self.listbox.bind('<<ListboxSelect>>', self.on_select)

    def on_select(self, event):
        # Get selected file
        index = self.listbox.curselection()[0]
        selected_file = self.files[index]

    def add_file(self):
        filename = filedialog.askopenfilename()
        if filename:  # Check if a file was selected
            if not os.path.exists("./uploads"):
                os.makedirs("./uploads")
            shutil.copy(filename, "./uploads")
            new_file = os.path.basename(filename)
            self.listbox.insert(tk.END, new_file)
            self.files.append(new_file)  # Update the files list
            tk.messagebox.showinfo("Sucesso", "Arquivo carregado com sucesso!")

    def rename_file(self):
        if self.listbox.curselection():  # Check if a file is selected
            index = self.listbox.curselection()[0]
            selected_file = self.files[index]
            new_name = tk.simpledialog.askstring("Input", "Novo nome:", parent=self.master)
            if new_name:
                new_path = os.path.join("./uploads", new_name)
                if not os.path.exists(new_path):  # Check if the new file name already exists
                    shutil.move(os.path.join("./uploads", selected_file), new_path)
                    self.listbox.delete(index)
                    self.listbox.insert(index, new_name)
                    self.files[index] = new_name  # Update the files list
                    tk.messagebox.showinfo("Sucesso", "Arquivo renomeado com sucesso!")
                else:
                    tk.messagebox.showerror("Error", "Esse nome já existe!")

    def delete_file(self):
        if self.listbox.curselection():  # Check if a file is selected
            index = self.listbox.curselection()[0]
            selected_file = self.files[index]
            os.remove(os.path.join("./uploads", selected_file))
            self.listbox.delete(index)
            del self.files[index]  # Update the files list
            tk.messagebox.showinfo("Sucesso", "Arquivo deletado com sucesso!")

class ManageFiles:
    def __init__(self, master):
        self.master = master
        self.manage_window = NewWindow(self.master)
        self.manage_window.title("Gerenciar arquivos")
        self.manage_window.geometry("600x500")
        self.manage_window.minsize(600, 500)
        self.manage_window.option_add("*Label.font", "Helvetica 15")  # for the font

        # Create a frame within the new window
        self.manage_files_frame = tk.Frame(self.manage_window#, bg='#ebebeb'
                                           )
        self.manage_files_frame.grid(row=0, column=0, padx=10, pady=10)
        self.manage_files_frame.place(relx=0.5, rely=0.5, anchor='center')

        gerenciar_texto = "Gerenciar arquivos"
        self.label = ctk.CTkLabel(self.manage_files_frame,
                                  text=gerenciar_texto,
                                  font=("Helvetica", 20, "bold"))
        self.label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Lista todos os arquivos
        self.files_frame = FilesFrame(self.manage_files_frame,
                                      width=500,
                                      height=300,
                                      fg_color="transparent")
        self.files_frame.grid(row=1, column=0, columnspan=4,padx=10, pady=10)

        # botao para deletar arquivo
        self.add_button = create_custom_button(self.manage_files_frame,
                                                text="Adicionar",
                                                command=self.files_frame.add_file,
                                                width=75,
                                                fg_color="#34bf49",
                                                hover_color="#279b37",
                                                text_color="#212121")
        self.add_button.grid(row=2, column=0, padx=10, pady=10)

        # botao para deletar arquivo
        self.rename_button = create_custom_button(self.manage_files_frame,
                                                  text="Renomear",
                                                  command=self.files_frame.rename_file,
                                                  width=75,
                                                  fg_color="#0099e5",
                                                  hover_color="#037ef3",
                                                  text_color="#212121")
        self.rename_button.grid(row=2, column=1, padx=10, pady=10)

        # botao para deletar arquivo
        self.delete_button = create_custom_button(self.manage_files_frame,
                                                  text="Deletar",
                                                  command=self.files_frame.delete_file,
                                                  width=75,
                                                  fg_color="#ff4c4c",
                                                  hover_color="#be0027",
                                                  text_color="#212121")
        self.delete_button.grid(row=2, column=2, padx=10, pady=10)

        self.return_button = create_custom_button(self.manage_files_frame,
                                                  text="Voltar",
                                                  command=self.manage_window.destroy,
                                                  width=75)
        self.return_button.grid(row=2, column=3, padx=10, pady=10)

class WellInfoInput:
    def __init__(self, master, file_uploader):
        self.master = master
        self.file_uploader = file_uploader
        ######################################################
        self.well_info_frame = tk.Frame(self.master, bg='#ebebeb')
        self.well_info_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        ######################################################

        texto_inicial = "Preencha as informações abaixo para plotar o gráfico de pressão.\n *Obrigatório"
        self.label = tk.Label(self.well_info_frame, text=texto_inicial, bg='#ebebeb')
        self.label.grid(row=0, column=0, columnspan=2, padx=15, pady=10)

        # Input do nome do poço
        tk.Label(self.well_info_frame, text="Digite o nome do poço: ", bg='#ebebeb') \
            .grid(row=1, columnspan=2, padx=10, pady=10)
        self.nome_entry = tk.Entry(self.well_info_frame,
                                   borderwidth=1,
                                   width=42,
                                   justify="center",
                                   relief="solid",
                                   font=("Helvetica", 12))
        self.nome_entry.grid(row=2, columnspan=2, padx=10, pady=10)

        # Depth inputs
        tk.Label(self.well_info_frame, text="Prof. Inicial", bg='#ebebeb') \
            .grid(row=3, column=0, padx=10, pady=10)
        self.prof_min = tk.Entry(self.well_info_frame,
                                 borderwidth=1,
                                 width=18,
                                 justify="center",
                                 relief="solid",
                                 font=("Helvetica", 12))
        self.prof_min.grid(row=4, column=0, padx=10, pady=10)

        tk.Label(self.well_info_frame, text="Prof. Final", bg='#ebebeb') \
            .grid(row=5, column=0, padx=10, pady=10)
        self.prof_max = tk.Entry(self.well_info_frame,
                                 borderwidth=1,
                                 width=18,
                                 justify="center",
                                 relief="solid",
                                 font=("Helvetica", 12))
        self.prof_max.grid(row=6, column=0, padx=10, pady=10)

        # Other options
        tk.Label(self.well_info_frame, text="Mesa Rotativa*", bg='#ebebeb') \
            .grid(row=3, column=1, padx=10, pady=10)
        self.mesa_rot = tk.Entry(self.well_info_frame,
                                 borderwidth=1,
                                 width=18,
                                 justify="center",
                                 relief="solid",
                                 font=("Helvetica", 12))
        self.mesa_rot.grid(row=4, column=1, padx=10, pady=10)

        self.plot_btn = create_custom_button(root=self.well_info_frame,
                            text="Plotar",
                            command=self.main_plot_pressure,
                            width=300)
        self.plot_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        self.calculate_btn = create_custom_button(root=self.well_info_frame,
                                                  text="Cálculos",
                                                  command=lambda: CalculationsPage(self.master),
                                                    width=300)
        self.calculate_btn.grid(row=8, column=0, columnspan=2, padx=10, pady=10)



    def plot_simples_pressao(self, x, y, title, xlabel, ylabel, pressao_df, prof_min, prof_max, mesa_rot):
        """
        Função que plota a pressão de formação em função da profundidade (cota)
        """
        ymin = int(prof_min.get()) if prof_min.get() else min(pressao_df['Profundidade'])
        ymax = int(prof_max.get()) if prof_max.get() else max(pressao_df['Profundidade'])

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

    def main_plot_pressure(self):
        """
        Plota os dados de pressão em relação à profundidade.

        Esta função lê um arquivo CSV contendo dados de pressão e os plota em relação
        aos valores de profundidade (em cota) correspondentes.
        Elimina quaisquer linhas com valores NaN.
        Os valores de profundidade em cota são calculados subtraindo
        os valores de 'Profundidade' do valor de 'mesa_rot'.
        """
        try:
            filename = self.file_uploader.selected_file.get()
            pressao_df = pd.read_csv(filename,
                                     delimiter='[;,]',
                                     names=["Profundidade", "Pressão"],
                                     engine='python')
            pressao_df = pressao_df.dropna(subset=['Profundidade', 'Pressão'])
            prof_cota = int(self.mesa_rot.get()) - pressao_df['Profundidade']

            self.plot_simples_pressao(x=pressao_df['Pressão'],
                        y=prof_cota,
                        title=self.nome_entry.get(),
                        xlabel='Pressão',
                        ylabel='Profundidade (m)',
                        pressao_df=pressao_df,
                        prof_min=self.prof_min,
                        prof_max=self.prof_max,
                        mesa_rot=self.mesa_rot)
        except Exception as e:
            tk.messagebox.showerror("Error", str(e))

class CalculationsPage:
    def __init__(self, master, app):
        self.master = master
        self.app = app

    def open_calculations(self):
        self.cal_window = tk.Toplevel(self.master)

        self.cal_window.title("Calculadora")
        self.cal_window.geometry("700x800")
        # self.cal_window.minsize(600, 600)
        self.cal_window.option_add("*Label.font", "Segoe\\ UI 12")

        self.super_calc_win_frame = ctk.CTkFrame(self.cal_window)
        self.super_calc_win_frame.grid(row=0, column=0, padx=10, pady=10)
        self.super_calc_win_frame.place(relx=0.5, rely=0.5, anchor='center')

        width=400

        # Criando um frame dentro da imagem
        self.calc_win_frame0 = ctk.CTkFrame(self.super_calc_win_frame, width=width)
        self.calc_win_frame0.grid(row=0, column=0, padx=10, pady=10, sticky='ew')

        self.calc_win_frame1 = ctk.CTkFrame(self.super_calc_win_frame, width=width)
        self.calc_win_frame1.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

        self.calc_win_frame2 = ctk.CTkFrame(self.super_calc_win_frame, width=width)
        self.calc_win_frame2.grid(row=2, column=0, padx=10, pady=10, sticky='ew')

        self.calc_win_frame3 = ctk.CTkFrame(self.super_calc_win_frame, width=width)
        self.calc_win_frame3.grid(row=3, column=0, padx=10, pady=10, sticky='ew')

        self.calc_win_frame4 = ctk.CTkFrame(self.super_calc_win_frame, width=width)
        self.calc_win_frame4.grid(row=4, column=0, padx=10, pady=10, sticky='ew')

        self.calculator_text_label = \
            "Preencha os campos abaixo para gerar os \n gráficos ou calcular o gradiente de pressão."
        self.calculator_text = ctk.CTkLabel(self.calc_win_frame0,
                                            text=self.calculator_text_label,
                                            font=("Segoe UI", 19, "bold"),
                                            justify="center",
                                            width=width)
        self.calculator_text.grid(row=0, column=0, padx=10, pady=10)

        class MyCTkOptionMenu(ctk.CTkOptionMenu):
            def destroy(self):
                self.tk.call('destroy', self._w)
        # Logica para o menu dropdown
        file_names = os.listdir("./uploads")
        selected_file = tk.StringVar(self.calc_win_frame1)
        self.arq_label = ctk.CTkLabel(self.calc_win_frame1,
                                  text="Selecione o arquivo: ",
                                  font=("Segoe UI", 14),
                                  width=width)
        self.arq_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='ew')
        self.arq_option_menu = MyCTkOptionMenu(master=self.calc_win_frame1,
                                                variable=selected_file,
                                                values= file_names,
                                                fg_color="#f0f0f0",
                                                button_color="#840000",
                                                width=260,
                                                button_hover_color="#a50000",
                                                text_color="#212121",
                                                text_color_disabled="#292929",
                                                )
        self.arq_option_menu.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


        self.prof_min_label = ctk.CTkLabel(self.calc_win_frame2,
                                       text="Prof. min: ",
                                       font=("Segoe UI", 14),
                                       width=width//2)
        self.prof_min_label.grid(row=0, column=0, padx=10, pady=10)
        self.prof_min_entry = create_custom_entry(self.calc_win_frame2,
                                                  width=120, placeholder_text="Insira a profundidade mínima")
        self.prof_min_entry.grid(row=1, column=0, padx=10, pady=10)

        self.prof_max_label = ctk.CTkLabel(self.calc_win_frame2,
                                           text="Prof. min: ",
                                           font=("Segoe UI", 14),
                                           width=width//2)
        self.prof_max_label.grid(row=0, column=1, padx=10, pady=10)
        self.prof_max_entry = create_custom_entry(self.calc_win_frame2,
                                                  width=120,
                                                  placeholder_text="Insira a profundidade máxima")
        self.prof_max_entry.grid(row=1, column=1, padx=10, pady=10)

        self.mesa_rot_label = ctk.CTkLabel(self.calc_win_frame3,
                                           text="Mesa Rotativa: ",
                                           width=width//2)
        self.mesa_rot_label.grid(row=2, column=0, padx=10, pady=10)
        self.mesa_rot_entry = create_custom_entry(self.calc_win_frame3,
                                                  width=120,
                                                  placeholder_text="Insira a profundidade da mesa rotativa")
        self.mesa_rot_entry.grid(row=3, column=0, columnspan=1, padx=10, pady=10)

        self.radiobtn_frame = ctk.CTkFrame(self.calc_win_frame3,
                                           fg_color="#cfcfcf",
                                           width=width//2)
        self.radiobtn_frame.grid(row=2, column=1, rowspan=2, columnspan=2, padx=10, pady=10)
        self.prof_cota_var = tk.StringVar()

        self.prof_cota_ou_nao = ctk.CTkLabel(self.radiobtn_frame, text="Profundidade está em cota?: ")
        self.prof_cota_ou_nao.grid(row=0, column=0, columnspan=2, padx=10, pady=10) #label grid
        self.prof_cota_radio_y = ctk.CTkRadioButton(self.radiobtn_frame,
                                                  command=self.radiobutton_event,
                                                  variable=self.prof_cota_var,
                                                  value="Sim",
                                                  text="Sim")
        self.prof_cota_radio_y.grid(row=1, column=0, padx=10, pady=10, sticky='ew')
        self.prof_cota_radio_n = ctk.CTkRadioButton(self.radiobtn_frame,
                                                  command=self.radiobutton_event,
                                                  variable=self.prof_cota_var,
                                                  value="Não",
                                                  text="Não")
        self.prof_cota_radio_n.grid(row=1, column=1, padx=10, pady=10, sticky='ew')



    def radiobutton_event(self):
        # Get the currently selected value
        selected_value = self.prof_cota_var.get()

        # Add your logic here
        if selected_value == "Sim":
            # TODO: This function will be the one where the plot is made
            # without any adaptation to the depth, because is already in cota
            print("Sim was selected")
        elif selected_value == "Não":
            # TODO: This function will be the one where the plot is made
            # with adaptations to the depth, because it is not in cota
            print("Não was selected")

    def on_button_click():
        print("Button clicked!")

    def calculate(self):
        def inv_polynomial(dobs, degree, x):
            """
            Funcao para calcular os parâmetros de uma regressao polinomial
            Dados de entrada:
                d = dados observados
                degree = grau do polinomio
                x = valores das posicoes onde d foi medido, tem que ter a mesma dimensao de d

            Output:
                m = parametros
                G = matriz de modelagem direta
            """
            nl = max(np.shape(dobs))

            G = np.ones((nl,1))
            for pw in range(1,degree+1):

                G = np.c_[G, x**pw ]

            m = np.dot(np.dot(inv(np.dot(G.T,G)),G.T), dobs)

            return m, G

        # m, G = inv_polynomial(dobs=pressao_ogx_93_ma['Profundidade'], degree=1, x=pressao_ogx_93_ma['Pressão de\nFormação\n(Kgf/cm2)'])
        # print(f"y = {m[0]:.2f} + {m[1]:.2f}x")

class SheetEditor:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.sheet = Sheet(self.master)

    def open_sheet(self):
        self.toolbar_frame = ctk.CTkFrame(self.master)
        self.toolbar_frame.grid(row=0, column=0, sticky='ew', padx=10, pady=10)

        self.row_frame = ctk.CTkFrame(self.toolbar_frame,
                                      corner_radius=10,
                                      border_width=0,
                                      fg_color="#fff")
        self.row_frame.grid(row=0, column=0, padx=10, pady=10)

        self.col_frame = ctk.CTkFrame(self.toolbar_frame,
                                      corner_radius=10,
                                      border_width=0,
                                      fg_color="#fff")
        self.col_frame.grid(row=0, column=1, padx=10, pady=10)

        self.font_frame = ctk.CTkFrame(self.toolbar_frame,
                                      corner_radius=10,
                                      border_width=0,
                                      fg_color="#fff")
        self.font_frame.grid(row=0, column=3, padx=10, pady=10)

        add_row_btn = ctk.CTkButton(self.row_frame,
                                    command=self.add_row,
                                    text="",
                                    image=add_img,
                                    width=10,
                                    height=10,
                                    fg_color="#75AFDE")
        add_row_btn.grid(row=0,column=0, padx=10, pady=10)

        add_row_txt = "Linhas"
        add_row_label = ctk.CTkLabel(self.row_frame, text=add_row_txt, font=("Segoe UI",14,"bold"))
        add_row_label.grid(row=0,column=1, padx=2, pady=2)
        # Add buttons to the toolbar


        rm_row_btn = ctk.CTkButton(self.row_frame,
                                text="",
                                command=self.remove_row,
                                image=remove_img,
                                width=10,
                                height=10,
                                fg_color="#de7575")
        rm_row_btn.grid(row=0,column=2, padx=10, pady=10)

        add_col_btn = ctk.CTkButton(self.col_frame,
                                    text="",
                                    command=self.add_column,
                                    image=add_img,
                                    width=10,
                                    height=10,
                                    fg_color="#75AFDE")
        add_col_btn.grid(row=0,column=0, padx=10, pady=10)

        add_col_txt = "Colunas"
        add_col_label = ctk.CTkLabel(self.col_frame, text=add_col_txt, font=("Segoe UI",14,"bold"))
        add_col_label.grid(row=0,column=1, padx=2, pady=2)

        rm_col_btn = ctk.CTkButton(self.col_frame,
                                   text="",
                                   command=self.remove_column,
                                   image=remove_img,
                                   width=10,
                                   height=10,
                                   fg_color="#de7575")
        rm_col_btn.grid(row=0,column=2, padx=10, pady=10)

        def open_font_chooser():
            FontChooser(self.master)

        font_selector = ctk.CTkButton(self.font_frame,
                                      text="",
                                      command=open_font_chooser,
                                      image=font_img,
                                      width=10,
                                      height=10,
                                      fg_color="transparent")
        font_selector.grid(row=0, column=0, padx=10, pady=10)

        # Create a frame for the sheet
        self.sheet_editor_frame = ctk.CTkFrame(self.master)
        self.sheet_editor_frame.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

        # Configure the master grid to expand
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        # Configure the sheet_editor_frame grid to expand
        self.sheet_editor_frame.grid_rowconfigure(0, weight=1)
        self.sheet_editor_frame.grid_columnconfigure(0, weight=1)

        # Create a sheet
        self.sheet = Sheet(self.sheet_editor_frame,
                        page_up_down_select_row=True,
                        default_column_width=120,
                        total_columns=100,
                        total_rows=100,
                        startup_select=(0, 1, "rows"),
                        data=[["" for _ in range(6)] for _ in range(3)],
                        theme="light green")

        self.sheet.grid(row=0, column=0, sticky='nsew')  # Place the sheet in the grid

        self.sheet.enable_bindings(("single_select", "drag_select", "column_drag_and_drop", "row_drag_and_drop",
                                   "column_select", "row_select", "column_width_resize", "double_click_column_resize",
                                   "row_width_resize", "column_height_resize", "arrowkeys", "row_height_resize",
                                   "double_click_row_resize", "right_click_popup_menu", "rc_select", "rc_insert_column",
                                   "rc_delete_column", "rc_insert_row", "rc_delete_row",
                                   "edit_cell", "paste", "cut", "delete", "copy", "undo",
                                   "ctrl_select", "shift_select", "ctrl_a", "double_click_cell", "right_click_cell"
                                   ))

        # Configure the grid to expand
        self.sheet.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        #self.sheet.set_all_cell_sizes_to_text()
        # print(self.sheet["A1"].expand().options(header=True, index=True).data)
        self.sheet.popup_menu_add_command("Abrir .csv", self.open_csv)
        self.sheet.popup_menu_add_command("Salvar", self.save_sheet)

        self.sheet_span = self.sheet.span(
            header=True,
            index=True,
            hdisp=False,
            idisp=False,
        )

    def add_row(self):
        # Insert a new row at the end of the sheet
        self.sheet.insert_rows(rows=1)

    def add_column(self):
        self.sheet.insert_columns(columns=1)

    def remove_row(self):
        last_row_index = self.sheet.total_rows() - 1
        self.sheet.delete_rows(rows=last_row_index, undo=True)

    def remove_column(self):
        last_column_index = self.sheet.total_columns() - 1
        self.sheet.delete_columns(columns=last_column_index, undo=True)

    def save_sheet(self):
        filepath = filedialog.asksaveasfilename(
            parent=self.master,
            title="Salvar a planilha como...",
            filetypes=[("CSV File", ".csv"), ("TSV File", ".tsv")],
            defaultextension=".csv",
            confirmoverwrite=True,
        )
        if not filepath or not filepath.lower().endswith((".csv", ".tsv")):
            return
        try:
            with open(normpath(filepath), "w", newline="", encoding="utf-8") as fh:
                writer = csv.writer(
                    fh,
                    dialect=csv.excel if filepath.lower().endswith(".csv") else csv.excel_tab,
                    lineterminator="\n",
                )
                for row in self.sheet.data:
                    # Clean the data: remove leading/trailing white space
                    cleaned_row = [cell.strip() for cell in row]
                    # Ignore rows that only contain empty cells
                    if any(cell != '' for cell in cleaned_row):
                        writer.writerow(cleaned_row)
        except Exception as error:
            print(error)

    def open_csv(self):

        filepath = filedialog.askopenfilename(parent=self.master, title="Select a csv file")
        if not filepath or not filepath.lower().endswith((".csv", ".tsv")):
            return
        try:
            with open(normpath(filepath), "r") as filehandle:
                filedata = filehandle.read()
            # self.sheet.reset()
            self.sheet.data = [
                r for r in csv.reader(
                    io.StringIO(filedata),
                    dialect=csv.Sniffer().sniff(filedata),
                    skipinitialspace=True,
                )
            ]
        except Exception as error:
            print(error)

    def new_sheet(self):
        self.sheet.reset()
        self.menu_bar.entryconfig(self.open_command, state='normal')

class CodeEditor:
    def __init__(self, master, app):
        self.master = master
        self.app = app

    def open_code_editor(self):
        code_editor = NewWindow(self.master)
        code_editor.title("Editor de texto")

        #function that centralizes the window
        # centralize_window(code_editor, 800, 600)

        # code_editor.minsize(300, 200)
        # code_editor.maxsize(300, 200)
        # code_editor.option_add("*Label.font", "Helvetica 15")

        self.code_editor_frame = tk.Frame(code_editor)
        self.code_editor_frame.grid(row=0, column=0, padx=10, pady=10)
        # self.code_editor_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Create a code editor
        self.code_editor = CodeView(self.code_editor_frame, lexer=pygments.lexers.RustLexer)
        self.code_editor.config(font=("Consolas", 16))
        self.code_editor.pack(fill="both", expand=True)

        self.code_editor_frame.grid_rowconfigure(0, weight=1)

        self.btn_code_editor_frame = tk.Frame(code_editor)
        self.btn_code_editor_frame.grid(row=1, column=0, padx=10, pady=10)

        self.save_code = create_custom_button(self.btn_code_editor_frame,
                                              text="Salvar",
                                              command=self.save_code,
                                              width=100)
        self.save_code.grid(row=0, column=0, padx=10, pady=10)

    def save_code(self):
        # Get the text from the CodeView widget
        code = self.code_editor.get("1.0", "end-1c")

        # Open a file dialog to select where to save the file
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")

        # Write the code to the file
        if file_path:
            with open(file_path, "w") as file:
                file.write(code)

class Application:
    def __init__(self, master):
        self.master = master
        # self.file_handling = FileViewerPandas(self.master, self)
        self.sheet_editor = SheetEditor(self.master, self)
        self.code_editor = CodeEditor(self.master, self)
        self.menu_bar = MenuBar(self.master, self)
        self.calculate = CalculationsPage(self.master, self)


class MenuBar:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.menu_bar = tk.Menu(self.master)


        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Novo", accelerator='Ctrl+N',
                              command = self.app.sheet_editor.open_sheet) # TODO: Create a function that creates a new file. What type of file?

        file_menu.add_command(label="Abrir",
                              command=self.app.sheet_editor.open_csv,
                              accelerator='Ctrl+O',
                              #state='disabled'
                              )

        file_menu.add_command(label="Salvar",
                              command=self.app.sheet_editor.save_sheet,
                              accelerator='Ctrl+S') # TODO: Create a function that saves the file¹

        file_menu.add_command(label="Salvar como...") # TODO: Create a function that saves the file²
        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.master.quit) # TODO: Closes an app
        # Adicionar o botão de arquivo ao menu
        self.menu_bar.add_cascade(label="Arquivo", menu=file_menu)

        # Create an Edit menu
        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        # edit_menu.add_command(label="Abrir PandasGUI", command=self.app.file_handling.view_file)
        edit_menu.add_command(label="Gerenciar arquivos", command=lambda: ManageFiles(self.master))
        edit_menu.add_command(label="Editor de texto", command=self.app.code_editor.open_code_editor)
        edit_menu.add_separator()
        edit_menu.add_command(label="Cortar", accelerator='Ctrl+X') # TODO: Create a function or implement the method that cuts the selected text
        edit_menu.add_command(label="Copiar", accelerator='Ctrl+C') # TODO: Create a function or implement the method that copies the selected text
        edit_menu.add_command(label="Colar", accelerator='Ctrl+V') # TODO: Create a function or implement the method that pastes the selected text
        # Add the Edit menu to the menu bar
        # accelerator argument adds the shortcut
        self.menu_bar.add_cascade(label="Editar", menu=edit_menu)

        calculations_menu = tk.Menu(self.menu_bar, tearoff=0)
        calculations_menu.add_command(label="Calculadora",
                                      command=self.app.calculate.open_calculations
                                      )

        self.menu_bar.add_cascade(label="Calcular", menu=calculations_menu)

        about_menu = tk.Menu(self.menu_bar, tearoff=0)
        about_menu.add_command(label="Ajuda", command=self.help_window) # TODO: Create a function that shows the about window
        about_menu.add_command(label="Sobre o GradPress", command=self.about_gradpress_window) # TODO: Create a function that shows the about window

        self.menu_bar.add_cascade(label="Sobre", menu=about_menu)


        self.master.config(menu=self.menu_bar)

    def save_file(self):
        # Get the data from the sheet
        data = self.sheet_editor.sheet.data()

        # Open a save file dialog
        filepath = filedialog.asksaveasfilename(defaultextension=".csv")

        # If a file was selected, save the data to the file
        if filepath:
            with open(filepath, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(data)

    def about_gradpress_window(self):
        self.about_page = AboutPage(self.master)


    def help_window(self):
        # TODO: Create a help window
        pass

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # self.file_handling = FileViewerPandas(self, self)

        ctk.set_appearance_mode("light")
        self.title("GradPress")
        self.iconbitmap(default="./icon.ico")  # icone
        self.option_add("*Label.font", "Helvetica 15")  # for the font
        centralize_window(self, 800, 600)
        self.minsize(800, 600)

        # Determinação de um frame para centralizar o conteúdo da página
        self.main_frame = tk.Frame(self, bg='#ebebeb')
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.sheet_editor = SheetEditor(self, self)
        self.code_editor = CodeEditor(self, self)
        self.calculate = CalculationsPage(self, self)

        self.menubar = MenuBar(self, self)

        # self.well_info_input = WellInfoInput(self.main_frame, self.file_uploader)
        self.sheet_editor.open_sheet()

if __name__ == "__main__":
    app = App()
    app.mainloop()