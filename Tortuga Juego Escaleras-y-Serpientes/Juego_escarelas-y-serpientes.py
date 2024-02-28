import turtle as tw
import random

posAct = 0
dado = 0
tortuga = tw.Turtle()
espacio = 33

def serpyesc():
  global posAct
  global espacio
  # Escaleras
  if posAct == 3:
    posAct = 60
    print('Subiste la Escalera y Llegaste a', posAct)
    
  elif posAct == 6:
    posAct = 47
    print('Subiste la Escalera y Llegaste a', posAct)
  elif posAct == 32:
    posAct = 53
    print('Subiste la Escalera y Llegaste a', posAct)
  elif posAct == 45:
    posAct = 86
    print('Subiste la Escalera y Llegaste a', posAct)
  elif posAct == 51:
    posAct = 94
    print('Subiste la Escalera y Llegaste a', posAct)
  elif posAct == 61:
    posAct = 83
    print('Subiste la Escalera y Llegaste a', posAct)
  # Serpientes
  elif posAct == 50:
    posAct = 13
    print('Caiste en una Serpiente y Llegaste a', posAct)
  elif posAct == 68:
    posAct = 55
    print('Caiste en una Serpiente y Llegaste a', posAct)
  elif posAct == 81:
    posAct = 16
    print('Caiste en una Serpiente y Llegaste a', posAct)
  elif posAct == 93:
    posAct = 43
    print('Caiste en una Serpiente y Llegaste a', posAct)
  elif posAct == 98:
    posAct = 36
    print('Caiste en una Serpiente y Llegaste a', posAct)

def movertortuga():
  global tortuga
  global posAct
  global espacio
  
  if posAct == 10 or posAct == 11 or posAct == 30 or posAct == 31 or posAct == 50 or posAct == 51 or posAct == 70 or posAct == 71 or posAct == 90 or posAct == 91:
    tortuga.left(90)
  
  elif posAct == 20 or posAct == 21 or posAct == 40 or posAct == 41 or posAct == 60 or posAct == 61 or posAct == 80 or posAct == 81 or posAct == 100:
    tortuga.right(90)

  
  tortuga.forward(espacio)
    
# configuramos el mundo de tortugas
tw.bgpic( "sye.png" )
screen = tw.Screen()
screen.setup( 350, 350 )
screen.title( "Serpientes y Escaleras" )

# creamos una tortuga
tortuga.shape( 'turtle' )
tortuga.setheading( 0 )
tortuga.speed( 4 )

# la preparamos para dibujar
tortuga.pensize( 6 )
tortuga.pencolor( "#FF0000" )
tortuga.setheading( 90 )

# dibujamos la solución
tortuga.penup()
tortuga.goto(-180,-150)
tortuga.right(90)

while posAct < 100:
  print('** NUEVO TURNO ** Casilla Actual: ', posAct)
  print('Pulsa ENTER para Lanzar el Dado')
  input()
  dado = random.randint(1,6)
  print('Avanzas', dado, 'casillas')
  posAct = posAct + dado
  serpyesc()

while dado > 0:
  
  dado = dado-1

  movertortuga()
  posAct = posAct+1
  
print('Ganaste!')
  