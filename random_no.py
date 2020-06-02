# Author : Koshvendra Singh
# Email  : koshvendra.singh@tifr.res.in
# date   : 21/05/2020
# Description : generating 10000 random numbers between 0 and 1 using np.random.rand()

import numpy as np
import matplotlib.pyplot as plt

# generating 10000 random numbers
num=10**4
rand_arr=np.random.rand(num)

#plotting a line of uniform distribution
x=np.linspace(0,1,30)
bin_no=10
y=num/bin_no*(x/x)
plt.plot(x,y,'black',label='uniform distribution')

#making histogram of random numbers
plt.hist(rand_arr,bins=10,range=(0.0,1.0))
plt.ylabel('PDF')
plt.title('histogram of random no generated using numpy function')
plt.show()
