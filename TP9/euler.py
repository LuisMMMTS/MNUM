# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 17:34:05 2019

@author: up201808912
"""

#MÉTODO DE EULER
import matplotlib.pyplot as plt

def derivada(x,y):
    return x**2+y**2

xmin=0
xmax=1.4
h=0.1
x=0
y=0
xlist=[x]
ylist=[y]
def euler(x,y,xmin,xmax,h):
    for i in range(int((xmax-xmin)/h)+1):
        xnext=x+h
        y=y+h*derivada(x,y)
        print("x="+str(xnext))
        xlist.append(xnext)
        print("y="+str(y))
        ylist.append(y)
        x=xnext
    print ("numero de iterações="+str(i))
    return y

#plt.plot(xlist, ylist)
#plt.show()

S=euler(x,y,xmin,xmax,h)
SS=euler(x,y,xmin,xmax,h/2)
SSS=euler(x,y,xmin,xmax,h/4)
print(S,SS,SSS)

print("QC="+str((SS-S)/(SSS-SS)))

print("Erro="+str(SSS-SS))