# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 18:36:59 2019

@author: up201808912
"""
def determinante():
    return 4

def quadratica(x,y,h,tolerancia):
    x_old,y_old=x+2*tolerancia, y+2*tolerancia
    i=0
    while abs(x-x_old)>tolerancia and abs(y-y_old)>tolerancia:
        i+=1
        x_old,y_old=x,y
        x_new=x-1/determinante()*(-2*y+4*x)
        y=y-1/determinante()*(2*y-2*x-6)
        x=x_new
    print((x,y,i))
    
quadratica(1,1,1,10**-3)