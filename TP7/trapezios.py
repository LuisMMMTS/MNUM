# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 17:51:10 2019

@author: up201808912
"""
import math

def f1(x):
    return math.sin(x)

def trapezios(x0,x,divisoes):
    area=0
    ponto=x0
    for h in range(0,divisoes):
        if h==0 or h==divisoes-1:
            area+=f1(ponto)
        else:
            area+=2*f1(ponto)
        ponto+=(x-x0)/divisoes
    return ((x-x0)/divisoes)/2*area

##lista=[4,8,16,32]
##for i in range(4):
    
##    print(trapezios(0,math.pi,lista[i]))

divisoes=8

s=trapezios(0,math.pi,divisoes)
print("s=",s)
s1=trapezios(0,math.pi,divisoes*2)
print("s1=",s1)
s2=trapezios(0,math.pi,divisoes*4)
print("s2=",s2)

print((s1-s)/(s2-s1))

##como com divisoes =2 quociente de convergencia estava proximo de 2, dupliquei-o e passei para divisoes=4 pois o resultado nao era fiáver
##com divisoes=4 tinhamos 3.75 no QC portanto voltei a diuplica-lo e QC passou a ser 3.93
#achei fair enough portanto p resultado obtido em s2 tem uma aproximação suficiente e pode ser considerado