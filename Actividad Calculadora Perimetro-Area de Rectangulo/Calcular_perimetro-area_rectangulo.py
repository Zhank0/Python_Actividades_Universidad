power = True
largo = 0
ancho = 0
while power == True: 
  largo = int(input('Ingresa el largo: '))
  ancho = int(input('Ingresa el ancho: '))
  if type(largo) != int or type(ancho) != int:
    print('Ingrese solo numeros.')
  elif largo != 0 and ancho != 0:
    print(f'El perimetro de este rectangulo es de: {2*largo + 2*ancho}')
    print(f'Y el area de este rectangulo es de: {largo*ancho}')
  else:
    print('Adios.')
    power = False
   