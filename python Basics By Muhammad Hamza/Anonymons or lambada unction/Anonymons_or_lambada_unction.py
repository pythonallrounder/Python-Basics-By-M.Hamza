# anonmynous / lambda function
from functools import reduce
add = lambda a,b:a+b

print(add(2,3))

# filter 
lis=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda a:a%2==0,lis))
print("filteres data is",even)

# map
add = list(map(lambda a:a+3,even))
print("map data is :",add)

# reduce
sum = reduce(lambda a,b:a+b,add)
print(sum)
