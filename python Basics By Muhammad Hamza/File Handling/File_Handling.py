#File Handling

"""print("this is file f")
# append the new data
f = open("earthquakes_small.csv",'a')
#f.write(" one")

# making file read able
f = open("earthquakes_small.csv",'r')
print(f.read())
print()"""

print("this is file f1")
# opening existing file
f1 = open("sampe.txt",'a')
# writing data
f1.write("love") # now every time we will run it will will add "love" to file every time

# making file read able
f1 = open("sampe.txt",'r')
print(f1.read())
print()


# we use  readline(also can pass no of chaaraters) to print one line

"""# coping the file
# first making file readable
f = open("sample",'r')
# creating the new empty file
n = open("new",'w')
for i in f:
    n.write(i)

n = open("new",'r')
print(n.read()) # currenty i don't know why it is not printing
print()"""

"""print ("image processing to run remove comment on line 38 and 46")
# image opening
f = open("c.png",'rb') # here rb is for read read binary
#print(f.read())

# coping the image
f1 = open("c1.png",'wb') # here wb us for write binary
for i in f:
    f1.write(i)

f1 = open("c1.png",'rb')
#print(f1.read())"""
