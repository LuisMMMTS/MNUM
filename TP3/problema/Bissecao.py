#bisseção
import math

def funcao(x):
    return (math.pi*pow(x,2)*(9-x))/3-30

a=[1.9,2.5]

old=a.copy()
erro=pow(10,-5)
first=True
iteracao=0

while abs((abs(a[0]+a[1])/2)-(abs(old[0]+old[1])/2))>erro or first:
    first=False
    old=a.copy()
    if funcao(a[0])*funcao((a[1]+a[0])/2)<0:
        a[1]=(a[1]+a[0])/2

    else:
        a[0]=(a[1]+a[0])/2
    iteracao+=1
    print(a)

print(iteracao)
        
    
