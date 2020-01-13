#metodo da Tangente
import math

def f(x):
    return x-2*math.log(x)-5
def ff(x):
    return 1-(2/x)

xn=float(input())
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
