# use of None value

class Nonevalue:

    def number(self,a = None , b  = None, c = None):
        sum=0
        if a!=None and b!=None and c!=None:
            sum = a+b+c
        elif a!=None and b!=None:
            sum = a+b
        else:
            sum = a
        return sum

object = Nonevalue()
print(object.number(1,2)) # it's works even we are passing 2 values but fun need 3

