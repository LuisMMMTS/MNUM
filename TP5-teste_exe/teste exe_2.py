'''aplique picard-peano e newton para calcular 1zero da funcao. preencha a tambela c 3 casas decimais
picard peano x g(x) ninteracos
             #4 2.280  0
             2.280  1.866 1
             1.866  1.751  2
newton       x   f(x) f'(x) n_interacoes
             #4  10.800  7.000  0
             2.457  2.380  3.914  1
             1.849  0.370  2.698  2

considerando a solucao 1.70416 calcule erro absoluto e relativo da ultima iteracao
'''


def f(x):
    return x**2-x-1.2
def ff(x):
    return 2*x-1
def g(x):
    return pow(x+1.2,1/2)

def newton(x):
    precisao=False
    i=0
    while (i<=2):
        print("x",round(x,3),"f(x)",round(f(x),3),"f'(x)",round(ff(x),3), "itera",i)
        x=x-(f(x)/ff(x))
        i+=1
    return





def picard_peano(x):
    precisao=False
    i=0
    while (i<=2):
        print("x",round(x,3),"g(x)",round(g(x),3), "itera",i)
        x=g(x)
        i+=1
    return


newton(4)
picard_peano(4)
