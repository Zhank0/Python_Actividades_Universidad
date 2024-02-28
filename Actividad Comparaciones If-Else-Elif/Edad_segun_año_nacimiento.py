añonac = int(input('Ingresa tu año de nacimiento: '))
# añoact = int(input('Ingresa el presente año: '))

# print('Tu edad es aproximadamente: ' + str(añoact - añonac))

edad = 2022 - añonac

print('Tienes',edad, 'Años')

if edad < 14 or edad == 14:
  print('Eres un niñ@')
elif edad < 18 or edad == 18:
  print('Eres un adolescente')
elif edad < 55 or edad == 55:
  print('Eres un adulto')
elif edad < 99 or edad == 99:
  print('Eres un adulto mayor')
else:
  print('No existes, o deberias estar descansando en paz')