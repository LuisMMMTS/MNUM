# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 17:24:30 2019

@author: up201808912
"""
import math

def f(x):
    return math.sin(x)

a=0
b=math.pi
n=4 #8#16

h=(b-a)/(2*n)

def simpson(a,b,n,h):
    aa=a
    somatorio=0
    for i in range (n):
        somatorio+=(h/3)*(f(a)+4*f(a+h)+f(a+2*h))
        a+=2*h
    somatorio2=f(a)+f(b)
    for i in range(1,n+1):
        aa+=h
        if (n%2!=0):
            somatorio2+=4*f(aa)
        else:
            somatorio2+=2*f(aa)
        
    somatorio2*=(h/3)
    return (somatorio,somatorio2)

somatorios=[]
for n in [4,8,16]:
    h=(b-a)/(2*n)
    somatorios.append(simpson(a,b,n,h)[0])
print((somatorios[1]-somatorios[0])/(somatorios[2]-somatorios[1]))