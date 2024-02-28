#1 usd -> 800 clp
#15 usd -> X

usd = 1
clpusd = 815.00
sol = 1
clpsol = 219.41
bol = 1
clpbol = 118.58
yen = 1
clpyen = 6.50
dinero = 0
conversion = 0
pick = 0

def menu():
  global pick
  print('Desea convertir de CLP a:')
  print('1. Usd')
  print('2. Soles')
  print('3. Bolivianos')
  print('4. Yenes')
  pick = int(input())

menu()
if pick == 1:
  dinero = int(input('Cuanto quieres convertir a USD?: '))
  conversion = (dinero*usd)/clpusd
  conversion = round(conversion,2)
  print(f'Serian {conversion:.2f} Dolares')
elif pick == 2:
  dinero = int(input('Cuanto quieres convertir a Soles?: '))
  conversion = (dinero*sol)/clpsol
  conversion = round(conversion,2)
  print(f'Serian {conversion:.2} Soles')
elif pick == 3:
  dinero = int(input('Cuanto quieres convertir a Bolivianos?: '))
  conversion = (dinero*bol)/clpbol
  conversion = round(conversion,2)
  print(f'Serian {conversion:.2f} Bolivianos')
elif pick == 4:
  dinero = int(input('Cuanto quieres convertir a Yenes?: '))
  conversion = (dinero*yen)/clpyen
  print(f'Serian {conversion:.2f} Yenes')
else:
  print()

print('Gracias por usar nuestros servicios.')
