from PIL import Image
import customtkinter as ctk

add_icon = Image.open("./img/icons/add.png") # Abre o arquivo de imagem
add_img = ctk.CTkImage(light_image=add_icon,
                       dark_image=add_icon,
                       size=(15,15)) # Cria um CTkImage

remove_icon = Image.open("./img/icons/remove.png") # Abre o arquivo de imagem
remove_img = ctk.CTkImage(light_image=remove_icon,
                          dark_image=remove_icon,
                          size=(15,15)) # Cria um CTkImage

font_icon = Image.open("./img/icons/font.png") # Abre o arquivo de imagem
font_img = ctk.CTkImage(light_image=font_icon,
                        dark_image=font_icon,
                        size=(15,15)) # Cria um CTkImage