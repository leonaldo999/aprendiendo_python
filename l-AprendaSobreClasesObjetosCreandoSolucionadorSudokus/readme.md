# Aprenda sobre clases y objetos creando un solucionador de sudokus

Las clases y los objetos son conceptos importantes en programación. Estas herramientas de programación orientada a objetos ayudan a los desarrolladores a lograr la modularidad, la abstracción y la legibilidad del código. Además, promueven la reutilización.

En este proyecto de resolutor de Sudoku, aprenderás a utilizar clases y objetos para crear una cuadrícula de Sudoku y resolver un rompecabezas de Sudoku.

---

## Paso 1

En este proyecto, aprenderás sobre clases y objetos creando un solucionador de sudokus.

En Python, una clase es un modelo para crear objetos. Los objetos creados a partir de una clase son instancias de esa clase. Puedes crear una clase utilizando esta sintaxis:

- **Codigo Ejemplo**

  ```py
  class ClassName:
      pass
  ```

Donde `class` es la palabra clave necesaria para definir la clase y `ClassName` es el nombre de la clase, escrito según la convención en *PascalCase*.

Comience creando una clase `Board`

- **Codigo**

  ```py
  class Board:
      pass
  ```

---

## Paso 2

Se crea una nueva instancia de una clase utilizando la notación de función, que consiste en añadir un par de paréntesis al nombre de la clase.

> Fuera de la definición de la clase, cree una instancia de la clase `Board` y asígnela a una variable llamada `gameboard`.

- **Codigo**

  ```py
  class Board:
      pass
  
  gameboard = Board()
  ```

---

## Paso 3

La instanciación crea un objeto vacío. Pero las clases pueden tener métodos, que son como funciones locales para cada instancia. Dentro de una clase, los métodos se declaran de la siguiente manera:

- **Codigo Ejemplo**

  ```py
  class ClassName:
      def method_name():
          pass
  ```

> Dentro de la clase `Board`, reemplaza `pass` por un método vacío `spam`.

- **Codigo**

  ```py
  class Board:
      def spam():
          pass
  
  gameboard = Board()
  ```

---

## Paso 4

Para ser un método de instancia, un método requiere un parámetro especial, denominado `self` por convención. Este parámetro es una referencia a la instancia de la clase y siempre debe ser el primer parámetro.

> Agrega un parámetro `self` a tu método `spam`.

- **Codigo**

  ```py
  class Board:
      def spam(self):
          pass
  
  gameboard = Board()
  ```

---

## Paso 5

> Ahora, reemplaza `pass` por una llamada a `print` y pásale la cadena `'Spam!'`.

- **Codigo**

  ```py
  class Board:
      def spam(self):
          print('Spam!')
  
  gameboard = Board()
  ```

---

## Paso 6

Para llamar a un método de instancia, debe utilizar la notación de punto:

- **Codigo Ejemplo**

  ```py
  instance_name.method_name()
  ```

Donde `instance_name` es la instancia u objeto, y `method_name` es el método que desea llamar.

> Llame al método `spam` del objeto `gameboard`.

- **Codigo**

  ```py
  class Board:
      def spam(self):
          print('Spam!')
  
  gameboard = Board()
  gameboard.spam()
  ```

---

## Paso 7

> Ahora, elimine su llamada `spam`.

- **Codigo**

  ```py
  class Board:
      def spam(self):
          print('Spam!')
  
  gameboard = Board()
  ```

---

## Paso 8

La instanciación crea un objeto vacío. El método `__init__` es un método especial que permite instanciar un objeto en un estado personalizado. Cuando una clase implementa un método `__init__`, `__init__` se llama automáticamente al instanciar.

> Dentro de la clase `Board`, elimine el método `spam` y sustitúyalo por un método `__init__` que incluya un parámetro `self`.

- **Codigo**

  ```py
  class Board:
      def __init__(self):
  
  gameboard = Board()
  ```

---

## Paso 9

El sudoku que hay que resolver será una lista de listas, como la siguiente:

- **Codigo Ejemplo**

  ```py
  [
    [0, 0, 2, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 7, 6, 2],
    [4, 3, 0, 0, 0, 0, 8, 0, 0],
    [0, 5, 0, 0, 3, 0, 0, 9, 0],
    [0, 4, 0, 0, 0, 0, 0, 2, 6],
    [0, 0, 0, 4, 6, 7, 0, 0, 0],
    [0, 8, 6, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 5, 1, 9, 0, 0, 8],
    [1, 7, 0, 0, 0, 6, 0, 0, 5]
  ]
  ```

*Tenga en cuenta que las celdas vacías se rellenan con un cero.*

> Declare una variable `puzzle` y asígnele la lista de listas del ejemplo anterior.

- **Codigo**

  ```py
  class Board:
      def __init__(self):
          pass
  
  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]
  gameboard = Board()
  ```

---

## Paso 10

Volviendo al método `__init__`, requiere un parámetro adicional que represente el rompecabezas a resolver.

> Agregue un segundo parámetro llamado `board` al método `__init__`y corrija la instanciación del `gameboard` pasándole la lista de `puzzle` como si fuera un argumento a una llamada de función.

- **Codigo**

  ```py
  class Board:
      def __init__(self, board):
          pass
  
  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]
  gameboard = Board(puzzle)
  ```

---

## Paso 11

Un atributo es una variable asociada a un objeto, que se utiliza para almacenar datos como variables normales.

> Dentro del método `__init__`, asigne el parámetro `board` (que se pasa al crear una instancia de la clase `Board`) a un atributo de instancia `board` utilizando `self.board`.
>
> `self.board` hace referencia al atributo `board` de la instancia de la clase. Es una variable que pertenece al objeto creado a partir de la clase `Board`.

