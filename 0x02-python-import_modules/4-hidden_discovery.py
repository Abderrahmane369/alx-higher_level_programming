#!/usr/bin/python3

def main():
    from hidden_4 import *
    
    for _ in dir():
        if '__' in _:
            print("{}".format(_))
    

if __name__ == '__main__':
    main()
