# operator overloading
print("             ******Overloaded Functions*******")
print()
class Overloading:

    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    # creating the overload function for __add__() 
    def __add__(self,object):

        m1 = self.m1 + object.m1
        m2 = self.m2 + object.m2
        m3 = m1 + m2
        return m3
    

    # creating the overload function for __sub__() 
    def __sub__(self,object):

        m1 = self.m1 - object.m1
        m2 = self.m2 - object.m2
        m3 = m1 - m2
        return m3
    
    # creating the overload function for __sub__() 
    def __mul__(self,object):

        m1 = self.m1 * object.m1
        m2 = self.m2 * object.m2
        m3 = m1 * m2
        return m3
    
    # creating the overload function for __div__() 
    def __div__(self,object):

        m1 = self.m1 / object.m1
        m2 = self.m2 / object.m2
        m3 = m1 / m2
        return m3
    
    # creating the overload function for __lt__() 
    def __lt__(self,object):

        if self.m1 < object.m1 and self.m2 < object.m2:
            return True
        else:
            return False

    # creating the overload function for __gt__() 
    def __gt__(self,object):

        if self.m1 > object.m1 and self.m2 > object.m2:
            return True
        else:
            return False
    
    # creating the overload function for __ge__() 
    def __ge__(self,object):

        if self.m1 >= object.m1 and self.m2 >= object.m2:
            return True
        else:
            return False

    # creating the overload function __str__()
    def __str__(self):
        return self.m1,self.m2

# creating objects
ob = Overloading(7,5)
ob1 = Overloading(2,3)

print("Addition is ")
# calling the function __add__ automacticaly
add = ob + ob1
print(add)
print()

print("Sub is ")
# calling __sub__
sub = ob - ob1
print(sub)
print()

print("Mul is ")
# calling __mul__ 
mul = ob * ob1
print(mul)
print()

print("lt is ")
#calling __lt__
if ob < ob1:
    print("less than")
else:
    print("not less than")
print()

print("gt is ")
#calling __gt__
if ob > ob1:
    print("greater than")
else:
    print("not greater than")
print()

print("ge is ")
#calling __gt__
if ob >= ob1:
    print("greater and equal")
else:
    print("not gretaer nor equla")
print()

# can't print directly the objects to pritn we have to make __str__()
print("printing objects data ")
# calling the __str__
print(ob.__str__(),ob1.__str__())