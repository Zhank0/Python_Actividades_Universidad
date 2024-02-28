#1  1  2  3  5  8  13 Pedir secuencia hasta el 7mo numero de un cualquiera

print('Secuencia de Fibonacci')
a = int(input('Ingresa un numero: '))
switch = True
while switch == True:
  d=a
  b=a+d
  print(d)
  c=b+d
  print(c)
  a=d
  b=a+c
  print(b)
  c=b
  d=b+a
  print(a)
  switch = False
print('Gracias por usar')