
# swaping 2 variable
a=12
b=5
# swaping
temp=a
a=b
b=temp
print(a)
print(b)

#in this case a third variable is wasting to over come this problem there is another solution

a=a+b
b=a-b
a=a-b
print(a)
print(b)

#even in this solution there is we are wasting a bit so to overcome this we use this solution
a=a^b
b=a^b
a=a^b
print(a)
print(b)

#that are some diffcult methid but in python there is very simple way to do
a,b=b,a
print(a)
print(b)
