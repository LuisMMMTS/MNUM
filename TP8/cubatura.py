# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 18:06:53 2019

@author: up201808912
"""
import math

def f(x,y):
    return math.sin(x+y)

def cubatura(x0,x1,y0,y1,hx,hy):
    somatorio=hx*hy/9
    for i in range(3):
        somatorio+=f(x0+i*hx,y0+i*hy)
    somatorio+=f(x0,y0+hy)
    somatorio+=f(x0+hx,y0)
    somatorio+=f(x0+hx,y0+2*hy)
    somatorio+=f(x0+2*hx,y0+hy)
    somatorio+=16*f(x0+hx,y0+hy)
    return somatorio

print(cubatura(0,math.pi,0))