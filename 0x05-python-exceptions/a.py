def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("")
    return x / y

try:
    result = divide(10, 0)
    print("Result:", result)
except ZeroDivisionError as e:
    print("Error:", e)
