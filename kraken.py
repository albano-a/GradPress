# Standard library imports #
import os
import shutil
from os.path import normpath
import csv
import io
from textwrap import fill
import subprocess
# Related third party imports #
from tkinter import scrolledtext
from click import command
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import pandas as pd
import webbrowser
from tksheet import Sheet
from tkinter import filedialog, ttk
import tkinter as tk
from PIL import Image, ImageTk
import pygments.lexers
from pygments.styles import get_style_by_name
from numpy.linalg import inv
from CTkMenuBar import *
from CTkMessagebox import CTkMessagebox
from CTkToolTip import CTkToolTip
from ttkwidgets.font import *
# Local application/library specific imports #
from components.about import AboutPage
from components.help_window import HelpWindow
from components.tomi_calculations import TOMICalc
from utility.fluid_pressure import fluid_pressure
from chlorophyll import CodeView
from utility.icons import (add_img, remove_img, font_img, show_plot_img,
                           inventory_img, code_img, folder_img, save_img, new_file_img)
from utility.utilities import (create_custom_button, custom_dropdown,
                               centralize_window, custom_CTkEntry,
                               update_and_centralize_geometry, placeholder_function,
                               custom_messagebox, custom_tooltip)
from utility.color_constants import (TEXT_COLOR, BORDER_COLOR, BTN_FG_COLOR,
                             BTN_FG_HOVER_COLOR, FG_COLOR_OUT, FG_COLOR_IN)
import scienceplots

plt.style.use(['science', 'notebook', 'grid'])

# GLOBAL VARIABLES
GIECAR_URL = "http://gcr.sites.uff.br/"
GITHUB_URL = "https://github.com/albano-a/GradPress"
SMALL_WINDOW_SIZE = (300, 200)

class NewWindow(tk.Toplevel):
    """
    A class used to create a new window in a tkinter application.

    Attributes
    ----------
    app : object
        an instance of the main application class
    menu_bar : object
        an instance of the MenuBar class

    Methods
    -------
    __init__(self, master=None, app=None)
        Initializes the NewWindow instance and configures the menu bar.
    """
    def __init__(self, master=None, app=None):
        super().__init__(master)
        self.app = app
        self.menu_bar = MenuBar(self, self.app)
        self.config(menu=self.menu_bar.menu_bar)

