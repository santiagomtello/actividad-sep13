"""

"""

def valid():
    longA=int(input('digite el valor del lado A: '))
    longB=int(input('digite el valor del lado B: '))
    longC=int(input('digite el valor del lado C: '))
    if (longA + longB) > longC and (longA+longC)>longB and (longB+longC)>longA:
        print('su triangulo es valido')
    else:
        print('su triangulo no es valido')
    

if __name__=='__main__':
    valid()