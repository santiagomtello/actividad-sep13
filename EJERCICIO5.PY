def continente():
    pais = str(input('ingrese el nombre del pais:'))
    if pais in ['argentina','usa','canada' 'brasil', 'chile', 'colombia', 'perú']:
        return 'América'
    elif pais in ['francia', 'alemania', 'españa','alemania', 'italia']:
        return 'Europa'
    elif pais in ['china', 'india', 'japón', 'corea']:
        return 'Asia'
    elif pais in ['áfrica del sur', 'nigeria', 'egipto']:
        return 'África'
    elif pais in ['australia', 'nueva zelanda']:
        return 'Oceanía'
    else:
        return 'No se pudo determinar el continente'


if __name__== '__main__':
    print(continente())