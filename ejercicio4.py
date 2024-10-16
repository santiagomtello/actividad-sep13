"""
verificar si una contraseña es valida
la contraseña es valida si cumple con 2 requisitos
1. tenga minimo 10 caracteres
2. tena como minimo una numero
"""

def valid():
    contraseña=str(input('ingrese una contraseña: '))
    numcaracter=len(contraseña)
    numcontraseña= bool(contraseña.isdigit)
    if numcaracter>=10 and numcontraseña:
        print('su contraseña es valida')
    else:
        print('su contraseña es invalida')

if __name__=='__main__':
    valid()