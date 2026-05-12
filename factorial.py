n=int(input("Enter a number: "))
num=n
fac=1
while num>0:
    fac=fac*num
    num = num -1
print(f"factorial of {n} is: {fac}")