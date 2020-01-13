import math
def calculo_25anos(valor_inicial):
    for i in range(1,26):
        valor_inicial=valor_inicial*i-1
        print(valor_inicial)
    return valor_inicial

print(calculo_25anos(math.exp(1)-1))
