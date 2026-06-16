# pokemons={
#     1:{"nombre":"Ekans", "nivel": 19 },
#     2:{"nombre":"Gastly", "nivel": 18 },
#     3:{"nombre":"Golduck", "nivel": 52 },
#     4:{"nombre":"Eevee", "nivel": 12 }
# } 
# print(list(pokemons.keys())[-1]+1)
# # print(pokemons.values())
# # print(pokemons.items())
# print(pokemons.keys())
# print(pokemons.values())
# print(pokemons.items())
# # # list()
# # for num, pkm in pokemons.items():
# #     print(num, pkm)
# def mostrar():
#     for p, z in pokemons.items():
#         print(f"{p}.- {z} ")
#     print("-"*30)
# def eliminar():
#     mostrar()
#     # borrar_pokemon=input("Cual es el pokemon que va a liberar ?: ")
#     # pokemons.remove(borrar_pokemon)
#     borrar_pokemon=int(input("Cual es el pokemon que va a liberar ?: "))
#     del pokemons[borrar_pokemon]
# def actualizar():
#     mostrar()
#     actualizar=int(input("que pokemon desea actualizar: "))
#     nombre=input("Ingrese el nombre del pokémon: ")
#     nivel=input("Ingrese el nivel del pokémon: ")
#     pokemons[actualizar]={"nombre":nombre, "nivel": nivel }
#     print("actualizado con exito")
# def agregar():
#     pkm=input("Ingrese el nombre del pokemon: ")
#     nvl=input("Ingrese el nivel del pokemon: ")
#     pokemons[list(pokemons.keys())[-1]+1]={"nombre":pkm, "nivel": nvl }
# def menuPokemon():
#     while True:
#         try:
#             print("1.- Agregar Pokemon")
#             print("2.- Eliminar Pokemon")
#             print("3.- Actualizar Pokemon")
#             print("4.- Mostrar Pokemons")
#             print("5.- Salir")
#             op=int(input("Seleccione una opcion: "))
#             match op:
#                 case 1:
#                     agregar()
#                 case 2:
#                     eliminar()
#                 case 3:
#                     actualizar()
#                 case 4:
#                     mostrar()
#                 case 5:
#                     print("Saliendo")
#                     break
#                 case _:
#                     print("Opcion Invalida")

#         except ValueError as e:
#             print("Solo numeros enteros. Error",e)

# # menuPokemon()

# # print(list(pokemons.keys())[-1]+1)

# productos={
#     1:{"nombre":"Uva", "precio": 2000 },
#     2:{"nombre":"Palta", "precio": 4000 },
#     3:{"nombre":"Pera", "precio": 1500 }
# } 

# # usar como ejemplo el menu CRUD de pokemon
# # para hacerlo con  productos y relizar el
# # menu a continuacion


# '''
#             print("1.- Agregar Producto")
#             print("2.- Eliminar Producto")
#             print("3.- Actualizar Producto")
#             print("4.- Mostrar Productos")
#             print("5.- Comprar Productos")
#             print("6.- Crear Boleta (calcula IVA) y Salir")
#             op=int(input("Seleccione una opcion: "))'''

# ### SOLUCION

# # menuProductos()

