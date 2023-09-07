#!/usr/bin/python3

def main():
    import hidden_4

    for _ in dir(hidden_4):
        if '__' not in _:
            print("{}".format(_))


if __name__ == '__main__':
    main()
