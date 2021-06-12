# Exception Handling

# example
# two exapmle variable
a = 7
b = 0

# applying exception handling
try: # this will try the statement if error come it will throw to except below
    a = int(input("Enter your no :"))
    print(a/b)
    
    # here Exception can handle all type o errors
except Exception as object: # here object will store the error type  
    print("something went wrong with input....",object) # here message will display by object

# for handling the only one sepcial error
# example
except ValueError as e:
    print("value error for input is",e)



