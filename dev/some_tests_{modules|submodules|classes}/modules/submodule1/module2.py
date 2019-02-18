#!/usr/bin/env python3

#Importing libraries

class class1:
    #Init
    def __init__(self,msg):
        self.msg = msg

    #Method 1:
    def method_1(self):
        print(self.msg+' By module 2, class 1 and method 1')

    #Method 2:
    def method_2(self):
        print(self.msg+' By module 2, class 1 and method 2')

class class2:
    #Init
    def __init__(self,msg):
        self.msg = msg

    #Method 1:
    def method_1(self):
        print(self.msg+' By module 2, class 2 and method 1')

    #Method 2:
    def method_2(self):
        print(self.msg+' By module 2, class 2 and method 2')