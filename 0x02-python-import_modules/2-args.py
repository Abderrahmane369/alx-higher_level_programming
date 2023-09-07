#!/usr/bin/python3

def main():
    from sys import argv

    print("{} {}{}".format(
        len(argv) - 1,
        "argument" if len(argv) == 2 else "arguments",
        ":" if len(argv) - 1 else "."
        ))

    for _, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(
            _,
            arg
        ))


if __name__ == '__main__':
    main()
