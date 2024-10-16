def lista():
    num=int(input('ingrese un numero: '))
    lim=int(1)
    while lim!=num>0:
        print(num)
        num-=1
    if num >= 1:
        return num

if __name__=='__main__':
    print (lista())