
# set is like list
et = {1,1.2,3,4,5,5}
print(et)
# add fun to add single vlaue
et.add(45)
print(et)
# remove fun to remove values
et.remove(45)
print(et)
# update fun to add new multiple value to existing set
et.update([56,76,8])
print(et)
# to add values from an other set
s1={54,43}
et.update(s1)
print(et)

# discard fun is like remove fun but in remove fun it dispaly error if we give a wrong value but in discard it will run
et.discard(766)
print(et)

#now performing the all function of math related to set
# let's assume 3 set

s1={1,2,3}
s2={2,3,4}
s3={3,4,5}

# intersection fun

s4 = s1.intersection(s2)
print(s4)

# we take intersection with many sets

s4=s1.intersection(s2,s3)
print(s4)

# difference fun
s4=s1.difference(s2)
print(s4)

#we can take many set in function
s4=s1.difference(s2,s3)
print(s4)

# symetric differnce

s4=s1.symmetric_difference(s2)
print(s4)











