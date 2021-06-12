# for else
# to check the no is prime or not
x = int (input("enter no:"))

for i in range(2,x):
    if x%i == 0:
        print("Not prime")
        break   # if do't you break here it will print not prime for every satetement
else:
    print("prime")