- **Codigo**

  ```py
  class Board:
      def __init__(self, board):
          self.board = board

  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]
  gameboard = Board(puzzle)
  ```

---

## Paso 12

También puede utilizar la notación de puntos para acceder a un atributo de instancia.

> Fuera de la clase `Board`, después de inicializar el objeto `gameboard`, utilice `gameboard.board` para acceder al atributo `board` de su objeto `gameboard` e imprima el resultado en la pantalla.

- **Codigo**

  ```py
  class Board:
      def __init__(self, board):
          self.board = board

  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]
  gameboard = Board(puzzle)
  print(gameboard.board)

  # -------Salida-------
  # [
  #     [0, 0, 2, 0, 0, 8, 0, 0, 0],
  #     [0, 0, 0, 0, 0, 3, 7, 6, 2],
  #     [4, 3, 0, 0, 0, 0, 8, 0, 0],
  #     [0, 5, 0, 0, 3, 0, 0, 9, 0],
  #     [0, 4, 0, 0, 0, 0, 0, 2, 6],
  #     [0, 0, 0, 4, 6, 7, 0, 0, 0],
  #     [0, 8, 6, 7, 0, 4, 0, 0, 0],
  #     [0, 0, 0, 5, 1, 9, 0, 0, 8],
  #     [1, 7, 0, 0, 0, 6, 0, 0, 5],
  # ]

---

## Paso 13

> Como puede ver, la placa se imprime en la pantalla. Ahora, elimine su llamada `print`.

- **Codigo**

  ```py
  class Board:
      def __init__(self, board):
          self.board = board

  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]
  gameboard = Board(puzzle)

  # -------Salida-------
  

---

## Paso 14

Ahora trabajarás en un método que encuentre las celdas vacías en el tablero de sudoku.

> Dentro de la clase `Board`, crea un método vacío llamado `find_empty_cell` y asígnale un parámetro `self`.

- **Codigo**

  ```py
  class Board:
      def __init__(self, board):
          self.board = board
      def find_empty_cell(self):
          pass

  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]
  gameboard = Board(puzzle)

  # -------Salida-------

---

## Paso 15

La función integrada `enumerate` toma un iterable como argumento y devuelve un objeto `enumerate` sobre el que se puede iterar. Proporciona el recuento (que por defecto comienza en cero) y el valor del iterable.

- **Codigo Ejemplo**

  ```py
  iterable = ['a', 'b', 'c']
  for i, j in enumerate(iterable):
      print(i, j)
  ```

El bucle del ejemplo anterior generaría las tuplas `0, a`, `1, b` y `2, c`.

> Dentro del método `find_empty_cell`, reemplaza `pass` por un bucle `for` que utilice la función `enumerate()` para iterar sobre cada fila del tablero de sudoku. Utiliza `row` como índice de la fila actual y `contents` para los elementos de la fila actual.

- **Codigo**

  ```py
  class Board:
      def __init__(self, board):
          self.board = board
  # ---Región editable por el usuario---
      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              pass
  # ---Región editable por el usuario---

  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]
  gameboard = Board(puzzle)

  # -------Salida-------

---

## Paso 16

Debes localizar la celda vacía, que está rellena con el número cero.

> Reemplaza `pass` por una variable `col` y asígnale una llamada a `.index()` en `contents`, pasando `0` como argumento.

- **Codigo**

  ```py
  class Board:
      def __init__(self, board):
          self.board = board
  # ---Región editable por el usuario---
      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              col = contents.index(0)
  # ---Región editable por el usuario---

  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]
  gameboard = Board(puzzle)

  # -------Salida-------

---

## Paso 17

El método `.index()` genera una excepción `ValueError` cuando no se encuentra el valor. Para evitar que el programa detenga la ejecución, anidará esta línea de código dentro de un bloque `try`. La instrucción `try` se utiliza para encapsular código que podría generar una excepción. La cláusula `except`, por otro lado, ofrece código alternativo para ejecutar si se produce una excepción:

- **Codigo Ejemplo**

  ```py
  try:
      <code>
  except:
      <code>
  ```

> Pon la asignación de `col` dentro de un bloque `try`. A continuación, crea una cláusula `except` y rellena su cuerpo con `pass`.

- **Codigo**

  ```py
  class Board:
      def __init__(self, board):
          self.board = board
  # ---Región editable por el usuario---
      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
              except:
                  pass
  # ---Región editable por el usuario---

  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]
  gameboard = Board(puzzle)

  # -------Salida-------

---

## Paso 18

Si se encuentra `0`, el método debe devolver inmediatamente una tupla que contenga el índice de fila y el índice de columna de la celda vacía.

> Dentro del bloque `try`, después de la asignación de `col`, devuelve `row, col`.

- **Codigo**

  ```py
  class Board:
      def __init__(self, board):
          self.board = board
  # ---Región editable por el usuario---
      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except:
                  pass
  # ---Región editable por el usuario---

  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]
  gameboard = Board(puzzle)

  # -------Salida-------

---

## Paso 19

Si el código dentro del bloque `try` genera una excepción, lo que quieres es que el programa continúe ejecutándose, y la instrucción `pass` lo consigue.

Aunque este código funciona, se considera una buena práctica especificar el tipo de excepción después de la palabra clave `except`.

> Como sabes que puede generarse un `ValueError`, deja un espacio después de la palabra clave `except` y añade `ValueError` a continuación.

- **Codigo**

  ```py
  class Board:
      def __init__(self, board):
          self.board = board
  # ---Región editable por el usuario---
      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
  # ---Región editable por el usuario---

  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]
  gameboard = Board(puzzle)

  # -------Salida-------

---

## Paso 20

> Fuera del bucle `for`, *return* `None`. Esto gestiona el caso en el que no se encuentra ninguna celda vacía, lo que indica que el tablero de sudoku está completamente lleno.

