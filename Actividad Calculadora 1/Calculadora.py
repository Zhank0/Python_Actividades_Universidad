Continuar = True
while Continuar == True:
    a = int(input('Ingrese un valor: '))
    b = int(input('Ingrese otro valor: '))
    res = int(input('Desea sumar, restar, multiplicar o dividir? (1. Suma, 2. Resta, 3. Multiplicacion, 4. Division): '))
    if res == 1:
        suma = a + b
        print('El resultado de su suma: ', suma)
    elif res == 2:
        resta = a - b
        print('El resultado de su resta: ', resta)
    elif res == 3:
        mult = a * b
        print('El resultado de la multiplicacion: ', mult)
    elif res == 4:
        test = b
        if test == 0:
            print('No se puede realizar la division')
        else:
            div = a / b
            print('El resultado de la division es: ', div)
    op = int(input('Desea continuar? (1. Si, 2. No): '))
    if op == 1:
        Continuar = True
    else:
        Continuar = False
print('Gracias por Calcular')