# # print(list(productos.keys())[-1]+1)
# # productos={
# #     1:{"nombre":"Uva", "precio": 2000 },
# #     2:{"nombre":"Palta", "precio": 4000 },
# #     3:{"nombre":"Pera", "precio": 1500 }
# # } 
# carrito=[]
# def mostrar():
#     for p, z in productos.items():
#         print(f"{p}.- {z['nombre']} - {z['precio']}")
#     for num, prod in productos.items():
#         print(f"{num}.- {prod['nombre']}  ${prod['precio']}")
#     print("-"*30)
# def eliminar():
#     mostrar()
#     # borrar_pokemon=input("Cual es el pokemon que va a liberar ?: ")
#     # pokemons.remove(borrar_pokemon)
#     try:
#         borrar_producto=int(input("Cual es el producto que va a eliminar ?: "))
#         if borrar_producto in productos:
#             del productos[borrar_producto]
#         else:
#             print("Producto no existe")
#     except ValueError:
#         print("Debe ingresar un número válido")
# def actualizar():
#     mostrar()
#     try:
#         key=int(input("que producto desea actualizar: "))
#         if key in productos:
#             nombre=input("Ingrese el nombre del producto: ")
#             precio=int(input("Ingrese el precio del producto: "))
#             productos[key]={"nombre":nombre, "precio": precio }
#             print("actualizado con exito")
#         else:
#             print("Producto no existe")
#     except ValueError:
#         print("ID o precio inválido")
# def agregar():
#     pkm=input("Ingrese el nombre del producto: ")
#     try:
#         nvl=int(input("Ingrese el precio del producto: "))
#     except ValueError:
#         print("Precio inválido, usando 0")
#         nvl=0
#     productos[list(productos.keys())[-1]+1]={"nombre":pkm, "precio": nvl }
# def comprar():
#     mostrar()
#     try:
#         comprar=int(input("Cual producto desea comprar ?: "))
#         if comprar in productos:
#             print(f"Usted ha comprado {productos[comprar]['nombre']} por un valor de {productos[comprar]['precio']}")
#             carrito.append(productos[comprar])
#         else:
#             print("Producto no existe")
#     except ValueError:
#         print("Debe ingresar un número válido")
#     while True:
#         mostrar()
#         try:
#             comprar=int(input("Cual producto desea comprar ? ( para salir, ponga 0): "))
#             if comprar==0:
#                 break
#             if comprar in productos:
#                 print(f"Usted ha comprado {productos[comprar]['nombre']} por un valor de {productos[comprar]['precio']}")
#                 carrito.append(productos[comprar])
#             else:
#                 print("Producto no existe")
#         except ValueError:
#             print("Debe ingresar un número válido")
# def boleta():
#     total=0
#     print("-"*30, "0", "-"*30)
#     print("Bienvenido a minimarquet Lost Woods")
#     print("-"*30, "0", "-"*30)
#     for p in carrito:
#         try:
#             total+=int(p["precio"])
            
#         except (ValueError, TypeError):
#             print(f"Precio inválido para {p.get('nombre','?')}, contando como 0")
#         total+=int(p["precio"])
#         print(p["nombre"],"---$", p["precio"])
#     iva=total*0.19
#     print("-"*30, "0", "-"*30)
#     print(f"El total de su compra es {total} y el IVA es {iva}")
#     print(f"El total a pagar es  {total+iva} ")
#     print("Gracias por comprar en minimarquet Lost Woods")
#     print("-"*30, "0", "-"*30)
# def menuProductos():
#     while True:
#         try:
#             print("1.- Agregar Producto")
#             print("2.- Eliminar Producto")
#             print("3.- Actualizar Producto")
#             print("4.- Mostrar Productos")
#             print("5.- Comprar Productos")
#             print("6.- Crear Boleta (calcula IVA) y Salir")
#             op=int(input("Seleccione una opcion: "))
#             match op:
#                 case 1:
#                     agregar()
#                 case 2:
#                     eliminar()
#                 case 3:
#                     actualizar()
#                 case 4:
#                     mostrar()
#                 case 5:
#                     comprar()
#                 case 6:
#                     boleta()
#                     break
#                 case _:
#                     print("Opcion Invalida")

#         except ValueError as e:
#             print("Solo numeros enteros. Error",e)


# menuProductos()

##reto 1
# Cambiar el menu 5 para que sea recursivo
# Voy a seguir comprando hasta que el usuario 
# ponga  condicion para salir.
##Reto 2
# Hacer que la boleta parezca boleta
# que tenga un mensaje de bienvenida
# luego cada productos listado de esta menera
# Prod 1---$5000
# Prod 2---$1000
# Prod 3---$2000
# Prod 4---$6000
# los totales a pagar
# Fialmente un mensaje de cierre
########TAREA########
# Tomar el CRUD de diccionario que está en este archivo
# y manipurar un diccionaario creado por usted
# puede ser cartas pokemon, autos, peliculas, series,  etc.
# Presentarlo el dia martes en la clase para revisarlo
# con el profesor.

# cartas_yugioh={
#     1:{"nombre":"Mago oscuro", "atk": 19, "defend": 2100  },
#     2:{"nombre":"Drangon blanco de ojos azules", "atk": 3000, "defend": 2500 },
#     3:{"nombre":"Kuribo", "atc": 300, "defend": 200 },
#     4:{"nombre":"Dragon negro de ojos rojos", "atk": 2400, "defend": 2000 }
# } 
# print(list(cartas_yugioh.keys())[-1]+1)

