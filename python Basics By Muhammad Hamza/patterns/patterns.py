# making patterns
import numpy

# square pattern
for i in range(5):
    for j in range(5):
        print("* ",end="")
    print()
print()
# left top triangle pattern
for i in range(5):
    for j in range(i,5):
        print("* ",end="")
    print()

print()
# left down triangle pattern
for i in range(5):
    for j in range(i+1):
        print("* ",end="")
    print()
print()

# print the upper triangle
n = int(input("enter the rows : "))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print('*',end=" ")
    print()