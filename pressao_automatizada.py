import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans # entender o porque desse import
from utility.fluid_pressure import fluid_pressure

fluid_pressure = fluid_pressure() # dictionary of fluid pressures

df = pd.read_csv('./uploads/ogx.csv',
				  sep=";",
				  skiprows=1,
				  names=["prof", "pressao"])

prof = df["prof"]
pressao = df["pressao"]

def calculate_slope(ps_a, ps_b):
    """
    Calculate the slope of the line of best fit for the given data points.

    Parameters:
    ps_a, ps_b : array_like, 1-dimensional
        The x and y coordinates of the data points.

    Returns:
    float
        The slope of the line of best fit.
    """
    if len(ps_a) != len(ps_b):
        raise ValueError("ps_a and ps_b must have the same length")

    coefficients = np.polyfit(ps_a, ps_b, 1)

    return coefficients[0]

slopes = []
slope_indices = {}
for i in range(len(prof) - 1):
	x_values = np.array([prof[i], prof[i + 1]])
	y_values = np.array([pressao[i], pressao[i + 1]])
	slope = calculate_slope(x_values, y_values) * -1
	slopes.append(slope)
	slope_indices[slope] = [i, i + 1]

# Convert the list of slopes to a numpy array
slopes_array = np.array([slopes, slopes])

# Perform KMeans clustering on the slopes
kmeans = KMeans(n_clusters=2, random_state=0).fit(slopes_array.T)

# Classify the data based on the clusters
classified_data = [list(kmeans.labels_)[0]] + list(kmeans.labels_)

def convert_classification(class_data):
	"""
	Convert the classification labels if the first value is 1.
	"""
	if class_data[0] == 1:
		return [1 - label for label in class_data]
	return class_data

# Convert the classification labels if necessary
converted_data = convert_classification(classified_data)

# Separate the data into two groups based on the classification
top_values = [(prof[i], pressao[i]) for i, label in enumerate(converted_data) if label == 1]
bottom_values = [(prof[i], pressao[i]) for i, label in enumerate(converted_data) if label == 0]

# Calculate the line of best fit for each group
top_prof, top_pressao = zip(*top_values)
bottom_prof, bottom_pressao = zip(*bottom_values)

slope_top, intercept_top = np.polyfit(top_prof, top_pressao, 1)
slope_bottom, intercept_bottom = np.polyfit(bottom_prof, bottom_pressao, 1)

# plt.plot(top_pressao,top_prof,'o',c="C0",label='top curve '+str(round(slope_top,4)))
# plt.plot(bottom_pressao,bottom_prof,'o',c="C3",label='bot curve '+str(round(slope_bottom,4)))
# plt.legend()
# plt.xlabel('Pressão (PSI)')
# plt.ylabel('Cota (M)')
# plt.grid()
# plt.show() # Plota o gráfico com os clusters divididos

# User input for pressure unit
pressure_unit = "psi/m"

# Initialize an empty dictionary for pressure ranges
pressure_ranges = {}

# Get a list of all fluid keys
fluid_keys = list(fluid_pressure.keys())

# Initialize an empty dictionary for pressure values
pressure_values = {}

# Iterate over each pair of consecutive fluids
for i in range(len(fluid_keys) - 1):
    # Get the top and bottom fluids
    top_fluid = fluid_keys[i]
    bottom_fluid = fluid_keys[i + 1]

    # Get the pressure gradient values for the top and bottom fluids
    top_pressure = fluid_pressure[top_fluid]["gradient"][pressure_unit]
    bottom_pressure = fluid_pressure[bottom_fluid]["gradient"][pressure_unit]

    # Store the pressure values in the dictionary
    pressure_values[top_fluid] = [top_pressure, bottom_pressure]

# Remove the first key-value pair from the dictionary
first_key = next(iter(pressure_values))
pressure_values.pop(first_key)

# Initialize the top fluid
top_fluid = 0

