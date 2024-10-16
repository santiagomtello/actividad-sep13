def tabla():
    numero= int(input('ingrese un numero: '))
    multiplo=0
    for i in range(0,10):
        if numero>0:
            multiplo+=1
            print(numero*multiplo)

if __name__=='__main__':
    tabla()

