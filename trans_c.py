# Author : Koshvendra Singh
# Date   : 01/06/2020
# Description : exponential distributed rendom number created by transformation method in c is plotted here

import numpy as np
import matplotlib.pyplot as plt

num=10000
bin_num=10
data=np.genfromtxt('/home/koshvendra/Assignment_comp/Ass4_2020/transformation.txt',skip_header=0,skip_footer=0)

# comparing plots
x1=np.linspace(0.001,1,10)
y1=(num/bin_num)*(x1/x1)

x2=np.linspace(0,10,200)
y2=num*0.5*np.exp(-0.5*x2)

fig,(axs1,axs2)=plt.subplots(1,2)
fig.suptitle('uniform and nonuniform distributed random number')
axs1.hist(data[:,0],range=(0.0,1.0))
axs1.plot(x1,y1,'g',label='uniform distribution')
plt.legend()

axs2.hist(data[:,1],range=(0.0,10.0))
axs2.plot(x2,y2,'black',label='exponential distribution')

axs1.set(xlabel='x',ylabel='no of elements in a bin')
axs2.set(xlabel='y',ylabel='no of elements in a bin')
plt.subplots_adjust(wspace=0.4)
plt.legend()
plt.show()
