from PyQt6.QtWidgets import QMainWindow, QFileDialog, QFontDialog, QMessageBox
from pyui.text_editor_window import Ui_textEditorWindow
from PyQt6.QtGui import QFont
import PyQt6.Qsci as Qsci
from PyQt6.Qsci import QsciScintilla
import numpy as np


class TextEditorWindow(QMainWindow, Ui_textEditorWindow):
    def __init__(self):
        super(TextEditorWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Editor de Texto")
        np.linspace(0, 10, 100)
        # reference the widget here
        self.scintillaWidget.setMarginType(0, QsciScintilla.
                                              MarginType.
                                              NumberMargin)
        self.scintillaWidget.setAutoCompletionSource(QsciScintilla.
                                                     AutoCompletionSource.
                                                     AcsAll)
        self.scintillaWidget.setAutoIndent(True)
        self.scintillaWidget.setBraceMatching(QsciScintilla.
                                              BraceMatch.
                                              StrictBraceMatch)
        self.scintillaWidget.setIndentationWidth(4)
        self.scintillaWidget.setFont(QFont("Consolas", 12))

        # Use QsciLexer for syntax highlighting
        self.python_lexer = Qsci.QsciLexerPython()
        self.python_lexer.setFont(QFont("Consolas", weight=500))
        self.cplusplus_lexer = Qsci.QsciLexerCPP()
        self.cplusplus_lexer.setFont(QFont("Consolas", weight=500))
        self.javascript_lexer = Qsci.QsciLexerJavaScript()
        self.javascript_lexer.setFont(QFont("Consolas", weight=500))
        self.matlab_lexer = Qsci.QsciLexerMatlab()
        self.matlab_lexer.setFont(QFont("Consolas", weight=500))
        self.markdown_lexer = Qsci.QsciLexerMarkdown()
        self.markdown_lexer.setFont(QFont("Consolas", weight=500))

        self.actionNovoArquivoTexto.triggered.connect(self.new_file)
        self.actionAbrirArquivoTexto.triggered.connect(self.open_file)
        self.actionSalvarArquivoTexto.triggered.connect(self.save_file)
        self.actionRecortar.triggered.connect(self.scintillaWidget.cut)
        self.actionCopiar.triggered.connect(self.scintillaWidget.copy)
        self.actionColar.triggered.connect(self.scintillaWidget.paste)
        self.actionDesfazer.triggered.connect(self.scintillaWidget.undo)
        self.actionRefazer.triggered.connect(self.scintillaWidget.redo)
        self.actionApagar.triggered.connect(self.scintillaWidget.clear)
        self.actionSelecionar_tudo.triggered.connect(self.
                                                     scintillaWidget.selectAll)
        self.actionFonte.triggered.connect(self.change_font)
        self.actionPython.triggered.connect(self.python_highlight)
        self.actionC_C.triggered.connect(self.c_c_highlight)
        self.actionC.triggered.connect(self.c_highlight)
        self.actionJavaScript.triggered.connect(self.javascript_highlight)
        self.actionR.triggered.connect(self.r_highlight)
        self.actionMatlab.triggered.connect(self.matlab_highlight)
        self.actionMarkdown.triggered.connect(self.markdown_highlight)

    def python_highlight(self):
        self.scintillaWidget.setLexer(self.python_lexer)

    def c_c_highlight(self):
        self.scintillaWidget.setLexer(self.cplusplus_lexer)

    def c_highlight(self):
        self.scintillaWidget.setLexer(self.cplusplus_lexer)

    def javascript_highlight(self):
        self.scintillaWidget.setLexer(self.javascript_lexer)

    def r_highlight(self):
        return QMessageBox.information(self, "Information",
                                       "R highlighting não foi implementado")

    def matlab_highlight(self):
        self.scintillaWidget.setLexer(self.matlab_lexer)

    def markdown_highlight(self):
        self.scintillaWidget.setLexer(self.markdown_lexer)

    def new_file(self):
        # Clear the current text
        self.scintillaWidget.clear()

        # Reset the current file path
        self.current_file_path = None


    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open File', '',
                                                'All Files (*)')
        if file_name:
            with open(file_name, 'r') as file:
                file_content = file.read()
            self.scintillaWidget.setPlainText(file_content)

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "",
                                                   "All Files (*)")
        if file_name:
            with open(file_name, 'w') as file:
                file_content = self.scintillaWidget.text()
                file_content = file_content.replace('\n', '\r\n')
                file.write(file_content)

    def change_font(self):
        font, ok = QFontDialog.getFont(self.scintillaWidget.font(), self)
        if ok:
            self.scintillaWidget.setFont(font)