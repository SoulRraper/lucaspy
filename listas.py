#      -5 -4  -3 -2 -1
# lista=[10, 6, 20, 4, 16]
#      0   1  2   3  4

# print(lista)
# print(lista[-5])
# print("-"*30)

# for i in lista:
#     print(i)

# lista.append(64)
# print("-"*30)
# for i in lista:
#     print(i)


# Cree una lista de 4 frutas 
# y muestrelas cada una

# frutas=["Uva", "Pera", "Mango", "Higo"]

# for f in frutas:
#     print(f)
# # frutas.remove("Pera")  
# frutas.pop(3) 
# print("-"*30)
# for f in frutas:
#     print(f)

pokemons=["Ekans", "Gastly"]
def mostrar():
    c=1
    for p in pokemons:
        print(c,".-", p)
        c+=1
    print("-"*30)
def eliminar():
    mostrar()
    # borrar_pokemon=input("Cual es el pokemon que va a liberar ?: ")
    # pokemons.remove(borrar_pokemon)
    borrar_pokemon=int(input("Cual es el pokemon que va a liberar ?: "))
    pokemons.pop(borrar_pokemon-1)
def actualizar():
    mostrar()
    actualizar=int(input("que pokemon desea actualizar: "))
    pokemons[actualizar-1]=input("cual sera el nombre nuevo?: ")
    print("actualizado con exito")
def agregar():
    pkm=input("Ingrese el nuevo pokemon: ")
    pokemons.append(pkm)
def menuPokemon():
    while True:
        try:
            print("1.- Agregar Pokemon")
            print("2.- Eliminar Pokemon")
            print("3.- Actualizar Pokemon")
            print("4.- Mostrar Pokemons")
            print("5.- Salir")
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
                    print("Saliendo")
                    break
                case _:
                    print("Opcion Invalida")

        except ValueError as e:
            print("Solo numeros enteros. Error",e)

menuPokemon()