# print(cartas_yugioh.keys())
# print(cartas_yugioh.values())
# print(cartas_yugioh.items())

# def mostrar():
#     for Y, H in cartas_yugioh.items():
#         print(f"{Y}.- {H} ")
#     print("-"*30)
# def eliminar():
#     mostrar()
 
#     borrar_cartas=int(input("Cual es la carta que vas a quitar de tu mazo ?: "))
#     del cartas_yugioh[borrar_cartas]
# def actualizar():
#     mostrar()
#     actualizar=int(input("que cartas desea actualizar en tu mazo: "))
#     nombre=input("Ingrese el nombre la carta: ")
#     atk=input("Ingrese el atk de la carta: ")
#     defend=input("Ingrese la defend de la carta: ")
#     cartas_yugioh[actualizar]={"nombre":nombre, "atc": atk, "defend": defend  }
#     print("actualizado con exito")
# def agregar():
#     cart=input("Ingrese el nombre de la carta: ")
#     atk=input("Ingrese el atk de la carta: ")
#     defend=input("Ingrese la defend de la carta: ")
#     cartas_yugioh[list(cartas_yugioh.keys())[-1]+1]={"nombre":cart, "atk": atk, "defend": defend }
# def menuCartasYugioh():
#     while True:
#         try:
#             print("1.- Agregar Carta")
#             print("2.- Eliminar Carta")
#             print("3.- Actualizar Carta")
#             print("4.- Mostrar Carta")
#             print("5.- Salir")
#             op=int(input("Seleccione una opcion: "))
#             match op:
#                 case 1:
#                     agregar()
#                 case 2:
#                     eliminar()
#                 case 3:
#                     actualizar()
#                 case 4:
#                     mostrar()
#                 case 5:
#                     print("Saliendo")
#                     break
#                 case _:
#                     print("Opcion Invalida")

#         except ValueError as e:
#             print("Solo numeros enteros. Error",e)

# menuCartasYugioh()



## crear un gestor de estacionamiento
# Un estacionamiento tiene 4 pisos
# y cada piso tiene 10 espacios
#  Preguntar cuando entra un vehiculo, que tipo de vheiculo es
# vehículo ligero 2000
# vehículo mediano 3000
# vehículo pesado 3500
# luego , acomodarlo en algun lugar de algun piso disponible.
# el menu dsebe tener las sigueintes alternativas
''' 1.- ingresar vehiculo
2.- contar ganancias
3.- contar vehiculos'''
# usa lista o diccionario segun le acomode mas


parking={
    1:[2000, 3500, 2000,2000, 3500, 2000,2000, 3500, 2000],
    2:[],
    3:[],
    4:[]
}

def ingresAuto():
    valor=0
    print("Ingresar vheiculo nuevo")
    tipo=int(input("Que tipo es?: \n1.-Ligero\n2.-Mediano\n3.-Pesado"))
    if tipo==1:
        valor=2000
    elif tipo==2:
        valor=3000
    elif tipo==3:
        valor=3500
    else:
        print("Vehiculo invalido")
    piso=int(input("EN que piso va?: "))
    if piso in [1,2,3,4] and valor>0 :
        if len(parking[piso])<10:
            parking[piso].append(valor)
            print("Agregado al piso", piso)
        else:
            print("Piso lleno")
    else:
        print("Piso no válido")
def calculaGanancias():
    totalGanancias=0
    print("Contando Ganancias")
    for piso in parking.values():
        totalGanancias+=sum(piso)
    print(f"El total recudado es {totalGanancias}")
def cuentAutos():
    totalAutos=0
    for piso in parking.values():
        totalAutos+=len(piso)
    print("El total de autos en el parking es:", totalAutos)
def muestrAutos():
    for h, t in parking.items():
        print(h, ".- ", t)

def parkingAutos():
    while True:
        try:
            print(''' 1.- ingresar vehiculo
                    2.- contar ganancias
                    3.- contar vehiculos
                    4.- Mostrar
                    5.- Salir''')
            op=int(input("Seleccione un a opcion: "))
            match op:
                case 1:
                    ingresAuto()
                case 2:
                    calculaGanancias()
                case 3:
                    cuentAutos()
                case 4:
                    muestrAutos()
                case 5:
                    print("Saliendo")
                    break
                case _:
                    print("Opción inválida")
        except Exception as e:
            print("Error:", e)

parkingAutos()