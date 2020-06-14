frase = input('escribe una frase: ')
letra = input('¿Qué letra quieres contar?: ')

if letra == ' ':
    list = frase.split()
    if len(list) == 2:
        print('en esta frase hay', len(list) - 1, 'espacio')
    else:
        print('en esta frase hay', len(list) - 1, 'espacios')
else:
    list = frase.split(letra)
    print('en esta frase hay', len(list) - 1, letra, 's' )