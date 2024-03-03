import customtkinter as ctk

def create_custom_button(root, text, command, width=200):
        # Your implementation of create_custom_button goes here
        return ctk.CTkButton(root,
                            text=text,
                            command=command,
                            corner_radius=10,
                            border_width=1,
                            border_color="#aeaeae",
                            hover_color="#104a78",
                            width=width,
                            font=("Helvetica", 15, "bold"))