# mapping or dictonary
# creaating dictonary for the student data
student={'name':'Hamza','rollno':'56','class':'bsse'}
print(student)

# for checking that which are the keys in the dictionary
c=student.keys()
print(c)

# for checking that which are the values in the dictionary

c=student.values()
print(c)


# to get specific value in the the dic
c=student['rollno']
print(c)

# another method to do get values by passing keys
c=student.get('class')
print(c)

# if we pass wrong key get() will display none if we want our meesage than we do like
c=student.get('56','please enter valid key')
print(c)

#adding new value to the dictonary
student['paper']='math'
print(student)

# update function is use to add or update any key or value
student.update({'paper':'urdu','uni':'uos'})
print(student)

# to del keys

del student['uni']
print(student)

# usingg pop fun
student.pop('name')
print(student)

# to ckec len of the Dictionary
print(len(student))

# items fun will shows the values and keys in couple
print(student.items())

# accusing all keys by for loop

for ke in student:
           print(ke)

# setdefauult fun is also use to show values
print(student.setdefault('class'))








  

