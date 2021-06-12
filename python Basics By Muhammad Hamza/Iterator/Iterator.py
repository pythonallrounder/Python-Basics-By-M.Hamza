# iterator

# taking list as example

list = [1,2,'hamza','wow',6]

ob = iter(list)

print(ob.__next__())

# we can perform any operation on every single value
if ob.__next__() == 2:
    print("great")
print(ob.__next__())
print(ob.__next__())
print(ob.__next__())
print()

# creating the iterator for printing no
print("own created iterator is")
class Iterate:

    def __init__(self):
        self.no = 1

    def __iter__(self): # need this during working of for loop 
        return self

    def __next__(self):
        va = self.no
        if va < 11: # stoping condition of for loop
            self.no += 1
            return va
        else:
            raise StopIteration
            
object = Iterate()

for i in object:
    print(i)