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
                       size=(30,30)) # Cria um CTkImage

remove_icon_path = os.path.join(basedir, 'img', 'icons', 'remove.png')
remove_icon = Image.open(remove_icon_path) # Abre o arquivo de imagem
remove_img = ctk.CTkImage(light_image=remove_icon,
                          dark_image=remove_icon,
                          size=(30,30)) # Cria um CTkImage

font_icon_path = os.path.join(basedir, 'img', 'icons', 'font.png')
font_icon = Image.open(font_icon_path) # Abre o arquivo de imagem
font_img = ctk.CTkImage(light_image=font_icon,
                        dark_image=font_icon,
                        size=(26,26)) # Cria um CTkImage

show_plot_icon = Image.open(os.path.join(basedir, 'img', 'icons', 'show_plot.png')) # Abre o arquivo de imagem
show_plot_img = ctk.CTkImage(light_image=show_plot_icon,
                             dark_image=show_plot_icon,
                             size=(30,30)) # Cria um CTkImage

code_icon = Image.open(os.path.join(basedir, 'img', 'icons', 'code.png'))
code_img = ctk.CTkImage(light_image=code_icon,
                       dark_image=code_icon,
                       size=(30,30))

folder_icon = Image.open(os.path.join(basedir, 'img', 'icons', 'folder.png'))
folder_img = ctk.CTkImage(light_image=folder_icon,
                         dark_image=folder_icon,
                         size=(30,30))

inventory_icon = Image.open(os.path.join(basedir, 'img', 'icons', 'inventory.png'))
inventory_img = ctk.CTkImage(light_image=inventory_icon,
                            dark_image=inventory_icon,
                            size=(30,30))

save_icon = Image.open(os.path.join(basedir, 'img', 'icons', 'save.png'))
save_img = ctk.CTkImage(light_image=save_icon,
                       dark_image=save_icon,
                       size=(30,30))

new_file_icon = Image.open(os.path.join(basedir, 'img', 'icons', 'new_file.png'))
new_file_img = ctk.CTkImage(light_image=new_file_icon,
                           dark_image=new_file_icon,
                           size=(30,30))