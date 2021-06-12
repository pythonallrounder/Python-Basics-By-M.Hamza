# Generator

# creating the function
def gen_iter():
     no = 1
     while no<=10: # using while loop b/c for loop directly call iterator
          yield no # will return the value every time
          no +=1


va = gen_iter()
for i in va:
    print(i)
