# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 18:38:15 2019

@author: up201808912
"""

def gauss_sidel(x,y,z,i):
    for j in range (i):
        x=(y-2*z+20)/4
        y=(25-x-2*z)/8
        z=(-10-3*x+y)/5
    print ("x:",x)
    print ("y:",y)
    print ("z:",z)
    

def gauss_jacobi(x,y,z,i):
    for j in range (i):
        x_new=(y-2*z+20)/4
        y_new=(25-x-2*z)/8
        z_new=(-10-3*x+y)/5
        x,y,z=x_new,y_new,z_new
    print ("x:",x)
    print ("y:",y)
    print ("z:",z)
    
x,y,z=0,0,0


gauss_jacobi(x,y,z,5)
gauss_sidel(x,y,z,5)