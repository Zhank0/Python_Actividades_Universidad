usd = 1 
clpusd = 815
dinero = 0
conversion = 0
registro = []
poslista = 0
on = True


def menu():
  print('Desea continuar usando el programa?')
  print('1. Si')
  print('2. No')

while on == True:
  dinero = int(input('Cuanto quieres convertir a USD?: '))
  conversion = (dinero*usd)/clpusd
  print(f'Serian {conversion:.2f} Dolares')
  
  registro.append(str(f'{dinero} CLP fue convertido a: {conversion:.2f} USD'))

  menu()
  pick = int(input())
  if pick == 1:
    on = True
  elif pick == 2:
    on = False
  else:
    print('Selecciona una opcion valida')
    pick = int(input())
    
print('Esta es el registro de las transacciones: ')
while len(registro) > poslista:
  print(registro[poslista])
  poslista = poslista+1  
