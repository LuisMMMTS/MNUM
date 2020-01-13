# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 17:14:52 2019

@author: up201808912
"""

def fz(x,y,z):
    return -0.6*z-8*y
def fy(x,y,z):
    return z

def alfa1(h,x,y,z):
    return h*fy(x,y,z)
def alfa2(h,x,y,z):
    return h*fy(x+h/2,y+alfa1(h,x,y,z)/2,z+beta1(h,x,y,z)/2)
def alfa3(h,x,y,z):
    return h*fy(x+h/2,y+alfa2(h,x,y,z)/2,z+beta2(h,x,y,z)/2)
def alfa4(h,x,y,z):
    return h*fy(x+h,y+alfa3(h,x,y,z),z+beta3(h,x,y,z))

def beta1(h,x,y,z):
    return h*fz(x,y,z)
def beta2(h,x,y,z):
    return h*fz(x+h/2,y+alfa1(h,x,y,z)/2,z+beta1(h,x,y,z)/2)
def beta3(h,x,y,z):
    return h*fz(x+h/2,y+alfa2(h,x,y,z)/2,z+beta2(h,x,y,z)/2)
def beta4(h,x,y,z):
    return h*fz(x+h,y+alfa3(h,x,y,z),z+beta3(h,x,y,z))


def rk4(x,y,z,h,i):
    for j in range(i):
        variacao_y=alfa1(h,x,y,z)/6+alfa2(h,x,y,z)/3+alfa3(h,x,y,z)/3+alfa4(h,x,y,z)/6
        variacao_z=beta1(h,x,y,z)/6+beta2(h,x,y,z)/3+beta3(h,x,y,z)/3+beta4(h,x,y,z)/6
        x=x+h
        y=y+variacao_y
        z=z+variacao_z
        print(variacao_y)
        print(x)
        print(y)
        print(z)
        if j==i-1:
            return y
        
y=4
dy=0
h=0.1
z=0
i=5
rk4(0,y,z,h,i)

S=rk4(0,y,z,h,i)
SS=rk4(0,y,z,h/2,i*2)
SSS=rk4(0,y,z,h/4,i*4)
print("QC="+str((SS-S)/(SSS-SS)))

print("Erro="+str((SSS-SS)/15))