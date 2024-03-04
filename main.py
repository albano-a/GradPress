import os
import shutil
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandasgui
from tkinter import filedialog, ttk, Label
import tkinter as tk
from utility.utilities import create_custom_button, custom_dropdown
from PIL import Image, ImageTk
from numpy.linalg import inv
from utility.fluid_pressure import fluid_pressure

class FileUploader:
    def __init__(self, master):
        self.master = master
        ######################################################
        self.upload_frame = tk.Frame(self.master, bg='#ebebeb')
        self.upload_frame.grid(row=0, column=0, columnspan=2,padx=10, pady=10)
        ######################################################
        # giecar logo handling
        self.img = Image.open("./img/giecar.png")
        or_width, or_height = self.img.size
        self.img = self.img.resize((or_width//3, or_height//3))
        self.photo_img = ImageTk.PhotoImage(self.img)
        img_giecar = Label(self.upload_frame, image=self.photo_img, bg='#ebebeb')
        img_giecar.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Texto inicial
        texto_inicial = "Importe e digite as informações do poço nos campos abaixo.\nÉ necessário selecionar o arquivo antes de prosseguir."
        self.label = tk.Label(self.upload_frame, text=texto_inicial, bg='#ebebeb')
        self.label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Botão para carregar arquivo
        self.upload_button = create_custom_button(self.upload_frame,
                                           text="Carregar arquivo",
                                           command=self.upload_file)
        # then the grid within the frame
        self.upload_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)


        # Dropdown menu to select file
        self.fname = tk.StringVar(self.upload_frame)
        self.fname.set("Selecione um arquivo")
        self.selected_file = tk.StringVar(self.master)

        files = os.listdir("./uploads")
        if not files:
            files = ["Nenhum arquivo encontrado"]

        self.dropdown = custom_dropdown(self.upload_frame,
                                        values=files,
                                        variable=self.fname)
        self.dropdown.grid(row=3, column=0, padx=10, pady=10)
        
        self.loaded_files = create_custom_button(self.upload_frame,
                                                text="Todos os arquivos",
                                                command=lambda: ManageFiles(self.master))
        self.loaded_files.grid(row=3, column=1,padx=10, pady=10)

        self.view_button = create_custom_button(self.upload_frame,
                                                "Visualizar dados",
                                                self.view_file)
        self.view_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.fname.trace_add('write', self.update_selected_file)

    def view_file(self):
        filename = self.selected_file.get()
        if os.path.exists(filename):
            df = pd.read_csv(filename, sep='[;,]')
            pandasgui.show(df)
        else:
            tk.messagebox.showerror("Error", "Arquivo não encontrado!")

    def upload_file(self):
        filename = filedialog.askopenfilename()
        print(filename)
        if not os.path.exists("./uploads"):
            os.makedirs("./uploads")
        shutil.copy(filename, "./uploads")
        tk.messagebox.showinfo("Sucesso", "Arquivo carregado com sucesso!")

        # Update the list of files in the dropdown
        files = os.listdir("./uploads")
        if not files:
            files = ["Nenhum arquivo encontrado"]
        self.dropdown['values'] = files
        
        # Update the StringVar associated with the dropdown
        self.fname.set(os.path.basename(filename))

    def update_selected_file(self, *args):
        self.selected_file.set(os.path.join("./uploads", self.fname.get()))
        
    
class FilesFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # List all files in ./uploads
        self.files = os.listdir("./uploads")
        
        listbox_frame = tk.Frame(self, bg='#ebebeb')
        listbox_frame.grid(row=0, column=0, padx=10, pady=10)
        
        self.listbox = tk.Listbox(listbox_frame, width=400, height=200)
        self.listbox.grid(row=0, column=0, sticky='nsew')  # Use grid instead of pack
        for file in self.files:
            self.listbox.insert(tk.END, file)

        # Create a scrollbar and attach it to the listbox
        scrollbar = tk.Scrollbar(listbox_frame, command=self.listbox.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')  # Use grid instead of pack
        self.listbox.config(yscrollcommand=scrollbar.set)

        self.listbox.bind('<<ListboxSelect>>', self.on_select)

    def on_select(self, event):
        # Get selected file
        index = self.listbox.curselection()[0]
        selected_file = self.files[index]
        
    def add_file(self):
        filename = filedialog.askopenfilename()
        if filename:  # Check if a file was selected
            if not os.path.exists("./uploads"):
                os.makedirs("./uploads")
            shutil.copy(filename, "./uploads")
            new_file = os.path.basename(filename)
            self.listbox.insert(tk.END, new_file)
            self.files.append(new_file)  # Update the files list
            tk.messagebox.showinfo("Sucesso", "Arquivo carregado com sucesso!")

    def rename_file(self):
        if self.listbox.curselection():  # Check if a file is selected
            index = self.listbox.curselection()[0]
            selected_file = self.files[index]
            new_name = tk.simpledialog.askstring("Input", "Novo nome:", parent=self.master)
            if new_name:
                new_path = os.path.join("./uploads", new_name)
                if not os.path.exists(new_path):  # Check if the new file name already exists
                    shutil.move(os.path.join("./uploads", selected_file), new_path)
                    self.listbox.delete(index)
                    self.listbox.insert(index, new_name)
                    self.files[index] = new_name  # Update the files list
                    tk.messagebox.showinfo("Sucesso", "Arquivo renomeado com sucesso!")
                else:
                    tk.messagebox.showerror("Error", "Esse nome já existe!")

    def delete_file(self):
        if self.listbox.curselection():  # Check if a file is selected
            index = self.listbox.curselection()[0]
            selected_file = self.files[index]
            os.remove(os.path.join("./uploads", selected_file))
            self.listbox.delete(index)
            del self.files[index]  # Update the files list
            tk.messagebox.showinfo("Sucesso", "Arquivo deletado com sucesso!")

class ManageFiles:
    def __init__(self, master):
        self.master = master
        self.manage_window = tk.Toplevel(self.master)
        self.manage_window.title("Gerenciar arquivos")
        self.manage_window.geometry("600x500")
        self.manage_window.minsize(600, 500)
        self.manage_window.option_add("*Label.font", "Helvetica 15")  # for the font
        
        # Create a frame within the new window
        self.manage_files_frame = tk.Frame(self.manage_window#, bg='#ebebeb'
                                           )
        self.manage_files_frame.grid(row=0, column=0, padx=10, pady=10)
        self.manage_files_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        gerenciar_texto = "Gerenciar arquivos"
        self.label = ctk.CTkLabel(self.manage_files_frame, 
                                  text=gerenciar_texto,
                                  font=("Helvetica", 20, "bold"))
        self.label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Lista todos os arquivos
        self.files_frame = FilesFrame(self.manage_files_frame, 
                                      width=500, 
                                      height=300,
                                      fg_color="transparent")
        self.files_frame.grid(row=1, column=0, columnspan=4,padx=10, pady=10)
        
        # botao para deletar arquivo
        self.add_button = create_custom_button(self.manage_files_frame,
                                                text="Adicionar",
                                                command=self.files_frame.add_file,
                                                width=75,
                                                fg_color="#34bf49",
                                                hover_color="#279b37",
                                                text_color="#212121")
        self.add_button.grid(row=2, column=0, padx=10, pady=10)
        
        # botao para deletar arquivo
        self.rename_button = create_custom_button(self.manage_files_frame,
                                                  text="Renomear",
                                                  command=self.files_frame.rename_file,
                                                  width=75,
                                                  fg_color="#0099e5",
                                                  hover_color="#037ef3",
                                                  text_color="#212121")
        self.rename_button.grid(row=2, column=1, padx=10, pady=10)
        
        # botao para deletar arquivo
        self.delete_button = create_custom_button(self.manage_files_frame,
                                                  text="Deletar",
                                                  command=self.files_frame.delete_file,
                                                  width=75,
                                                  fg_color="#ff4c4c",
                                                  hover_color="#be0027",
                                                  text_color="#212121")
        self.delete_button.grid(row=2, column=2, padx=10, pady=10)
        
        self.return_button = create_custom_button(self.manage_files_frame,
                                                  text="Voltar",
                                                  command=self.manage_window.destroy,
                                                  width=75)
        self.return_button.grid(row=2, column=3, padx=10, pady=10)

class WellInfoInput:
    def __init__(self, master, file_uploader):
        self.master = master
        self.file_uploader = file_uploader
        ######################################################
        self.well_info_frame = tk.Frame(self.master, bg='#ebebeb')
        self.well_info_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        ######################################################

        texto_inicial = "Preencha as informações abaixo para plotar o gráfico de pressão.\n *Obrigatório"
        self.label = tk.Label(self.well_info_frame, text=texto_inicial, bg='#ebebeb')
        self.label.grid(row=0, column=0, columnspan=2, padx=15, pady=10)

        # Input do nome do poço
        tk.Label(self.well_info_frame, text="Digite o nome do poço: ", bg='#ebebeb') \
            .grid(row=1, columnspan=2, padx=10, pady=10)
        self.nome_entry = tk.Entry(self.well_info_frame,
                                   borderwidth=1,
                                   width=42,
                                   justify="center",
                                   relief="solid",
                                   font=("Helvetica", 12))
        self.nome_entry.grid(row=2, columnspan=2, padx=10, pady=10)

        # Depth inputs
        tk.Label(self.well_info_frame, text="Prof. Inicial", bg='#ebebeb') \
            .grid(row=3, column=0, padx=10, pady=10)
        self.prof_min = tk.Entry(self.well_info_frame,
                                 borderwidth=1,
                                 width=18,
                                 justify="center",
                                 relief="solid",
                                 font=("Helvetica", 12))
        self.prof_min.grid(row=4, column=0, padx=10, pady=10)

        tk.Label(self.well_info_frame, text="Prof. Final", bg='#ebebeb') \
            .grid(row=5, column=0, padx=10, pady=10)
        self.prof_max = tk.Entry(self.well_info_frame,
                                 borderwidth=1,
                                 width=18,
                                 justify="center",
                                 relief="solid",
                                 font=("Helvetica", 12))
        self.prof_max.grid(row=6, column=0, padx=10, pady=10)

        # Other options
        tk.Label(self.well_info_frame, text="Mesa Rotativa*", bg='#ebebeb') \
            .grid(row=3, column=1, padx=10, pady=10)
        self.mesa_rot = tk.Entry(self.well_info_frame,
                                 borderwidth=1,
                                 width=18,
                                 justify="center",
                                 relief="solid",
                                 font=("Helvetica", 12))
        self.mesa_rot.grid(row=4, column=1, padx=10, pady=10)

        # Error message
        self.error_message = tk.StringVar(self.well_info_frame)
        self.error_label = tk.Label(self.well_info_frame,
                                    textvariable=self.error_message,
                                    fg="red")
        self.error_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.plot_btn = create_custom_button(root=self.well_info_frame,
                            text="Plotar",
                            command=self.main_plot_pressure,
                            width=300)
        self.plot_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
        
        self.calculate_btn = create_custom_button(root=self.well_info_frame,
                                                  text="Cálculos",
                                                  command=lambda: CalculationsPage(self.master),
                                                    width=300)
        self.calculate_btn.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
            


    def plot_simples_pressao(self, x, y, title, xlabel, ylabel, pressao_df, prof_min, prof_max, mesa_rot):
        """
        Função que plota a pressão de formação em função da profundidade (cota)
        """
        ymin = int(prof_min.get()) if prof_min.get() else min(pressao_df['Prof./Intv.(m)'])
        ymax = int(prof_max.get()) if prof_max.get() else max(pressao_df['Prof./Intv.(m)'])

        ymin = int(mesa_rot.get()) - ymin
        ymax = int(mesa_rot.get()) - ymax

        plt.plot(x, y, 'o')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.ylim(ymin, ymax)
        plt.gca().invert_yaxis()
        plt.grid()
        plt.show()

    def main_plot_pressure(self):
        """
        Plota os dados de pressão em relação à profundidade.

        Esta função lê um arquivo CSV contendo dados de pressão e os plota em relação
        aos valores de profundidade (em cota) correspondentes.
        Elimina quaisquer linhas com valores NaN.
        Os valores de profundidade em cota são calculados subtraindo
        os valores de 'Prof./Intv.(m)' do valor de 'mesa_rot'.
        """
        try:
            filename = self.file_uploader.selected_file.get()
            pressao_df = pd.read_csv(filename, delimiter=';')
            pressao_df = pressao_df.dropna(subset=['Prof./Intv.(m)', 'Pressão de Formação (Kgf/cm2)'])
            prof_cota = int(self.mesa_rot.get()) - pressao_df['Prof./Intv.(m)']

            self.plot_simples_pressao(x=pressao_df['Pressão de Formação (Kgf/cm2)'],
                        y=prof_cota,
                        title=self.nome_entry.get(),
                        xlabel='Pressão de Formação (Kgf/cm2)',
                        ylabel='Profundidade (m)',
                        pressao_df=pressao_df,
                        prof_min=self.prof_min,
                        prof_max=self.prof_max,
                        mesa_rot=self.mesa_rot)
        except Exception as e:
            self.error_message.set(str(e))

class CalculationsPage:
    def __init__(self, master):
        self.master = master
        self.calculations_window = tk.Toplevel(self.master)
        self.calculations_window.title("Cálculos")
        self.calculations_window.geometry("600x600")
        self.calculations_window.minsize(600, 600)
        self.calculations_window.option_add("*Label.font", "Helvetica 15")
        
        # Criando um frame dentro da imagem
        self.calculations_window_frame = tk.Frame(self.calculations_window)
        self.calculations_window_frame.grid(row=0, column=0, padx=10, pady=10)
        self.calculations_window_frame.place(relx=0.5,rely=0.5,anchor="center")
        
        calculos_texto = "Cálculos de pressão"
        self.label = ctk.CTkLabel(self.calculations_window_frame, 
                                  text=calculos_texto,
                                  font=("Helvetica", 20, "bold"))
        self.label.grid(row=0, column=0, padx=10, pady=10)
        
        calculos_descricao = "Escolha o que quer fazer com os dados que carregou:"
        self.label = ctk.CTkLabel(self.calculations_window_frame, 
                                  text=calculos_texto,
                                  font=("Helvetica", 20, "bold"))
        self.label.grid(row=0, column=0, padx=10, pady=10)
        
        #### WIP ########
        self.plot_data = create_custom_button(self.calculations_window_frame,
                                              text="Plotar os Dados Tratados",
                                              command=self.on_button_click,
                                              width=100)
        self.plot_data.grid(row=1, column=0, padx=10, pady=10)
        
        self.plot_slopes = create_custom_button(self.calculations_window_frame,
                                                text="Retas de Ajuste",
                                                command=self.on_button_click,
                                                width=100)
        self.plot_slopes.grid(row=2, column=0, padx=10, pady=10)
        
        self.plot_intersections = create_custom_button(self.calculations_window_frame,
                                                       text="Plotar Interseções",
                                                       command=self.on_button_click,
                                                       width=100)
        self.plot_intersections.grid(row=3, column=0, padx=10, pady=10)
        
        self.see_calculations_data = create_custom_button(self.calculations_window_frame,
                                                          text="Ver Dados",
                                                          command=self.on_button_click,
                                                          width=100)
        self.see_calculations_data.grid(row=4, column=0, padx=10, pady=10)
        
        
    def on_button_click():
        print("Button clicked!")   

    def calculate(self):
        def inv_polynomial(dobs, degree, x):
            """
            Funcao para calcular os parâmetros de uma regressao polinomial
            Dados de entrada:
                d = dados observados
                degree = grau do polinomio
                x = valores das posicoes onde d foi medido, tem que ter a mesma dimensao de d

            Output:
                m = parametros
                G = matriz de modelagem direta
            """
            nl = max(np.shape(dobs))

            G = np.ones((nl,1))
            for pw in range(1,degree+1):

                G = np.c_[G, x**pw ]

            m = np.dot(np.dot(inv(np.dot(G.T,G)),G.T), dobs)

            return m, G

        # m, G = inv_polynomial(dobs=pressao_ogx_93_ma['Prof./Intv.(m)'], degree=1, x=pressao_ogx_93_ma['Pressão de\nFormação\n(Kgf/cm2)'])
        # print(f"y = {m[0]:.2f} + {m[1]:.2f}x")

class Footer:
    def __init__(self, master):
        import webbrowser
        self.master = master
        self.footer_frame = tk.Frame(self.master, bg='#ebebeb')
        # Se eu quiser adicionar mais alguma coisa antes do footer
        # alterar o argumento row abaixo.
        self.footer_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        # Botoes de acesso a giecar, github e sair
        giecar_link = create_custom_button(self.footer_frame,
                                           text="GIECAR",
                                           command=lambda: \
                                           webbrowser.open("http://gcr.sites.uff.br/"),
                                           width=100)
        giecar_link.grid(row=0, column=0, padx=10, pady=10)

        github_link = create_custom_button(self.footer_frame,
                                           text="GitHub",
                                           command=lambda: \
                                           webbrowser.open("https://github.com/albano-a/GradPress"),
                                           width=100)
        github_link.grid(row=0, column=1, padx=10, pady=10)

        exit_button = create_custom_button(self.footer_frame,
                                           text="Sair",
                                           command=self.master.quit,
                                           width=100)
        exit_button.grid(row=0, column=2, padx=10, pady=10)

        texto_inicial = "Desenvolvido por André Albano\nGIECAR - UFF\n2024"
        self.label = tk.Label(self.footer_frame, text=texto_inicial, bg='#ebebeb', font=("Helvetica", 10))
        self.label.grid(row=1, column=0, columnspan=3, padx=15, pady=10)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("light")
        self.geometry("600x950")
        self.minsize(600, 950)
        self.title("GradPress")
        self.iconbitmap(default="./icon.ico")  # icone
        self.option_add("*Label.font", "Helvetica 15")  # for the font

        # Determinação de um frame para centralizar o conteúdo da página
        self.main_frame = tk.Frame(self, bg='#ebebeb')
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.file_uploader = FileUploader(self.main_frame)
        self.well_info_input = WellInfoInput(self.main_frame, self.file_uploader)
        self.footer = Footer(self.main_frame)




if __name__ == "__main__":
    app = App()
    app.mainloop()