import numpy as np
from scipy import interpolate

import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import pyEX as p


x = np.array([-100000,-65500,1500, 31400,80000]) 
y = np.array([0,0, 7500, 15106, 16000]) 

array_kilos = np.genfromtxt('kilos.csv',delimiter='\t')
print(array_kilos[:,2])

xx = array_kilos[:,1]
yy = array_kilos[:,2]

f = interpolate.interp1d(x, y)
ynew = f(yy)

df = pd.DataFrame({'B': ynew})
ttt = df.ewm(alpha=1).mean()
ttt = df.ewm(com=100).mean()

kkk = []

plt.plot(ttt,'-')
plt.show()
