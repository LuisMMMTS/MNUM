#corda

def funcao(x):
    return (x**10)-1

a=[0,1.5]
old=a.copy()
erro=pow(10,-5)
first=True
iteracao=0

while ((abs(a[0]+a[1])/2)-(abs(old[0]+old[1])/2))>erro or first:
    first=False
    old=a.copy()
    new_x=(a[0]*funcao(a[1])-a[1]*funcao(a[0]))/(funcao(a[1])-funcao(a[0]))

    if funcao(a[0])*funcao(new_x)<0:
        a[1]=new_x
    else:
        a[0]=new_x

    iteracao+=1
    print(a)
print(iteracao)
