# Inheritance

print("Single level inheritane")
# single level inheritance 
class A:

    def student1(self):
        print("this is student1 from class A")

    def student2(self):
        print("this is student2 from class A")

# creating a new class B and inheriting by passing A
class B(A):
    def student3(self):
        print("This is student3 from class B")

# creating Objects for class B
object3= B()
object3.student1() # aessing the methods from class A in class B

print()
print("Multi level inheritance")

# creating class F for multi level inheritance
class F(B):

    def student_F(self):
        print("this is student_F from class F ")

# creating object for class F 
object2 = F()
object2.student2() # accessing the methof of class A
object2.student3() # accessing the meyhod of class B also


print()
print("Multiple leveL nheritance")
# multiple level inheritance
# will use class A from above

class C:

    def student4(self):
        print("this is student4 from class C")

# creating class for multiple lavel inheritnace
class D(A,C):  # passing more than one is multiple level inheritance 

    def student5(self):
        print("this is student5 from class D")

object1 = D()
# acessing the method of class A and CLASS C by mulitple level inheritence
object1.student2() # calling from class A
object1.student4() # calling from class B
print()