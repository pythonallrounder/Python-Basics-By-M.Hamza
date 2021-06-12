# list is like array
name =[1,2,3]
print(name)
# we can use string as a value in list
name = ['hamza','ali']
print(name)

# we can use multiple data type values in the list
name = [8.99,'can',9]
print(name)

# we can do same fecthing tec as on we have done on string we can single element by index no

print(name[0])
print(name[0:1])
print(name[:2])
print(name[0:12])
# if we use index like this but it will print blank
print(name[12:0])
# we can use -ve values as index
print(name[-0])
print(name[0:-1])
print(name[:-2])
print(name[0:-12])
# list functions
new = [1,2,34]
# append function use to add value as last
new.append(56)
print(new)
#insert fun use to add value at specfic index by passing index value
new.insert(1,21)
print(new)
# remove fun is use to remove will remove the which we will give as object
new.remove(21)
print(new)
# pop fun  will work like an stack like if will pass no object it will remove or pop last value
new.pop()
print(new)
# and if we want to remove specfic vaue than we have pass index value
new.pop(2)
print(new)
# exrend fun is use to add multiple values
new.extend([23,45,6,'hamza'])
print(new)
# clear function is use to clear the list
new.clear()
print(new)
#again add values to empty list

new.extend([1,23,45,6])
print(new)
# we can also some more fun on list
min(new)
max(new)
sum(new)
# we can directly sort the list
new.sort()
print(new)
print(len(new))

# we can also perform math operation  on value which are not string but string can be multiply to an int

print(new[0]/new[1])

print(new[0]+new[1])
print(new[0]-new[1])
print(new[0]*new[1])



