# method overloading

# crerating class 
class Over:

    # creating sample method
    def sample(self):
        print("this is sample")

    def sample(self):
        print("this is overload")


ob = Over()
ob1 = Over()
ob.sample() # we can't overload b/c it call last one

# overriding

class A:

    def sample1(self):
        print("this sample1")

class B(A):

    def sample1(self):
        print("this is override")

object = B()
object.sample1()