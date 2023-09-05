#!/usr/bin/python3
for _ in range(100):
    print("{:02}{}".format(_, ", " if _ != 99 else ""),
          end="" if _ != 99 else "\n")
