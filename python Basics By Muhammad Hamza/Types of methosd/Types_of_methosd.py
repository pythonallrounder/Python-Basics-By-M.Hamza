# types of methods

class types_of_methods:

    # instance method
    # the method which use self

    def instance_method(self):
        print("this is instance method")
    
    # instance method
    # the method which use self
    @classmethod
    def class_method(cls):
        print("this is class method")

    # static method
    # the method which use no object

    @staticmethod
    def static_method():
        print("this is static method")

# creating objects

ob = ob = types_of_methods()
ob.instance_method()
ob.class_method()
ob.static_method()
