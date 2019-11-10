def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("You cant divide by zero!!!")

print(divide(1, 0))