@echo off

pyuic6 ui/maingui.ui -o pyui/maingui.py
pyuic6 ui/plot_tendencia_window.ui -o pyui/plot_tendencia_window.py
pyuic6 ui/simple_plot_window.ui -o pyui/simple_plot_window.py
pyuic6 ui/text_editor.ui -o pyui/text_editor_window.py
pyuic6 ui/manage_files.ui -o pyui/manage_files.py
pyuic6 ui/help.ui -o pyui/help.py
pyuic6 ui/gradiente_pressao_window.ui -o pyui/gradiente_pressao_window.py
pyuic6 ui/about.ui -o pyui/about.py