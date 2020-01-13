import math

def funcao(x):
    return x-2*math.log(x)-5

def corda(old):
    #old=[0.05,2]
    start=old
    erro=10**-3
    start_round=True


    while True:
        x=(funcao(start[0])*start[1]-funcao(start[1])*start[0])/(funcao(start[0])-funcao(start[1]))
        if funcao(start[0])*funcao(x)<=0:
            if abs(old[1]-start[1])<=erro and not start_round:
                print(old)
                #print(start)
                break
            old[1]=start[1]
            start[1]=x
        else:
            if abs(old[0]-start[0])<=erro and not start_round:
                print(old)
                #print(start)
                break
            old[0]=start[0]
            start[0]=x

        start_round=False
    return

corda([0.05,2])
corda([8,10])

        
