@echo off

pyuic5 src/main/python/interface/design/maingui.ui -o src/main/python/interface/python/maingui_ui.py
pyuic5 src/main/python/interface/design/regression.ui -o src/main/python/interface/python/regression_ui.py
pyuic5 src/main/python/interface/design/plot.ui -o src/main/python/interface/python/plot_ui.py
pyuic5 src/main/python/interface/design/crud.ui -o src/main/python/interface/python/crud_ui.py
pyuic5 src/main/python/interface/design/help.ui -o src/main/python/interface/python/help_ui.py
pyuic5 src/main/python/interface/design/gradient.ui -o src/main/python/interface/python/gradient_ui.py
pyuic5 src/main/python/interface/design/about.ui -o src/main/python/interface/python/about_ui.py
pyuic5 src/main/python/interface/design/temperatureinterface.ui -o src/main/python/interface/python/temperatureinterface.py
pyuic5 src/main/python/interface/design/temperatureinterfaceDialog.ui -o src/main/python/interface/python/temperatureinterfaceDialog.py