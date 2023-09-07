#!/usr/bin/python3

def main():
    import hidden_4

    for _ in dir():
        if '__' in _:
            print("{}".format(_))


if __name__ == '__main__':
    main()
