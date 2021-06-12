# Duck Typing
# creating class for different model of car with same function name but differen operstion

# class 1
class Honda:

    def feature(self):
        print("Modle : Latest")
        print("color : Black")
        print("power  : 3000 wts")

# class 2
class Oddi:

    def feature(self):
        print("Model : old")
        print("color : All")
        print("power  : 500 wts")

# class 3
class Farrari:

    def feature(self):
        print("Model : All")
        print("color : Red")
        print("power  : 4000 wts")

# creating final class
class car:
    def about(self,quality): # we can only access the feature function by passing the on=bject of the outer class 
        quality.feature()

print("feature of the named car in classes are")
# creating objects for outer class 
object = Honda() # here we can shift the outer class by chagning the class name just 

# creating objects for car class
object1 = car()
object1.about(object)