import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate


x = np.array([235000,255000, 294000, 298000,310000]) 
y = np.array([0, 25, 50, 56,100]) 

# x = np.linspace(0, 10, num=11, endpoint=True)
# y = np.cos(-x**2/9.0)


f = interpolate.interp1d(x, y)
f3 = interpolate.interp1d(x, y, kind='cubic')

# strain =input("Entre com o strain: ")

xnew = np.arange(235001,309999,1)
# xnew = np.linspace(0, 10, num=41, endpoint=True)
ynew = f(xnew)
ynew3= f3(xnew)

print(ynew)

# plt.plot(x,y,'o',xnew,ynew,'-', xnew,ynew3, '--')
plt.plot(x,y,'o',xnew,ynew,'-')


plt.show()
# plt.show()

# response = a * int(strain) + b
# print(response)
# print(a, b)