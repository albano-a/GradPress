import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from CTkToolTip import CTkToolTip
from utility.color_constants import TEXT_COLOR, BORDER_COLOR, BTN_FG_COLOR, BTN_FG_HOVER_COLOR

def create_custom_button(root,
                         text,
                         command,
                         width=200,
                         fg_color=BTN_FG_COLOR,
                         hover_color=BTN_FG_HOVER_COLOR,
                         text_color=TEXT_COLOR):
        # Your implementation of create_custom_button goes here
        return ctk.CTkButton(root,
                            text=text,
                            fg_color=fg_color,
                            command=command,
                            border_spacing=1,
                            corner_radius=5,
                            border_width=1,
                            border_color=BORDER_COLOR,
                            hover_color=hover_color,
                            width=width,
                            text_color=text_color,
                            font=("Segoe UI", 15))


def custom_CTkEntry(root,
                        placeholder_text,
                        width=240,
                        *args, **kwargs
                        ):
    return ctk.CTkEntry(root,
                        font=("Segoe UI", 14),
                        width=width,
                        corner_radius=5,
                        border_width=0,
                        fg_color="#f7f7f7",
                        placeholder_text=placeholder_text,
                        placeholder_text_color="#999999",
                        justify="center")


def custom_dropdown(root, values, variable, width=200):
        # Your implementation of custom_dropdown goes here
        return ctk.CTkComboBox(root,
                               values=values,
                               variable=variable,
                               corner_radius=3,
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


def update_and_centralize_geometry(window,
                                   frame,
                                   drift=0,
                                   max_size=False,
                                   child_window=False,
                                   maxwidth=0,
                                   maxheight=0):
    """
    Update the geometry of the window based on the current size of the frame and centralize the window on the screen.

    Parameters:
    window: The window to update and centralize.
    frame: The frame whose size is used to update the window's geometry.
    drift: The amount to offset the window's position from the center of the screen.
    max_size: A boolean indicating whether to set the window's maximum size.
    child_window: A boolean indicating whether the window is a child window.
    maxwidth: The maximum width of the window.
    maxheight: The maximum height of the window.
    """
    # Update the geometry of the window based on the current size of the frame
    frame_width = frame.winfo_width()
    frame_height = frame.winfo_height()

    # Centralize the window on the screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - frame_height / 2) - drift
    position_right = int(screen_width / 2 - frame_width / 2) - drift
    window.geometry(f"{frame_width}x{frame_height}+{position_right}+{position_top}")

    window.minsize(frame_width, frame_height)

    if max_size:
        if child_window:
            window.maxsize(frame_width, frame_height)
        else:
            window.maxsize(maxwidth, maxheight)

def placeholder_function():
    custom_messagebox(title="Info", message="Essa funcionalidade ainda não foi implementada!",
                  icon="./img/icons/info.png", width=400)


def custom_messagebox(title, message, icon, width=400, *args, **kwargs):
    CTkMessagebox(title=title,
                  message=message,
                  icon=icon,
                  width=width,
                  font=("Segoe UI", 16),
                  bg_color="#e5e7eb",
                  fg_color="#f3f4f6",
                  text_color="#212121",
                #   button_bg_color="#d1d5db",
                  button_hover_color="#9ca3af")

def custom_tooltip(widget, text, delay, *args, **kwargs):
    return CTkToolTip(widget,
                      text,
                      bg_color="#f3f4f6",
                      fg_color="#f0f0f0",
                      text_color="#212121",
                      corner_radius=3,
                      font=("Segoe UI", 12),
                      border_width=1,
                      border_color="#d1d1d1",)