# Form implementation generated from reading ui file 'ui/help.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_HelpMainWindow(object):
    def setupUi(self, HelpMainWindow):
        HelpMainWindow.setObjectName("HelpMainWindow")
        HelpMainWindow.resize(800, 600)
        HelpMainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../help.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        HelpMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=HelpMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(260, 10, 521, 531))
        self.frame.setStyleSheet("QFrame {\n"
"    border: 1px solid #212121\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.helpTextEdit = QtWidgets.QTextEdit(parent=self.frame)
        self.helpTextEdit.setGeometry(QtCore.QRect(0, 0, 521, 531))
        self.helpTextEdit.setObjectName("helpTextEdit")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 241, 531))
        self.frame_2.setStyleSheet("QFrame {\n"
"    border: 1px solid #212121\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.helpTreeView = QtWidgets.QTreeView(parent=self.frame_2)
        self.helpTreeView.setGeometry(QtCore.QRect(0, 0, 241, 531))
        self.helpTreeView.setObjectName("helpTreeView")
        HelpMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=HelpMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        HelpMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=HelpMainWindow)
        self.statusbar.setObjectName("statusbar")
        HelpMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HelpMainWindow)
        QtCore.QMetaObject.connectSlotsByName(HelpMainWindow)

    def retranslateUi(self, HelpMainWindow):
        _translate = QtCore.QCoreApplication.translate
        HelpMainWindow.setWindowTitle(_translate("HelpMainWindow", "MainWindow"))
        self.helpTextEdit.setHtml(_translate("HelpMainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Seja bem vindo ao guia de uso do Kraken Software v0.2</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Este software foi desenvolvido com o propósito de auxiliar os estudantes da graduação de Geofísica a realizar suas pesquisas de forma rápida e direta. Neste guia, você encontrará tudo necessário para realizar todas as funcionalidades do programa.</span></p></body></html>"))
