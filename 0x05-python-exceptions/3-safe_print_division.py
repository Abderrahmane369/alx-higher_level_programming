#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        c = a / b
    
    except Exception:
        pass
    
    finally:
        print("{}".format(c))
        
        return c

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))