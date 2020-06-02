#Author : Koshvendra Singh
# Email  : koshvendra.singh@tifr.res.in
# date   : 22/05/2020
# Description : using rejection method to produce non uniform deviates of random number
# non uniform deviate function : sqrt(2/pi)*exp(-x*x/2)  (x>=0)

import numpy as np
import matplotlib.pyplot as plt

num=10**4
x=np.random.rand(num)*10.0
x=-np.log(x)
y=np.random.rand(num)*1.5*np.exp(-x)
z=np.random.rand(num)*(np.sqrt(2/np.pi)*np.exp(-(x*x)/2))

y_good=y[y<z]
x_good=x[y<z]

x1=np.linspace(0,10,100)
y1=np.sqrt(2/np.pi)*np.exp(-(x1*x1)/2)
y2=1.5*np.exp(-x1)

plt.plot(x1,y1,'r',label='non-uniform variate function')
plt.plot(x1,y2,'black',label='envelop function')
plt.hist(x_good,range=(0.0,10.0),density='true')
plt.xlabel('x')
plt.ylabel('PDF')
plt.legend()
plt.show()
