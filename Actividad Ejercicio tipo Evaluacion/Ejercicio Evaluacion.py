import random
ingresos = 0
numsims = 0
equipoa = 0
equipob = 0
equipoc = 0
aingresos = []
bingresos = []
cingresos = []
atarea = 0
btarea = 0
ctarea = 0
tareas = ['Recopilacion Requerimientos','Planificacion y Desarrollo de Software','Venta y Publicidad del Software']
tmin = 300000
tmid = 700000
tmax = 1000000
power = True
pick = 0
test = 0
cantsim = 0

def menu():
  global pick
  print('1. Nueva Simulacion')
  print('2. Modificar Nombre de Tareas')
  print('3. Modificar Valores condicionales de Tareas')
  print('4. Imprimir todos los ingresos del Equipo A')
  print('5. Imprimir todos los ingresos del Equipo B')
  print('6. Imprimir todos los ingresos del Equipo C')
  print('7. Imprimir Total Presupuesto de los Equipos')
  print('8. Imprimir las tareas de cada Equipo')
  print('9. Cerrar Programa')
  pick = int(input('Selecciona: '))

while power == True:
  menu()
  if pick == 1:
    cantsim = int(input('Cuantas simulaciones desea realizar?: '))
    while cantsim != test:
      ingresos = random.randint(100000,500000)
      if ingresos >= 100000 and ingresos < 250000:
        aingresos.append(ingresos)
        equipoa = equipoa+ingresos
        test = test+1
      elif ingresos > 250000 and ingresos < 400000:
        bingresos.append(ingresos)
        equipob = equipob+ingresos
        test = test+1
      elif ingresos >= 400000:
        cingresos.append(ingresos)
        equipoc = equipoc+ingresos
        test = test+1
  elif pick == 2:
    opt = 0
    print('Qué nombre deseas modificar?')
    print(f'1. {tareas[0]}')
    print(f'2. {tareas[1]}')
    print(f'3. {tareas[2]}')
    opt = int(input())
    if opt == 1:
      tareas[0] = str(input('Ingrese un nuevo nombre de tarea: '))
    elif opt == 2:
      tareas[1] = str(input('Ingrese un nuevo nombre de tarea: '))
    elif opt == 3:
      tareas[2] = str(input('Ingrese un nuevo nombre de tarea: '))
    else:
      print('Ingresa una opcion valida.')
      opt = int(input())
  elif pick == 3:
    opt = 0
    print('Qué valores desea modificar?')
    print(f'1. {tmin}')
    print(f'2. {tmid}')
    print(f'3. {tmax}')
    opt = int(input())
    if opt == 1:
      tmin = int(input('Ingrese un nuevo valor: '))
    elif opt == 2:
      tmid = int(input('Ingrese un nuevo valor: '))
    elif opt == 3:
      tmax = int(input('Ingrese un nuevo valor: '))
    else:
      print('Ingrese una opcion valida.')
      opt = int(input())
  elif pick == 4:
    print('Todos los ingresos del Equipo A son los siguientes:')
    print(aingresos)
  elif pick == 5:
    print('Todos los ingresos del Equipo B son los siguientes:')
    print(bingresos)
  elif pick == 6:
    print('Todos los ingresos del Equipo C son los siguientes:')
    print(cingresos)
  elif pick == 7:
    print('El Total de Presupuesto de los Equipos son los siguientes: ')
    print(f'Equipo A: {equipoa}')
    print(f'Equipo B: {equipob}')
    print(f'Equipo C: {equipoc}')
  elif pick == 8:
    atarea = 0
    btarea = 0
    ctarea = 0
    if equipoa > tmin and equipoa < tmid:
      atarea = tareas[:1] 
    elif equipoa > tmid and equipoa < tmax:
      atarea = tareas[:2]
    elif equipoa > tmax:
      atarea = tareas[:3]
    
    if equipob > tmin and equipob < tmid:
      btarea = tareas[:1] 
    elif equipob > tmid and equipob < tmax:
      btarea = tareas[:2]
    elif equipob > tmax:
      btarea = tareas[:3]
    
    if equipoc > tmin and equipoc < tmid:
      ctarea = tareas[:1] 
    elif equipoc > tmid and equipoc < tmax:
      ctarea = tareas[:2]
    elif equipoc > tmax:
      ctarea = tareas[:3]
    print('Las tareas de cada equipo son las siguientes')
    print(f'Equipo A: {atarea}')
    print(f'Equipo B: {btarea}')
    print(f'Equipo C: {ctarea}')
  elif pick == 9:
    power = False
    print('Gracias por usar nuestros servicios.')
  else:
    print('Selecciona una opcion correcta.')