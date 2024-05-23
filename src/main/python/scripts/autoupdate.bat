@echo off

pyuic5 src/interface/design/maingui.ui -o src/interface/python/maingui_ui.py
pyuic5 src/interface/design/regression.ui -o src/interface/python/regression_ui.py
pyuic5 src/interface/design/plot.ui -o src/interface/python/plot_ui.py
pyuic5 src/interface/design/crud.ui -o src/interface/python/crud_ui.py
pyuic5 src/interface/design/help.ui -o src/interface/python/help_ui.py
pyuic5 src/interface/design/gradient.ui -o src/interface/python/gradient_ui.py
pyuic5 src/interface/design/about.ui -o src/interface/python/about_ui.py
pyuic5 src/interface/design/temperatureinterface.ui -o src/interface/python/temperatureinterface.py
pyuic5 src/interface/design/temperatureinterfaceDialog.ui -o src/interface/python/temperatureinterfaceDialog.py