import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from PyQt6.QtWidgets import QMessageBox


def pressure_gradient_classification(data, kmeans_number, pressure_unit,
                                     superior_title, x_axis, y_axis):
    prof = data.iloc[:, 0]
    pressao = data.iloc[:, 1]

    def calculate_slope(ps_a, ps_b):
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
    kmeans = KMeans(n_clusters=kmeans_number, random_state=0).fit(slopes_array.T)

    # Classify the data based on the clusters
    classified_data = [list(kmeans.labels_)[0]] + list(kmeans.labels_)

    def convert_classification(class_data):
        if class_data[0] == 1:
            return [1 - label for label in class_data]
        return class_data

    # Convert the classification labels if necessary
    converted_data = convert_classification(classified_data)

    # Separate the data into two groups based on the classification
    top_values = [(prof[i], pressao[i]) for i, label in enumerate(converted_data) if label == 0]
    bottom_values = [(prof[i], pressao[i]) for i, label in enumerate(converted_data) if label == 1]

    # Calculate the line of best fit for each group
    top_prof, top_pressao = zip(*top_values)
    bottom_prof, bottom_pressao = zip(*bottom_values)

    slope_top, intercept_top = np.polyfit(top_prof, top_pressao, 1)
    slope_bottom, intercept_bottom = np.polyfit(bottom_prof, bottom_pressao, 1)

    pressure_unit = pressure_unit
    # four pressure units to choose from (psi/ft, psi/m, Kgf/cm2/m, bar/m)

    fluid_pressure = {
    "dry_gas_zero": {"name":"Dry gas zero","gradient":{"psi/ft":0.0,"psi/m":0.0,"kgf/cm2/m":0.0,"bar/m":0.0}},
    "dry_gas": {"name":"Dry gas","gradient":{"psi/ft":0.0,"psi/m":0.0,"kgf/cm2/m":0.0,"bar/m":0.0}},
    "wet_gas": {"name":"Wet gas","gradient":{"psi/ft":0.140,"psi/m":0.459,"kgf/cm2/m":0.030,"bar/m":0.032}},
    "oil_limit": {"name":"Oil limit","gradient":{"psi/ft":0.300,"psi/m":0.984,"kgf/cm2/m":0.069,"bar/m":0.069}},
    "oil_60": {"name":"Oil 60°","gradient":{"psi/ft":0.387,"psi/m":1.270,"kgf/cm2/m":0.089,"bar/m":0.087}},
    "oil_20": {"name":"Oil 20° (heavy)","gradient":{"psi/ft":0.404,"psi/m":1.325,"kgf/cm2/m":0.093,"bar/m":0.091}},
    "fresh_water": {"name":"Fresh water","gradient":{"psi/ft":0.433,"psi/m":1.421,"kgf/cm2/m":0.100,"bar/m":0.098}},
    "sea_water": {"name":"Sea Water","gradient":{"psi/ft":0.444,"psi/m":1.457,"kgf/cm2/m":0.102,"bar/m":0.101}},
    "salt_sat_water": {"name":"Salt sat. Water","gradient":{"psi/ft":0.520,"psi/m":1.706,"kgf/cm2/m":0.120,"bar/m":0.118}},
    "salt_max": {"name":"Salt sat. Water Max","gradient":{"psi/ft":100.000,"psi/m":100.000,"kgf/cm2/m":100.000,"bar/m":100.000}}
    }

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
    extended_cota_top = list(top_prof) + [(np.min(top_prof) - np.abs(mean_cota_top))]
    extended_pressure_top = np.array(extended_cota_top)*slope_top + intercept_top

    # Extended bot curve
    mean_cota_bot = np.mean(np.diff(bottom_prof))
    extended_cota_bot = [(np.max(bottom_prof) - mean_cota_bot)] + list(bottom_prof)
    extended_pressure_bot = np.array(extended_cota_bot)*slope_bottom + intercept_bottom

    # Calculate the line of best fit for the top and bottom fluids
    line_top = slope_top * np.array(top_prof) + intercept_top
    line_bottom = slope_bottom * np.array(bottom_prof) + intercept_bottom

    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(13,5))
    fig.suptitle(superior_title, fontsize=16)

    messages = []
    messages.append(f"Fluido do topo: {top_fluid_name} | Fluido da base: {bottom_fluid_name}")
    messages.append(f"O ponto de interseção das retas é {x_intercept:.2f} {y_intercept:.2f}")

    # First subplot - just the data itself
    axs[0].plot(top_pressao,top_prof,'o',c="C0",label='top curve '+str(round(slope_top,4)))
    axs[0].plot(bottom_pressao,bottom_prof,'o',c="C3",label='bot curve '+str(round(slope_bottom,4)))
    axs[0].set_title('Pressão x Profundidade')
    axs[0].legend(fontsize='small')
    axs[0].set_xlabel(x_axis)
    axs[0].set_ylabel(y_axis)
    # axs[0].grid()

    # Plot the data points for the top and bottom fluids
    axs[1].plot(top_pressao, top_prof, 'o', c="C0", label=top_fluid_name)
    axs[1].plot(bottom_pressao, bottom_prof, 'o', c="C3", label=bottom_fluid_name)
    axs[1].plot(line_top, top_prof, c="C9", label=f'{top_fluid_name} {round(slope_top, 4)}')
    axs[1].plot(line_bottom, bottom_prof, c="C1", label=f'{bottom_fluid_name} {round(slope_bottom, 4)}')
    axs[1].set_title('Linha de tendências')
    axs[1].legend(fontsize='small')
    axs[1].set_xlabel(x_axis)
    axs[1].set_ylabel(y_axis)

    axs[2].plot(top_pressao,top_prof,'o',c="C0",label=top_fluid_name)
    axs[2].plot(bottom_pressao,bottom_prof,'o',c="C3",label=bottom_fluid_name)
    axs[2].plot(extended_pressure_top,extended_cota_top,c="C9",label=bottom_fluid_name+" "+str(round(slope_bottom,4)))
    axs[2].plot(extended_pressure_bot,extended_cota_bot,c="C1",label=top_fluid_name+" "+str(round(slope_top,4)))
    axs[2].plot(y_intercept,x_intercept,'s',c="k",label="Intersection "+str(round(x_intercept,4)) )
    axs[2].set_title('Contato dos fluidos')
    axs[2].legend(fontsize='small')
    axs[2].set_xlabel(x_axis)
    axs[2].set_ylabel(y_axis)

    plt.tight_layout()
    return fig, axs, messages

def open_file_for_plotting(header_lines, selected_file, file_type_button_text):
    if header_lines != '':
        skiprows = int(header_lines)
    else:
        skiprows = 0

    if file_type_button_text == 'csv':
        try:
            dataframe = pd.read_csv(f'uploads/{selected_file}',
                            delimiter='[;,]',
                            names=["prof", "pressao"],
                            engine='python',
                            skiprows=skiprows)
            return dataframe
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Um erro ocorreu: {e}")
            return pd.DataFrame()

    elif file_type_button_text == 'txt':
        try:
            dataframe = pd.read_csv(f'uploads/{selected_file}',
                            skiprows=skiprows,
                            delimiter='\t',
                            names=["prof", "pressao"],
                            engine='python')
            return dataframe
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Um erro ocorreu: {e}")
            return pd.DataFrame()

    elif file_type_button_text == 'xlsx':
        try:
            dataframe = pd.read_excel(f'uploads/{selected_file}',
                                        skiprows=skiprows,
                                        names=["prof", "pressao"])
            return dataframe
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Um erro ocorreu: {e}")
            return pd.DataFrame()