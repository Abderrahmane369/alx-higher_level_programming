#!/usr/bin/python3

def main():
    from sys import argv

    print("{}".format(sum(list(map(int, argv[1:])))))


if __name__ == '__main__':
    main()
