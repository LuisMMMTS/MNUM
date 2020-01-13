def f(x,y):
    return x**2+y**2

def y1(x,y):
    return h*f(x,y)

def y2(x,y):
    return h*f(x+(h/2),y+(y1(x,y)/2))

def y3(x,y):
    return h*f(x+(h/2),y+(y2(x,y)/2))

def y4(x,y):
    return h*f(x+h,y+y3(x,y))

try:
    h=int(input())
except:
    h=float(input())
def runge_kutta(x,y):
    y_fin=y+(1/6)*y1(x,y)+(1/3)*y2(x,y)+(1/3)*y3(x,y)+(1/6)*y4(x,y)
    x_fin=x+h
    print(y_fin)
    return (y_fin)
x=1
y=1
while x<1.4:
    y=runge_kutta(x,y)
    x+=h
    
