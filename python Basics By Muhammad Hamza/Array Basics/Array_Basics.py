# Array Basics
import array as a  # use of iles

# a sample array
arr = a.array("i",[1,2,3,4])
print(arr)

# copying an array
arr1 = a.array(arr.typecode,(a for a in arr))
print(arr)

# for using function
from array import *    # use for importing all functions

# taking in put from user

a1 = array('i',[])

size = int(input("Enter size of array :"))

for i in range(size):
     x = int(input("Enter Next value"))

     a1.append(x)
print(a1)

# searching element in array

s = int(input("Enter vlaue to search:"))

for j in a1:
    if j==s:
        print("FOund value is",j)
        break
# to print the index value
print(a1.index(j))

