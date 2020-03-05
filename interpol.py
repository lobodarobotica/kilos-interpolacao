import numpy as np
from scipy import stats
from scipy import interpolate

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import pyEX as p
import time

import numpy as np
from sklearn.linear_model import LinearRegression

def timestamp_align(strain_big, array_big, array_small):
        
    j = 0

    new_strain = []

    for i in range(0, len(array_small)):
    # for i in range(0, 1000):
            
            # print(i)

            while array_big[j] <= array_small[i]:
                # print("j: ", j)
                j += 1

                # if j >= len(timestamp_sensor_3):
                #     # j -= 1
                #     break

            # print("O J é: ", j)
            # print("timestamp 3: ", array_big[j])
            # print("O i é: ", i)
            # print("timestamp sensor 2: ", array_small[i])

            new_strain.append(strain_big[j])
            

    return new_strain

payload_sensor_1 = np.genfromtxt('kilos1.csv',delimiter='\t')
payload_sensor_2 = np.genfromtxt('kilos2.csv',delimiter='\t')
payload_sensor_3 = np.genfromtxt('kilos3.csv',delimiter='\t')

timestamp_sensor_1 = payload_sensor_1[:,1]
timestamp_sensor_2 = payload_sensor_2[:,1]
timestamp_sensor_3 = payload_sensor_3[:,1]

strain_sensor_1 = payload_sensor_1[:,2]
strain_sensor_2 = payload_sensor_2[:,2]
strain_sensor_3 = payload_sensor_3[:,2]

new_strain_sensor_1 = timestamp_align(strain_sensor_1,timestamp_sensor_1,timestamp_sensor_2)
new_strain_sensor_3 = timestamp_align(strain_sensor_3,timestamp_sensor_3,timestamp_sensor_2)

range_timestamp_sensor_2 = []

range_strain_sensor_1 = []
range_strain_sensor_2 = []
range_strain_sensor_3 = []

for i in range(370000, len(timestamp_sensor_2), 1):

        range_timestamp_sensor_2.append(timestamp_sensor_2[i])

        range_strain_sensor_1.append(new_strain_sensor_1[i]-70000)
        range_strain_sensor_2.append(strain_sensor_2[i]-120000)
        range_strain_sensor_3.append(new_strain_sensor_3[i]-0)

media = []

for i in range(0, len(range_timestamp_sensor_2)):

    media.append(((range_strain_sensor_2[i]) + range_strain_sensor_3[i] + range_strain_sensor_1[i])/3)

x_data = np.array([-183000,-145300]) 
y_data = np.array([0, 5000]) 

# reg = LinearRegression().fit(X, y)

slope, intercept, r_value, p_value, std_err = stats.linregress(x_data, y_data)

# f = sp.interp1d(x_data, y_data)
ynew= []
for i in range(0, len(media)):
    ynew.append(media[i]*slope + intercept)

# plt.plot(range_timestamp_sensor_2, range_strain_sensor_1,'r--', range_timestamp_sensor_2, range_strain_sensor_2, 'g--', range_timestamp_sensor_2, range_strain_sensor_3, 'b--', range_timestamp_sensor_2, media, 'y-')
plt.plot(range_timestamp_sensor_2, ynew, 'y-')
plt.show()
