# Funcion
# basic Example
def sample(a):
    print(a)
sample(4)
print()

# adding two no , and returning two values 
def add(a1,a2): # here parameters are called formal argument
    b=a1+a2
    c=a1-a2
    return b,c
x,x2 = add(1,2) # here parameters are called actual argument which are (1,2)
print("addition is:",x,"    :Subtraction is : ",x2)
print()

# function to update value
def update(a):
    print(a)
a=10 # there is no effect of change on the a in fun
print("Value of a by fun is :",end="")
update(8)
print("Value of a by without fun is :",a)

# let's check the change on imutable data type

def list(li):
    li[1]='hamza'   #this shows that it's effect the outside the function 
    print(li)
Li=[1,2,3,4,5]
print("Value of List by fun is :",end="")
list(Li)
print("Value of list by without fun is :",end="")
print(Li)
print()

# Position
print("Example for Position")
def position(Name,age):
    print("Name is :",Name)
    print("Age is :",age)
position(34,"hamza") #due to wrong positon name in fun will get the integer value and age will get the hamza as string 
print()

# keyword = solution to problem of position
print("Example for keyword")
def keyword(Name,age):
    print("Name is :",Name)
    print("Age is :",age)
# use of keywords
keyword(age=34,Name='hamza')
print()

# Default
print("Example for Default")
def Default(Name,age=19): # here age have default value 19
    print("Name is :",Name)
    print("Age is :",age)
# use of keywords
Default(Name='hamza') # here we are not giving age but it will take default value from formal arguments
print()

# Lenth_variable
# how to control unlimited actual element
print("Example for Lenght_variable")
def Lenth_variable(*b): # here b as tuple
    print(b) 
# use of keywords
Lenth_variable(34,4,65,98)
print()

# problem in lenght variable as position
# solution as use of keyword
print("solution for problem in tuple knowing excat values")
def person(**b):
    for i,j in b.items():
        print(i,j)
person(name='hamza',age=24,jan='arooj',mob=1234567)
