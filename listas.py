# #      -5 -4 -3  -2  -1
# lista=[10, 6, 20, 4, 16]
# #      0   1  2   3   4

# print(lista)
# print(lista[-5])
# print("-"*30)

# for i in lista:
#     print (i*2)

# lista.append(64)
# print("-"*30)

# for i in lista:
#     print (i)

# cree una lista de cuatro frutas 
# y muestrelas cada una

# frutas=["manzana", "naranja", "platano", "pera"]

# for f in frutas:
#     print (f)
# frutas.remove("pera")
# frutas.pop(3)
# print("-"*30)
# for f in frutas:
#     print (f)

pokemon=["Ekans", "Gastly"]
def mostrar():
     c=1
     for p in pokemon:
        print(c,".-", p)
        c+=1
     print("-"*30)

while True:
    try:
      print("1.- Agregar pokemon")
      print("2- Eliminar pokemon")
      print("3.- Actualizar pokemon")
      print("4.- Mostrar pokemon")
      print("5.- Salir")
      op=int(input("seleccione una opcion"))
      match op:
         case 1:
            pkm=input("Ingrese el el nuevo pokemon: ")
            pokemon.append(pkm)
         case 2:
            mostrar()
            # borrar_pokemon=input("Cual es el pokemon que vas a liberar?: ")
            # pokemon.remove(borrar_pokemon)
            borrar_pokemon=int(input("Cual es el pokemon que vas a liberar?: "))
            pokemon.pop(borrar_pokemon-1)

         case 3:
              mostrar()
              actualizar=int(input("Que pokemon desea actualizar: "))
              pokemon[actualizar-1]=input("cual sera el nombre nuevo?: ")
              print("Actualizado con exito")
         case 4:
            mostrar()
         case 5:
            print("Saliendo")
            break
         case _:
            print("Opcion invalida")


