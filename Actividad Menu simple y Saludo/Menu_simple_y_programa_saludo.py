def mimenu():
  print("1. Saludar")
  print("2. Salir")
  print("Ingresa su opcion y pulsa salir")
opcion=0
while opcion != 2:
  mimenu()
  opcion=int(input(''))
  if opcion == 1:
    nombre=input('Dame tu nombre: ')
    print('Hola,', nombre)
print('Cerrando Programa')