- **Codigo**

  ```py
  class Board:
      def __init__(self, board):
          self.board = board
  # ---Región editable por el usuario---
      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None
  # ---Región editable por el usuario---

  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]
  gameboard = Board(puzzle)

  # -------Salida-------

---

## Paso 21

> Comprueba que el método `find_empty_cell` funciona correctamente llamándolo en `gameboard` e imprimiendo el resultado.

**Nota** Ten en cuenta que, aunque `find_empty_cell` se define con un parámetro, no debes darle un valor pasando un argumento a la llamada a la función, ya que `self` se pasa automáticamente como el objeto en el que estás llamando al método.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]
  gameboard = Board(puzzle)
  
  # ---Región editable por el usuario---
  print(gameboard.find_empty_cell())
  # ---Región editable por el usuario---

  # -------Salida-------
  # (0, 0)

---

## Paso 22

`find_empty_cell` return (0, 0), que es la posición de la primera celda vacía en el tablero de sudoku.

> Cambia el primer `0` del `puzzle` por un `1`. Verás en el resultado que se encuentra la siguiente celda vacía.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

  # ---Región editable por el usuario---
  puzzle = [
      [1, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]
  # ---Región editable por el usuario---

  gameboard = Board(puzzle)
  print(gameboard.find_empty_cell())

  # -------Salida-------
  # (0, 1)

---

## Paso 23

> Ahora, cambie el `1` que modificó anteriormente por un `0` para restaurar la configuración original de la placa. A continuación, elimine la llamada `print`.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

  # ---Región editable por el usuario---
  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

  gameboard = Board(puzzle)
  # ---Región editable por el usuario---

  # -------Salida-------

---

## Paso 24

A continuación, vas a trabajar en un método que comprueba si un número dado se puede insertar en una fila específica del tablero de sudoku.

> Dentro de la clase `Board`, crea un método llamado `valid_in_row` y asígnale tres parámetros: `self`, `row` y `num`. Donde `self` representa la instancia de la clase, y `row` y `num` son el índice de la fila y el número que se va a comprobar, respectivamente.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

  # ---Región editable por el usuario---
      def valid_in_row(self, row, num):
          pass
  # ---Región editable por el usuario---
  
  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

  gameboard = Board(puzzle)

  # -------Salida-------

---

## Paso 25

> Reemplaza `pass` con una expresión que compruebe si el número `num` no está ya presente en esa fila.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

  # ---Región editable por el usuario---
      def valid_in_row(self, row, num):
          num not in self.board[row]
  # ---Región editable por el usuario---
  
  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

  gameboard = Board(puzzle)

  # -------Salida-------

---

## Paso 26

Si `num` no está en la fila, la expresión se evalúa como `True`, lo que significa que el número es válido para su inserción.

Si `num` está en la fila, la expresión se evalúa como `False` y la inserción infringiría las reglas.

> Añade la palabra clave `return` al principio de la expresión dentro del cuerpo del método `valid_in_row`, para que se pueda comprobar la validez del número.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

  # ---Región editable por el usuario---
      def valid_in_row(self, row, num):
          return num not in self.board[row]
  # ---Región editable por el usuario---
  
  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

  gameboard = Board(puzzle)

  # -------Salida-------

---

## Paso 27

> Es hora de probar el método `valid_in_row`. Llame a `valid_in_row` en `gameboard`. Pásele `0` y `8` como argumentos e imprima el resultado.
>
> Una vez más, observe cómo el método se define con tres parámetros, pero se llama con solo dos argumentos porque `self` se pasa automáticamente como el objeto sobre el que se llama al método.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

      def valid_in_row(self, row, num):
          return num not in self.board[row]
  
  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

  gameboard = Board(puzzle)
  
  # ---Región editable por el usuario---
  print(gameboard.valid_in_row(0, 8))
  # ---Región editable por el usuario---

  # -------Salida-------
  # False

---

## Paso 28

> Como puede ver, el resultado es `False` porque el `8` ya está presente en la primera fila del tablero. Ahora cambie el `8` por un `7`.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

      def valid_in_row(self, row, num):
          return num not in self.board[row]
  
  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

  gameboard = Board(puzzle)
  
  # ---Región editable por el usuario---
  print(gameboard.valid_in_row(0, 7))
  # ---Región editable por el usuario---

  # -------Salida-------
  # True

---

## Paso 29

¡Genial! El `7` no está presente en la primera fila del tablero de sudoku y el método indica que el `7` es una opción válida para esa fila.

> Ahora elimina la llamada `print`.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

      def valid_in_row(self, row, num):
          return num not in self.board[row]
  
  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

  gameboard = Board(puzzle)
  
  # ---Región editable por el usuario---
  # ---Región editable por el usuario---

  # -------Salida-------

---

## Paso 30

A continuación, vas a crear un método que compruebe si un número se puede insertar en una columna específica del tablero de sudoku, verificando si el número ya está presente en esa columna.

Dentro de la clase `Board`, crea un método llamado `valid_in_col` y asígnale tres parámetros: `self`, `col` y `num`. Donde `col` y `num` son el índice de la columna y el número que se va a comprobar, respectivamente.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

      def valid_in_row(self, row, num):
          return num not in self.board[row]
  
  # ---Región editable por el usuario---
      def valid_in_col(self, col, num):
          pass
  # ---Región editable por el usuario---
  
  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

  gameboard = Board(puzzle)
  

  # -------Salida-------

---

## Paso 31

Debes comprobar si un número determinado no es igual al número de la columna especificada de la fila actual.

> Para ello, sustituye `pass` por una expresión generadora que itere sobre el rango de `0` a `8` (inclusive) y, para cada fila=(`row`), evalúe si el número de la fila=(`row`) y columna=(`col`) especificadas en el tablero es diferente de `num`.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

      def valid_in_row(self, row, num):
          return num not in self.board[row]
  
  # ---Región editable por el usuario---
      def valid_in_col(self, col, num):
          (self.board[row][col] != num for row in range(9))
  # ---Región editable por el usuario---
  
  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

  gameboard = Board(puzzle)
  

  # -------Salida-------

---

## Paso 32

La expresión generadora que acaba de escribir en el paso anterior genera una lista de valores booleanos que representan si la condición `self.board[row][col] != num` es `True` o `False` para cada elemento de la columna especificada en todas las filas.

> Pase esa expresión generadora a la función `all()` para comprobar si todos los elementos de la columna son diferentes de `num` y devuelva el resultado.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

      def valid_in_row(self, row, num):
          return num not in self.board[row]
  
  # ---Región editable por el usuario---
      def valid_in_col(self, col, num):
          return all(self.board[row][col] != num for row in range(9))
  # ---Región editable por el usuario---
  
  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

  gameboard = Board(puzzle)
  

  # -------Salida-------

---

## Paso 33

> Llama a `valid_in_col` en `gameboard`. Pásale `0` y `7` como argumentos para ver si el número `7` está permitido en la primera columna del tablero e imprime el resultado.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

      def valid_in_row(self, row, num):
          return num not in self.board[row]
  
      def valid_in_col(self, col, num):
          return all(self.board[row][col] != num for row in range(9))
  
  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

  gameboard = Board(puzzle)
  
  # ---Región editable por el usuario---
  print(gameboard.valid_in_col(0, 7))
  # ---Región editable por el usuario---

  # -------Salida-------
  # True

---

## Paso 34

> Ahora cambia el `7` por un `1`.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

      def valid_in_row(self, row, num):
          return num not in self.board[row]
  
      def valid_in_col(self, col, num):
          return all(self.board[row][col] != num for row in range(9))
  
  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

  gameboard = Board(puzzle)
  
  # ---Región editable por el usuario---
  print(gameboard.valid_in_col(0, 1))
  # ---Región editable por el usuario---

  # -------Salida-------
  # False

---

## Paso 35

> El `1` ya está presente en la primera columna. Por lo tanto, todo parece funcionar correctamente. Ahora elimine su llamada `print`.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

      def valid_in_row(self, row, num):
          return num not in self.board[row]
  
      def valid_in_col(self, col, num):
          return all(self.board[row][col] != num for row in range(9))
  
  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

  gameboard = Board(puzzle)
  
  # ---Región editable por el usuario---
  # ---Región editable por el usuario---

  # -------Salida-------

---

## Paso 36

Otra cosa que hay que comprobar es si un número se puede insertar en un cuadrado de *3x3*.

> Dentro de la clase `Board`, crea un método llamado `valid_in_square` con cuatro parámetros: `self`, `row`, `col` y `num`. Donde `row`, `col` y `num` representan el índice de fila, el índice de columna y el número que se va a comprobar, respectivamente.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

      def valid_in_row(self, row, num):
          return num not in self.board[row]
  
      def valid_in_col(self, col, num):
          return all(self.board[row][col] != num for row in range(9))
  
  # ---Región editable por el usuario---
      def valid_in_square(self, row, col, num):
          pass
  # ---Región editable por el usuario---

  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

  gameboard = Board(puzzle)
  
  # -------Salida-------

---

## Paso 37

Ahora debes calcular el índice de la fila inicial para el cuadrado de 3x3 dentro de la cuadrícula del tablero y asegurarte de que el índice de la fila inicial para cada cuadrado de 3x3 sea un múltiplo de 3.

> Esto se puede lograr tomando el resultado de la división entera `row // 3` multiplicado por `3`. Reemplaza `pass` por una variable `row_start` y asígnale `(row // 3) * 3`.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

      def valid_in_row(self, row, num):
          return num not in self.board[row]
  
      def valid_in_col(self, col, num):
          return all(self.board[row][col] != num for row in range(9))
  
  # ---Región editable por el usuario---
      def valid_in_square(self, row, col, num):
          row_start = (row // 3) * 3
  # ---Región editable por el usuario---

  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

  gameboard = Board(puzzle)
  
  # -------Salida-------

---

## Paso 38

De manera similar al paso anterior, debes asegurarte de que el índice de la columna inicial de cada cuadrado de 3x3 sea un múltiplo de 3.

> Declara una variable `col_start` y asígnale `(col // 3) * 3`.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

      def valid_in_row(self, row, num):
          return num not in self.board[row]
  
      def valid_in_col(self, col, num):
          return all(self.board[row][col] != num for row in range(9))
  
  # ---Región editable por el usuario---
      def valid_in_square(self, row, col, num):
          row_start = (row // 3) * 3
          col_start = (col // 3) * 3
  # ---Región editable por el usuario---

  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

  gameboard = Board(puzzle)
  
  # -------Salida-------

---

## Paso 39

> Ahora, itere solo sobre las filas dentro del cuadrado de 3x3 creando un bucle `for`. Utilice la función `range()` para generar una secuencia que comience en `row_start` y utilice `row_no` como variable del bucle.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

      def valid_in_row(self, row, num):
          return num not in self.board[row]
  
      def valid_in_col(self, col, num):
          return all(self.board[row][col] != num for row in range(9))
  
  # ---Región editable por el usuario---
      def valid_in_square(self, row, col, num):
          row_start = (row // 3) * 3
          col_start = (col // 3) * 3
          for row_no in range(row_start, row_start + 3):
              pass
  # ---Región editable por el usuario---

  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

  gameboard = Board(puzzle)
  
  # -------Salida-------

---

## Paso 40

> Dentro del bucle creado en el paso anterior, anida otro bucle `for` para iterar sobre una secuencia de tres elementos que comienza en `col_start`. Utiliza la función `range()` para generar esta secuencia y `col_no` como variable del bucle.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

      def valid_in_row(self, row, num):
          return num not in self.board[row]
  
      def valid_in_col(self, col, num):
          return all(self.board[row][col] != num for row in range(9))
  
  # ---Región editable por el usuario---
      def valid_in_square(self, row, col, num):
          row_start = (row // 3) * 3
          col_start = (col // 3) * 3
          for row_no in range(row_start, row_start + 3):
              for col_no in range(col_start, col_start + 3):
                  pass
  # ---Región editable por el usuario---

  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

  gameboard = Board(puzzle)
  
  # -------Salida-------

---

## Paso 41

Ahora, comprueba si el número dado `num` ya está presente en la celda actual del cuadrado *3x3*.

> Reemplaza `pass` por una instrucción `if` que compruebe si el número de la celda actual del tablero de sudoku es igual a `num`. Si es así, **return** `False` desde el cuerpo de `if`, indicando que el número no es una opción válida.

- **Codigo**

  ```py
  class Board:

      def __init__(self, board):
          self.board = board

      def find_empty_cell(self):
          for row, contents in enumerate(self.board):
              try:
                  col = contents.index(0)
                  return row, col
              except ValueError:
                  pass
          return None

      def valid_in_row(self, row, num):
          return num not in self.board[row]
  
      def valid_in_col(self, col, num):
          return all(self.board[row][col] != num for row in range(9))
  
  # ---Región editable por el usuario---
      def valid_in_square(self, row, col, num):
          row_start = (row // 3) * 3
          col_start = (col // 3) * 3
          for row_no in range(row_start, row_start + 3):
              for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
  # ---Región editable por el usuario---

  puzzle = [
      [0, 0, 2, 0, 0, 8, 0, 0, 0],
      [0, 0, 0, 0, 0, 3, 7, 6, 2],
      [4, 3, 0, 0, 0, 0, 8, 0, 0],
      [0, 5, 0, 0, 3, 0, 0, 9, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 6],
      [0, 0, 0, 4, 6, 7, 0, 0, 0],
      [0, 8, 6, 7, 0, 4, 0, 0, 0],
      [0, 0, 0, 5, 1, 9, 0, 0, 8],
      [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

  gameboard = Board(puzzle)
  
  # -------Salida-------

---

## Paso 42

Si el número no está presente, se puede insertar en la casilla sin infringir las reglas del sudoku.

> Después del bucle `for` externo, devuelve `True`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

    # ---Región editable por el usuario---
        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)

    # -------Salida-------

---

## Paso 43

> Prueba el método para asegurarte de que funciona correctamente llamando a `valid_in_square` en `gameboard`. Pásale `1`, `0` y `3` como argumentos e imprime el resultado.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)

    # ---Región editable por el usuario---
    print(gameboard.valid_in_square(1, 0, 3))
    # ---Región editable por el usuario---

    # -------Salida-------
    # False

---

## Paso 44

> El método devuelve `False` porque el `3` ya está presente en esa casilla. Prueba con otra casilla cambiando el índice de columna a `6`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)

    # ---Región editable por el usuario---
    print(gameboard.valid_in_square(1, 6, 3))
    # ---Región editable por el usuario---

    # -------Salida-------
    # True

---

## Paso 45

> Todo funciona correctamente. Ahora elimine su llamada `print`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)

    # ---Región editable por el usuario---
    # ---Región editable por el usuario---

    # -------Salida-------

---

## Paso 46

> Dentro de la clase `Board`, crea otro método llamado `is_valid` y asígnale tres parámetros: `self`, `empty` y `num`. Donde `empty` es una tupla que representa los índices de fila y columna de una celda vacía y `num` es el número que se va a comprobar.

Este método comprobará si un número dado es una opción válida para una celda vacía en el tablero de sudoku, validando su compatibilidad con la fila, columna y cuadrado 3x3 de la celda vacía especificada.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
    # ---Región editable por el usuario---
        def is_valid(self, empty, num):
            pass
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 47

Una tupla se puede desempaquetar, lo que significa que los elementos que contiene se pueden asignar a variables, de la siguiente manera:

- **Codigo Ejemplo**

  ```py
    spam = ('lemon', 'curry')
    item1, item2 = spam
  ```

En el ejemplo anterior, `item1` tendría el valor `'lemon'` y `item2` tendría el valor `'curry'`.

> Dentro del método, elimine el `pass` y desempaque la tupla `empty` en fila=`row` y columna=`col`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
    # ---Región editable por el usuario---
        def is_valid(self, empty, num):
            row, col = empty
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 48

> Dentro del método `is_valid`, comprueba si el número es válido para su inserción en la fila especificada llamando al método `valid_in_row()` con `row` y `num` como argumentos, y asigna el resultado a una variable `valid_in_row`. Recuerda utilizar `self` para hacer referencia a los métodos de la instancia actual.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
    # ---Región editable por el usuario---
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 49

> Comprueba si el número es válido para su inserción en la columna especificada llamando al método `valid_in_col()` con `col` y `num` como argumentos y asigna el resultado a una variable `valid_in_col`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
    # ---Región editable por el usuario---
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 50

> Comprueba si el número es válido para insertarlo en el cuadrado 3x3 especificado llamando al método `valid_in_square()` con `row`, `col` y `num` como argumentos y asigna el resultado a una variable `valid_in_square`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
    # ---Región editable por el usuario---
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 51

> Para verificar que el número es válido después de todas esas comprobaciones, llame a la función `all()` y pásele una lista que contenga `valid_in_row,` `valid_in_col` y `valid_in_square`. Además, devuelva el resultado de la llamada a `all()`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
    # ---Región editable por el usuario---
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 52

A continuación, trabajarás en un método que intenta resolver el sudoku en el lugar, lo que significa que modificará el tablero de sudoku existente en lugar de crear uno nuevo.

> Dentro de la clase `Board`, crea un método llamado `solver` y asígnale un único parámetro, `self`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
    # ---Región editable por el usuario---
        def solver(self):
            pass
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 53

> Elimine el `pass` y cree una instrucción `if` que compruebe si el valor devuelto por `find_empty_cell` es `None`. En ese caso, el rompecabezas está resuelto. Por lo tanto, devuelva `True` desde el cuerpo de `if`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
    # ---Región editable por el usuario---
        def solver(self):
            if self.find_empty_cell() is None:
                return True
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 54

El operador `:=` le permite asignar variables en medio de una expresión. La sintaxis es: `name := val`, donde `name` es el nombre de la variable y `val` es el valor de la variable.

Esta construcción se denomina formalmente expresiones de asignación, mientras que el operador `:=` se conoce comúnmente como operador morsa.

> Dado que va a necesitar la llamada `self.find_empty_cell()` más de una vez, asígnela a una variable `next_empty` utilizando el operador morsa. A continuación, encierre la asignación entre un par de paréntesis.

De esta manera, combinará la asignación y la comprobación condicional en una sola línea, lo que hará que el código sea más conciso.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
    # ---Región editable por el usuario---
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 55

> Después de la instrucción `if`, crea un bucle `for` para iterar sobre el rango de `1` a `9`, ambos inclusive. Utiliza `guess` como variable del bucle.

Este bucle te permitirá comprobar sistemáticamente si algún dígito del `1` al `9` es adecuado para rellenar una celda vacía.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
    # ---Región editable por el usuario---
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                pass
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 56

Dentro del cuerpo del bucle, reemplaza `pass` por una instrucción `if` que compruebe si el número es una opción válida para la celda actual.

> Crea la condición `if` con una llamada a `is_valid`, pasando `next_empty` y `guess` como argumentos.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
    # ---Región editable por el usuario---
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    pass
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 57

> Dentro del cuerpo del `if`, elimine `pass` y desempaque la tupla `next_empty` en `row`, `col`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
    # ---Región editable por el usuario---
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 58

> Ahora, modifique el tablero en su lugar accediendo a la celda de la fila y columna indicadas y asignándole el valor de la `guess`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
    # ---Región editable por el usuario---
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 59

> Anida una instrucción `if` dentro de la `if`actual. Para la condición `if`, utiliza una llamada recursiva a `solver()` y devuelve `True` desde el nuevo cuerpo de la `if`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
    # ---Región editable por el usuario---
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 60

Si la llamada recursiva devuelve `False`, significa que la suposición ha dado lugar a un sudoku irresoluble. Por lo tanto, deberá restaurar la celda para que quede vacía y explorar otra suposición.

> Después de la instrucción `if` más interna, vuelva a establecer el valor de la celda actual en `0`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
    # ---Región editable por el usuario---
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 61

> Por último, haz que el método `solver` devuelva `False` si ninguna de las conjeturas conduce a una solución. Presta atención a la sangría.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
    # ---Región editable por el usuario---
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
            return False
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 62

> Fuera de la definición de la clase, crea una función `solve_sudoku` para imprimir y resolver el tablero de sudoku.
>
> Dale un único parámetro `board` que será tu lista 2D.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
            return False
    
    # ---Región editable por el usuario---
    def solve_sudoku(board):
        pass
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 63

> Dentro de la función `solve_sudoku`, elimine `pass` y cree una variable `gameboard` y asígnele una instancia de la clase `Board`, pasando `board` como argumento.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
            return False
    
    # ---Región editable por el usuario---
    def solve_sudoku(board):
        gameboard = Board(board)
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 64

> Ahora, agrega una llamada a `print()` para imprimir la siguiente cadena f: `f'Puzzle to solve:\n{gameboard}'`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
            return False
    
    # ---Región editable por el usuario---
    def solve_sudoku(board):
        gameboard = Board(board)
        print(f'Puzzle to solve:\n{gameboard}')
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 65

> Cree una instrucción `if` que compruebe si la llamada al método `solver()` desde el objeto `gameboard` devuelve `True`.
>
> A continuación, añada una llamada `print()` dentro del cuerpo de `if` pasando la siguiente cadena f: `f'Solved puzzle:\n{gameboard}'`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
            return False
    
    # ---Región editable por el usuario---
    def solve_sudoku(board):
        gameboard = Board(board)
        print(f'Puzzle to solve:\n{gameboard}')
        if gameboard.solver():
            print(f'Solved puzzle:\n{gameboard}')
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 66

> Cree una cláusula `else` para cuando el sudoku no se pueda resolver e imprima la siguiente cadena dentro del nuevo bloque `else`: `'The provided puzzle is unsolvable.'`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
                    else:
                        print('The provided puzzle is unsolvable.')
            return False
    
    # ---Región editable por el usuario---
    def solve_sudoku(board):
        gameboard = Board(board)
        print(f'Puzzle to solve:\n{gameboard}')
        if gameboard.solver():
            print(f'Solved puzzle:\n{gameboard}')
        else:
            print("The provided puzzle is unsolvable.")
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 67

> Después de las sentencias condicionales, devuelve tu instancia de la clase `Board`, que representa el estado final del tablero de sudoku después de intentar resolverlo.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
                    else:
                        print('The provided puzzle is unsolvable.')
            return False
    
    # ---Región editable por el usuario---
    def solve_sudoku(board):
        gameboard = Board(board)
        print(f'Puzzle to solve:\n{gameboard}')
        if gameboard.solver():
            print(f'Solved puzzle:\n{gameboard}')
        else:
            print("The provided puzzle is unsolvable.")
        return gameboard
    # ---Región editable por el usuario---

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    gameboard = Board(puzzle)


    # -------Salida-------

---

## Paso 68

> Todavía hay algo que arreglar. Intenta imprimir tu objeto `gameboard`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
                    else:
                        print('The provided puzzle is unsolvable.')
            return False
    
    def solve_sudoku(board):
        gameboard = Board(board)
        print(f'Puzzle to solve:\n{gameboard}')
        if gameboard.solver():
            print(f'Solved puzzle:\n{gameboard}')
        else:
            print("The provided puzzle is unsolvable.")
        return gameboard

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    # ---Región editable por el usuario---
    gameboard = Board(puzzle)
    print(gameboard)
    # ---Región editable por el usuario---


    # -------Salida-------
    # <__main__.Board object at 0x000001FDD8F0FFD0>

---

## Paso 69

Cuando imprimes tu objeto `gameboard`, obtienes algo como `<**main**.Board object at 0xf3c1c8>`, que es la representación predeterminada de un objeto. Esto significa que la función `solve_sudoku` también te dará un resultado diferente al que esperas.

> Elimina tanto la llamada a `print()` como el objeto `gameboard`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
                    else:
                        print('The provided puzzle is unsolvable.')
            return False
    
    def solve_sudoku(board):
        gameboard = Board(board)
        print(f'Puzzle to solve:\n{gameboard}')
        if gameboard.solver():
            print(f'Solved puzzle:\n{gameboard}')
        else:
            print("The provided puzzle is unsolvable.")
        return gameboard

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    # ---Región editable por el usuario---

    # ---Región editable por el usuario---


    # -------Salida-------

---

## Paso 70

El método `__str__` es un método especial que se invoca internamente cuando se imprime el objeto con la función `print()` o se convierte en una cadena con la función `str()`.

> Defina un método `__str__` vacío dentro de la clase `Board` y asígnele un parámetro `self`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        # ---Región editable por el usuario---
        def __str__(self):
            pass
        # ---Región editable por el usuario---

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
                    else:
                        print('The provided puzzle is unsolvable.')
            return False
    
    def solve_sudoku(board):
        gameboard = Board(board)
        print(f'Puzzle to solve:\n{gameboard}')
        if gameboard.solver():
            print(f'Solved puzzle:\n{gameboard}')
        else:
            print("The provided puzzle is unsolvable.")
        return gameboard

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]


    # -------Salida-------

---

## Paso 71

> Reemplaza `pass` por una variable `board_str` y asígnale una cadena vacía. Utilizarás esta variable para crear la representación de cadena personalizada que se devolverá.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        # ---Región editable por el usuario---
        def __str__(self):
            board_str = ''
        # ---Región editable por el usuario---

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
                    else:
                        print('The provided puzzle is unsolvable.')
            return False
    
    def solve_sudoku(board):
        gameboard = Board(board)
        print(f'Puzzle to solve:\n{gameboard}')
        if gameboard.solver():
            print(f'Solved puzzle:\n{gameboard}')
        else:
            print("The provided puzzle is unsolvable.")
        return gameboard

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]


    # -------Salida-------

---

## Paso 72

> Ahora, crea un bucle `for` para iterar sobre las filas del tablero. Utiliza `row` como variable del bucle.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        # ---Región editable por el usuario---
        def __str__(self):
            board_str = ''
            for row in self.board:
                pass
        # ---Región editable por el usuario---

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
                    else:
                        print('The provided puzzle is unsolvable.')
            return False
    
    def solve_sudoku(board):
        gameboard = Board(board)
        print(f'Puzzle to solve:\n{gameboard}')
        if gameboard.solver():
            print(f'Solved puzzle:\n{gameboard}')
        else:
            print("The provided puzzle is unsolvable.")
        return gameboard

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]


    # -------Salida-------

---

## Paso 73

> Dentro del bucle `for`, declare una variable `row_str` y asígnele una comprensión de lista que itere sobre `row` y convierta cada elemento `i` de `row` en una cadena. Utilice la función `str()` para ello.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        # ---Región editable por el usuario---
        def __str__(self):
            board_str = ''
            for row in self.board:
                row_str = [str(i) for i in row]
        # ---Región editable por el usuario---

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
                    else:
                        print('The provided puzzle is unsolvable.')
            return False
    
    def solve_sudoku(board):
        gameboard = Board(board)
        print(f'Puzzle to solve:\n{gameboard}')
        if gameboard.solver():
            print(f'Solved puzzle:\n{gameboard}')
        else:
            print("The provided puzzle is unsolvable.")
        return gameboard

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]


    # -------Salida-------

---

## Paso 74

> Modifique la comprensión `row_str` para que solo devuelva una cadena cuando el elemento no sea cero y, en caso contrario, devuelva un asterisco.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        # ---Región editable por el usuario---
        def __str__(self):
            board_str = ''
            for row in self.board:
                row_str = [str(i) if i != 0 else '*' for i in row]
        # ---Región editable por el usuario---

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
                    else:
                        print('The provided puzzle is unsolvable.')
            return False
    
    def solve_sudoku(board):
        gameboard = Board(board)
        print(f'Puzzle to solve:\n{gameboard}')
        if gameboard.solver():
            print(f'Solved puzzle:\n{gameboard}')
        else:
            print("The provided puzzle is unsolvable.")
        return gameboard

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]


    # -------Salida-------

---

## Paso 75

> A continuación, une los elementos de `row_str` con un espacio y añade el resultado al valor actual de `board_str`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        # ---Región editable por el usuario---
        def __str__(self):
            board_str = ''
            for row in self.board:
                row_str = [str(i) if i != 0 else '*' for i in row]
                board_str += ' '.join(row_str)
        # ---Región editable por el usuario---

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
                    else:
                        print('The provided puzzle is unsolvable.')
            return False
    
    def solve_sudoku(board):
        gameboard = Board(board)
        print(f'Puzzle to solve:\n{gameboard}')
        if gameboard.solver():
            print(f'Solved puzzle:\n{gameboard}')
        else:
            print("The provided puzzle is unsolvable.")
        return gameboard

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]


    # -------Salida-------

---

## Paso 76

> Agregue un carácter de nueva línea al valor actual de `board_str`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        # ---Región editable por el usuario---
        def __str__(self):
            board_str = ''
            for row in self.board:
                row_str = [str(i) if i != 0 else '*' for i in row]
                board_str += ' '.join(row_str)
                board_str += '\n'
        # ---Región editable por el usuario---

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
                    else:
                        print('The provided puzzle is unsolvable.')
            return False
    
    def solve_sudoku(board):
        gameboard = Board(board)
        print(f'Puzzle to solve:\n{gameboard}')
        if gameboard.solver():
            print(f'Solved puzzle:\n{gameboard}')
        else:
            print("The provided puzzle is unsolvable.")
        return gameboard

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]


    # -------Salida-------

---

## Paso 77

> Por último, devuelve `board_str` después del bucle `for`.

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        # ---Región editable por el usuario---
        def __str__(self):
            board_str = ''
            for row in self.board:
                row_str = [str(i) if i != 0 else '*' for i in row]
                board_str += ' '.join(row_str)
                board_str += '\n'
            return board_str
        # ---Región editable por el usuario---

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
                    else:
                        print('The provided puzzle is unsolvable.')
            return False
    
    def solve_sudoku(board):
        gameboard = Board(board)
        print(f'Puzzle to solve:\n{gameboard}')
        if gameboard.solver():
            print(f'Solved puzzle:\n{gameboard}')
        else:
            print("The provided puzzle is unsolvable.")
        return gameboard

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]


    # -------Salida-------

---

## Paso 78

> Ahora llama al método `solve_sudoku` pasando `puzzle` como argumento. Deberías ver el rompecabezas parcialmente vacío para resolver y el rompecabezas resuelto como resultado.

**¡Con esto, has completado el proyecto del solucionador de sudokus!**

- **Codigo**

  ```py
    class Board:

        def __init__(self, board):
            self.board = board

        def __str__(self):
            board_str = ''
            for row in self.board:
                row_str = [str(i) if i != 0 else '*' for i in row]
                board_str += ' '.join(row_str)
                board_str += '\n'
            return board_str

        def find_empty_cell(self):
            for row, contents in enumerate(self.board):
                try:
                    col = contents.index(0)
                    return row, col
                except ValueError:
                    pass
            return None

        def valid_in_row(self, row, num):
            return num not in self.board[row]
    
        def valid_in_col(self, col, num):
            return all(self.board[row][col] != num for row in range(9))

        def valid_in_square(self, row, col, num):
            row_start = (row // 3) * 3
            col_start = (col // 3) * 3
            for row_no in range(row_start, row_start + 3):
                for col_no in range(col_start, col_start + 3):
                    if self.board[row_no][col_no] == num:
                        return False
            return True
    
        def is_valid(self, empty, num):
            row, col = empty
            valid_in_row = self.valid_in_row(row, num)
            valid_in_col = self.valid_in_col(col, num)
            valid_in_square = self.valid_in_square(row, col, num)
            return all(
                [
                    valid_in_row,
                    valid_in_col,
                    valid_in_square,
                ]
            )
    
        def solver(self):
            if (next_empty := self.find_empty_cell()) is None:
                return True
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0
                    else:
                        print('The provided puzzle is unsolvable.')
            return False
    
    def solve_sudoku(board):
        gameboard = Board(board)
        print(f'Puzzle to solve:\n{gameboard}')
        if gameboard.solver():
            print(f'Solved puzzle:\n{gameboard}')
        else:
            print("The provided puzzle is unsolvable.")
        return gameboard

    puzzle = [
        [0, 0, 2, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 7, 6, 2],
        [4, 3, 0, 0, 0, 0, 8, 0, 0],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 4, 0, 0, 0, 0, 0, 2, 6],
        [0, 0, 0, 4, 6, 7, 0, 0, 0],
        [0, 8, 6, 7, 0, 4, 0, 0, 0],
        [0, 0, 0, 5, 1, 9, 0, 0, 8],
        [1, 7, 0, 0, 0, 6, 0, 0, 5]
    ]

    # ---Región editable por el usuario---
    solve_sudoku(puzzle)
    # ---Región editable por el usuario---

    # -------Salida-------
    # Puzzle to solve:
    # * * 2 * * 8 * * *
    # * * * * * 3 7 6 2
    # 4 3 * * * * 8 * *
    # * 5 * * 3 * * 9 *
    # * 4 * * * * * 2 6
    # * * * 4 6 7 * * *
    # * 8 6 7 * 4 * * *
    # * * * 5 1 9 * * 8
    # 1 7 * * * 6 * * 5
    
    # Solved puzzle:
    # 9 6 2 1 7 8 3 5 4
    # 8 1 5 9 4 3 7 6 2
    # 4 3 7 6 5 2 8 1 9
    # 6 5 8 2 3 1 4 9 7
    # 7 4 3 8 9 5 1 2 6
    # 2 9 1 4 6 7 5 8 3
    # 5 8 6 7 2 4 9 3 1
    # 3 2 4 5 1 9 6 7 8
    # 1 7 9 3 8 6 2 4 5

---
