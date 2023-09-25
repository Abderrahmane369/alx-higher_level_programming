def divide(x, y):
    return x / y

try:
    result = divide(10, 0)
    print("Result:", result)
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed")
