num = int(input("Enter a number: "))
if num <=1 or (num %2==0 or num %3==0 or num %5==0 or num %7==0):
    print("not a prime")
else:
    print("Prime")