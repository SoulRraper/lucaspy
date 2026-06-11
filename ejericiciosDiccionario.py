# pokemons={
#     1:{"nombre":"Ekans", "nivel": 19 },
#     2:{"nombre":"Gastly", "nivel": 18 },
#     3:{"nombre":"Eevee", "nivel": 12 }
# } 
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

# menuPokemon()

# print(list(pokemons.keys())[-1]+1)

# productos={
#     1:{"nombre":"Uva", "precio": 2000 },
#     2:{"nombre":"Palta", "precio": 4000 },
#     3:{"nombre":"Pera", "precio": 1500 }
# } 
# carrito=[]

# def AgregarProducto():
#     pds=input("Ingrese el nombre del producto: ")
#     pre=input("Ingrese el precio del producto: ")
#     productos[list(productos.keys())[-1]+1]={"nombre":pds, "precio": pre }

# def EliminarProducto():
#     MostarProducto()
#     borrar_producto=int(input("Cual es el producto que va a eliminar ?: "))
#     del productos[borrar_producto]

# def ActualizarProducto():
#     MostarProducto()
#     actualizar=int(input("que pokemon desea actualizar: "))
#     nombre=input("Ingrese el nombre del pokémon: ")
#     pre=input("Ingrese el nivel del pokémon: ")
#     productos[actualizar]={"nombre":nombre, "precio": pre }
#     print("actualizado con exito")

# def MostarProducto():
#     for p, z in productos.items():
#         print(f"{p}.- {z} ")
#     print("-"*30)

# def ComprarProductos():
# carrito=[]

# producto={1:{"nombre":"Uva", "precio": 2000 },
#         2:{"nombre":"Palta", "precio": 4000 },
#         3:{"nombre":"Pera", "precio": 1500 }
#         }
        
# pro=int(input("Que producto llevaras?:"))
# carrito.append(productos[pro])



# def menuproductos():


# while True:
#     try:
#         print("1.- Agregar Producto")
#         print("2.- Eliminar Producto")
#         print("3.- Actualizar Producto")
#         print("4.- Mostrar Productos")
#         print("5.- Comprar Productos")
#         print("6.- Crear Boleta (calcula IVA) y Salir")
#         op=int(input("Seleccione una opcion: "))
#         match op:
#             case 1:
#                 AgregarProducto()
#             case 2:
#                 EliminarProducto()
#             case 3:
#                 ActualizarProducto()
#             case 4:
#                 MostarProducto()
#             case 5:
#                 ComprarProductos()
#             case 6:
#                 CrearBoleta(calcula IVA)ySalir()
#                 print("Saliendo")
#                 break
#             case _:
#                 print("Opcion Invalida")

#     except ValueError as e:
#         print("Solo numeros enteros. Error",e)


# SOLUCION

productos={
    1:{"nombre":"Uva", "precio": 2000 },
    2:{"nombre":"Palta", "precio": 4000 },
    3:{"nombre":"Pera", "precio": 1500 }
} 

# usar como ejemplo el menu CRUD de pokemon
# para hacerlo con  productos y relizar el
# menu a continuacion



print("1.- Agregar Producto")
print("2.- Eliminar Producto")
print("3.- Actualizar Producto")
print("4.- Mostrar Productos")
print("5.- Comprar Productos")
print("6.- Crear Boleta (calcula IVA) y Salir")
op=int(input("Seleccione una opcion: "))
op=int(input("Seleccione una opcion: "))

### SOLUCION

# menuProductos()

# print(list(productos.keys())[-1]+1)
# productos={
#     1:{"nombre":"Uva", "precio": 2000 },
#     2:{"nombre":"Palta", "precio": 4000 },
#     3:{"nombre":"Pera", "precio": 1500 }
# } 
carrito=[]
def mostrar():
    for num, prod in productos.items():
        print(f"{num}.- {prod['nombre']} ${prod['precio']}")
    print("-"*30)
def eliminar():
    mostrar()
    # borrar_pokemon=input("Cual es el pokemon que va a liberar ?: ")
    # pokemons.remove(borrar_pokemon)
    try:
        borrar_producto=int(input("Cual es el producto que va a eliminar ?: "))
        if borrar_producto in productos:
            del productos[borrar_producto]
        else:
            print("Producto no existe")
    except ValueError:
        print("Debe ingresar un número válido")
def actualizar():
    mostrar()
    try:
        key=int(input("que producto desea actualizar: "))
        if key in productos:
            nombre=input("Ingrese el nombre del producto: ")
            precio=int(input("Ingrese el precio del producto: "))
            productos[key]={"nombre":nombre, "precio": precio }
            print("actualizado con exito")
        else:
            print("Producto no existe")
    except ValueError:
        print("ID o precio inválido")
def agregar():
    nom=input("Ingrese el nombre del producto: ")
    try:
        pre=int(input("Ingrese el precio del producto: "))
    except ValueError:
        print("Precio inválido, usando 0")
        pre=0
    productos[list(productos.keys())[-1]+1]={"nombre":nom, "precio": pre }
def comprar():
    while True:
      mostrar()
      try:
        comprar=int(input("Cual producto desea comprar ? (para salir, ponga 0): "))
        if comprar==0:
            break
        if comprar in productos:
            print(f"Usted ha comprado {productos[comprar]['nombre']} por un valor de {productos[comprar]['precio']}")
            carrito.append(productos[comprar])
        else:
            print("Producto no existe")
      except ValueError:
        print("Debe ingresar un número válido")
def boleta():
    print("-"*30, "0", "-"*30)
    print("Bienvenido a Death Market")
    total=0
    for p in carrito:
        total+=int(p["precio"])
        print(p["nombre"], "---$", p["precio"])
    iva=total*0.19
    print(f"El total de su compra es {total} y el IVA es {iva}")
    print(f"El total a pagar es  {total+iva} ")
def menuProductos():
    while True:
        try:
            print("1.- Agregar Producto")
            print("2.- Eliminar Producto")
            print("3.- Actualizar Producto")
            print("4.- Mostrar Productos")
            print("5.- Comprar Productos")
            print("6.- Crear Boleta (calcula IVA) y Salir")
            op=int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    agregar()
                case 2:
                    eliminar()
                case 3:
                    actualizar()
                case 4:
                    mostrar()
                case 5:
                    comprar()
                case 6:
                    boleta()
                    break
                case _:
                    print("Opcion Invalida")

        except ValueError as e:
            print("Solo numeros enteros. Error",e)


menuProductos()