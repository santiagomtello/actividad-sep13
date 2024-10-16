sumanumero=0
def promedio():
    global sumanumero
    Nnumeros=0
    numero=0
    while Nnumeros>=0:   
        numero=int(input('digite un numero: '))
        if numero <0:
            break
        Nnumeros+=1  

        sumanumero= sumanumero+numero
        numero=numero-numero
        print('para cerrar el ciclo, digite un numero negativo')

    prom=sumanumero/Nnumeros
    return prom
    

if __name__=='__main__':
    print(promedio())


