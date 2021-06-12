# basic program of class

class test:
    def add(self,a,b):
        print("addition is :",a+b)

    def add1(self):
        print('bye')

object=test()
# one way to call
test.add1(object)
# second way to call
object.add(9,8)
    