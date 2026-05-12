a=input("Enter a string: ")
a=a.lower()
v={'a','e','i','o','u'}
sm =sum(1 for ch in a if ch in v)
print(sm)