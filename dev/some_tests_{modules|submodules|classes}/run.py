#!/usr/bin/env python3

import sys

from modules.submodule1 import module1, module2

if __name__ == "__main__":
    a = str(sys.argv[1])
    b = str(sys.argv[2])
    c = str(sys.argv[3])
    d = str(sys.argv[4])

    command = a+'.'+b+'("'+d+'").'+c+'()'

    #print(command)

    exec(command)