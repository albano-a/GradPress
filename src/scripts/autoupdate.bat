@echo off

pyuic5 src/Interface/maingui.ui -o src/Interface/pyInterface/maingui_ui.py
pyuic5 src/Interface/regression.ui -o src/Interface/pyInterface/regression_ui.py
pyuic5 src/Interface/plot.ui -o src/Interface/pyInterface/plot_ui.py
pyuic5 src/Interface/crud.ui -o src/Interface/pyInterface/crud_ui.py
pyuic5 src/Interface/help.ui -o src/Interface/pyInterface/help_ui.py
pyuic5 src/Interface/gradient.ui -o src/Interface/pyInterface/gradient_ui.py
pyuic5 src/Interface/about.ui -o src/Interface/pyInterface/about_ui.py