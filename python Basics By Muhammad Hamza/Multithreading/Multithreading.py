# Multithreading
# importing 

from threading import *
from time import *

class hello(Thread): # by pasing thread class will work as thdread
    def run(self):
        for i in range(5):
            print("1st")
            sleep(0.2) # for switching
           


class hello2(Thread):
    def run(self):
        for i in range(5):
            print("2nd")
            sleep(0.2) # for switching
            

#creating objects
ob = hello()
ob1 = hello2()

ob.start()
sleep(.1)
ob1.start()

# for closing or waith till all threads 
ob.join() # wait for ending
ob1.join()

print()
print("bye")
