# Author : Koshvendra Singh
# Email  : koshvendra.singh@tifr.res.in
# Date   : 27/05/2020
# Description : Using Box-muller method to produce 10000 random number distributed a/c to sqrt(1/2*pi)*exp(-x*x/2)

import numpy as np
import matplotlib.pyplot as plt

# generating random numbers
num= 10**4
x1=np.random.rand(num)
x2=np.random.rand(num)

# 2d transformation to get gaussian distribution
y1=np.sqrt(-2*np.log(x1))*np.cos(2*np.pi*x2)
y2=np.sqrt(-2*np.log(x1))*np.sin(2*np.pi*x2)

# comparing plot
x=np.linspace(-6,6,100)
y=(1/(2*np.pi)**0.5)*np.exp(-x*x)

#plotting the PDF
fig,(axs1,axs2) = plt.subplots(1,2)
fig.suptitle('10000 random number having gaussian distribution')
axs1.hist(y1,range=(-5.0,5.0),density='true')
axs1.plot(x,y,'b',label='gaussian distribution')

axs2.hist(y2,range=(-5.0,5.0),density='true')
axs2.plot(x,y,'g',label='gaussian distribution')

axs1.set(xlabel='y',ylabel='PDF')
axs2.set(xlabel='y',ylabel='PDF')
plt.subplots_adjust(wspace=0.4)

plt.show()
