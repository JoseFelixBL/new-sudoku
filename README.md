# Sudoku

Programa en python para resolver sudokus

## Notas para SUDOKU
13/08/2020, 17:25

### Representación lo primero
Primero ver cómo represento el SUDOKU completo.

Opciones:
1. Al comienzo pensé en una lista de 2 dimensiones:
    sudoku[0:9][0:9]

Pero las funciones para comprobar las posibillidades e ir encontrando soluciones se hacían complicadas.

2. Mejor crear un diccionario de conjuntos sudoku[fc] = set(...) ya que las operaciones de comapración y eliminación de posibilidades se hacen con métodos built-in de la clase set(). Además dicen que son muy rápidas.

### Anotaciones a lápiz
Si una celda del sudoku tiene un único elemento, entonces he encontrado la solución a esa celda.

Si tiene más de un elemento, entonces está "escrita a lápiz"

Al comienzo usaba un dict para las celdas descubierta y otro dict para las celdas a lápiz, pero era engorroso, mejor tener un sólo sudoku/dict con las posibilidades.

### Actualización de celdas - by object reference call semantics
Hay que tener cuidado de usar los métodos adecuados para actualizar el sudoku ya que de otra forma se pierde el valor encontrado.

Lo que se pasa a la función es la referencia del objeto, si dentro de la función creamos otro objeto, dicho objeto vivirá únicamente dentro de la función.

Usar los métodos de set que tienen "update", los que NO crean un shallow copy.

### Formas de resolución

Para resolverlo:
1- Fuerza bruta: recursivo
2- programar reglas:
2.1- buscar posiciones obvias: una sóla posibilidad en:
2.1.1- fila
2.1.2- columna
2.1.3- cuadro 3x3
2.2- Eliminar de las celdas escritas a lápiz los números encontrados en fila/columna/cuadrado.
...
