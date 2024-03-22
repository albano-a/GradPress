# Standard library imports #
import os
import shutil
from os.path import normpath
import csv
import io
from textwrap import fill
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
from tkinter import filedialog, ttk, Label
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

class AboutPage:
    """
    A class used to create an 'About' page in a tkinter application.

    Attributes
    ----------
    master : object
        The parent window.
    about_window : object
        The 'About' window.
    about_frame : object
        The frame in the 'About' window.
    giecar_link : object
        The 'GIECAR' link button.
    github_link : object
        The 'GitHub' link button.
    label : object
        The label displaying the initial text.

    Methods
    -------
    __init__(self, master)
        Initializes the AboutPage instance and sets up the window, links, and label.
    setup_window(self)
        Sets up the 'About' window.
    setup_links(self)
        Sets up the 'GIECAR' and 'GitHub' link buttons.
    setup_label(self)
        Sets up the label displaying the initial text.
    """
    def __init__(self, master):
        self.master = master
        self.about_window = tk.Toplevel(self.master)
        self.about_window.title("Sobre o GradPress")

        # Função que centraliza a janela
        centralize_window(self.about_window, *SMALL_WINDOW_SIZE)

        self.setup_window() # Inicia a janela de about
        self.setup_links() # Inicia os links
        self.setup_label()

    def setup_window(self):
        self.about_window.minsize(*SMALL_WINDOW_SIZE)
        self.about_window.maxsize(*SMALL_WINDOW_SIZE)
        self.about_window.option_add("*Label.font", "Segoe\\ UI 15")

        self.about_frame = tk.Frame(self.about_window)
        self.about_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.about_frame.place(relx=0.5, rely=0.5, anchor='center')

    def setup_links(self):
        self.giecar_link = create_custom_button(self.about_frame,
                                                text="GIECAR",
                                                command=lambda: \
                                                webbrowser.open(GIECAR_URL),
                                                width=100)
        self.giecar_link.grid(row=1, column=0, padx=10, pady=10)

        self.github_link = create_custom_button(self.about_frame,
                                                text="GitHub",
                                                command=lambda: \
                                                webbrowser.open(GITHUB_URL),
                                                width=100)
        self.github_link.grid(row=1, column=1, padx=10, pady=10)

    def setup_label(self):
        texto_inicial = "Desenvolvido por André Albano\nGIECAR - UFF\n2024"
        self.label = tk.Label(self.about_frame, text=texto_inicial, font=("Segoe UI", 10, "bold"))
        self.label.grid(row=2, column=0, columnspan=2, padx=15, pady=10)