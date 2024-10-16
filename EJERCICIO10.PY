def datos():
    añoactual= 2024
    nombre=str(input('ingrese su nombre:'))
    telefono=int(input('ingrese su numero: '))
    añoingreso=int(input('ingrese el año en el que ingreso a la empresa: '))
    apellidos=str(input('ingrese sus apellidos: '))
    edad=int(input('ingrese su edad: '))
    

    print(f'su nombre es {nombre}{apellidos} y tienes {añoactual-añoingreso} años de antiguedad')

if __name__=='__main__':
    datos()