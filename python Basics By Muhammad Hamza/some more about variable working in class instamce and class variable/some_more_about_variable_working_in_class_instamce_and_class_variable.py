# some more on variable

class test:
    s=10 # class variable
    
    def __init__(self): 
        self.name="hamza"  # instance variable
        self.age=23

    def update(self):
        self.name="ali"
        test.s=34 # changing the class vriable by class
        print(self.name,self.s)

ob=test()
ob1=test()
ob.name="afzzal" # we can change the value of object b/c it's independent on other
# calling from constructor
print("constructor values are with change value :")
print(ob.name)
print(ob1.name)
print()

print("updateing instance varable by fun")
# calling from function
ob.update()
print()

print("changing class avriable")
# chanikng classs variable
ob.s=98  # changing the calss variable value by onject
print(ob.s)
