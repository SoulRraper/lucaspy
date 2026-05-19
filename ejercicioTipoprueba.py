print("REGISTRO DE JUEGOS")

while True:
    try:
        numJuegos=int(input("cuantos juegos son: "))
        break
    except:
        print("Error, pon un numero")
        numJuegos=0

indie=0
estudio=0
e=0
a12=0
m=0

for i in range(numJuegos):
    print("njuegoss",i+1)

    nombreJuego=input("Nombre:").upper()

try:
    precio=int(input("Precio: "))
except:
    print("Precio invalido se pondra 0")
    precio=0

if 20000<precio<40000:
    indie+=1
    print("Es indice")
elif precio>=40000:
    estudio+=1
    print("Es estudio")
else:
    print("No clasifica")

clasificacion=input("Clasificacion E, +12, M:").upper()
if clasificacion=="E":
    e+=1
if clasificacion=="+12":
    a12+=1
if clasificacion=="M":
    m+=1

print("RESUMEN")
print("Indies:", indie)
print("Estudio:", estudio)
print("E:",e, "+12:",a12, "M:",m)

