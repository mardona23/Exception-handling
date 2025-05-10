try:
    a=int(input("Enter your number"))
    b=int(input("Enter a second number"))
    print(a/b)
except ZeroDivisionError:
    print("number div by zero is not allowed")
except ValueError:
    print("Exception handling")
finally:
    print("thank you")