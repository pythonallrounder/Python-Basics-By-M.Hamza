# comparing objects

class compare:
    def __init__(self):
        self.clas=15
        self.roll_no=56
    def comparing(self,ob):
        if self.clas==ob1.clas:
            print("Equal")
        else:
            print("not equal")
ob=compare()
ob1=compare()
ob.clas=13 # changing values

# calling comparing function
ob.comparing(ob1)

