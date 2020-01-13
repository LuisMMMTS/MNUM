# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 18:02:14 2019

@author: up201808912
"""

def f(x,y):
    return y**2-2*x*y-6*y+2*x**2+12

def gradiente_x(x,y):
    return -2*y+4*x
def gradiente_y(x,y):
    return 2*y-2*x-6


def gradiente(x,y,h,tolerancia):
    x_old,y_old=x+2*tolerancia,y+2*tolerancia  #dummy just so that it does not start on the beggining of the while
    while abs(x-x_old)>tolerancia and abs(y-y_old)>tolerancia:
        x_new=x-h*gradiente_x(x,y)
        y_new=y-h*gradiente_y(x,y)
        if f(x_new,y_new)>f(x,y):
            h=h/2
        else:
            h=2*h
            x_old,y_old=x,y
            x,y=x_new,y_new
    print((x,y))
    
    
    
    

    
    
    
x,y,h=1,1,1
tolerancia=10**-3

gradiente(x,y,h,tolerancia)