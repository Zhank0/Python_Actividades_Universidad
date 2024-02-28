nota1 = int(input('Ingrese una nota: '))*0.10
nota2 = int(input('Ingrese una nota: '))*0.30
nota3 = int(input('Ingrese una nota: '))*0.25
nota4 = int(input('Ingrese una nota: '))*0.10
nota5 = int(input('Ingrese una nota: '))*0.25

notafinal = nota1+nota2+nota3+nota4+nota5

notafinal = round(notafinal,2)

print('El promedio de las notas es: ', str(notafinal))

if notafinal > 40 or notafinal == 40:
  print('Aprobaste!')
else:
  print('Reprobaste')
