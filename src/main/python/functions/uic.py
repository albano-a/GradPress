from PyQt5 import uic


def import_ui(self, filename):
    return uic.loadUi("src/main/python/interface/design/" + filename + ".ui", self)
