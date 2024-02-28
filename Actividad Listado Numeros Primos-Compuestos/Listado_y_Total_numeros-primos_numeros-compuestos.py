inputnum = 1
power = True
primos = 0
numprim = []
compuestos = 0
numcomp = []
divisores = 0
eluno = 0

while power == True:
  print('Ingrese un numero del 1 al 100')
  print('-Ingresar 0 terminara e programa-')
  inputnum = int(input())
  if inputnum > 100:
    print('Ingrese un valor valido.')
  elif inputnum < 0:
    print('Ingrese un valor valido.')
  elif inputnum == 0:
    power = False
  elif inputnum == 1:
    eluno = eluno+1
  elif inputnum > 1 or inputnum <= 100:
    for n in range(1,inputnum+1):
      if inputnum % n == 0:
        divisores = divisores+1
      if divisores > 2:
        compuestos = compuestos+1
        numcomp.append(inputnum)
        print('Numero Compuesto')
      elif divisores == 2:
        primos = primos+1
        numprim.append(inputnum)
        print('Numero Primo')

print('Se mostrara el total de numeros primos e compuestos y un listado de los numeros ingresados de cada tipo')
print(f'Total numeros primos: {primos}')
print(f'Listado numeros primos: {numprim}')
print(f'Total numeros compuestos: {compuestos}')
print(f'Listado numeros compuestos: {numcomp}')
print(f'Cantidad de 1s: {eluno}')