# Constructors in inheritance

# creating class A
class A:

    # creating constructor
    def __init__(self):
        print("this is from class A")

# creating the class B from inheritance
class B(A):
    pass

object = B() # Now it's accessing the constructor class A b/c it have not its own so due to inheritance iut call the class A constuctor

# for calling the constructor of like class B

print()
print("Calling the constructor for own class which is child")
class D:

    # creating constructor
    def __init__(self):
        print("this is from class D")

# creating the class B from inheritance
class C(D):

    # creating the class C comstructor
    def __init__(self):
        print("this is is from child class C")
# creating the objects for class C 
ob = C()
print()

#calling Both class Construcotr in one inherited class
print("calling Both class Construcotr in one inherited class")

class X:

    # creating constructor
    def __init__(self):
        print("this is from class X")

# creating the class B from inheritance
class Y(X):

    super(X)
    # creating the class C comstructor
    def __init__(self):
        super().__init__() # asseccing the constructor of class A also
        print("this is from class Y")   

# creating object for class Y
object1 = Y()

print()
# working of constructors in multiple leve; inheritence
print("working of constructors in multiple level inheritence")

class A1:

    # creating constructor
    def __init__(self):
        print("this is from class A1")

class A2:
    
    # creating constructor
    def __init__(self):
       
        print("this is from class A2")

class A3(A1,A2):

    # creating constructor
    def __init__(self):
        super().__init__() # will call according to MRO from A1 class
        print("this is from class A3")

object2 = A3() 