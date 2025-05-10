try:
    a=int(input("Enter your number"))
    b=int(input("Enter a 2 number"))
    print(a+b)
except ValueError:
    print(ValueError)