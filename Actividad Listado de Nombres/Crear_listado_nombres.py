lista= []
on = True

def menu():
  print('Desea seguir añadiendo nombres?')
  print('1. Si')
  print('2. No')

while on == True:
  print('Añada nombres a la lista.')
  lista.append(input('Nombre:'))
  menu()
  pick = int(input('Selecciona una opcion: '))
  if pick == 1:
    on = True
  elif pick == 2:
    on = False
  else:
    print('Inserte una opcion valida.')
    pick = int(input('Selecciona una opcion: '))
print('Gracias por agregar a la lista')
print(lista)