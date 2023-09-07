#!/usr/bin/python3

def main():
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    _operators_ = ['+', '-', '*', '/']
    _func_operators_ = [add, sub, mul, div]

    if len(argv) != 4:
        print("{}".format(
            'Usage: ./100-my_calculator.py <a> <operator> <b>'
            )), exit(1)

    if argv[2] not in _operators_:
        print("{}".format(
            'Unknown operator. Available operators: +, -, * and /'
        )), exit(1)

    print("{} {} {} = {}".format(
        argv[1],
        argv[2],
        argv[3],
        _func_operators_[_operators_.index(argv[2])](
            int(argv[1]), int(argv[3]))
    ))


if __name__ == "__main__":
    main()
