from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QUrl
from PyQt5 import uic
from functions.uic import import_ui


class AboutWindow(QMainWindow):
    def __init__(self):
        super(AboutWindow, self).__init__()

        import_ui(self, "about")
        self.setWindowTitle("Sobre")

        # Connect the buttons to the openUrl method
        self.giecarBtn.clicked.connect(lambda: self.openUrl("http://gcr.sites.uff.br/"))
        self.githubBtn.clicked.connect(lambda: self.openUrl("https://github.com"))

    def openUrl(self, url):
        QDesktopServices.openUrl(QUrl(url))
