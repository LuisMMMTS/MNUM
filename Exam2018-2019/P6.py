# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

def f(x):
    return ((x-2)**2)+x**4
B=(math.sqrt(5)-1)/2
A=B**2


x1=-10
x2=10
x3=(A*(x2-x1))+x1
x4=(B*(x2-x1))+x1

for i in range(20):
    if f(x3)<f(x4):
        x2=x4
        x4=x3
        x3=B*(x4-x1)+x1
    elif f(x4)<f(x3):
        x1=x3
        x3=x4
        x4=B*(x2-x3)+x3
print(x1,x2,x3,x4)