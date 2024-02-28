def menu():
  print()
  print('Desea sumar, restar, multiplicar o dividir?')
  print('1. Suma')
  print('2. Resta')
  print('3. Multiplicacion')
  print('4. Division')
  print('5. Cerrar programa')
  res = ingresarnum(False)
  while res < 1 or res > 5:
    print('Opcion no valida, intente nuevamente.')
    res = ingresarnum(False)
  return res


def ingresarnum(tipo):
  if tipo == True:
    print('Ingrese un valor entero')
    numingresado = int(input())
  else:
    print('Selecciona una opcion: ')
    numingresado = int(input())
  return numingresado

def ingresarnumNo0():
  numingresado = ingresarnum()
  while numingresado == 0:
    print('Debe ingresar un numero distinto a 0')
    numingresado = ingresarnum()

  return numingresado

def opsuma():
  a = ingresarnum(True)
  b = ingresarnum(True)
  suma = a+b
  print('La suma de ambos numeros es de: ', suma)

def opresta():
  a = ingresarnum(True)
  b = ingresarnum(True)
  resta = a-b
  print('La resta de ambos numeros es de: ', resta)

def opmult():
  a = ingresarnum(True)
  b = ingresarnum(True)
  mult = a*b
  print('La multiplicacion de ambos numeros es de: ', mult)

def opdiv():
  a = ingresarnum(True)
  b = ingresarnumNo0(True)
  div = a/b
  print('La division de ambos numeros es de: ', div)

res = 0
while res != 5:
  res = menu()
  if res == 1:
    print('Elegiste: Suma')
    opsuma()
  
  if res == 2:
    print('Elegiste: Resta')
    opresta()
  
  if res == 3:
    print('Elegiste: Multiplicacion')
    opmult()
    
  if res == 4:
    print('Elegiste: Division')
    opdiv()
    
print('Cerrando programa...')
