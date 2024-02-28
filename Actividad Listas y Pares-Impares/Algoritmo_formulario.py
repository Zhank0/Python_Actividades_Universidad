# Crea un algoritmo para un sistema que me permita llenar un formulario donde preguntan: Nombre, Apellido, Edad, Sexo (M-F), Fecha de Nacimiento (DD-MM-YYYY), Direccion (Calle - N° - Ciudad - Pais), Corre, Estado Civil y Nacionalidad, al final de la encuesta debe imprimirse cada opcion marcada y al final mostrar el siguiente mensaje 'Desea ingresar una nueva ficha: Ingresar (N) o Salir (S)'

on = True
lista = []


def cuestionario():
  print('Ingrese los siguientes datos para llenar el formulario: ')
  nombre = input('Ingrese su Nombre: ')
  apellido = input('Ingrese su Apellido: ')
  sexo = input('Ingresa tu Sexo (Masculino, Femenino): ')
  fnac = input('Ingresa tu Fecha de Nacimiento(DD-MM-YYYY): ')
  direc = input('Ingresa tu Direccion(Calle, N° Casa, Ciudad, Pais): ')
  correo = input('Ingresa tu Correo Electronico: ')
  estciv = input('Ingresa tu Estado Civil: ')
  nacionalidad = input('Ingresa tu Nacionalidad: ')
  lista.append(str(f'\n Nombre: {nombre}\n Apellido: {apellido}\n Sexo: {sexo}\n Fecha de Nacimiento: {fnac}\n Direccion: {direc}\n Correo Electronico: {correo}\n Estado Civil: {estciv}\n Nacionalidad: {nacionalidad}'))

while on == True:
  cuestionario()
  print('Desea ingresar una nueva ficha?')
  print('Ingresar una nueva ficha: N')
  print('Salir: S')
  opc = str(input())
  if opc == 'N' or opc == 'n':
    on = True
  elif opc == 'S' or opc == 's':
    on = False
  else:
    print('Opcion Invalida.')
    print('Intente nuevamente')
    opc = str(input())

poslista = 0
while len(lista) > poslista:
  print(lista[poslista])
  poslista = poslista+1