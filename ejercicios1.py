def mayoria():
    edad=int(input('ingrese su edad: '))
    if edad >= 18:
        print ('usted es mayor de edad')
    else:
        print('usted es menor de edad')

    return mayoria

if __name__=='__main__':
    mayoria()