# Tarea 52: Estructuras de datos

Los ejercicios se ejecutan en Python, sin necesidad de cargar ningún tipo de librería adicional. 

### Ejercicio 1: 

Se solicita crear una lista de números ingresador por el usuario, y que acabe de solicitar una vez ingresado el 0, sin incluir éste en la lista.
Una vez finalizado el ingreso de números:
  - Se solicita un número al usuario y se elimina su primera ocurrencia
  - Se recorre la lista para imprimir el sumatorio
  - Se solicita un número y se genera una lista a partir de los valores menores al ingresado por el usuario y se imprime esta nueva lista
  - Se crea una lista de tuplas compuesta por el número y su número de ocurrencias

Para este ejercicio se utiliza la estructura de datos LISTA, ya que su ejecución en las actividades inserción y eliminación es de O(1), es decir, constante independientemente del número de datos.
En los casos en los que implica recorrer todos los datos, será O(n).

### Ejercicio 2:

Se solicita al usuario que ingrese los nombres de pila de los alumnos de primaria y luego los nombres de pila de los alumnos de secundaria. En ambos casos, se finaliza una vez ingresado "?x?"
Se debe:
  - Informar de los nombres de los alumnos de primaria y secundaria, sin repeticiones
  - Informar de los nombres que se repiten entre ambos cursos
  - Informar de los nombres de primaria que no se repiten en secundaria.

Se selecciona la estructura de datos CONJUNTO, que nos permite utilizar expresiones aritmeticas para extraer sumas de conjuntos, diferencias y similitudes entre ellos y que no permite elementos repetidos.

