# Author : Koshvendra Singh
# Date   : 01/06/2020
# description : Use of metropolis algorithm
import numpy as np
import matplotlib.pyplot as plt

#defining target normalised pdf function
def func(x):
    if x>3 and x<7:
        return(1)
    else:
        return(0)

# random number array generator ,linear congruential method in [0,1)
def gen(n):
    a=42841917443
    c=22673
    x=1      # seed
    m=2**31
    arr=[x]
    for i in range(n-1):
        x=(a*x+c) % m
        x=x/(m-1)
        arr.append(x)
    return(arr)

# defining function for gaussian distributed (mean=0,var=2) random number array by box muller method
def gpdf(n):
    x1=gen(n)
    x2=gen(n)
    y=[]
    for i in range(n):
        k=(2*(-2*np.log(x1[i]))**0.5)*(np.cos(8*np.pi*x2[i]))
        y.append(k)
    return(y)

nsteps=10**4               
gauss=gpdf(nsteps)      # generating gauss distibuted random number array
rand=gen(nsteps)        # uniform distributed random number array
theta=2.0               # initiation
chain=[theta]           # to contain markov chain element
for i in range(nsteps -1):
    theta_prime=theta + gauss[i]
    if func(theta_prime)  > rand[i]*func(theta):
        chain.append(theta_prime)
        theta= theta_prime
    else:
        pass
    
# plottings
x3=np.arange(1,101,1)
x4=np.linspace(3,7,10)

no_bins=8
nor_dist=(len(chain)/no_bins)*(x4/x4)

fig,(ax1,ax2)=plt.subplots(2,1)
fig.suptitle('Metropolis method')
ax1.scatter(x3,chain[0:100],s=0.1,c='red',label='Markov chain')
ax1.set(xlabel='no. of iterations',ylabel='theta')

ax2.hist(chain)
ax2.plot(x4,nor_dist,'black',label='uniform pdf')
ax2.set(xlabel='x',ylabel=' PDF')

plt.subplots_adjust(hspace=0.6)
plt.legend()
plt.show()
        
    
