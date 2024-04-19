import os
import shutil
from PyQt6.QtWidgets import QMainWindow,  QFileDialog, QInputDialog
from PyQt6.QtCore import QDir
from PyQt6.QtGui import QFileSystemModel
from Interface.pyInterface.crud_ui import Ui_ManageFilesWindow



class ManageFiles(QMainWindow, Ui_ManageFilesWindow):
    def __init__(self):
        super(ManageFiles, self).__init__()
        self.setupUi(self)

        self.selected_file_path = None

         # Create a QFileSystemModel
        self.model = QFileSystemModel()
        self.model.setRootPath(QDir.rootPath())

        # Set the model for manageFilesTreeView
        self.manageFilesTreeView.setModel(self.model)

        # Set the root index for manageFilesTreeView
        self.root_path = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
        self.manageFilesTreeView.setRootIndex(self.model.index(self.root_path))

        # Connect the clicked signal to our custom slot
        self.manageFilesTreeView.clicked.connect(self.on_manageFilesTreeView_clicked)

        # Connect buttons to their respective methods
        self.addFileBtn.clicked.connect(self.add_file)
        self.renameFileBtn.clicked.connect(self.rename_file)
        self.deleteFileBtn.clicked.connect(self.delete_file)
        self.exitManageFilesBtn.clicked.connect(self.close)

        # self.show()

    def on_manageFilesTreeView_clicked(self, index):
        try:
            # Get the clicked file name
            self.selected_file_path = self.model.filePath(index)
            if self.selected_file_path:
                print(f"Você clicou em {self.selected_file_path}")
            else:
                print("Nenhum arquivo selecionado.")
        except Exception as e:
            print(f"Erro ao acessor o arquivo: {e}")

    def add_file(self):
        try:
            # Abre um diálogo de arquivo para selecionar um arquivo para adicionar
            file_path, _ = QFileDialog.getOpenFileName(self, "Abrir arquivo", "", 'CSV, TXT, XLSX (*.csv *.txt *.xlsx)')

            if file_path:
                # Define o diretório de destino
                dest_path = os.path.join(self.root_path, os.path.basename(file_path))

                # Tenta copiar o arquivo para o diretório de destino
                try:
                    shutil.copy(file_path, dest_path)
                except Exception as e:
                    print(f"Erro ao copiar o arquivo: {e}")
                    return

                # Tenta atualizar a visualização em árvore
                try:
                    self.manageFilesTreeView.setModel(None)
                    self.manageFilesTreeView.setModel(self.model)

                    # Define a visualização em árvore de volta para o diretório de uploads
                    self.manageFilesTreeView.setRootIndex(self.model.index(self.root_path))
                except Exception as e:
                    print(f"Erro ao atualizar a visualização em árvore: {e}")
        except Exception as e:
            print(f"Erro ao abrir o diálogo de arquivo: {e}")

    def rename_file(self):
        try:
            # Obtém o arquivo selecionado
            selected_indexes = self.manageFilesTreeView.selectedIndexes()
            if selected_indexes:
                file_path = self.model.filePath(selected_indexes[0])

                # Lembra o diretório atual
                current_directory = os.path.dirname(file_path)

                # Obtém o novo nome do arquivo do usuário
                new_file_name, ok = QInputDialog.getText(self, "Renomear arquivo", "Digite o novo nome do arquivo:")
                if ok and new_file_name:
                    # Cria o novo caminho do arquivo
                    new_file_path = os.path.join(os.path.dirname(self.selected_file_path), new_file_name)

                    # Tenta renomear o arquivo
                    try:
                        os.rename(file_path, new_file_path)
                    except Exception as e:
                        print(f"Erro ao renomear o arquivo: {e}")
                        return

                    # Tenta atualizar a visualização em árvore
                    try:
                        self.manageFilesTreeView.setModel(None)
                        self.manageFilesTreeView.setModel(self.model)

                        # Define a visualização em árvore de volta para o diretório atual
                        self.manageFilesTreeView.setRootIndex(self.model.index(current_directory))
                    except Exception as e:
                        print(f"Erro ao atualizar a visualização em árvore: {e}")
        except Exception as e:
            print(f"Erro ao acessar o caminho do arquivo: {e}")

    def delete_file(self):
        try:
            # Obtém o arquivo selecionado
            selected_indexes = self.manageFilesTreeView.selectedIndexes()
            if selected_indexes:
                file_path = self.model.filePath(selected_indexes[0])

                # Lembra o diretório atual
                current_directory = os.path.dirname(file_path)

                # Tenta excluir o arquivo
                try:
                    os.remove(file_path)
                except Exception as e:
                    print(f"Erro ao excluir o arquivo: {e}")
                    return

                # Tenta atualizar a visualização em árvore
                try:
                    self.manageFilesTreeView.setModel(None)
                    self.manageFilesTreeView.setModel(self.model)

                    # Define a visualização em árvore de volta para o diretório atual
                    self.manageFilesTreeView.setRootIndex(self.model.index(current_directory))
                except Exception as e:
                    print(f"Erro ao atualizar a visualização em árvore: {e}")
        except Exception as e:
            print(f"Erro ao acessar o caminho do arquivo: {e}")