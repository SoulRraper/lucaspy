## crear un gestor de pacientes

pacientes=[
  {"nombre": " Aquiles Baeza", "prevision": "Fonasa", 
   "temperatura": 34.6, "grave": False}   
]

'''crear el gestor de pacientes em un centro medico
Para poner el nombre se debe validar que no este vacio
y ademas tenga mas de 8 caracteres
Para la prevision de salud solo existen 3 posibilidades valores
Fonasa, Isapre, o Fonasa
Al ingresar un paciente, se debe poner la temperatura
Crear una funcion que valide si esta grave o no
Para que este grave debe tener mas de 39°'''

def agregar():
    Nombre=input("Nombre")
    if len(Nombre) ==0 or len(Nombre) <8:
        print("Nombre invalido, debe tener mas de 8 caracteres en su nombre")
        return

def es_grave(temperatura):
    return temperatura > 39


def mostrar():
    for p, z in .items():
      print(f"{p}.- {z['nombre']} - {z['precio']}")
    for num, prod in .items():
         print(f"{}.- {['nombre']}  ${['precio']}")
    print("-"*30)

def


