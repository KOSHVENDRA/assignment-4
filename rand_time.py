# Author : Koshvendra Singh
# Email  : koshvendra.singh@tifr.res.in
# date   : 21/05/2020
# Description : this code is to compute time taken by 'self made ' and 'np.random,rand' function for creating 10000 random numbers in [0,1)

# self made lineae congruential random number generator
import numpy as np
import matplotlib.pyplot as plt
import time

# fixing seed(x0),modulus(m),multiplier(a)and increament(c)
x0=1
m=785498568
a=423895
c=352687859

# defining a function to get max value element of an array
def arr_max(array):
    m=array[0]
    for i in range(len(array)):
        if m>= array[i]:
            pass
        else:
            m=array[i]
    return m

# computation of time consumption  by my code

start_time=time.time()
# linear congruential  method gives random number in [0,m)
arr=[]                                 # array to collect random numbers
for i in range(10**4):
    k=(a*x0 + c)% m
    arr.append(k)
    x0=k

# to get random numbers in between 0 qnd 1
max=arr_max(arr)
rand_arr=[]               # array to contain random numbers between [0,1)

for i in range(len(arr)):
    m=arr[i]/max
    r=round(m,3)
    rand_arr.append(r)
end_time=time.time()
my_time=end_time-start_time                   # time taken

# computation of time consumption  by my code

start_time1=time.time()
rando_arr=np.random.rand(10**4)
end_time1=time.time()

num_time=end_time1-start_time1                # time taken

print("time taken by my code :",my_time)
print('time taken by numpy function :',num_time)



