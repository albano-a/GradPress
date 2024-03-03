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
from pressure_plot import plot_pressure

def plot_pressao(x, y, title, xlabel, ylabel, pressao_df, prof_min, prof_max):
    ymin = int(prof_min.get()) if prof_min.get() else min(pressao_df['Prof./Intv.(m)'])
    ymax = int(prof_max.get()) if prof_max.get() else max(pressao_df['Prof./Intv.(m)'])

    plt.plot(x, y, 'o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.ylim(ymin, ymax)
    plt.gca().invert_yaxis()
    plt.grid()
    plt.show()

# importing files
def plot_pressure():
    filename = selected_file.get()
    pressao_df = pd.read_csv(filename, delimiter=';')
    pressao_df = pressao_df.dropna(subset=['Prof./Intv.(m)', 'Pressão de Formação (Kgf/cm2)'])

    plot_pressao(x=pressao_df['Pressão de Formação (Kgf/cm2)'],
                 y=pressao_df['Prof./Intv.(m)'],
                 title=nome_entry.get(),
                 xlabel='Pressão de Formação (Kgf/cm2)',
                 ylabel='Profundidade (m)',
                 pressao_df=pressao_df,
                 prof_min=prof_min,
                 prof_max=prof_max)


# Upload handeling
def upload_file():
    filename = filedialog.askopenfilename()
    print('Selected:', filename)

    # Define the destination directory
    dest_dir = "./uploads"

    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Move the file
    shutil.copy(filename, dest_dir)

    # Update the text of the message label
    message_label.config(text="Arquivo carregado com sucesso!")


# Function to reset the plot
def reset_plot():
    global canvas
    if canvas is not None:
        canvas.get_tk_widget().destroy()
        canvas = None

# Função que automatiza a customização dos botões
def create_custom_button(root, text, command):
    return ctk.CTkButton(root,
                         text=text,
                         command=command,
                         corner_radius=10,
                         hover_color="#104a78",
                         width=200,
                         font=("Arial", 15, "bold"))

def update_selected_file(*args):
    selected_file.set(os.path.join("./uploads", fname.get()))

# Criando a janela principal, o título e o ícone
root = tk.Tk()
root.title("GradPress")
root.iconbitmap(default="./icon.ico") #icone
root.option_add("*Label.Font", "Poppins 15") #for the font
root.configure(bg='#F2F2F2') # Trocando o pano de fundo


# Criação dos frames
texto_inicial = "Importe e digite as informações do poço nos campos abaixo."
label = tk.Label(root, text=texto_inicial,bg='#F2F2F2')
label.grid(row=0,column=0, columnspan=2,padx=10, pady=10)

# Butão para carregar arquivo

upload_button = create_custom_button(root, "Carregar arquivo", upload_file)
upload_button.grid(row=1,column=0, columnspan=2,padx=10, pady=10)
message_label = tk.Label(root, text="",bg='#F2F2F2')
message_label.grid(row=2,column=0, columnspan=2)

# INPUT
# tk.Label(root, text="Digite o passo: ").pack(padx=10, pady=10)
# passo_entry = tk.Entry(root, borderwidth=2)
# passo_entry.pack(padx=10, pady=10)

# Dropdown menu to select file
files = os.listdir("./uploads")

# Check if files is empty
if not files:
    files = ["No files found"]

fname = tk.StringVar(root)
fname.set("Select a file")
fname.trace_add('write', update_selected_file)  # Add this line

dropdown = tk.OptionMenu(root, fname, *files)
dropdown.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

selected_file = tk.StringVar(root)

# Opções do que se fazer com o arquivo
tk.Label(root, text="Digite o nome do poço: ",bg='#F2F2F2')\
    .grid(row=4, columnspan=2,padx=10, pady=10)
nome_entry = tk.Entry(root, borderwidth=2, width=32)
nome_entry.grid(row=5, columnspan=2,padx=10, pady=10)

# Determinação das profundidades
tk.Label(root, text="Prof. A",bg='#F2F2F2')\
    .grid(row=6,column=0,padx=10, pady=10)
prof_min = tk.Entry(root, borderwidth=2, width=16)
prof_min.grid(row=7,column=0,padx=10, pady=10)

tk.Label(root, text="Prof. B",bg='#F2F2F2')\
    .grid(row=8,column=0,padx=10, pady=10)
prof_max = tk.Entry(root, borderwidth=2, width=16)
prof_max.grid(row=9,column=0,padx=10, pady=10)

# Outras opções
tk.Label(root, text="Mesa Rotativa", bg='#F2F2F2')\
    .grid(row=6,column=1,padx=10, pady=10)
mesa_rot = tk.Entry(root, borderwidth=2, width=16)\
    .grid(row=7,column=1,padx=10, pady=10)

create_custom_button(root, "Submit", plot_pressure)\
    .grid(row=9,column=1,padx=10, pady=10)



# Start the event loop
root.mainloop()