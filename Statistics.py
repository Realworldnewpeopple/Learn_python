#!/usr/bin/env python

import numpy as np
import math

# we inputed the array from the user and our task is to output the correlation between the two variables
def input_array():
    i=[]
    lists=input("input the values for variable: ").split(',')
    return [int(i) for i in lists]

array1=input_array()
array2=input_array()


# #### So we have multiplied each index of two different arrays/values, so to find the dot product we neet to sum up all the arrays
# #### As we all know the mathematical dot product is [A][B]=[AB]cos@ or A1B1+A2B2+A3B3+....+AnBn where 1,2,....n are the indexes of the array

def addition(x):
    add=0
    for i in x:
        add+=i
    return add

#print(addition(array1))
#print(addition(array2))

# #3 We have created an addition funcioon so now what we need to do is create a dot product function
def dot(x,y):
    return addition(i*j for i,j in zip(x,y))

print("The dot product is:"+str(dot(array1,array2)))

def mean(x):
    total=0
    n=len(x)
    for i in x:
        total+=i
        average=total/n
    return average        

def variance_part1(x):
    diff=[i-mean(x) for i in x]
    return diff

#variance_part1(array1)

def variance_comp(x):
    var=np.array(variance_part1(x))
    var=var**2
    variance=addition(var)/len(x)
    return variance

# #3 We need to find the co-variance of the two variables and later find the corelation between the 2 variables
# #3 Here we are using the dot product to multyply both the arrays and then later divide it ny its length

def covariance(x,y):
    varx,vary=np.array(variance_part1(x)),np.array(variance_part1(y))
    total=dot(varx,vary)
    return total/len(x)


# # We have found the covariance, so now we can find the correlation

def correlation(x,y):
    return (covariance(x,y)/math.sqrt(variance_comp(x)*variance_comp(y)))

print("Correlation between the two given variables: "+str(correlation(array1,array2)))
