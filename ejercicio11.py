def valorluz():
    mesdeconsumo=str(input('ingrese el mes a cobrar: '))
    valorkw=float(input('cuanto vale el kw en pesos: '))
    totalconsumo=int(input(f'cuantos kw consumio en {mesdeconsumo}: '))

    costoluz=(valorkw*totalconsumo)
    return print(f'el valor del recibo de del mes de {mesdeconsumo} es de {costoluz} pesos')
    
if __name__=='__main__':
    valorluz()