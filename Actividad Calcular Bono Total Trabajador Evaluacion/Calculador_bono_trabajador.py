# Nombre: Manuel Andres Arturo Rojas Araya

CantHijosMenores = 0
CantMayores = 0
CantAdultMayor = 0
BonoBase = 100000
BonoporMenor = 50000
BonoporMayor = 80000
BonoporAdultMayor = 30000
BonoRecibido = 0


NombreTrabajador = str(input('Introduzca su Nombre: '))
print('Cuantos hijos menores de edad tiene?')
CantHijosMenores = int(input())
print('Cuantas personas mayores de edad viven con usted? (Excluyendole)')
CantMayores = int(input())
print('De las personas mayor de edad, cuantos son Adulto Mayor? (65 Años o mas)')
CantAdultMayor = int(input())

BonoRecibido = BonoporMenor * CantHijosMenores
BonoRecibido = BonoRecibido+(BonoporMayor*CantMayores)

if CantMayores > CantAdultMayor or CantMayores == CantAdultMayor:
  BonoRecibido = BonoRecibido+(BonoporAdultMayor*CantAdultMayor)
elif CantMayores < CantAdultMayor:
  print('La cantidad de Adultos Mayores ingresada no es valida asi que no se aplicara el bono.')

BonoRecibido = BonoRecibido+BonoBase

print(NombreTrabajador)
print('Recibiras en total un bono de: ', BonoRecibido)