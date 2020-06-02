# Author : Koshvendra Singh
# Date   : 01/06/2020
# Email  : koshvendra.singh@tifr.res.in
# Description : Applying chi-square test for the test of randomness of given sample

import numpy as np
import scipy.stats as ss

# given random arrays
#rand_arr0=[9,6,14,10,20,22,17,13,21,10,2]
rand_arr1=[4,10,10,13,20,18,18,11,13,14,13]
rand_arr2=[3,7,11,15,19,24,21,17,13,9,5]

# defining chi square test function 
def rand_test(arr):
    v=0
    nps=[4,8,12,16,20,24,20,16,12,8,4]
    for i in range(len(arr)):
        l=((arr[i]-nps[i])**2) / (nps[i])
        v=l+v
    prob=(1.0 - ss.chi2.cdf(v,len(nps)-1) )*100

    if prob<1 or prob>99:
        print('Given array is "NOT SUFFICIENTLY RANDOM "' )
    elif prob>1 and prob<5 or prob>95 and prob<99 :
        print('given array is "SUSPECTED"to be random')
    elif prob>5 and prob<10  or prob>90 and prob<95 :
        print('given array is "ALMOST SUSPECTED "to be random')
    else:
        print('given array is "SIFFICIENTLY RANDOM"')
    

# testing randomness of the arrays
print('chi square test for array 1 says:')
test_1=rand_test(rand_arr1)
print('chi square test for array 2 says:')
test_2=rand_test(rand_arr2)
