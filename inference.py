# Author : Koshvendra Singh
# date   : 05/06/2020
# Email : koshvendra1999@gmail.com
# description : fitting the given data by an equation of the the  ' a*x**2 + b*x +c ' and doing inference for 'a,b,c'

import numpy as np
import matplotlib.pyplot as plt
import emcee
from scipy.optimize import minimize
import corner

data=np.genfromtxt('/home/koshvendra/Assignment_comp/Ass4_2020/data.txt',skip_header=5,delimiter='&')
x=data[:,1]
y=data[:,2]
yerr=data[:,3]

# log of probability for data given the parameters
def log_likelihood(theta,x,y,yerr):
    a,b,c=theta
    model=a*x**2 + b*x + c
    sigma= yerr**2
    # negative of log of likelihood function
    return 0.5*np.sum((y-model)**2/sigma + np.log(2*np.pi*sigma))

# log of the prior knowledge of probability of parameters
def log_prior(theta):
    a,b,c=theta
    if -500<a<500 and -500<b<500 and -500<c<500:
        return 0.0
    return -np.inf

#
def log_probability(theta,x,y,yerr):
    lp=log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp - log_likelihood(theta,x,y,yerr)

guess=(1.0,1.0,1.0)
soln=minimize(log_likelihood,guess,args=(x,y,yerr))
nwalkers,ndim=32,3
pos=soln.x + 1e-4*np.random.randn(nwalkers,ndim)
sampler = emcee.EnsembleSampler(nwalkers,ndim,log_probability,args=(x,y,yerr))
sampler.run_mcmc(pos,5000)

samples=sampler.get_chain()

fig,(ax1,ax2,ax3)=plt.subplots(3,1)
ax1.plot(samples[:,:,0],'black')
ax1.set(xlabel='no of steps',ylabel='a')
ax2.plot(samples[:,:,1],'black')
ax2.set(xlabel='no of steps',ylabel='b')
ax3.plot(samples[:,:,2],'black')
ax3.set(xlabel='no of steps',ylabel='c')
plt.subplots_adjust(hspace=0.7)
plt.legend()
plt.show()

sample=np.zeros([144000,3])
sample[:,0]=samples[500:5000, :, 0].reshape((144000))
sample[:,1]=samples[500:5000, :, 1].reshape((144000))
sample[:,2]=samples[500:5000, :, 2].reshape((144000))
medians = np.median(sample,axis=0)
a_true ,b_true, c_true = medians

fig= corner.corner(sample,labels=['a','b','c'],truths=[a_true ,b_true, c_true],show_titles=True)

plt.figure()
plt.show()

# plotting other candidates of fitting
x1=np.linspace(np.min(x),np.max(x),400)

rand_arr=np.random.randint(140000,size=150)
for i in rand_arr:
    y_candi=sample[i,0]*(x1**2) +sample[i,1]*(x1) + sample[i,2]
    plt.plot(x1,y_candi,'g')

# plotting best plot

y1=a_true*(x1**2) + b_true*x1 + c_true
plt.plot(x1,y1,'black',label='best 2nd order polynomial fit')
plt.xlabel('x')
plt.ylabel('y')

plt.errorbar(x,y,yerr=yerr,fmt='ok')

plt.title('Data distribution with best and candidate fit')
plt.legend()
plt.show()