class FilesFrame(ctk.CTkScrollableFrame):
    """
    A class used to create a scrollable frame that displays a list of files.

    Attributes
    ----------
    files : list
        A list of file names in the './uploads' directory.
    listbox : object
        The listbox widget that displays the file names.

    Methods
    -------
    __init__(self, master, **kwargs)
        Initializes the FilesFrame instance and sets up the listbox and scrollbar.
    on_select(self, event)
        Handles the event when a file is selected in the listbox.
    add_file(self)
        Opens a file dialog to select a file to add to the listbox.
    rename_file(self)
        Renames the selected file.
    delete_file(self)
        Deletes the selected file.
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # List all files in ./uploads
        self.files = os.listdir("./uploads")

        listbox_frame = tk.Frame(self, bg='#ebebeb')
        listbox_frame.grid(row=0, column=0, padx=10, pady=10)

        self.listbox = tk.Listbox(listbox_frame, width=400, height=200, font=("Segoe UI", 15))
        self.listbox.grid(row=0, column=0, sticky='nsew')  # Use grid instead of pack
        for file in self.files:
            self.listbox.insert(tk.END, file)

        # Create a scrollbar and attach it to the listbox
        scrollbar = ctk.CTkScrollbar(listbox_frame, command=self.listbox.yview, corner_radius=5, fg_color="#f7f7f7")
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
            custom_messagebox(title="Sucesso", message="Arquivo carregado com sucesso!",
                          icon="./img/icons/check.png", option_1="OK", width=400)

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
                    custom_messagebox(title="Sucesso", message="Arquivo renomeado com sucesso!",
                                  icon="./img/icons/check.png", option_1="OK", width=400)
                else:
                    custom_messagebox(title="Aviso!", message="Esse nome já existe!",
                                  icon="./img/icons/warning.png", option_1="OK", width=400)

    def delete_file(self):
        if self.listbox.curselection():  # Check if a file is selected
            index = self.listbox.curselection()[0]
            selected_file = self.files[index]
            os.remove(os.path.join("./uploads", selected_file))
            self.listbox.delete(index)
            del self.files[index]  # Update the files list
            custom_messagebox(title="Sucesso", message="Arquivo deletado com sucesso!",
                          icon="./img/icons/check.png", option_1="OK", width=400)

class ManageFilesWindow:
    def __init__(self, master, app):
        self.master = master
        self.app = app

    def open_manage_window(self):
        self.manage_window = NewWindow(self.master, self.app)
        self.manage_window.title("Gerenciar arquivos")
        centralize_window(self.manage_window, 600, 500)
        self.manage_window.geometry("600x500")
        self.manage_window.minsize(600, 500)
        self.manage_window.option_add("*Label.font", "Helvetica 15")  # for the font

        # Create a frame within the new window
        self.manage_files_frame = tk.Frame(self.manage_window)
        self.manage_files_frame.grid(row=0, column=0, padx=5, pady=5)
        self.manage_files_frame.place(relx=0.5, rely=0.5, anchor='center')

        # label for the title
        gerenciar_texto = "Gerenciar arquivos"
        self.label = ctk.CTkLabel(self.manage_files_frame, text=gerenciar_texto, font=("Helvetica", 20, "bold"))
        # frame for the list of files
        self.files_frame = FilesFrame(self.manage_files_frame, width=500, height=300, fg_color="transparent")
        # buttons for managing files
        # add btn
        self.add_btn = create_custom_button(self.manage_files_frame, text="Adicionar", font=("Segoe UI", 18, "bold"),
                                            command=self.files_frame.add_file, width=75, fg_color="#28a745",
                                            hover_color="#1f7f35", text_color="#212121")
        # rename btn
        self.rnm_btn = create_custom_button(self.manage_files_frame, text="Renomear", font=("Segoe UI", 18, "bold"),
                                            command=self.files_frame.rename_file, width=75, fg_color="#ffc107",
                                            hover_color="#d19d00", text_color="#212121")
        # delete btn
        self.del_btn = create_custom_button(self.manage_files_frame, text="Deletar", font=("Segoe UI", 18, "bold"),
                                            command=self.files_frame.delete_file, width=75, fg_color="#dc3545",
                                            hover_color="#bf2231", text_color="#212121")
        # return btn
        self.return_btn = create_custom_button(self.manage_files_frame, text="Voltar", font=("Segoe UI", 18, "bold"),
                                               command=self.manage_window.destroy, width=75,fg_color="#17a2b8",
                                               hover_color="#117c8d", text_color="#212121")

        self.label.grid(      row=0, column=0, columnspan=4, padx=10, pady=10)
        self.files_frame.grid(row=1, column=0, columnspan=4,padx=5, pady=5)
        self.add_btn.grid(    row=2, column=0, padx=5, pady=5)
        self.rnm_btn.grid(    row=2, column=1, padx=5, pady=5)
        self.del_btn.grid(    row=2, column=2, padx=5, pady=5)
        self.return_btn.grid( row=2, column=3, padx=5, pady=5)

class CalculationsWindow:
    def __init__(self, master, app):
        self.master = master
        self.app = app

    def open_calculations_window(self):
        self.cal_window = tk.Toplevel(self.master)
        self.cal_window.attributes('-toolwindow', True)

        self.cal_window.title("Calculadora")
        # self.cal_window.minsize(600, 600)
        self.cal_window.option_add("*Label.font", "Segoe\\ UI 12")

        # centralize_window(self.cal_window, 410, 500)


        # TODO: Trocar isso por ttk.Notebook
        self.super_calc_win_frame = ttk.Notebook(self.cal_window)
        # self.super_calc_win_frame = ctk.CTkFrame(self.cal_window, fg_color=FG_COLOR_OUT)
        self.super_calc_win_frame.bind("<Configure>", \
            lambda event: update_and_centralize_geometry(self.cal_window, self.super_calc_win_frame))
        self.super_calc_win_frame.place(relx=0.5, rely=0.5, anchor='center')

        width=250; height=15; border_width=1.2

        # frames
        self.calc_win_frame0 = ctk.CTkFrame(self.super_calc_win_frame, corner_radius=3, border_color=BORDER_COLOR,
                                            fg_color=FG_COLOR_IN, border_width=border_width,width=width)
        self.calc_win_frame1 = ctk.CTkFrame(self.super_calc_win_frame, corner_radius=3, border_color=BORDER_COLOR,
                                            fg_color=FG_COLOR_IN, border_width=border_width, width=width)
        self.calc_win_frame2 = ctk.CTkFrame(self.super_calc_win_frame, corner_radius=3, border_color=BORDER_COLOR,
                                            fg_color=FG_COLOR_IN, border_width=border_width, width=width)
        self.calc_win_frame3 = ctk.CTkFrame(self.super_calc_win_frame, corner_radius=3, border_color=BORDER_COLOR,
                                            fg_color=FG_COLOR_IN, border_width=border_width, width=width)
        #btns frames
        self.calc_win_frame4 = ctk.CTkFrame(self.super_calc_win_frame, corner_radius=3, width=width,
                                            fg_color="transparent")

        # Add the tabs to the tab control
        self.super_calc_win_frame.add(self.calc_win_frame0, text='Plotagem simples')
        self.super_calc_win_frame.add(self.calc_win_frame1, text='Linhas de Tendência')
        self.super_calc_win_frame.add(self.calc_win_frame2, text='Gradiente de Pressão')
        self.super_calc_win_frame.add(self.calc_win_frame3, text='Tab 4')
        self.super_calc_win_frame.add(self.calc_win_frame4, text='Tab 5')

        # Pack the tab control
        self.super_calc_win_frame.pack(expand=1, fill="both")



        # self.calc_win_frame0.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')
        # self.calc_win_frame1.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
        # self.calc_win_frame2.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')
        # self.calc_win_frame3.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')
        # self.calc_win_frame4.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

        self.calculator_text_label = \
            "Calculadora"
        self.calculator_text = ctk.CTkLabel(self.calc_win_frame0,
                                            text=self.calculator_text_label,
                                            font=("Segoe UI", 18, "bold"),
                                            justify="center",
                                            width=width, height=height)
        self.calculator_text.pack(fill='x', expand=True, padx=5, pady=5)

        self.calculator_text_label = \
            "Preencha os campos abaixo para gerar os \n gráficos ou calcular o gradiente de pressão."
        self.calculator_text = ctk.CTkLabel(self.calc_win_frame0,
                                            text=self.calculator_text_label,
                                            font=("Segoe UI", 16),
                                            justify="center",
                                            width=width, height=height)
        self.calculator_text.pack(fill='x', expand=True, padx=5, pady=5)

        #----------------------------- Frame 1 -------------------------------------------
        # File dropdown menu frame
        # Logica para o menu dropdown
        class CTkCustomOptionMenu(ctk.CTkOptionMenu):
            def destroy(self):
                self.tk.call('destroy', self._w)

        file_names = os.listdir("./uploads")
        self.selected_file = tk.StringVar(self.calc_win_frame1)
        self.arq_label = ctk.CTkLabel(self.calc_win_frame1,
                                  text="Selecione o arquivo: ",
                                  font=("Segoe UI", 16),
                                  width=width, height=height)
        self.arq_label.pack(fill='x', padx=5, pady=5)
        self.arq_option_menu = CTkCustomOptionMenu(master=self.calc_win_frame1,
                                                variable=self.selected_file,
                                                values= file_names,
                                                fg_color="#f7f7f7",
                                                button_color=BTN_FG_COLOR,
                                                width=240,
                                                button_hover_color=BTN_FG_HOVER_COLOR,
                                                text_color=TEXT_COLOR,
                                                text_color_disabled="#292929",
                                                )
        self.arq_option_menu.pack(fill='x', padx=5, pady=5)
        #------------------------------ Frame 2 ----------------------------------------------------
        # Frame for prof_min
        self.prof_min_Frame = ctk.CTkFrame(self.calc_win_frame2, fg_color="transparent") # FRAME
        self.prof_min_Label = ctk.CTkLabel(self.prof_min_Frame, text="Prof. min:", font=("Segoe UI", 16), height=height)
        self.prof_min_entry = custom_CTkEntry(self.prof_min_Frame, width=120, placeholder_text="Prof. mínima...")
        custom_tooltip(self.prof_min_entry, "Insira a profundidade mínima se quiser plotar um intervalo", delay=1)

        self.prof_min_Frame.pack(side='top', fill='both', padx=5, pady=5)
        self.prof_min_Label.pack(side='left', padx=5, pady=5)
        self.prof_min_entry.pack(fill='x', expand=True, side='left', padx=5, pady=5)

        # Frame for prof_max
        self.prof_max_frame = ctk.CTkFrame(self.calc_win_frame2, fg_color="transparent")
        self.prof_max_label = ctk.CTkLabel(self.prof_max_frame, text="Prof. max:", font=("Segoe UI", 16), height=height)
        self.prof_max_entry = custom_CTkEntry(self.prof_max_frame, width=120, placeholder_text="Prof. máxima...")
        custom_tooltip(self.prof_max_entry, "Insira a profundidade máxima se quiser plotar um intervalo", delay=1)

        self.prof_max_frame.pack(side='top', fill='x', padx=5, pady=5)
        self.prof_max_label.pack(side='left', padx=5, pady=5)
        self.prof_max_entry.pack(fill='x', expand=True, side='left', padx=5, pady=5)

        #---------------------------- Frame 3 --------------------------------------------------------
        #------------------------ Radio Button Frame -------------------------------------------------
        self.radiobtn_frame = ctk.CTkFrame(self.calc_win_frame3,
                                   fg_color="transparent",
                                   height=height)
        self.radiobtn_frame.pack(side="left", padx=5, pady=5)

        self.prof_cota_var = tk.StringVar()
        self.prof_cota_ou_nao = ctk.CTkLabel(self.radiobtn_frame, text="Profundidade está em cota?: ",
                                                font=("Segoe UI", 16))
        self.prof_cota_ou_nao.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.prof_cota_radio_y = ctk.CTkRadioButton(self.radiobtn_frame,
                                                    command=self.radiobutton_event,
                                                    variable=self.prof_cota_var,
                                                    value="Sim",
                                                    text="Sim")
        self.prof_cota_radio_y.grid(row=1, column=0, padx=5, pady=5)

        self.prof_cota_radio_n = ctk.CTkRadioButton(self.radiobtn_frame,
                                                    command=self.radiobutton_event,
                                                    variable=self.prof_cota_var,
                                                    value="Não",
                                                    text="Não")
        self.prof_cota_radio_n.grid(row=1, column=1, padx=5, pady=5)

        self.mesa_rot_frame = ctk.CTkFrame(self.calc_win_frame3,
                                                fg_color="transparent",
                                                height=height)
        self.mesa_rot_frame.pack(side="right", padx=5, pady=5)

        self.mesa_rot_label = ctk.CTkLabel(self.mesa_rot_frame,
                                        text="Mesa Rotativa: ",
                                         height=height,
                                         font=("Segoe UI", 16))
        self.mesa_rot_label.pack(side="top", padx=5, pady=5)

        self.mesa_rot_entry = custom_CTkEntry(self.mesa_rot_frame,
                                                placeholder_text="Insira aqui...")
        self.mesa_rot_entry.pack(side="bottom", expand=True, padx=5, pady=5)

        custom_tooltip(
                self.mesa_rot_entry,
                "Mesa Rotativa é a distância entre a superfície do oceano \n"
                "(do solo no caso de poços terrestres), e a profundidade em cota é \n"
                "calculada usando o valor de altura da mesa rotativa",
                delay=1
            )
        #------------------------------------ Frame 4 ------------------------------------
        self.calc_btn = create_custom_button(root=self.calc_win_frame4,
                                             text="Plot Simples",
                                             command=self.open_plot_window,
                                             width=200)
        self.calc_btn.pack(side="top", padx=5, pady=5)

        self.calc_btn = create_custom_button(root=self.calc_win_frame4,
                                            text="Linhas de tendência",
                                            command=placeholder_function,
                                            width=200)
        self.calc_btn.pack(side="top", padx=5, pady=5)

        self.calc_btn = create_custom_button(root=self.calc_win_frame4,
                                            text="Gradiente de pressão",
                                            command=placeholder_function,
                                            width=200)
        self.calc_btn.pack(side="top", padx=5, pady=5)



    def open_plot_window(self):
         # Check radio button selection
        self.cal_window.attributes('-toolwindow', True)

        self.radiobutton_event()
        # Check radio button selection
        if not self.selected_value:  # substitua 'selected_value' por 'selected_file'
            msg = custom_messagebox(title="Erro", message="É obrigatório selecionar se a profundidade é em cota ou não.",
                                icon="./img/icons/cancel.png", option_1="Cancelar", width=400)

        self.plot_window = tk.Toplevel(self.master)
        self.plot_window.title("Plotar")
        self.plot_window.option_add("*Label.font", "Segoe\\ UI 12")

        # Frame
        self.super_plot_win_frame = ctk.CTkFrame(self.plot_window, fg_color=FG_COLOR_OUT)
        self.super_plot_win_frame.bind("<Configure>",
                                        lambda event: \
                                        update_and_centralize_geometry(self.plot_window, self.super_plot_win_frame))
        self.super_plot_win_frame.place(relx=0.5, rely=0.5, anchor='center')

        width=300; height=15

        # Organização dos frames
        self.plot_win_frame0 = ctk.CTkFrame(self.super_plot_win_frame,
                                            width=width, fg_color=FG_COLOR_IN,
                                            border_width=1.2, border_color=BORDER_COLOR)
        self.plot_win_frame0.pack(fill="x", padx=5, pady=5)

        self.plot_win_frame1 = ctk.CTkFrame(self.super_plot_win_frame,
                                            width=width, fg_color=FG_COLOR_IN,
                                            border_width=1.2, border_color=BORDER_COLOR)
        self.plot_win_frame1.pack(fill="x", padx=5, pady=5)

        self.plot_win_frame2 = ctk.CTkFrame(self.super_plot_win_frame,
                                            width=width, fg_color=FG_COLOR_IN,
                                            border_width=1.2, border_color=BORDER_COLOR)
        self.plot_win_frame2.pack(fill="x", padx=5, pady=5)

        #btns frames
        self.plot_win_frame3 = ctk.CTkFrame(self.super_plot_win_frame,
                                            width=width, fg_color="transparent")
        self.plot_win_frame3.pack(fill="x", padx=5, pady=5)

        self.plot_text_label = "Aqui estão as opções de plot. Algumas \ndelas podem ser alteradas na janela que abrirá"
        self.plot_text = ctk.CTkLabel(self.plot_win_frame0,
                                    text=self.plot_text_label,
                                    font=("Segoe UI", 18, "bold"),
                                    justify="center",
                                    width=width, height=height)
        self.plot_text.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        # FRAME 1 -------------------------------------------------------------------------
        # Frame da determinação do título e dos eixos
        self.plot_title = ctk.CTkLabel(self.plot_win_frame1,
                                            text="Nome do Poço: ",
                                            font=("Segoe UI", 16),
                                            height=height)
        self.plot_title.grid(row=0, column=0, padx=5, pady=5)
        self.plot_title_entry = custom_CTkEntry(self.plot_win_frame1,
                                                    width=200,
                                                    placeholder_text="Insira aqui...")
        self.plot_title_entry.grid(row=0, column=1, padx=5, pady=5)

        self.skip_rows = ctk.CTkLabel(self.plot_win_frame1,
                                        text="Pular quantas linhas*: ",
                                        font=("Segoe UI", 16),
                                        height=height)
        self.skip_rows.grid(row=1, column=0, padx=5, pady=5)
        self.skip_rows_entry = custom_CTkEntry(self.plot_win_frame1,
                                                    width=200,
                                                    placeholder_text="Insira aqui...")
        self.skip_rows_entry.grid(row=1, column=1, padx=5, pady=5)
        # FRAME 2 -------------------------------------------------------------------------
        self.x_label = ctk.CTkLabel(self.plot_win_frame2,
                                        text="Nome do eixo x: ",
                                        font=("Segoe UI", 16),
                                        height=height)
        self.x_label.grid(row=0, column=0, padx=5, pady=5)
        self.x_label_entry = custom_CTkEntry(self.plot_win_frame2,
                                                width=200,
                                                placeholder_text="Insira aqui...")
        self.x_label_entry.grid(row=0, column=1, padx=5, pady=5)

        self.y_label = ctk.CTkLabel(self.plot_win_frame2,
                                        text="Nome do eixo y: ",
                                        font=("Segoe UI", 16),
                                        height=height)
        self.y_label.grid(row=1, column=0, padx=5, pady=5)
        self.y_label_entry = custom_CTkEntry(self.plot_win_frame2,
                                                width=200,
                                                placeholder_text="Insira aqui...")
        self.y_label_entry.grid(row=1, column=1, padx=5, pady=5)
        # FRAME 3 -------------------------------------------------------------------------+

        self.plot_final_btn = create_custom_button(self.plot_win_frame3,
                                                text="Plot final",
                                                command=\
                                                self.plot_final)
        self.plot_final_btn.pack(fill="x", padx=5, pady=5)

    def radiobutton_event(self):
        # Get the currently selected value
        self.selected_value = self.prof_cota_var.get()

        if self.selected_value == "Sim":
            return "Sim"
        elif self.selected_value == "Não":
            return "Não"

    def open_file(self):
        skip_rows_str = self.skip_rows_entry.get()
        if skip_rows_str == "":
            skipped_rows = 0
        else:
            skipped_rows = int(skip_rows_str)
        arq_label_selected_file = "./uploads/" + self.selected_file.get()
        try:
            pressao_df = pd.read_csv(arq_label_selected_file,
                                    delimiter='[;,]',
                                    skiprows=skipped_rows,
                                    names=["A", "B"],
                                    engine='python')
            pressao_df = pressao_df.dropna()
            return pressao_df
        except Exception as e:
            custom_messagebox(title="Erro", message=f"Erro ao ler o arquivo {self.selected_file.get()}: {e}",
                          icon="./img/icons/cancel.png", option_1="OK", width=400)
            return None

    # dataframe = self.open_file()

    def plot_simples(self, x, y, title, xlabel, ylabel, ymin, ymax, dataframe):
        ymin = int(self.prof_min_entry.get()) if self.prof_min_entry.get() else None
        ymax = int(self.prof_max_entry.get()) if self.prof_max_entry.get() else None

        try:
            self.boolean = self.radiobutton_event()

            if self.boolean == "Sim":
                plt.plot(x, y, 'o')
                plt.title(title)
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                if ymin is not None and ymax is not None:
                    plt.ylim(ymin, ymax)
                plt.show()
                print("Sim was selected")

            elif self.boolean == "Não":
                plt.plot(x, y, 'o')
                plt.title(title)
                plt.xlabel(xlabel)
                plt.ylabel(ylabel)
                if ymin is not None and ymax is not None:
                    plt.ylim(ymin, ymax)
                    plt.gca().invert_yaxis()
                plt.show()
                print("Não was selected")

        except Exception as e:
            custom_messagebox(title="Error", message=f"Um erro ocorreu: {e}",
                        icon="./img/icons/cancel.png", option_1="OK", width=400)

    def plot_final(self):
        self.dataframe = self.open_file()
        self.plot_simples(self.dataframe.iloc[:, 1],
                          self.dataframe.iloc[:, 0],
                          self.plot_title_entry.get(),
                          self.x_label_entry.get(),
                          self.y_label_entry.get(),
                          self.prof_min_entry.get(),
                          self.prof_max_entry.get(),
                          self.dataframe)

    def plot_dos_dados(self):
        pass


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
    """
    A class used to represent a Sheet Editor.
    This class provides the functionality to create and manipulate a sheet within a GUI.
    It allows for operations such as adding and removing rows
    and columns, opening and saving the sheet as a CSV file,
    and various other operations provided by the underlying `Sheet` class from the `ctk` library.
    """

    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.sheet = Sheet(self.master)

    def toolbar(self):
        ########################## TOOLBAR ##############################
        self.toolbar_frame = ctk.CTkFrame(self.master, fg_color="#fff")
        self.toolbar_frame.grid(row=0, column=0, sticky='ew', padx=10, pady=10)

        self.new_file_frame = ctk.CTkFrame(self.toolbar_frame,
                                            corner_radius=10,
                                            border_width=0,
                                            fg_color="transparent")
        self.new_file_frame.pack(side='left', padx=5, pady=5)

        self.folder_icon_frame = ctk.CTkFrame(self.toolbar_frame,
                                                corner_radius=10,
                                                border_width=0,
                                                fg_color="transparent")
        self.folder_icon_frame.pack(side='left', padx=5, pady=5)

        self.save_icon_frame = ctk.CTkFrame(self.toolbar_frame,
                                            corner_radius=10,
                                            border_width=0,
                                            fg_color="transparent")
        self.save_icon_frame.pack(side='left', padx=5, pady=5)

        self.inventory_frame = ctk.CTkFrame(self.toolbar_frame,
                                            corner_radius=10,
                                            border_width=0,
                                            fg_color="transparent")
        self.inventory_frame.pack(side='left', padx=5, pady=5)

        self.plot_frame = ctk.CTkFrame(self.toolbar_frame,
                                    corner_radius=10,
                                        border_width=0,
                                        fg_color="transparent")
        self.plot_frame.pack(side='left', padx=5, pady=5)

        self.code_icon_frame = ctk.CTkFrame(self.toolbar_frame,
                                            corner_radius=10,
                                            border_width=0,
                                            fg_color="transparent")
        self.code_icon_frame.pack(side='left', padx=5, pady=5)

        self.font_frame = ctk.CTkFrame(self.toolbar_frame,
                                    corner_radius=10,
                                    border_width=0,
                                    fg_color="transparent")
        self.font_frame.pack(side='left', padx=5, pady=5)

        self.col_frame = ctk.CTkFrame(self.toolbar_frame,
                                    corner_radius=10,
                                    border_width=0,
                                    fg_color="transparent")
        self.col_frame.pack(side='right', padx=5, pady=5)

        self.row_frame = ctk.CTkFrame(self.toolbar_frame,
                                    corner_radius=10,
                                    border_width=0,
                                    fg_color="transparent")
        self.row_frame.pack(side='right', padx=5, pady=5)



        add_row_btn = ctk.CTkButton(self.row_frame,
                                    command=self.add_row,
                                    border_width=0,
                                    text="",
                                    image=add_img,
                                    width=10,
                                    height=10,
                                    fg_color="transparent",
                                    hover_color="#6da3d1"
                                    )
        add_row_btn.grid(row=0,column=0, padx=5, pady=5)
        custom_tooltip(add_row_btn, "+Linhas", delay=0.5)

        add_row_txt = "L"
        add_row_label = ctk.CTkLabel(self.row_frame, text=add_row_txt, font=("Segoe UI",16,"bold"))
        add_row_label.grid(row=0,column=1, padx=2, pady=2)
        # Add buttons to the toolbar


        rm_row_btn = ctk.CTkButton(self.row_frame,
                                text="",
                                command=self.remove_row,
                                image=remove_img,
                                width=10,
                                height=10,
                                fg_color="transparent",
                                hover_color="#d97373"
                                )
        rm_row_btn.grid(row=0,column=2, padx=5, pady=5)
        custom_tooltip(rm_row_btn, "-Linhas", delay=0.5)

        add_col_btn = ctk.CTkButton(self.col_frame,
                                    text="",
                                    command=self.add_column,
                                    image=add_img,
                                    width=10,
                                    height=10,
                                    fg_color="transparent",
                                    hover_color="#6da3d1"
                                    )
        add_col_btn.grid(row=0,column=0, padx=5, pady=5)
        custom_tooltip(add_col_btn, "+Colunas", delay=0.5)

        add_col_txt = "C"
        add_col_label = ctk.CTkLabel(self.col_frame, text=add_col_txt, font=("Segoe UI",16,"bold"))
        add_col_label.grid(row=0,column=1, padx=2, pady=2)

        rm_col_btn = ctk.CTkButton(self.col_frame,
                                   text="",
                                   command=self.remove_column,
                                   image=remove_img,
                                   width=10,
                                   height=10,
                                   fg_color="transparent",
                                   hover_color="#d97373"
                                   )
        rm_col_btn.grid(row=0,column=2, padx=5, pady=5)
        custom_tooltip(rm_col_btn, "-Colunas", delay=0.5)

        font_selector = ctk.CTkButton(self.font_frame,
                                      text="",
                                      command=placeholder_function,
                                      image=font_img,
                                      width=10,
                                      height=10,
                                      fg_color="transparent",
                                      hover_color="#e2e8f0")
        font_selector.grid(row=0, column=0, padx=0, pady=0)
        custom_tooltip(font_selector, "Selecionar fonte", delay=0.5)

        plot_btn_toolbar = ctk.CTkButton(self.plot_frame,
                                        text="",
                                        command=self.app.calculate.open_calculations_window,
                                        image=show_plot_img,
                                        width=10,
                                        height=10,
                                        fg_color="transparent",
                                      hover_color="#e2e8f0")
        plot_btn_toolbar.grid(row=0, column=0, padx=0, pady=0)
        custom_tooltip(plot_btn_toolbar, "Abrir Calculadora", delay=0.5)

        inventory_btn_toolbar = ctk.CTkButton(self.inventory_frame,
                                            text="",
                                            command=self.app.manage_files.open_manage_window,
                                            image=inventory_img,
                                            width=10,
                                            height=10,
                                            fg_color="transparent",
                                            hover_color="#e2e8f0")
        inventory_btn_toolbar.grid(row=0, column=0, padx=0, pady=0)
        custom_tooltip(inventory_btn_toolbar, "Gerenciador de Arquivos", delay=0.5)

        code_btn_toolbar = ctk.CTkButton(self.code_icon_frame,
                                        text="",
                                        command=self.app.code_editor.open_code_editor,
                                        image=code_img,
                                        width=10,
                                        height=10,
                                        fg_color="transparent",
                                        hover_color="#e2e8f0")
        code_btn_toolbar.grid(row=0, column=0, padx=0, pady=0)
        custom_tooltip(code_btn_toolbar, "Editor de Texto", delay=0.5)

        save_btn_toolbar = ctk.CTkButton(self.save_icon_frame,
                                        text="",
                                        command=self.app.sheet_editor.save_sheet,
                                        image=save_img,
                                        width=10,
                                        height=10,
                                        fg_color="transparent",
                                        hover_color="#e2e8f0")
        save_btn_toolbar.grid(row=0, column=0, padx=0, pady=0)
        custom_tooltip(save_btn_toolbar, "Salvar", delay=0.5)

        folder_btn_toolbar = ctk.CTkButton(self.folder_icon_frame,
                                        text="",
                                        command=self.app.sheet_editor.open_csv,
                                        image=folder_img,
                                        width=10,
                                        height=10,
                                        fg_color="transparent",
                                        hover_color="#e2e8f0")
        folder_btn_toolbar.grid(row=0, column=0, padx=0, pady=0) # Open
        custom_tooltip(folder_btn_toolbar, "Abrir", delay=0.5)

        new_file_btn_toolbar = ctk.CTkButton(self.new_file_frame,
                                            text="",
                                            command=self.app.sheet_editor.open_sheet,
                                            image=new_file_img,
                                            width=10,
                                            height=10,
                                            fg_color="transparent",
                                            hover_color="#e2e8f0")
        new_file_btn_toolbar.grid(row=0, column=0, padx=0, pady=0)
        custom_tooltip(new_file_btn_toolbar, "Novo", delay=0.5)

    def open_sheet(self):
        self.toolbar()
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
                        data=[["" for _ in range(26)] for _ in range(100)],
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
                    cleaned_row = [cell.strip() for cell in row if cell.strip() != '']
                    # Ignore rows that only contain empty cells
                    if cleaned_row:
                        writer.writerow(cleaned_row)
            # Updating the backup
            self.sheet.data_backup = self.sheet.data.copy()
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

class CodeEditorWindow:
    def __init__(self, master, app):
        self.master = master
        self.app = app

    def open_code_editor(self):
        self.code_editor = NewWindow(self.master, self.app)
        self.code_editor.title("Editor de texto")

        #function that centralizes the window
        # centralize_window(code_editor, 800, 600)

        # code_editor.minsize(300, 200)
        # code_editor.maxsize(300, 200)
        # code_editor.option_add("*Label.font", "Helvetica 15")

        self.code_editor_frame = tk.Frame(self.code_editor)
        self.code_editor_frame.bind("<Configure>",
                                    lambda event:\
                                        update_and_centralize_geometry(self.code_editor,
                                                                       self.code_editor_frame,
                                                                       max_size=True,
                                                                       child_window=True))
        self.code_editor_frame.grid(row=0, column=0, padx=10, pady=10)
        # self.code_editor_frame.place(relx=0.5, rely=0.5, anchor='center')


        # Create a code editor
        self.code_editor_view = CodeView(self.code_editor_frame,
                                         lexer=pygments.lexers.RustLexer, tab_width=4)
        self.code_editor_view.config(font=("Consolas", 16))
        self.code_editor_view.grid(row=0, column=0, sticky='nsew')

        self.code_editor_frame.grid_rowconfigure(0, weight=1)

        self.btn_code_editor_frame = tk.Frame(self.code_editor_frame)
        self.btn_code_editor_frame.grid(row=1, column=0, padx=10, pady=10)

        self.save_code = create_custom_button(self.btn_code_editor_frame,
                                              text="Salvar",
                                              command=self.save_code,
                                              width=100)
        self.save_code.grid(row=0, column=0, padx=10, pady=10)

    def save_code(self):
        # Get the text from the CodeView widget
        code = self.code_editor_view.get("1.0", "end-1c")

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
        self.code_editor = CodeEditorWindow(self.master, self)
        self.menu_bar = MenuBar(self.master, self)
        self.calculate = CalculationsWindow(self.master, self)
        self.tomi = TOMICalc(self.master, self)
        self.manage_files = ManageFilesWindow(self.master, self)

class MenuBar:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.menu_bar = tk.Menu(self.master)

        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Novo", accelerator='Ctrl+N',
                              command = self.app.sheet_editor.open_sheet)
        self.master.bind_all('<Control-n>', lambda event: self.app.sheet_editor.open_sheet())

        file_menu.add_command(label="Abrir",
                              command=self.app.sheet_editor.open_csv,
                              accelerator='Ctrl+O',
                              #state='disabled'
                              )
        self.master.bind_all('<Control-o>', lambda event: self.app.sheet_editor.open_csv())

        file_menu.add_command(label="Salvar",
                              command=self.app.sheet_editor.save_sheet,
                              accelerator='Ctrl+S')
        self.master.bind_all('<Control-s>', lambda event: self.app.sheet_editor.save_sheet())


        file_menu.add_separator()
        file_menu.add_command(label="Sair", command=self.master.quit) # TODO: If something is not saved, ask if the user wants to save it
        # Adicionar o botão de arquivo ao menu
        self.menu_bar.add_cascade(label="Arquivo", menu=file_menu)

        # Create an Edit menu
        edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        # edit_menu.add_command(label="Abrir PandasGUI", command=self.app.file_handling.view_file)
        edit_menu.add_command(label="Gerenciar arquivos", command=self.app.manage_files.open_manage_window)
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
                                      command=self.app.calculate.open_calculations_window
                                      )
        calculations_menu.add_command(label="TOMI Index",
                                      command=self.app.tomi.open_tomi_window)

        self.menu_bar.add_cascade(label="Calcular", menu=calculations_menu)

        about_menu = tk.Menu(self.menu_bar, tearoff=0)
        about_menu.add_command(label="Ajuda", command=self.help_window) # TODO: Create a function that shows the about window
        self.master.bind_all('<Control-h>', lambda event: self.help_window())
        about_menu.add_command(label="Sobre o GradPress", command=self.about_gradpress_window)

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
        help_window = HelpWindow(self.master)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # startup the application
        ctk.set_appearance_mode("light")
        self.title("Kraken Geophysics")
        self.iconbitmap(default="./icon.ico")  # icon
        self.option_add("*Label.font", "Segoe\\ UI 15")  # font
        centralize_window(self, 900, 600) # function that centralizes the window
        self.minsize(800, 600)

        self.sheet_editor = SheetEditor(self, self)
        self.code_editor = CodeEditorWindow(self, self)

        self.calculate = CalculationsWindow(self, self)
        self.tomi = TOMICalc(self, self)
        self.manage_files = ManageFilesWindow(self, self)
        self.menubar = MenuBar(self, self)


        self.sheet_editor.open_sheet()

if __name__ == "__main__":
    app = App()
    app.mainloop()