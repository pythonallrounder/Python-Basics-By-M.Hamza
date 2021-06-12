# factorial

def fac(n):
    fa=1
    for i in range(1,n+1):
        fa=fa*i
    return fa
c=5
x=fac(c)
print(x)


# with recursion
def fre(n):
    if n==0:
        return 1
    return n*fre(n-1)
x=fre(5)
print("Result with recursion",x)