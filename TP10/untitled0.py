# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:14:59 2019

@author: up201808912
"""

def f1(x,y,z):
    return z*y+x
def f2(x,y,z):
    return z*x+y

x,y,z=0,1,1
h=0.05
xn=0.5
def euler(x,y,z,h,xn):
    for i in range(int((xn-x)/h)):
        new_x=x+h
        new_y=y+h*f1(x,y,z)
        new_z=z+h*f2(x,y,z)
        x,y,z=new_x,new_y,new_z
        if x==0.1 or x>=0.49:
            print("x=",x,'\n',"y=",y,'\n',"z=",z)
    return y,z

def QC_euler(x,y,z,h,xn):
    return(((euler(x,y,z,h/2,xn)[0]-euler(x,y,z,h,xn)[0])/(euler(x,y,z,h/4,xn)[0]-euler(x,y,z,h/2,xn)[0])),((euler(x,y,z,h/2,xn)[1]-euler(x,y,z,h,xn)[1])/(euler(x,y,z,h/4,xn)[1]-euler(x,y,z,h/2,xn)[1])))

def erro_euler(x,y,z,h,xn):
    return euler(x,y,z,h/4,xn)-euler(x,y,z,h/2,xn)
"""
def rk2(x,y,z,h,xn):
    yy=f1(x,y,z)
    zz=f2(x,y,z)
    ym=f(x+h/2,y+h/2*yy)
    y=ym*h
   """ 
euler(x,y,z,h,xn)
print(QC_euler(x,y,z,h,xn))