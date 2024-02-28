import random

puntc = 0
puntw = 0

def puntajejugador():
  global puntw
  puntw = puntw+1
  print('Metiste un gol!')

def puntajecpu():
  global puntc
  puntc = puntc+1
  print('Te atajaron el gol.')

def dirpelota():
  print('Di a que direccion le pegaras a la pelota')
  print('1. Izquierda')
  print('2. Centro')
  print('3. Derecha')
  direccion = int(input())
  if direccion < 1 or direccion > 3:
    print('ERROR')
    print('Ingresa una opcion valida')
    direccion = int(input())
  elif direccion == 1:
    print('Le vas a pegar hacia la izquierda')
  elif direccion == 2:
    print('Le vas a pegar hacia el centro')
  else:
    print('Le vas a pegar hacia la derecha')
  return direccion
  
turns = 0
while turns!=5:
  direccion = dirpelota()
  cpu = random.randint(1,3)
  if direccion != cpu:
    puntajejugador()
    turns = turns+1
  elif direccion == cpu:
    puntajecpu()
    turns = turns+1
if puntw > puntc:
  print('GANASTE')
elif puntw < puntc:
  print('GANO LA CPU')