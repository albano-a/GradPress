import customtkinter as ctk

def create_custom_button(root, text, command):
        # Your implementation of create_custom_button goes here
        return ctk.CTkButton(root,
                            text=text,
                            command=command,
                            corner_radius=10,
                            hover_color="#104a78",
                            width=200,
                            font=("Helvetica", 15, "bold"))