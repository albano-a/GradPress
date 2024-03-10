from PIL import Image
import customtkinter as ctk
import os
import sys

# Check if we're running as a PyInstaller bundle
if getattr(sys, 'frozen', False):
    # We're running in a PyInstaller bundle
    basedir = sys._MEIPASS
else:
    # We're running in a normal Python environment
    basedir = os.path.dirname(os.path.dirname(__file__))

add_icon_path = os.path.join(basedir, 'img', 'icons', 'add.png')
add_icon = Image.open(add_icon_path) # Abre o arquivo de imagem
add_img = ctk.CTkImage(light_image=add_icon,
                       dark_image=add_icon,
                       size=(15,15)) # Cria um CTkImage

remove_icon_path = os.path.join(basedir, 'img', 'icons', 'remove.png')
remove_icon = Image.open(remove_icon_path) # Abre o arquivo de imagem
remove_img = ctk.CTkImage(light_image=remove_icon,
                          dark_image=remove_icon,
                          size=(15,15)) # Cria um CTkImage

font_icon_path = os.path.join(basedir, 'img', 'icons', 'font.png')
font_icon = Image.open(font_icon_path) # Abre o arquivo de imagem
font_img = ctk.CTkImage(light_image=font_icon,
                        dark_image=font_icon,
                        size=(15,15)) # Cria um CTkImage