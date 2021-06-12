# for loop
# using on data type you can use it on many data 
x=['hazma',6,7.8]
for i in x:
    print(i,end=" ")

x='hamza'
for i in x:
    print(i)

# for loop with range
for i in range(5):
    print(i,end=" ")

# range for selected value limit
for i in range(2,6):
    print(i)

# for increment and decrement increment is default

for i in range(9,1,-2):# you can set any value for decremet or increment 
    print(i,end=" ")

# program for printing the values of perfect sqaues and divid by 2
import math 

for i in range(1,500):
    x=math.sqrt(i)
   
    if x%2==0:
        print("even values are",x)
    