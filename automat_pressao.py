import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from utility.fluid_pressure import fluid_pressure

fluid_pressure = fluid_pressure()

df = pd.read_csv('./uploads/pressao_exemplo_2.csv',
                 sep=";",
                 skiprows=1,
                 names=["prof","pressao"])

prof = df["prof"]
pressao = df["pressao"]

def reta(ps_a,ps_b):
    val = np.polyfit(ps_a, ps_b, 1)
    #print(val[0],val[1])
    return val[0]

reta(np.array([prof[0],prof[1]]),np.array([pressao[0],pressao[1]]))

for i in range(len(prof)-1):
    val = reta(np.array([prof[i],prof[i+1]]),np.array([pressao[i],pressao[i+1]]))
    print(val*-1)

coeficients = {}
array_coeficients = []
for i in range(len(prof)-1):
    val = reta(np.array([prof[i],prof[i+1]]),np.array([pressao[i],pressao[i+1]]))
    coeficients[val*(-1.)] = [i,i+1]
    array_coeficients.append(val*(-1.))
    #print(val*(-1.))

print(coeficients)
array_coeficients = np.array([array_coeficients,array_coeficients])
#print(array_coeficients)
kmeans = KMeans(n_clusters=2, random_state=0).fit(array_coeficients.T)

classified_data = [list(kmeans.labels_)[0]]+list(kmeans.labels_)
print(classified_data)

def conversion(class_data):
    new_class_data = []
    first_value = classified_data[0]

    if first_value == 1:
        for i in range(len(classified_data)):
            if classified_data[i] == 1:
                new_class_data.append(0)
            if classified_data[i] == 0:
                new_class_data.append(1)

        return new_class_data

    return class_data

conversion(classified_data)

values_top_p = []
values_top_c = []

values_bot_p = []
values_bot_c = []

for i in range(len(classified_data)):
    if classified_data[i] == 1:
        values_top_p.append(pressao[i])
        values_top_c.append(prof[i])
    if classified_data[i] == 0:
        values_bot_p.append(pressao[i])
        values_bot_c.append(prof[i])

slope_top, intercept_top = np.polyfit(values_top_c,values_top_p, 1)
slope_bot, intercept_bot = np.polyfit(values_bot_c,values_bot_p, 1)

plt.plot(values_top_p,values_top_c,'o',c="C0",label='top curve '+str(round(slope_top,4)))
plt.plot(values_bot_p,values_bot_c,'o',c="C3",label='bot curve '+str(round(slope_bot,4)))
plt.legend()
plt.xlabel('Pressão (PSI)')
plt.ylabel('Cota (M)')
plt.grid()
# plt.show()

### input usuário da unidade de pressão

UP = "psi/m" # unidade de pressão

ranges = {}

fluids = list(fluid_pressure.keys())

dict_pressure = {}
for i in  range(len(fluid_pressure.keys())-1):
    top = fluids[i]
    bot = fluids[i+1]
    top_value = fluid_pressure[top]["gradient"][UP]
    bot_value = fluid_pressure[bot]["gradient"][UP]
    dict_pressure[fluids[i]] = [top_value,bot_value]

(k := next(iter(dict_pressure)), dict_pressure.pop(k))
print(dict_pressure)

fluid_top = 0

for fluid in dict_pressure:
    if -1.*round(slope_top,4) >= dict_pressure[fluid][0] and -1.*round(slope_top,4) < dict_pressure[fluid][1]:
        fluid_top = fluid

for fluid in dict_pressure:
    if -1.*round(slope_bot,4) >= dict_pressure[fluid][0] and -1.*round(slope_bot,4) < dict_pressure[fluid][1]:
        fluid_bot = fluid

fluid_top_name = fluid_pressure[fluid_top]['name']
fluid_bot_name = fluid_pressure[fluid_bot]['name']

print(fluid_top_name,"|",fluid_bot_name)

reta_top = slope_top*np.array(values_top_c) + intercept_top
reta_bot = slope_bot*np.array(values_bot_c) + intercept_bot


plt.plot(values_top_p,values_top_c,'o',c="C0",label=fluid_top_name)
plt.plot(values_bot_p,values_bot_c,'o',c="C3",label=fluid_bot_name)

plt.plot(reta_top,values_top_c,c="C9",label=fluid_top_name+str(round(slope_top,4)))
plt.plot(reta_bot,values_bot_c,c="C1",label=fluid_bot_name+str(round(slope_bot,4)))
plt.legend()
plt.xlabel('Pressão (PSI)')
plt.ylabel('Cota (M)')
plt.grid()
# plt.show()

x_intercept = (intercept_bot - intercept_top) / (slope_top - slope_bot)
y_intercept = slope_top * x_intercept + intercept_top
print('O ponto de interseção das retas é',x_intercept,y_intercept)

diff = np.diff(values_top_c)
print(diff)

# Extended top curve

mean_cota_top = np.mean(np.diff(values_top_c))
print(mean_cota_top)
extended_cota_top = list(values_top_c) + [mean_cota_top+np.min(values_top_c)]
print(values_top_c)
print(extended_cota_top)
extended_pressure_top = np.array(extended_cota_top)*slope_top + intercept_top
print(extended_pressure_top)

# Extended bot curve

mean_cota_bot = np.mean(np.diff(values_bot_c))
print(mean_cota_bot)
print(np.max(values_bot_c))
extended_cota_bot =  [(np.max(values_bot_c) - mean_cota_bot)] + list(values_bot_c)
print(values_bot_c)
print(extended_cota_bot)
extended_pressure_bot = np.array(extended_cota_bot)*slope_bot + intercept_bot
print(extended_pressure_bot)

plt.plot(values_top_p,values_top_c,'o',c="C0",label=fluid_top_name)
plt.plot(values_bot_p,values_bot_c,'o',c="C3",label=fluid_bot_name)

plt.plot(extended_pressure_top,extended_cota_top,c="C9",label=fluid_bot_name+" "+str(round(slope_bot,4)))
plt.plot(extended_pressure_bot,extended_cota_bot,c="C1",label=fluid_top_name+" "+str(round(slope_top,4)))
plt.plot(y_intercept,x_intercept,'s',c="k",label="Intersection "+str(round(x_intercept,4)) )

plt.legend()
plt.xlabel('Pressure (PSI)')
plt.ylabel('Level (M)')
plt.grid()
# plt.show()