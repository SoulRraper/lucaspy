#uso y explicacion de diccionarios

alumno={
    "nombre": "agusto pino",
    "edad": 64,
    "nacionalidad": "chilena"

}

print(alumno)
print(alumno["nombre"])

alumno["Email"]="pino@gamil.com"
alumno["nacionalidad"]="peruana"
del alumno["edad"]
print(alumno)