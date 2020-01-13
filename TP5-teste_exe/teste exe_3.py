"""sistema:
    x**2+xy-10=0
    y+3xy**2-57=0

resolver com x0=0.5 e y0=3.0
precisao absoluta 10**-4
solucao x=2 y=3
"""

def f1(x,y):
    return pow(x,2)+x*y-10
def f1_x(x,y):
    return 2*x+y
def f1_y(x,y):
    return x
def f2(x,y):
    return y+3*x*pow(y,2)-57
def f2_x(x,y):
    return 3*pow(y,2)
def f2_y(x,y):
    return 3*x*2*y

def newton(x,y):
    precisao=False
    i=0
    while not precisao:
        xn=x-(f1(x,y)*f2_y(x,y)-f2(x,y)*f1_y(x,y))/(f1_x(x,y)*f2_y(x,y)-f2_x(x,y)*f1_y(x,y))
        yn=y-(f2(x,y)*f1_x(x,y)-f1(x,y)*f2_x(x,y))/(f1_x(x,y)*f2_y(x,y)-f2_x(x,y)*f1_y(x,y))
        precisao=precisao_absoluta(x,y,xn,yn)
        x,y=xn,yn
        i+=1
    print(x,y,i)
    return

def g1(x,y):
    return pow(-x*y+10,1/2)
def g2(x,y):
    return pow((-y+57)/(3*x),1/2)

def picard_peano(x,y):
    precisao=False
    i=0
    while not precisao:
        xn=g1(x,y)
        yn=g2(x,y)
        precisao=precisao_absoluta(x,y,xn,yn)
        x,y=xn,yn
        i+=1
    print(x,y,i)
    return

def precisao_absoluta(x,y,xn,yn):
    erro=10**-4
    if abs(x-xn)<=erro and abs(y-yn)<=erro:
        return True
    return False

#newton(0.5,3)
picard_peano(2.915,3)

##neste caso o picard peano nao converge no g2 portanto não vai funcionar
