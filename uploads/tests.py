from tkinter import Y
import matplotlib.pyplot as plt
import numpy as np

data = np.load("F:\\Universidade\\IC\\Impedance\\model0.npy")

# Choose a specific y to start with
x = 1

fig, ax = plt.subplots()
im = ax.imshow(data[x, :, :].T)

# Function to update figure
def update(x):
    im.set_array(data[:, int(x), :].T)
    fig.canvas.draw_idle()

# Create a slider
from matplotlib.widgets import Slider
ax_slider = plt.axes([0.1, 0.02, 0.8, 0.05])
slider = Slider(ax_slider, 'x', 0, data.shape[1] - 1, valinit=x, valstep=1)

# Connect the slider to the update function
slider.on_changed(update)

plt.show()