log = True
saldo = 50000
pick = 0
retiro = 0
deposito = 0
test = 0
contraseña = str('lavacavaquera')
c = 0

def menu():
  global pick
  global retiro
  print('Tiene de saldo: ', saldo)
  print('Desea hacer un giro o desea depositar?')
  print('1. Giro')
  print('2. Deposito')
  pick = int(input())

def giroyretiro():
  global pick
  global saldo
  global retiro
  if pick == 1:
      print('Tiene de saldo: ', saldo)
      retiro = int(input('Cuanto desea girar? '))
      if saldo > retiro or saldo == retiro:
        saldo = saldo-retiro
        print('Tu giro fue exitoso.')
      else:
        print('No tienes saldo suficiente para ese giro')
    if pick == 2:
      print('Tiene de saldo: ', saldo)
      deposito = int(input('Cuanto desea depositar? '))
      if saldo > deposito or saldo == deposito:
        saldo = saldo-deposito
        print('Tu deposito fue exitoso')
      else:
        print('No tienes saldo suficiente para ese deposito')