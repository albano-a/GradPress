import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arq_label_selected_file = "./uploads/pressao_exemplo.csv"
#prof_min_entry = None
#prof_max_entry = None
#mesa_rot_entry = None
prof_cota_var = "Sim"
skip_rows_entry = 1
plot_title_entry = "Pressão x Profundidade"
x_label_entry = "Pressão"
y_label_entry = "Profundidade"


# open the file and load the data in a pandas dataframe
def open_file(arq_label_selected_file):
    try:
        pressao_df = pd.read_csv(arq_label_selected_file,
                                delimiter='[;,]',
                                skiprows=skip_rows_entry,
                                names=["A", "B"],
                                engine='python')
        pressao_df = pressao_df.dropna()
        return pressao_df
    except Exception as e:
        print(e)
        return None

dataframe = open_file(arq_label_selected_file)

def plot_simples(x, y, title, xlabel, ylabel):
    selected_value = prof_cota_var.get()

    # Add your logic here
    if selected_value == "Sim":
        # TODO: This function will be the one where the plot is made
        # without any adaptation to the depth, because is already in cota
        plt.plot(x, y, 'o')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid()
        plt.show()
        print("Sim was selected")

    elif selected_value == "Não":
        # TODO: This function will be the one where the plot is made
        # with adaptations to the depth, because it is not in cota
        plt.plot(x, y, 'o')
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.gca().invert_yaxis(False)
        plt.grid()
        plt.show()
        print("Não was selected")




plot_simples(dataframe["B"], dataframe["A"], plot_title_entry, x_label_entry, y_label_entry)

# def plot_simples_pressao(self, x, y, title, xlabel, ylabel, pressao_df, prof_min, prof_max, mesa_rot):
#         """
#         Função que plota a pressão de formação em função da profundidade (cota)
#         """
#         ymin = int(prof_min.get()) if prof_min.get() else min(pressao_df['Profundidade'])
#         ymax = int(prof_max.get()) if prof_max.get() else max(pressao_df['Profundidade'])

#         ymin = int(mesa_rot.get()) - ymin
#         ymax = int(mesa_rot.get()) - ymax

#         plt.plot(x, y, 'o')
#         plt.title(title)
#         plt.xlabel(xlabel)
#         plt.ylabel(ylabel)

#         plt.ylim(ymin, ymax)
#         plt.gca().invert_yaxis()
#         plt.grid()
#         plt.show()

# def main_plot_pressure(self):
#     """
#     Plota os dados de pressão em relação à profundidade.

#     Esta função lê um arquivo CSV contendo dados de pressão e os plota em relação
#     aos valores de profundidade (em cota) correspondentes.
#     Elimina quaisquer linhas com valores NaN.
#     Os valores de profundidade em cota são calculados subtraindo
#     os valores de 'Profundidade' do valor de 'mesa_rot'.
#     """
#     try:
#         filename = self.file_uploader.selected_file.get()
#         pressao_df = pd.read_csv(filename,
#                                     delimiter='[;,]',
#                                     names=["Profundidade", "Pressão"],
#                                     engine='python')
#         pressao_df = pressao_df.dropna(subset=['Profundidade', 'Pressão'])
#         prof_cota = int(self.mesa_rot.get()) - pressao_df['Profundidade']

#         self.plot_simples_pressao(x=pressao_df['Pressão'],
#                     y=prof_cota,
#                     title=self.nome_entry.get(),
#                     xlabel='Pressão',
#                     ylabel='Profundidade (m)',
#                     pressao_df=pressao_df,
#                     prof_min=self.prof_min,
#                     prof_max=self.prof_max,
#                     mesa_rot=self.mesa_rot)
#     except Exception as e:
#         tk.messagebox.showerror("Error", str(e))