import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import pandas as p


x = np.array([-100000,-65500,1500, 31400,80000]) 
y = np.array([0,0, 7500, 15106, 16000]) 

array_kilos = np.genfromtxt('kilos.csv',delimiter='\t')
print(array_kilos[:,2])

xx = array_kilos[:,1]
yy = array_kilos[:,2]

f = interpolate.interp1d(x, y)
# f3 = interpolate.interp1d(x, y, kind='cubic')


# while True:
#     print(f(input('Digite o strain: ')))
# print(str(f))
# # strain =input("Entre com o strain: ")
# print(type(f))
# print(dir(f))
# xnew = np.arange(235001,309999,1)

# xnew = np.linspace(0, 10, num=41, endpoint=True)
ynew = f(yy)

# ynew3= f3(xnew)

# plt.plot(x,y,'o',xnew,ynew,'-', xnew,ynew3, '--')

kkk = []


for i in range(0, len(ynew), 1000):
    kkk.append(ynew[i])
    print('oi amiguinho')

print(kkk)

plt.plot(x,y,'o',yy,ynew,'-')
plt.show()

plt.plot(kkk)
plt.show()



# plt.show()

# response = a * int(strain) + b
# print(response)
# print(a, b)

