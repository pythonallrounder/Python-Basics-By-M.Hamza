# inner classes

# outer class
class outer:
    

    def out(self):
        print("outer")

    # inner class
    class inner:
        def inn(self):
            print("inner")

# creating objects
ob=outer()
# creating the objects for inner class 
ob1 = outer.inner()
# assectign the outer function out()
ob.out()

# asseccing the inner class function inn()
ob1.inn()

# one more way to access the inner class directly
ob.inner().inn()


