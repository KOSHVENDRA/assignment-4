# Author : Koshvendra Singh
# Email  : koshvendra.singh@tifr.res.in
# date   : 21/05/2020
# Description : writing a code for linear congruential random no. generators

import numpy as np
import matplotlib.pyplot as plt

# fixing seed(x0),modulus(m),multiplier(a)and increament(c)
x0=1
m=785498568
a=423895
c=352687859

arr=[]              # array to collect random numbers

# linear congruential  method
for i in range(10**4):
    k=(a*x0 + c)% m
    arr.append(k)
    x0=k

# defining a function to get max value element of array
def arr_max(array):
    m=array[0]
    for i in range(len(array)):
        if m>= array[i]:
            pass
        else:
            m=array[i]
    return m

# to get random numbers in between 0 qnd 1
max=arr_max(arr)
rand_arr=[]               # array to contain random numbers between [0,1)

for i in range(len(arr)):
    m=arr[i]/max
    r=round(m,3)
    rand_arr.append(r)

x=np.linspace(0.001,1,20)
y=1*(x/x)
plt.plot(x,y,'black',label='uniform distribution')
# plotting the histogram of random no's generated
plt.hist(rand_arr,range=(0.0,1.0),density='true')
plt.ylabel('PDF')
plt.title('PDF of random number generated from linear congruential method')
plt.legend()
plt.show()

    
    

    
    

