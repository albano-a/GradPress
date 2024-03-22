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


class HelpWindow(tk.Toplevel):
    def __init__(self, master):
        self.master = master
        self.help_window = tk.Toplevel(self.master)
        # self.help_window.attributes('-toolwindow', True)

        self.help_window.title("Ajuda")
        self.help_window.option_add("*Label.font", "Segoe\\ UI 12")

        # Create a PanedWindow to divide the window into two parts
        self.paned_window = tk.PanedWindow(self.help_window)
        self.paned_window.pack(fill=tk.BOTH, expand=1)

        # Create the Treeview on the left side
        self.treeview = ttk.Treeview(self.paned_window)
        self.paned_window.add(self.treeview)

        # Create a Text widget on the right side to display the content
        self.text = scrolledtext.ScrolledText(self.paned_window,
                            state='normal',
                            font=("Consolas", 12),  # Set the font and size
                            fg="#212121",  # Set the text color
                            bg="#f0f0f0",  # Set the background color
                            wrap="word",  # Set word wrapping
                            undo=True,  # Enable the undo feature
                            padx=10,  # Set the left and right padding
                            pady=10)  # Set the top and bottom padding
        self.paned_window.add(self.text)
        # Insert the placeholder text
        self.text.insert(tk.END, "Select an item to view its content")

        # Add some items to the Treeview
        self.help_options = {
            "Página inicial": "getting_started",
            "Introdução": "introduction",
            "Como funciona": "como_funciona",
            "Primeiros passos": "first_steps",
            "FAQ": "faq",
            "Perguntas Gerais": "general_questions",
            "Perguntas Técnicas": "technical_questions",
            "Resolução de Problemas": "troubleshooting",
            "Problemas comuns": "common_issues",
            "Reportar Bugs": "reporting_bugs",
            "Sobre": "about",
            "Info da Versão": "version_info",
            "Créditos": "credits"
        }
        self.help_more_options = {
            "Página inicial": ["Introdução", "Como funciona", "Primeiros passos"],
            "FAQ": ["Perguntas Gerais", "Perguntas Técnicas"],
            "Resolução de Problemas": ["Problemas comuns", "Reportar Bugs"],
            "Sobre": ["Info da Versão", "Créditos"]
        }

        # Add the items to the Treeview
        for category, subcategories in self.help_more_options.items():
            parent_item = self.treeview.insert('', 'end', text=category)
            for subcategory in subcategories:
                self.treeview.insert(parent_item, 'end', text=subcategory)

        # Bind the click event on the Treeview to a function
        self.treeview.bind('<<TreeviewSelect>>', self.on_treeview_select)


    def on_treeview_select(self, event):
        # Get the selected item's text
        selected_item = self.treeview.selection()[0]
        selected_text = self.treeview.item(selected_item, 'text')

        # Get the corresponding file name
        file_name = self.help_options.get(selected_text, selected_text)

        # Try to open the corresponding text file and read its contents
        try:
            with open(f'./guides/{file_name}.txt', 'r', encoding='utf-8') as file:
                file_contents = file.read()
        except FileNotFoundError:
            file_contents = f"No help file found for {selected_text}"

        # Display the contents in the Text widget
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, file_contents)
        # self.text.config(state='disabled')  # Make the text read-only