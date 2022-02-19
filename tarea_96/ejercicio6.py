"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir."""

asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

aprobados = list()

for asignatura in asignaturas:
    nota = int(input("Que nota has sacado en " + asignatura + "? "))
    if nota >= 5:
        aprobados.append(asignatura)

for aprobado in aprobados:
    asignaturas.remove(aprobado)

for asignatura in asignaturas:
    print("Tienes que repetir la asignatura " + asignatura)
