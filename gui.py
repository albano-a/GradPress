import os
import shutil
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import customtkinter as ctk
from tkinter import filedialog

# Global variable for the canvas
canvas = None

# Function to plot the graph
def plot():
    global canvas
    inicial = int(inicial_entry.get())
    final = int(final_entry.get())
    passo = int(passo_entry.get())

    x = np.linspace(inicial, final, passo)
    y = np.sin(x)

    fig = plt.Figure()
    ax = fig.add_subplot(111)
    ax.plot(x, y)

    if canvas is not None:
        canvas.get_tk_widget().destroy()

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

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

    # Update the text area with the name of the uploaded file
    text_area.delete('1.0', tk.END)
    text_area.insert(tk.END, os.path.basename(filename))

# Function to reset the plot
def reset_plot():
    global canvas
    if canvas is not None:
        canvas.get_tk_widget().destroy()
        canvas = None

# Create the main window
root = tk.Tk()

# Add the widgets
tk.Label(root, text="Digite o valor inicial: ").pack(padx=10, pady=10)
inicial_entry = tk.Entry(root, borderwidth=2)
inicial_entry.pack(padx=10, pady=10)

tk.Label(root, text="Digite o valor final: ").pack(padx=10, pady=10)
final_entry = tk.Entry(root, borderwidth=2)
final_entry.pack(padx=10, pady=10)

tk.Label(root, text="Digite o passo: ").pack(padx=10, pady=10)
passo_entry = tk.Entry(root, borderwidth=2)
passo_entry.pack(padx=10, pady=10)

upload_button = ctk.CTkButton(root, text="Upload File", command=upload_file)
upload_button.pack()

text_area = tk.Text(root, height=4, width=50)
text_area.pack()

plot_button = ctk.CTkButton(root,
                            text="Plot",
                            command=plot,
                            hover_color="green")
plot_button.pack(padx=10, pady=10)

reset_button = ctk.CTkButton(root, text="Reset", command=reset_plot)
reset_button.pack(padx=10, pady=10)

plot_frame = ctk.CTkFrame(root, border_width=2)
plot_frame.pack(padx=10, pady=10)

# Start the event loop
root.mainloop()