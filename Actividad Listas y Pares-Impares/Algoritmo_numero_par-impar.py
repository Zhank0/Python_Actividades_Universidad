# Crear un algoritmo que pueda ingresar 20 numeros del 1 al 100 e indentificar si el numero ingresado es par o impar, ademas de contar la cantidad de numeros pares o impares ingresados, si el numero esta fuera del rango avisar por medio de mensaje

lista = []
poslista = 0
pares = 0
impares = 0

while len(lista) < 20:
  numero = int(input('Ingrese un numero desde el 1 al 100: '))
  if numero > 100 or numero == 0 or numero < 1:
    print('El numero ingresado esta fuera de rango')
    print('Intentelo nuevamente')
    
  lista.append(numero)

while poslista < 20:
  if (lista[poslista] % 2) == 0:
    print(f'El numero {lista[poslista]} es Par')
    pares = pares+1
    poslista = poslista+1
  else: 
    print(f'El numero {lista[poslista]} es Impar')
    impares = impares+1
    poslista = poslista+1

print(f'En total hay {pares} numeros pares, y {impares} numeros impares')