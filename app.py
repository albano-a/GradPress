from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit
from main_window import Ui_GradPress_MainWindow
import os

class GradPress(QMainWindow, Ui_GradPress_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # # Assuming self.textEdit is your QTextEdit widget
        # self.actionUndo.triggered.connect(self.textEdit.undo)
        # self.actionRedo.triggered.connect(self.textEdit.redo)
        # self.actionCopy.triggered.connect(self.textEdit.copy)
        # self.actionPaste.triggered.connect(self.textEdit.paste)
        # self.actionCut.triggered.connect(self.textEdit.cut)



app = QApplication([])
window = GradPress()
window.show()
app.exec_()