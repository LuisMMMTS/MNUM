matriz=[[7,2,0,24],[4,10,1,27],[5,-2,8,27]]

guessy=250
guessz=10
n=0
while n<40:
    x=((matriz[0][3]-matriz[0][1]*guessy-matriz[0][2]*guessz)/matriz[0][0])
    guessx=x
    y=((matriz[1][3]-matriz[1][0]*guessx-matriz[1][2]*guessz)/matriz[1][1])
    guessy=y
    z=((matriz[2][3]-matriz[2][0]*guessx-matriz[2][1]*guessy)/matriz[2][2])
    guessz=z
    n+=1

print(x,y,z)
