import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy.linalg import inv

# importing files
def plot_pressure():
    filename = fname.get()
    pressao_df = pd.read_csv(filename, delimiter=';')
    pressao_df = pressao_df.dropna(subset=['Prof./Intv.(m)', 'Pressão de Formação (Kgf/cm2)'])

    def plot_pressao(x, y, title, xlabel, ylabel, ymin, ymax):
        plt.plot(x, y, 'o')
        plt.gca().invert_yaxis()
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.ylim(ymin, ymax)
        plt.grid()
        plt.show()

    plot_pressao(x=pressao_df['Pressão de Formação (Kgf/cm2)'],
                 y=pressao_df['Prof./Intv.(m)'],
                 title=nome_entry.get(),
                 xlabel='Pressão de Formação (Kgf/cm2)',
                 ylabel='Profundidade (m)',
                 ymin=prof_min.get(),
                 ymax=prof_max.get())
