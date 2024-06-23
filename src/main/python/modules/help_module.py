import os
import markdown
from PyQt5.QtWidgets import QMainWindow, QFileSystemModel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QDir, QUrl
from PyQt5.QtGui import QIcon
from PyQt5 import uic
from functions.uic import import_ui


class HelpWindow(QMainWindow):
    def __init__(self):
        super(HelpWindow, self).__init__()

        import_ui(self, "help")
        self.setWindowIcon(QIcon("src/main/icons/Icon.ico"))
        self.setWindowTitle("Ajuda")

        self.browser = QWebEngineView()
        self.browser.load(QUrl("file:///src/main/python/docs/index.html"))
        self.setCentralWidget(self.browser)
