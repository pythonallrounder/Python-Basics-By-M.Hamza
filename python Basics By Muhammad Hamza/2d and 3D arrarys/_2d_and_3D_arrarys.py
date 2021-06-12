
# 2D arrays
from numpy import *

arr = array([
              [1,2,3,4],
              [6,7,8,9],
              [3,2,4,5]
            ])
print(arr)
print()

# ndim function 
print("Diminsion of arrary is :",arr.ndim) # this function will tell about diminsion of array
print()

# shape()
print("no of Rows and clns are :",arr.shape) # shpe() will give the no of rows and coln
print()

# size()
print("size of array is :",arr.size) # size() will tell about the total no of element in array
print()

# flatten()
print("2D to 1D array is :",arr.flatten()) # this function is use for conversion of 2d to 1d array
print()

# reshape()
arr1 = array([1,2,3,4,5,6,7,8,9,88])
print("1D to 2D array is :",arr1.reshape(5,2))
print()

# 3D array
arr2 = array([1,2,3,4,5,6,7,8,9,10,11,12])
print("3D array is :",arr2.reshape(2,2,3))
print()

# matrix()
print("converted into matrix is :",matrix(arr)) # matrix() is use to coovert array into martix
print()

# one more way to get array into matrix
ar = matrix('1 2 3 4 ; 5 6 7 8')
print("By one more way matrix is",ar)
print()

# function on matrix
# min()
print("min value is",ar.min)

# max()
print("max value is :",ar.max)

# diagonal()
print("Digonal od matrix are :",arr.diagonal())

# sum()
print("sum is :",arr.sum())






