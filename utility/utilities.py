import customtkinter as ctk

def create_custom_button(root,
                         text,
                         command,
                         width=200,
                         fg_color="#840000",
                         hover_color="#a50000",
                         text_color="#f0f0f0"):
        # Your implementation of create_custom_button goes here
        return ctk.CTkButton(root,
                            text=text,
                            fg_color=fg_color,
                            command=command,
                            corner_radius=10,
                            border_width=1,
                            border_color="#aeaeae",
                            hover_color=hover_color,
                            width=width,
                            text_color=text_color,
                            font=("Helvetica", 15, "bold"))


def custom_dropdown(root, values, variable, width=200):
        # Your implementation of custom_dropdown goes here
        return ctk.CTkComboBox(root,
                               values=values,
                               variable=variable,
                               corner_radius=10,
                               fg_color="#fff",
                               button_color="#840000",
                               width=width,
                               button_hover_color="#a50000",
                               text_color="#212121",
                               border_color="#aeaeae",
                               border_width=1,
                               hover=True,
                               font=("Helvetica", 15, "bold"))


        
def centralize_window(window,
                      width,
                      height,
                      drift=0):
            # Obtenha a largura e a altura da tela
            screen_width = window.winfo_screenwidth()
            screen_height = window.winfo_screenheight()

            # Calcule a posição para centralizar a janela
            position_top = int(screen_height / 2 - height / 2) - drift
            position_right = int(screen_width / 2 - width / 2) - drift

            # Defina a geometria da janela
            window.geometry(f"{width}x{height}+{position_right}+{position_top}")