# copying and conatenation of two arrays
from numpy import *

a1 = array([1,2,3,4,5])
#a2= array([6,7,8,9,9])

# copying
a2=a1
print(a1)
print(a2)

# here is only one array and other is just pointing
# by adrress we can check
print(id(a1))
print(id(a2))

# two create two different array after copying we use view()
# this is also called shallow copy both array dependent we can't change any value
a3=a2.view() # view will make a second array
a3[1]=98 # making change in one will effect other 
print(a3)
print(a2)

# adress with view() are
print(id(a3))
print(id(a2))

# deep copy to make both independent
a4=a2.copy() # copy() make both idependent 
a4[1]=45 # there will be change in only a4 no effect on a2
print(a4)
print(a2)

# adress with copy() are
print(id(a4))
print(id(a2))


# concatnetation of two arrays
print("concatenation of 2 arrays is:",concatenate([a1,a4]))