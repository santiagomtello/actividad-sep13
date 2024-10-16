def datos():
    dia = int(input('Ingrese el día: '))
    mes = int(input('Ingrese el mes: '))
    año = int(input('Ingrese el año: '))
    if fechavalida(dia, mes, año):
        print('La fecha es válida')
    else:
        print('La fecha no es válida')

def bisiesto(año):
    return año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)

def fechavalida(dia, mes, año):
    if mes < 1 or mes > 12:
        return False
    if dia < 1:
        return False
    if mes in (1, 3, 5, 7, 8, 10, 12):
        return dia <= 31
    if mes in (4, 6, 9, 11): 
        return dia <= 30
    if mes == 2: 
        return dia  <= 29 if bisiesto(año) else dia <= 28
    return False

if  __name__ == '__main__':
    datos()