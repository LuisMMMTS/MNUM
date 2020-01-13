# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def X1(x2,x3):
    return (7-x2-x3)/3

def X2(x1,x3):
    return (4-x1-2*x3)/4

def X3(x1,x2):
    return (5-2*x2)/5


x1,x2,x3=0,0,0
erro=10**-3


def seidel(x1,x2,x3):
    iterações=0
    print("seidel")
    while(True):
        iterações+=1
        x1old,x2old,x3old=x1,x2,x3
        x1=X1(x2,x3)
        x2=X2(x1,x3)
        x3=X3(x1,x2)
        print("i=",iterações)
        print (x1,x2,x3)
        if abs(x1-x1old)<=erro and abs(x2-x2old)<=erro and abs(x3-x3old)<=erro:
            break
        
def jacobi(x1,x2,x3):
    iterações=0
    print("jacobi")
    while(True):
        iterações+=1
        x1old,x2old,x3old=x1,x2,x3
        x1=X1(x2,x3)
        x2=X2(x1old,x3old)
        x3=X3(x1old,x2old)
        print("i=",iterações)
        print (x1,x2,x3)
        if abs(x1-x1old)<=erro and abs(x2-x2old)<=erro and abs(x3-x3old)<=erro:
            break
        
seidel(x1,x2,x3)
jacobi(x1,x2,x3)