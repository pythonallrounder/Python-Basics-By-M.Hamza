# numpy function and arraya
from numpy import *
# numpy array
 
arr = array([1,2,3,4,5])
print(arr) # integer type even we don't write 'i'

arr1 = array([1,2,3,4.6,7]) # here impicit conversion is happenning
print(arr1) # float type it will do automaticlay

arr2 = array (['a','b','c'])
print(arr2)

# checking data type of above 
print(arr.dtype)
print(arr1.dtype)
print(arr2.dtype)

# explicit conversion

arr3=array([1,2,3,5.6],float)
print(arr3.dtype)
print()

# function of numpy

# linspace()
lin = linspace(1,12,13)
print("linspace is :",lin)
print()

# id do' write the steps or parts value than by defaulf it will divide into 50
lin1 = linspace(1,12)
print("linspace without step value is:",lin1)
print()


# arange()
ar = arange(1,12,3)
print("arange is :",ar)
print()

# logspace()
log = logspace(1,30,10)
print("logspace is :",log)
print()
# here output will be in +e format in above case of using logsoace()
# we can get decimal vales 
print("decimal value is :",'%.2f'%log[1])

# zeros()
zero = zeros(10)
print("zeros is :",zero)
print()

# ones()
one = ones(5)
print("ones is: ",one)
print()













