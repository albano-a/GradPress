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
from tksheet import Sheet
from tkinter import filedialog
import tkinter as tk
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

class TOMICalc:
    # TODO - Completely implement this functionality
    def __init__(self, master, app):
        self.master = master
        self.app = app


    def open_tomi_window(self):
        self.tomi_window = tk.Toplevel(self.master)
        self.tomi_window.title("TOMI Index Calculator")
        self.tomi_window.option_add("*Label.font", "Segoe\\ UI 12")

        self.super_tomi_win_frame = ctk.CTkFrame(self.tomi_window)
        self.super_tomi_win_frame.bind("<Configure>",
            lambda event: update_and_centralize_geometry(self.tomi_window,
                                                        self.super_tomi_win_frame,
                                                        max_size=True, child_window=True))
        self.super_tomi_win_frame.place(relx=0.5, rely=0.5, anchor='center')

        width=300; height=15

        self.tomi_win_frame0 = ctk.CTkFrame(self.super_tomi_win_frame, width=width)
        self.tomi_win_frame0.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        self.tomi_win_frame1 = ctk.CTkFrame(self.super_tomi_win_frame, width=width)
        self.tomi_win_frame1.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

        self.tomi_win_frame2 = ctk.CTkFrame(self.super_tomi_win_frame, width=width)
        self.tomi_win_frame2.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')

        self.tomi_text_label = \
        "Escolha o arquivo para fazer o plot do TOMI Index."
        self.tomi_text = ctk.CTkLabel(self.tomi_win_frame0,
                                    text=self.tomi_text_label,
                                    font=("Segoe UI", 19, "bold"),
                                    justify="center",
                                    width=width, height=height)
        self.tomi_text.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        class CTkCustomOptionMenu(ctk.CTkOptionMenu):
            def destroy(self):
                self.tk.call('destroy', self._w)

        file_names = os.listdir("./uploads")
        self.selected_file = tk.StringVar(self.tomi_win_frame1)
        self.tomi_upload_label = ctk.CTkLabel(self.tomi_win_frame1,
                                    text="Selecione o arquivo: ",
                                    font=("Segoe UI", 16),
                                    width=width, height=height)
        self.tomi_upload_label.pack(fill='x', padx=5, pady=5)
        self.tomi_upload_option_menu = CTkCustomOptionMenu(master=self.tomi_win_frame1,
                                                            variable=self.selected_file,
                                                            values= file_names,
                                                            fg_color="#f7f7f7",
                                                            button_color=BTN_FG_COLOR,
                                                            width=240,
                                                            button_hover_color=BTN_FG_HOVER_COLOR,
                                                            text_color=TEXT_COLOR,
                                                            text_color_disabled="#292929",
                                                            )
        self.tomi_upload_option_menu.pack(fill='x', padx=5, pady=5)

        self.calc_tomi_btn = create_custom_button(root=self.tomi_win_frame2,
                                            text="Plot Simples",
                                            command=placeholder_function,
                                            width=120)
        self.calc_tomi_btn.pack(side="top", padx=5, pady=5)

    def dummy_function(self):
       	pass