from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import QUrl
from pyui.about import Ui_AboutWindow

class AboutWindow(QMainWindow, Ui_AboutWindow):
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sobre")

        # Connect the buttons to the openUrl method
        self.giecarBtn.clicked.connect(lambda: self.openUrl
                                       ('http://gcr.sites.uff.br/'))
        self.githubBtn.clicked.connect(lambda: self.openUrl
                                       ('https://github.com'))

    def openUrl(self, url):
        QDesktopServices.openUrl(QUrl(url))