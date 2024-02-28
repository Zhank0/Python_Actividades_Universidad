productos = {}
iniciar = {"usuario": "Admin", "password": "admin1234"}
bucle = True
fallido = 0
loginbuc = True


def menu():
    print(" ")
    print("""1) Agregar producto y cantidad
2) Modificar la cantidad de un producto
3) Cantidad de producto especifico
4) Eliminar producto
5) Mostrar productos y cantidades
6) Salir
  """)


while bucle:
    while loginbuc:
        try:
            login1 = input("Usuario: ")
            login2 = input("Contraseña: ")
        except:
            print("Algo ha salido mal, intenta otra vez")
            continue
        if login1 == iniciar["usuario"] and login2 == iniciar["password"]:
            loginbuc = False
        elif fallido >= 2:
            print("Te equivocaste demasiadas veces...")
            bucle = False
            loginbuc = False
            break
        else:
            fallido += 1
            print("Tienes 3 intentos, intento n°", fallido)
    if fallido >= 2:
        break
    else:
        menu()
        try:
            opc = int(input("Opcion: "))
        except:
            print(" ")
            print("Solo numeros!!")
            print(" ")
            continue
        if opc == 1:
            try:
                prod = input("Nombre Producto: ")
                cant = int(input("Cantidad producto: "))
            except:
                print(" ")
                print("Ponga algo valido!!")
                print(" ")
                continue
            if prod.upper() in productos:
                print(" ")
                print("Producto ya existe..")
                print(" ")
            elif cant < 0:
                print(" ")
                print("Cantidad invalida")
                print(" ")
            else:
                productos[prod.upper()] = cant
        elif opc == 2:
            try:
                prod = input("Nombre Producto a modificar: ")
                cant = int(input("Cantidad producto nueva: "))
            except ValueError:
                print(" ")
                print("Ponga algo valido!!")
                print(" ")
                continue
            if cant < 0:
                print(" ")
                print("Cantidad invalida")
                print(" ")
            elif prod.upper() in productos:
                productos[prod.upper()] = cant
            else:
                print(" ")
                print("El producto es inexistente.")
                print(" ")
        elif opc == 3:
            try:
                prod = input("Nombre Producto: ")
            except ValueError:
                print(" ")
                print("Ponga algo valido!!")
                print(" ")
                continue
            if prod.upper() in productos:
                print("Cantidad: ", productos[prod.upper()])
            else:
                print(" ")
                print("El producto es inexistente.")
                print(" ")
        elif opc == 4:
            try:
                prod = input("Nombre Producto: ")
            except ValueError:
                print(" ")
                print("Ponga algo valido!!")
                print(" ")
                continue
            if prod.upper() in productos:
                del (productos[prod.upper()])
            else:
                print(" ")
                print("El producto es inexistente.")
                print(" ")
        elif opc == 5:
            for x, y in productos.items():
                print(" ")
                print(x, ":", y)
        elif opc == 6:
            print("Adios...")
            break
        else:
            print("Elige una opcion valida..")
