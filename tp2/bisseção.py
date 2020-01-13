import math

def funcao(x):
    return x-2*math.log(x)-5


def bisseção(start):
    erro=10**-3
    old=-10000000 #random number
    start_round=True

    while True:
        midpoint=(2+0.05)/2
        if funcao(start[0]) * funcao(midpoint)<=0:
            if abs(midpoint-start[1])<=erro and not start_round:
                print(old)
                break
            start[1]=midpoint
        else:
            if abs(midpoint-start[0])<=erro and not start_round:
                print(old)
                break
            start[0]=midpoint
        old=midpoint
        start_round=False
    return

bisseção([0.05,2])
bisseção([8,10])
