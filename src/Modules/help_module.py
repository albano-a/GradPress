import os
import markdown
from PyQt5.QtWidgets import QMainWindow, QFileSystemModel
from PyQt5.QtCore import QDir
from interface.python.help_ui import Ui_HelpMainWindow


class HelpWindow(QMainWindow, Ui_HelpMainWindow):
    def __init__(self):
        super(HelpWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Ajuda")

        # Create a QFileSystemModel
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())

        # Set the model for helpTreeView
        self.helpTreeView.setModel(self.model)

        # Set the root index for helpTreeView
        root_path = os.path.dirname(os.path.abspath(__file__)) + "/docs"
        self.helpTreeView.setRootIndex(self.model.index(root_path))

        # Hide the "Size" and "Type" columns
        self.helpTreeView.hideColumn(1)
        self.helpTreeView.hideColumn(2)
        self.helpTreeView.hideColumn(3)

        # Connect the clicked signal to our custom slot
        self.helpTreeView.clicked.connect(self.on_helpTreeView_clicked)

        self.show()

    def on_helpTreeView_clicked(self, index):
        # Get the full file path of the clicked item
        file_path = self.helpTreeView.model().filePath(index)

        # Check if it's a markdown file
        if os.path.isfile(file_path) and file_path.endswith(".md"):
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()

            # Convert markdown to HTML and display the
            # content in the helpTextEdit
            html = markdown.markdown(content)
            self.helpTextEdit.setHtml(html)
