#Girar Dinero - Preguntar cuanto dinero va a retirar
#Leer por teclado (input)
#Validacion (Saldo > Giro)
#Opc 2 Depositar Dinero - 
#Sistema siempre debe indicar cuanto dinero hay en la cuenta
log = True
contracheck = True
saldo = 50000
pick = 0
retiro = 0
deposito = 0
test = 0
contraseña = str('lavacavaquera')
c = 0
intentos = 0

def menu():
  global pick
  global retiro
  print('Tiene de saldo: ', saldo)
  print('Desea hacer un giro o desea depositar?')
  print('1. Giro')
  print('2. Deposito')
  pick = int(input())

while contracheck == True and c != contraseña and intentos != 3:
    c = str(input('Ingrese la contraseña: '))
    if c == contraseña:
      print('Contraseña correcta!')
      intentos == 3
    elif c != contraseña and intentos < 2:
      print('Contraseña incorrecta! Intentelo nuevamente')
      intentos = intentos+1
    else:
      contracheck = False
      print('Contraseña incorrecta! Se te acabaron los intentos.')
      

while log == True and contracheck == True:
  menu()
  if pick == 1:
    print('Tiene de saldo: ', saldo)
    retiro = int(input('Cuanto desea girar? '))
    if saldo > retiro and retiro > 0 or saldo == retiro:
      saldo = saldo-retiro
      print('Tu giro fue exitoso.')
    elif retiro < 0 or retiro == 0:
      print('Intenta con un valor positivo')
    else:
      print('No tienes saldo suficiente para ese giro')
    
  if pick == 2:
    print('Tiene de saldo: ', saldo)
    deposito = int(input('Cuanto desea depositar? '))
    if saldo > deposito  and deposito > 0 or saldo == deposito:
      saldo = saldo+deposito
      print('Tu deposito fue exitoso')
    elif deposito < 0 or deposito == 0:
      print('Intenta con un valor positivo')
    else:
      print('No tienes saldo suficiente para ese deposito')
  print('Desea realizar otra transaccion? (1. Si | 2. No)')
  test = int(input())
  if test == 1:
    log == True
  else:
    log == False
 
print('Gracias por utilizar nuestros servicios.')