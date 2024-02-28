import random

numero = int(input('Ingrese la cantidad de simulaciones: '))
contador = 0
while contador < numero :
  num = random.randint(0,100)
  if num % 2 == 0 :
    print(f'Simulacion numero {contador+1}: {num}. El numero es par')
    contador = contador+1
  else:
    print(f'Simulacion numero {contador+1}: {num}. El numero es impar')
    contador = contador+1