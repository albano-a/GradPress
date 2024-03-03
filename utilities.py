import customtkinter as ctk

def create_custom_button(root, text, command, width=200):
        # Your implementation of create_custom_button goes here
        return ctk.CTkButton(root,
                            text=text,
                            fg_color="#23479e",
                            command=command,
                            corner_radius=10,
                            border_width=1,
                            border_color="#aeaeae",
                            hover_color="#0a0f53",
                            width=width,
                            font=("Helvetica", 15, "bold"))


def custom_dropdown(root, values, variable, width=200):
        # Your implementation of custom_dropdown goes here
        return ctk.CTkComboBox(root,
                               values=values,
                               variable=variable,
                               corner_radius=10,
                               fg_color="#fff",
                               button_color="#23479e",
                               width=width,
                               button_hover_color="#0a0f53",
                               text_color="#212121",
                               border_color="#aeaeae",
                               border_width=1,
                               hover=True,
                               font=("Helvetica", 15, "bold"))