# Find the fluid that matches the top slope
for fluid, pressures in pressure_values.items():
    if -1.*round(slope_top,4) >= pressures[0] and -1.*round(slope_top,4) < pressures[1]:
        top_fluid = fluid

# Find the fluid that matches the bottom slope
for fluid, pressures in pressure_values.items():
    if -1.*round(slope_bottom,4) >= pressures[0] and -1.*round(slope_bottom,4) < pressures[1]:
        bottom_fluid = fluid

# Get the names of the top and bottom fluids
top_fluid_name = fluid_pressure[top_fluid]['name']
bottom_fluid_name = fluid_pressure[bottom_fluid]['name']

# Print the names of the top and bottom fluids
print(top_fluid_name, "|", bottom_fluid_name)


x_intercept = (intercept_bottom - intercept_top) / (slope_top - slope_bottom)
y_intercept = slope_top * x_intercept + intercept_top
print('O ponto de interseção das retas é',x_intercept,y_intercept)

diff = np.diff(top_prof)
print(diff)

# Extended top curve
mean_cota_top = np.mean(np.diff(top_prof))
extended_cota_top = [(np.abs(mean_cota_top) + np.max(top_prof))] + list(top_prof)
extended_pressure_top = np.array(extended_cota_top)*slope_top + intercept_top

# Extended bot curve
mean_cota_bot = np.mean(np.diff(bottom_prof))
extended_cota_bot =  list(bottom_prof) + [(np.min(bottom_prof) + mean_cota_bot)]
extended_pressure_bot = np.array(extended_cota_bot)*slope_bottom + intercept_bottom

# Calculate the line of best fit for the top and bottom fluids
line_top = slope_top * np.array(top_prof) + intercept_top
line_bottom = slope_bottom * np.array(bottom_prof) + intercept_bottom

plt.figure(figsize=(13,5))

plt.subplot(131)
plt.plot(top_pressao,top_prof,'o',c="C0",label='top curve '+str(round(slope_top,4)))
plt.plot(bottom_pressao,bottom_prof,'o',c="C3",label='bot curve '+str(round(slope_bottom,4)))
plt.legend()
plt.xlabel('Pressão (PSI)')
plt.ylabel('Cota (M)')
plt.grid()
# plt.show() # Plota o gráfico com os clusters divididos

plt.subplot(132)
# Plot the data points for the top and bottom fluids
plt.plot(top_pressao, top_prof, 'o', c="C0", label=top_fluid_name)
plt.plot(bottom_pressao, bottom_prof, 'o', c="C3", label=bottom_fluid_name)

# Plot the lines of best fit for the top and bottom fluids
plt.plot(line_top, top_prof, c="C9", label=f'{top_fluid_name} {round(slope_top, 4)}')
plt.plot(line_bottom, bottom_prof, c="C1", label=f'{bottom_fluid_name} {round(slope_bottom, 4)}')

# Add a legend, labels, and a grid
plt.legend()
plt.xlabel('Pressão (PSI)')
plt.ylabel('Cota (M)')
plt.grid()

plt.subplot(133)
plt.plot(top_pressao,top_prof,'o',c="C0",label=top_fluid_name)
plt.plot(bottom_pressao,bottom_prof,'o',c="C3",label=bottom_fluid_name)

plt.plot(extended_pressure_top,extended_cota_top,c="C9",label=bottom_fluid_name+" "+str(round(slope_bottom,4)))
plt.plot(extended_pressure_bot,extended_cota_bot,c="C1",label=top_fluid_name+" "+str(round(slope_top,4)))
plt.plot(y_intercept,x_intercept,'s',c="k",label="Intersection "+str(round(x_intercept,4)) )

plt.legend()
plt.xlabel('Pressure (PSI)')
plt.ylabel('Level (M)')
plt.grid()

plt.tight_layout()
plt.show() # Plota o gráfico com as linhas de tendência, mas não esticadas