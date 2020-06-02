# Author : Koshvendra Singh
# date : 01/06/2020
# Description : calculating the area of a circle using monte carlo integration then calculating the volume of ten dimensional unit sphere.

# note : i am calculating 1/4 of circle's area by monte carlo method then multiplying by 4 to gettotal area.

import numpy as np
import matplotlib.pyplot as plt

x=2*np.random.rand(10000)-1
y=2*np.random.rand(10000)-1

radius=1
# definig circle
def func(u,v):
    return np.sqrt(u*u + v*v)

# for plotting of circle in first quadrant
x1=np.linspace(-1,1,100)
circle1=np.sqrt(1-x1*x1)
x2=np.linspace(-1,1,100)
circle2=-np.sqrt(1-x2*x2)

y_good=[]
x_good=[]
y_bad=[]
x_bad=[]
for i in range(len(x)):
    if func(x[i],y[i])<=1:
        y_good.append(y[i])
        x_good.append(x[i])
    else :
        y_bad.append(y[i])
        x_bad.append(x[i])
        pass

#plotting / scattering the circle / 2d random number
plt.plot(x1,circle1,'black')
plt.plot(x2,circle2,'black',label='circle of unit radius')
plt.scatter(x_good,y_good,s=0.1,c='blue',label='good 2d random number')
plt.scatter(x_bad,y_bad,s=0.2,c='green',label='bad 2d random number')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Area of unit circle by monte carlo method')
plt.legend()
plt.show()

# area of circle by monte carlo integration
area=1*len(y_good)/len(x)

print('area of circle by monte carlo integration:',4*area)
print('analytical area of 2d circle:',np.pi*radius**2)

# 10 dimensional unit sphere area
# defining function for caculating volume of sphere of dimension d
def MC_integ(d):
    num=10**5
    mat=np.zeros((d,num))
    for i in range(d):
        mat[i,:]=2*np.random.rand(num)-1
    good_points=0
    for i in range(num):
        radius=np.sum(mat[:,i]**2)
        if radius < 1:
            good_points=good_points+1
        else:
            pass        
    vol= ( 2**d )*good_points/num
    return vol

vol_10d=MC_integ(10)
print('Volume of 10 dimensional sphere :',vol_10d)
