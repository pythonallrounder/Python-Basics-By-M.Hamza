# all about input
x=input('Enetr x :')
y=input('Enter y :')
print(x+y)

# so here is issue values are as string we have convert to use it as other data type
x1=int(input('Enetr x1 :'))
y1=int(input('Enter y1 :'))
print(x1+y1)

# if we want to take input as single charater even we have have enetered string
# two method
a=input('Enter string :')
print(a[0])

b=input('Enter string1 :')[0]
print(b)

# for expression if we enterd directly it we take it as string and print same so for calculation we uue eval function
d=eval(input('Enter expresson :'))
print(d)
# without eval function
d=(input('Enter expresson :'))
print(d)





