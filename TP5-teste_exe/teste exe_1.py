'''considere a funçaõ 5x^2+6x-2
determine recorrendo aos metodos intervalares o nº de iteraçoes necessarias para calcular o zero em [-2,-1], utilizando diferentes criterios de precisao
precisao 10**-4
'''

def f(x):
    return 5*pow(x,2)+6*x-2

def bissecao(a,b):
    precisao=False
    i=0
    while not (precisao):
        i+=1
        m=(a+b)/2
        if f(a)*f(m)<0:
            new_a=a
            new_b=m
            precisao=erro_diferença_relativo(new_b,b)
        elif f(a)==0:
            return a
        elif f(b)==0:
            return b
        elif f(m)==0:
            return m
        else:
            new_a=m
            new_b=b
            precisao=erro_diferença_relativo(new_a,a)
        #precisao=erro_relativo(new_a,new_b)
        a,b=new_a,new_b
    return i,a,b

def corda(an,bn):
        precisao=False
        i=0
        while not(precisao):
            i+=1
            w =(an*f(bn) - bn*f(an))/(f(bn)-f(an))
            if f(an)*f(w)<0:
                an_1 = an
                bn_1 = w
                #precisao=erro_diferença_relativo(bn_1,bn)
            else:
                an_1 = w
                bn_1 = bn
                #precisao=erro_diferença_relativo(an_1,an)
            precisao=erro_absoluto(an_1,bn_1)
            an,bn=an_1,bn_1
        return i,an,bn

def erro_absoluto(a,b):
        if abs((a-b))<=10**-4:
            return True
        return False

def erro_relativo(a,b):
        if abs((a-b)/a)<=10**-4:
            return True
        return False
def erro_diferença(xn_1,xn):
        if abs((xn_1-xn))<=10**-4:
            return True
        return False
def erro_diferença_relativo(xn_1,xn):
        if abs((xn_1-xn)/xn_1)<=10**-4:
            return True
        return False

a,b=-2,-1
i,a,b=corda(a,b)
print('iteracoes: ',i,'\n','a_final: ',a,'\n','b_final: ',b)


'''bisseçao erro absoluto
iteracoes:  14 
 a_final:  -1.4718017578125 
 b_final:  -1.47174072265625'''

'''bisseção erro relativo
iteracoes:  13 
 a_final:  -1.4718017578125 
 b_final:  -1.4716796875'''

'''bisseçao erro diferença
iteracoes:  14 
 a_final:  -1.4718017578125 
 b_final:  -1.47174072265625'''

'''bissecao erro diferença relativo
iteracoes:  13 
 a_final:  -1.4718017578125 
 b_final:  -1.4716796875'''



'''corda erro absoluto
iteracoes:  25 
 a_final:  -1.4717797887081345 
 b_final:  -1.471779788708134'''
                                #estes dois não podem ser aplicados no método da corda
'''corda erro relativo
iteracoes:  25 
 a_final:  -1.4717797887081345 
 b_final:  -1.471779788708134'''

'''corda erro diferença
iteracoes:  7 
 a_final:  -2 
 b_final:  -1.471756025790234'''

'''corda erro diferença relativo
iteracoes:  7 
 a_final:  -2 
 b_final:  -1.471756025790234'''
