flurbos = 1
clpflurbos = 450
clp = 0
flurboscomp = 0
pick = 0
recaudadoenclp = 0
recaudadoenflurb = 0
ventas = 0
system = True

def menu():
  global pick
  print('Que desea hacer?')
  print('1. Comprar Flurbos')
  print('2. Visualizar ventas del dia')
  pick = int(input())

def menuexit():
  global pick
  if pick == 1:
    print('Desea realizar otra accion?')
    print('1. Si')
    print('2. No')
    pick = int(input())
  else:
    print()

while system == True:
  menu()
  if pick == 1:
    print('(450 CLP = 1 Flurbo)')
    print('Cuantos pesos deseas gastar?')
    clp = int(input())
    flurboscomp = (clp*flurbos)/clpflurbos
    ventas = ventas+1
    recaudadoenclp = recaudadoenclp+clp
    recaudadoenflurb = recaudadoenflurb+flurboscomp
    print(f'La transaccion fue exitosa, compraste {flurboscomp:.2f} flurbos.')
    
  elif pick == 2:
    print(f'Las ventas del dia en CLP: {recaudadoenclp:.2f}')
    print(f'Las ventas del dia en Flurbos: {recaudadoenflurb:.2f}')
    print('Y el total de ventas del dia fue de: ', ventas)
    system = False
    
  menuexit()  
  if pick == 1:
    system = True
  else:
    system = False
print('Gracias por usar nuestros servicios.')
  
    