def crearSet(): #devuelve un set de nombre de alumnos
    alumnos = set()
    nombre = input("Introduzca el nombre de pila del alumno: ")
    while nombre != "?x?":
        alumnos.add(nombre)
        nombre = input("Introduzca el nombre de pila del siguiente alumno: ")
    return alumnos

print ("____ALUMNOS DE PRIMARIA____")
primaria = crearSet()

print("____ALUMNOS DE SECUNDARIA____")
secundaria = crearSet()

print("Los nombres de pila de los alumnos de primaria y secundaria son: ")

todosNombres = primaria | secundaria # Se genera la union de conjuntos para listar los nombres de pila de ambos cursos, sin repeticiones

for elemento in todosNombres:
    print(elemento)

print("Los nombres que se repiten entre ambos cursos son: ")

repetidos = primaria & secundaria # Genero set con la interseccion de conjuntos

for elemento in repetidos:
    print(elemento)

print("Los nombres de pila existentes en primaria que no están en secundaria son: ")

soloPrimaria = primaria - secundaria # Genero set con diferencia de conjuntos

for elemento in soloPrimaria:
    print(elemento)


