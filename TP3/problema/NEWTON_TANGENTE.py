#metodo da Tangente
import math

def f(x):
    return (math.pi*pow(x,2)*(9-x))/3-30
def ff(x):
    return (2*math.pi*(9-x)*x-math.pi*pow(x,2))/3

xn=1.9
if ff(xn)==0:
    print("derivada 0")
    quit

erro=pow(10,-5)
old=xn+erro+1
first=True

while first or abs(xn-old)>=erro:
    first=False
    old=xn
    xn=xn-(f(xn)/ff(xn))
    print(xn)
