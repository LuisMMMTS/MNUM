# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:21:41 2019

@author: up201808912
"""
import math



def f(x):
    return (2*x+1)**2-5*math.cos(10*x)


def regra_aurea_min(x1,x2,intervalo):
    B=(math.sqrt(5)-1)/2
    A=B**2
    while abs(x2-x1)>intervalo:
        x3=x1+A*(x2-x1)
        x4=x1+B*(x2-x1)
        if f(x3)>f(x4):
            x1=x3
        elif f(x3)<f(x4):
            x2=x4
        else:
            print("ERRROR")
            
    if f(x3)<f(x4):
        return x3
    else:
        return x4
    
def regra_aurea_max(x1,x2,intervalo):
    B=(math.sqrt(5)-1)/2
    A=B**2
    i=0
    while abs(x2-x1)>intervalo:
        i+=1
        x3=x1+A*(x2-x1)
        x4=x1+B*(x2-x1)
        if f(x3)<f(x4):
            x1=x3
        elif f(x3)>f(x4):
            x2=x4
        else:
            print("ERRROR")
            
    print(i)
    if f(x3)>f(x4):
        return x3
    else:
        return x4





intervalo=10**-3
x1=-1
x2=0

print(regra_aurea_min(x1,x2,intervalo))
print(regra_aurea_max(x1,x2,intervalo))


