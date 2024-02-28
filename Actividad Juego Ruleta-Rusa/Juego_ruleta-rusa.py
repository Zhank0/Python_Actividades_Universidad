import random

jugadores = []

#        0 1 2 3 4 5
balas = [1,0,0,0,0,0]

inscribir = True
posicionJugador = 0
posicionBala = 0

while inscribir == True:
  nombre = input('Inscribir el nombre del nuevo jugador: ')
  jugadores.append(nombre)

  opcion = input('Faltan más jugadores? S/N: ')

  if opcion == 'n':
    inscribir = False

print('**\n Que comience el juego.')

while len(jugadores) > 1:
  print('Es tu turno', jugadores[posicionJugador])
  input('Pulsa ENTER para Jugar')
  posicionBala = random.randint(0, len(balas)-1)

  if balas[posicionBala] == 0:
    print('\nClick!\n')
    del balas[posicionBala]
    posicionJugador = posicionJugador+1
    
  else:
    print('\nBANG!')
    print(jugadores[posicionJugador], 'a mimir...\n')
    del jugadores[posicionJugador]
    balas = [1,0,0,0,0,0]
    
  if posicionJugador >= len(jugadores):
    posicionJugador = 0
