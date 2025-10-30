# Aprende recursividad resolviendo el rompecabezas de la Torre de Hanoi

La recursividad es un enfoque de programación que permite resolver problemas computacionales complicados con solo un poco de código.

En este proyecto, comenzará con un enfoque basado en bucles para resolver el *rompecabezas matemático conocido como la Torre de Hanoi*. Luego, aprenderá a implementar una solución recursiva.

---

## Paso 1

En este proyecto, resolverás el *rompecabezas matemático conocido como la Torre de Hanoi*. El rompecabezas consta de tres varillas y varios discos de diferentes diámetros.

El objetivo de este rompecabezas es mover los discos de la primera varilla a la tercera, siguiendo unas reglas específicas que impiden colocar un disco más grande encima de uno más pequeño.

> Empieza creando un diccionario vacío llamado *varillas*=`rods` para representar las varillas.

- **Codigo**
  
  ```py
  rods = {}
  ```

---

## Paso 2

> El diccionario `rods` representará las tres varillas con sus discos. Asigna las cadenas `'A'`, `'B'` y `'C'` como claves y configura cada una de ellas como una lista vacía.

- **Codigo**
  
  ```py
  rods = {
      'A': [],
      'B': [],
      'C': []
  }
  ```

---

## Paso 3

El rompecabezas comienza con los discos apilados en la primera varilla, en orden decreciente de tamaño, con el disco más pequeño en la parte superior y el más grande en la parte inferior. Debes completar tu primera lista con números que representen los distintos tamaños de los discos.

> En lugar de añadir los elementos manualmente a la primera lista, genera una secuencia de números que cuente hacia atrás desde `3` hasta `1` utilizando la función `range()` y asígnala a `rods['A']`. Aquí, `3` representa el disco más grande en la parte inferior de la pila y `1` representa el disco más pequeño en la parte superior de la pila.
>
> La sintaxis es `range(x, y, h)`, donde `x` es el entero inicial (incluido), `y` es el último entero (no incluido) y `h` es la diferencia entre un número y el siguiente en la secuencia.

- **Codigo**
  
  ```py
  rods = {
      'A': range(3, 0, -1),
      'B': [],
      'C': []
  }
  ```

---

## Paso 4

> Ahora comprueba el tipo de datos de tu tecla `'A'` pasándola a la función `type()` e imprime el resultado en la terminal.

- **Codigo**
  
  ```py
  rods = {
      'A': range(3, 0, -1),
      'B': [],
      'C': []
  }
  print(type(rods['A']))
  # ----Salida esperada----
  # <class 'range'>
  ```

---

## Paso 5

La función `range()` devuelve una secuencia inmutable de números. Como puede ver, el tipo de datos de `rods['A']` es `range`, pero usted quiere que sea una lista.

> Para ello, pase su llamada a `range()` a la función `list()`.

- **Codigo**
  
  ```py
  rods = {
      'A': list(range(3, 0, -1)),
      'B': [],
      'C': []
  }
  print(type(rods['A']))
  # ----Salida esperada----
  # <class 'list'>
  ```

---

## Paso 6

> Ahora que el tipo está *listado*=`list` como se requiere, puede eliminar la llamada a `print()`.

- **Codigo**
  
  ```py
  rods = {
      'A': list(range(3, 0, -1)),
      'B': [],
      'C': []
  }
  # ----Salida esperada----
  ```

---

## Paso 7

El objetivo de *la Torre de Hanoi* es mover todos los discos a la última varilla. Para ello, debes seguir tres reglas sencillas:

- Solo se pueden mover los discos que están en la parte superior.
- Solo se puede mover un disco a la vez.
- No se pueden colocar discos más grandes encima de discos más pequeños.

> Debajo del código existente, declare una función vacía llamada `move`. Más adelante, utilizará esa función para mover los discos entre las varillas. Por ahora, para evitar errores, utilice la palabra clave `pass` dentro del cuerpo de la función.

- **Codigo**
  
  ```py
  rods = {
      'A': list(range(3, 0, -1)),
      'B': [],
      'C': []
  }
  def move():
      pass
  # ----Salida esperada----
  ```

---

## Paso 8

> En la parte superior del código, declare una variable llamada `NUMBER_OF_DISKS` para almacenar el número de discos y asígnele el valor `3`. A continuación, sustituya el primer argumento pasado a la función `range()` por su nueva variable.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  def move():
      pass
  # ----Salida esperada----
  ```

---

## Paso 9

> El rompecabezas de *la Torre de Hanoi* se puede resolver en $2^n - 1$ movimientos, donde `n` es el número de discos. Declare una variable llamada `number_of_moves` y asigne el número total de movimientos a esta variable.
>
> El operador de potencia en Python es `**`.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  def move():
      pass
  # ----Salida esperada----
  ```

---

## Paso 10

> Imprima la variable que declaró en el paso anterior y no dude en cambiar el número de discos para ver cómo aumenta la rapidez con la que aumenta el número mínimo de movimientos necesarios.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  print(number_of_moves)
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  def move():
      pass
  # ----Salida esperada----
  # 7

  ```

---

## Paso 11

> Ahora puede eliminar la llamada a `print()`. A continuación, dentro de la función `move()`, elimine la palabra clave `pass` e *imprima*=`print()` el contenido de su diccionario `rods`.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  def move():
      print(rods)
  # ----Salida esperada----

  ```

---

## Paso 12

> Ahora llame a su función y vea el resultado en la terminal.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  def move():
      print(rods)

  move()
  # ----Salida esperada----
  # {'A': [3, 2, 1], 'B': [], 'C': []}

  ```

---

## Paso 13

En el rompecabezas de *la Torre de Hanoi*, puedes identificar las tres varillas según su finalidad:

- La primera varilla es la fuente, donde todos los discos se apilan unos encima de otros al comienzo del juego.
- La segunda varilla es una varilla auxiliar, y ayuda a mover los discos a la varilla de destino.
- La tercera varilla es el destino, donde se deben colocar todos los discos en orden al final del juego.

> Actualmente, la función `move()` no toma ningún parámetro. Cambia la declaración de la función para que tome 4 parámetros: `n`, `source`, `auxiliary`, and `target`. A continuación, pasa `NUMBER_OF_DISKS` y las cadenas `'A'`, `'B'` y `'C'` como argumentos a la llamada a la función. El orden es importante.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  def move(n, source, auxiliary, target):
      print(rods)

  move(NUMBER_OF_DISKS, 'A', 'B', 'C')
  # ----Salida esperada----
  # {'A': [3, 2, 1], 'B': [], 'C': []}

  ```

---

## Paso 14

> Antes de llamar a la función, escriba un comentario que diga `initiate call from source A to target C with auxiliary B`.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  def move(n, source, auxiliary, target):
      print(rods)

  # initiate call from source A to target C with auxiliary B
  move(NUMBER_OF_DISKS, 'A', 'B', 'C')
  # ----Salida esperada----
  # {'A': [3, 2, 1], 'B': [], 'C': []}

  ```

---

## Paso 15

> Agregue otro comentario antes de su llamada a `print()`, `display starting configuration`.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  def move(n, source, auxiliary, target):
    # display starting configuration
      print(rods)

  # initiate call from source A to target C with auxiliary B
  move(NUMBER_OF_DISKS, 'A', 'B', 'C')
  # ----Salida esperada----
  # {'A': [3, 2, 1], 'B': [], 'C': []}

  ```

---

## Paso 16

Al final de este proyecto, crearás una solución recursiva para el rompecabezas de *la Torre de Hanoi*, pero ahora vas a explorar un enfoque iterativo para este problema.

> Comienza agregando un bucle `for` a tu función que itera a través del `number_of_moves` e imprime el número de iteración actual.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  def move(n, source, auxiliary, target):
    # display starting configuration
      print(rods)
      for i in range(number_of_moves):
          print(i)

  # initiate call from source A to target C with auxiliary B
  move(NUMBER_OF_DISKS, 'A', 'B', 'C')
  # ----Salida esperada----
  # {'A': [3, 2, 1], 'B': [], 'C': []}
  # 0
  # 1
  # 2
  # 3
  # 4
  # 5
  # 6

  ```

---

## Paso 17

Los movimientos permitidos entre las varillas siguen un patrón repetitivo que se produce cada tres movimientos. Por ejemplo, los movimientos entre la varilla `A` y la varilla `C` están permitidos en el primer, cuarto y séptimo movimiento, donde el resto de la división entre el número de movimiento y 3 es igual a 1.

> Dentro del bucle `for` creado anteriormente, reemplace la llamada `print()` existente por una instrucción `if` que se active cuando `(i + 1) % 3 == 1`. Dentro de esta instrucción `if`, imprima `f'Move {i + 1} allowed between {source} and {target}'` utilizando una *cadena f*. Tenga en cuenta que `i + 1` es el número de movimiento, ya que `i` es cero durante la primera iteración.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  def move(n, source, auxiliary, target):
    # display starting configuration
      print(rods)
      for i in range(number_of_moves):

          if (i + 1) % 3 == 1:
              print(f'Move {i + 1} allowed between {source} and {target}')

  # initiate call from source A to target C with auxiliary B
  move(NUMBER_OF_DISKS, 'A', 'B', 'C')

  # ----Salida esperada----
  # {'A': [3, 2, 1], 'B': [], 'C': []}
  # Move 1 allowed between A and C
  # Move 4 allowed between A and C
  # Move 7 allowed between A and C

  ```

---

## Paso 18

Dado que vas a utilizar la expresión `(i + 1) % 3` varias veces, es conveniente almacenarla en una variable.

> Justo encima de la instrucción if, declara una variable `remainder` y asígnale el valor `(i + 1) % 3`.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  # Región editable por el usuario
  def move(n, source, auxiliary, target):
    # display starting configuration
      print(rods)
      for i in range(number_of_moves):
          remainder = (i + 1) % 3
          if (i + 1) % 3 == 1:
              print(f'Move {i + 1} allowed between {source} and {target}')
  # Región editable por el usuario

  # initiate call from source A to target C with auxiliary B
  move(NUMBER_OF_DISKS, 'A', 'B', 'C')

  # ----Salida esperada----
  # {'A': [3, 2, 1], 'B': [], 'C': []}
  # Move 1 allowed between A and C
  # Move 4 allowed between A and C
  # Move 7 allowed between A and C

  ```

---

## Paso 19

> Ahora, reemplaza la expresión en la condición `if` con la variable `remainder`.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  # Región editable por el usuario
  def move(n, source, auxiliary, target):
    # display starting configuration
      print(rods)
      for i in range(number_of_moves):
          remainder = (i + 1) % 3
          if remainder == 1:
              print(f'Move {i + 1} allowed between {source} and {target}')
  # Región editable por el usuario

  # initiate call from source A to target C with auxiliary B
  move(NUMBER_OF_DISKS, 'A', 'B', 'C')

  # ----Salida esperada----
  # {'A': [3, 2, 1], 'B': [], 'C': []}
  # Move 1 allowed between A and C
  # Move 4 allowed between A and C
  # Move 7 allowed between A and C

  ```

---

## Paso 20

Cuando el resto del número de movimientos dividido por 3 es igual a 2, se permite el movimiento entre `'A'` y `'B'` (las varillas de origen y auxiliar).

> Añade una instrucción `elif` para eso. A continuación, imprime la cadena adecuada si se cumple la condición.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  # Región editable por el usuario
  def move(n, source, auxiliary, target):
    # display starting configuration
      print(rods)
      for i in range(number_of_moves):
          remainder = (i + 1) % 3
          if remainder == 1:
              print(f'Move {i + 1} allowed between {source} and {target}')
          elif remainder == 2:
              print(f"Move {i + 1} allowed between {source} and {auxiliary}")
  # Región editable por el usuario

  # initiate call from source A to target C with auxiliary B
  move(NUMBER_OF_DISKS, 'A', 'B', 'C')

  # ----Salida esperada----
  # {'A': [3, 2, 1], 'B': [], 'C': []}
  # Move 1 allowed between A and C
  # Move 2 allowed between A and B
  # Move 4 allowed between A and C
  # Move 5 allowed between A and B
  # Move 7 allowed between A and C

  ```

---

## Paso 21

Finalmente, cuando el número de movimientos dividido por 3 no tiene resto, se permite el movimiento entre `'B'` y `'C'`.

> Añade una instrucción `elif` para eso. A continuación, imprime la cadena adecuada si se cumple la condición.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  # Región editable por el usuario
  def move(n, source, auxiliary, target):
    # display starting configuration
      print(rods)
      for i in range(number_of_moves):
          remainder = (i + 1) % 3
          if remainder == 1:
              print(f'Move {i + 1} allowed between {source} and {target}')
          elif remainder == 2:
              print(f"Move {i + 1} allowed between {source} and {auxiliary}")
          elif remainder == 0:
              print(f'Move {i + 1} allowed between {auxiliary} and {target}')
  # Región editable por el usuario

  # initiate call from source A to target C with auxiliary B
  move(NUMBER_OF_DISKS, 'A', 'B', 'C')

  # ----Salida esperada----
  # {'A': [3, 2, 1], 'B': [], 'C': []}
  # Move 1 allowed between A and C
  # Move 2 allowed between A and B
  # Move 3 allowed between B and C
  # Move 4 allowed between A and C
  # Move 5 allowed between A and B
  # Move 6 allowed between B and C
  # Move 7 allowed between A and C

  ```

---

## Paso 22

> Has escrito el código para encontrar el movimiento permitido entre las varillas, pero el movimiento real podría ser en ambas direcciones. Después de la llamada a `print()`, declara una variable llamada `forward` y establécela en `False`. Utilizarás esa variable para comprobar en qué dirección debes mover el disco entre las varillas.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  def move(n, source, auxiliary, target):
    # display starting configuration
      print(rods)
      for i in range(number_of_moves):
          remainder = (i + 1) % 3
  
  # Región editable por el usuario
          if remainder == 1:
              print(f'Move {i + 1} allowed between {source} and {target}')
              forward = False
  # Región editable por el usuario

          elif remainder == 2:
              print(f"Move {i + 1} allowed between {source} and {auxiliary}")
          elif remainder == 0:
              print(f'Move {i + 1} allowed between {auxiliary} and {target}')

  # initiate call from source A to target C with auxiliary B
  move(NUMBER_OF_DISKS, 'A', 'B', 'C')

  # ----Salida esperada----
  # {'A': [3, 2, 1], 'B': [], 'C': []}
  # Move 1 allowed between A and C
  # Move 2 allowed between A and B
  # Move 3 allowed between B and C
  # Move 4 allowed between A and C
  # Move 5 allowed between A and B
  # Move 6 allowed between B and C
  # Move 7 allowed between A and C

  ```

---

## Paso 23

Cuando el *destino*=`target` está vacío, el disco debe moverse necesariamente desde el `source` al `target`.

> Después de la declaración de `forward`, agrega una instrucción `if` para verificar si `rods[target]` está vacío. Si lo está, cambia `forward` a `True`.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  def move(n, source, auxiliary, target):
    # display starting configuration
      print(rods)
      for i in range(number_of_moves):
          remainder = (i + 1) % 3
          if remainder == 1:
              print(f'Move {i + 1} allowed between {source} and {target}')
              forward = False
  
  # Región editable por el usuario
              if not rods[target]:
                  forward = True
  # Región editable por el usuario

          elif remainder == 2:
              print(f"Move {i + 1} allowed between {source} and {auxiliary}")
          elif remainder == 0:
              print(f'Move {i + 1} allowed between {auxiliary} and {target}')

  # initiate call from source A to target C with auxiliary B
  move(NUMBER_OF_DISKS, 'A', 'B', 'C')

  # ----Salida esperada----
  # {'A': [3, 2, 1], 'B': [], 'C': []}
  # Move 1 allowed between A and C
  # Move 2 allowed between A and B
  # Move 3 allowed between B and C
  # Move 4 allowed between A and C
  # Move 5 allowed between A and B
  # Move 6 allowed between B and C
  # Move 7 allowed between A and C

  ```

---

## Paso 24

El otro caso en el que es necesario mover el disco del `source` al `target` es cuando la lista de origen *not* está vacía *and* el último disco del `source` es inferior al último disco del `target`.

> Agregue una instrucción `elif` para comprobar esta condición. A continuación, establezca la variable `forward` en `True` si se cumple la condición.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  def move(n, source, auxiliary, target):
    # display starting configuration
      print(rods)
      for i in range(number_of_moves):
          remainder = (i + 1) % 3

  # Región editable por el usuario
          if remainder == 1:
              print(f'Move {i + 1} allowed between {source} and {target}')
              forward = False
              if not rods[target]:
                  forward = True
              elif rods[source] and rods[source][-1] < rods[target][-1]:
                  forward = True
  # Región editable por el usuario

          elif remainder == 2:
              print(f"Move {i + 1} allowed between {source} and {auxiliary}")
          elif remainder == 0:
              print(f'Move {i + 1} allowed between {auxiliary} and {target}')

  # initiate call from source A to target C with auxiliary B
  move(NUMBER_OF_DISKS, 'A', 'B', 'C')

  # ----Salida esperada----
  # {'A': [3, 2, 1], 'B': [], 'C': []}
  # Move 1 allowed between A and C
  # Move 2 allowed between A and B
  # Move 3 allowed between B and C
  # Move 4 allowed between A and C
  # Move 5 allowed between A and B
  # Move 6 allowed between B and C
  # Move 7 allowed between A and C

  ```

---

## Paso 25

> A continuación, debajo de la instrucción `elif` anidada, agregue otra instrucción `if` que se debe ejecutar cuando `forward` sea `True`. Dentro de esta condición, imprima la siguiente *f-string*: `f'Moving disk {rods[source][-1]} from {source} to {target}'`

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  def move(n, source, auxiliary, target):
    # display starting configuration
      print(rods)
      for i in range(number_of_moves):
          remainder = (i + 1) % 3

  # Región editable por el usuario
          if remainder == 1:
              print(f'Move {i + 1} allowed between {source} and {target}')
              forward = False
              if not rods[target]:
                  forward = True
              elif rods[source] and rods[source][-1] < rods[target][-1]:
                  forward = True
              if forward:
                  print(f'Moving disk {rods[source][-1]} from {source} to {target}')
  # Región editable por el usuario

          elif remainder == 2:
              print(f"Move {i + 1} allowed between {source} and {auxiliary}")
          elif remainder == 0:
              print(f'Move {i + 1} allowed between {auxiliary} and {target}')

  # initiate call from source A to target C with auxiliary B
  move(NUMBER_OF_DISKS, 'A', 'B', 'C')

  # ----Salida esperada----
  # {'A': [3, 2, 1], 'B': [], 'C': []}
  # Move 1 allowed between A and C
  # Moving disk 1 from A to C
  # Move 2 allowed between A and B
  # Move 3 allowed between B and C
  # Move 4 allowed between A and C
  # Moving disk 1 from A to C
  # Move 5 allowed between A and B
  # Move 6 allowed between B and C
  # Move 7 allowed between A and C
  # Moving disk 1 from A to C

  ```

---

## Paso 26

> Después de imprimir el movimiento, debe eliminar el último elemento de la barra de origen y añadirlo a la barra de destino. Para ello, utilice los métodos `.pop()` y `.append()`.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  def move(n, source, auxiliary, target):
    # display starting configuration
      print(rods)
      for i in range(number_of_moves):
          remainder = (i + 1) % 3

  # Región editable por el usuario
          if remainder == 1:
              print(f'Move {i + 1} allowed between {source} and {target}')
              forward = False
              if not rods[target]:
                  forward = True
              elif rods[source] and rods[source][-1] < rods[target][-1]:
                  forward = True
              if forward:
                  print(f'Moving disk {rods[source][-1]} from {source} to {target}')
                  rods[target].append(rods[source].pop())
  # Región editable por el usuario

          elif remainder == 2:
              print(f"Move {i + 1} allowed between {source} and {auxiliary}")
          elif remainder == 0:
              print(f'Move {i + 1} allowed between {auxiliary} and {target}')

  # initiate call from source A to target C with auxiliary B
  move(NUMBER_OF_DISKS, 'A', 'B', 'C')

  # ----Salida esperada----
  # {'A': [3, 2, 1], 'B': [], 'C': []}
  # Move 1 allowed between A and C
  # Moving disk 1 from A to C
  # Move 2 allowed between A and B
  # Move 3 allowed between B and C
  # Move 4 allowed between A and C
  # Move 5 allowed between A and B
  # Move 6 allowed between B and C
  # Move 7 allowed between A and C

  ```

---

## Paso 27

> Cuando `forward` es `False`, el disco debe moverse en la dirección opuesta. Escriba una cláusula `else` para ello. Imprima el movimiento y cambie el contenido de las listas según corresponda.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  def move(n, source, auxiliary, target):
    # display starting configuration
      print(rods)
      for i in range(number_of_moves):
          remainder = (i + 1) % 3
          if remainder == 1:
              print(f'Move {i + 1} allowed between {source} and {target}')
              forward = False
              if not rods[target]:
                  forward = True
              elif rods[source] and rods[source][-1] < rods[target][-1]:
                  forward = True

  # Región editable por el usuario
              if forward:
                  print(f'Moving disk {rods[source][-1]} from {source} to {target}')
                  rods[target].append(rods[source].pop())
              else:
                  print(f'Moving disk {rods[target][-1]} from {target} to {source}')
                  rods[source].append(rods[target].pop())
  # Región editable por el usuario

          elif remainder == 2:
              print(f"Move {i + 1} allowed between {source} and {auxiliary}")
          elif remainder == 0:
              print(f'Move {i + 1} allowed between {auxiliary} and {target}')

  # initiate call from source A to target C with auxiliary B
  move(NUMBER_OF_DISKS, 'A', 'B', 'C')

  # ----Salida esperada----
  # {'A': [3, 2, 1], 'B': [], 'C': []}
  # Move 1 allowed between A and C
  # Moving disk 1 from A to C
  # Move 2 allowed between A and B
  # Move 3 allowed between B and C
  # Move 4 allowed between A and C
  # Moving disk 1 from C to A
  # Move 5 allowed between A and B
  # Move 6 allowed between B and C
  # Move 7 allowed between A and C
  # Moving disk 1 from A to C

  ```

---

## Paso 28

> Fuera del bloque `else`, agrega un comentario que diga `display our progress` e imprime el contenido de las listas para verificar que todo funcione correctamente.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  def move(n, source, auxiliary, target):
    # display starting configuration
      print(rods)
      for i in range(number_of_moves):
          remainder = (i + 1) % 3
          if remainder == 1:
              print(f'Move {i + 1} allowed between {source} and {target}')
              forward = False
              if not rods[target]:
                  forward = True
              elif rods[source] and rods[source][-1] < rods[target][-1]:
                  forward = True

  # Región editable por el usuario
              if forward:
                  print(f'Moving disk {rods[source][-1]} from {source} to {target}')
                  rods[target].append(rods[source].pop())
              else:
                  print(f'Moving disk {rods[target][-1]} from {target} to {source}')
                  rods[source].append(rods[target].pop())
              # display our progress
              print(rods)
  # Región editable por el usuario

          elif remainder == 2:
              print(f"Move {i + 1} allowed between {source} and {auxiliary}")
          elif remainder == 0:
              print(f'Move {i + 1} allowed between {auxiliary} and {target}')

  # initiate call from source A to target C with auxiliary B
  move(NUMBER_OF_DISKS, 'A', 'B', 'C')

  # ----Salida esperada----
  # {'A': [3, 2, 1], 'B': [], 'C': []}
  # Move 1 allowed between A and C
  # Moving disk 1 from A to C
  # {'A': [3, 2], 'B': [], 'C': [1]}
  # Move 2 allowed between A and B
  # Move 3 allowed between B and C
  # Move 4 allowed between A and C
  # Moving disk 1 from C to A
  # {'A': [3, 2, 1], 'B': [], 'C': []}
  # Move 5 allowed between A and B
  # Move 6 allowed between B and C
  # Move 7 allowed between A and C
  # Moving disk 1 from A to C
  # {'A': [3, 2], 'B': [], 'C': [1]}

  ```

---

## Paso 29

> Como puede ver, el disco 1 se mueve hacia adelante y hacia atrás cada tres movimientos. Esto ocurre porque aún debe ocuparse de los movimientos entre las otras varillas. En lugar de repetir el mismo código que escribió durante los pasos anteriores y cambiar las varillas, sería mejor mover ese código dentro de una función para llamarlo en cada instrucción condicional. Declare una función vacía llamada `make_allowed_move()` y no olvide la palabra clave `pass`.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  
  # Región editable por el usuario
  def make_allowed_move():
      pass
  # Región editable por el usuario

  def move(n, source, auxiliary, target):
      # display starting configuration
      print(rods)
      for i in range(number_of_moves):
          remainder = (i + 1) % 3
          if remainder == 1:
              print(f'Move {i + 1} allowed between {source} and {target}')
              forward = False
              if not rods[target]:
                  forward = True
              elif rods[source] and rods[source][-1] < rods[target][-1]:
                  forward = True
              if forward:
                  print(f'Moving disk {rods[source][-1]} from {source} to {target}')
                  rods[target].append(rods[source].pop())
              else:
                  print(f'Moving disk {rods[target][-1]} from {target} to {source}')
                  rods[source].append(rods[target].pop())
              # display our progress
              print(rods)
          elif remainder == 2:
              print(f"Move {i + 1} allowed between {source} and {auxiliary}")
          elif remainder == 0:
              print(f'Move {i + 1} allowed between {auxiliary} and {target}')

  # initiate call from source A to target C with auxiliary B
  move(NUMBER_OF_DISKS, 'A', 'B', 'C')

  # ----Salida esperada----
  # {'A': [3, 2, 1], 'B': [], 'C': []}
  # Move 1 allowed between A and C
  # Moving disk 1 from A to C
  # {'A': [3, 2], 'B': [], 'C': [1]}
  # Move 2 allowed between A and B
  # Move 3 allowed between B and C
  # Move 4 allowed between A and C
  # Moving disk 1 from C to A
  # {'A': [3, 2, 1], 'B': [], 'C': []}
  # Move 5 allowed between A and B
  # Move 6 allowed between B and C
  # Move 7 allowed between A and C
  # Moving disk 1 from A to C
  # {'A': [3, 2], 'B': [], 'C': [1]}

  ```

---

## Paso 30

> Agregue dos parámetros llamados `rod1` y `rod2` a su nueva función.

- **Codigo**
  
  ```py
  NUMBER_OF_DISKS = 3
  number_of_moves = 2**NUMBER_OF_DISKS - 1
  rods = {
      'A': list(range(NUMBER_OF_DISKS, 0, -1)),
      'B': [],
      'C': []
  }
  
  # Región editable por el usuario
  def make_allowed_move(rod1, rod2):
      pass
  # Región editable por el usuario

  def move(n, source, auxiliary, target):
      # display starting configuration
      print(rods)
      for i in range(number_of_moves):
          remainder = (i + 1) % 3
          if remainder == 1:
              print(f'Move {i + 1} allowed between {source} and {target}')
              forward = False
              if not rods[target]:
                  forward = True
              elif rods[source] and rods[source][-1] < rods[target][-1]:
                  forward = True
              if forward:
                  print(f'Moving disk {rods[source][-1]} from {source} to {target}')
                  rods[target].append(rods[source].pop())
              else:
                  print(f'Moving disk {rods[target][-1]} from {target} to {source}')
                  rods[source].append(rods[target].pop())
              # display our progress
              print(rods)
          elif remainder == 2:
              print(f"Move {i + 1} allowed between {source} and {auxiliary}")
          elif remainder == 0:
              print(f'Move {i + 1} allowed between {auxiliary} and {target}')

  # initiate call from source A to target C with auxiliary B
  move(NUMBER_OF_DISKS, 'A', 'B', 'C')

  # ----Salida esperada----
  # {'A': [3, 2, 1], 'B': [], 'C': []}
  # Move 1 allowed between A and C
  # Moving disk 1 from A to C
  # {'A': [3, 2], 'B': [], 'C': [1]}
  # Move 2 allowed between A and B
  # Move 3 allowed between B and C
  # Move 4 allowed between A and C
  # Moving disk 1 from C to A
  # {'A': [3, 2, 1], 'B': [], 'C': []}
  # Move 5 allowed between A and B
  # Move 6 allowed between B and C
  # Move 7 allowed between A and C
  # Moving disk 1 from A to C
  # {'A': [3, 2], 'B': [], 'C': [1]}

  ```

---

## Paso 31

> Es hora de mover parte del código de la función `move()` a la función `make_allowed_move()`. Mueva el código anidado dentro de la primera instrucción `if` (excepto la primera llamada a `print()`) a su nueva función. Preste mucha atención a la sangría. No olvide eliminar la palabra clave `pass`.

- **Codigo**
  
  ```py
    NUMBER_OF_DISKS = 3
    number_of_moves = 2**NUMBER_OF_DISKS - 1
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    
    # Región editable por el usuario
    def make_allowed_move(rod1, rod2):
          forward = False
          if not rods[target]:
              forward = True
          elif rods[source] and rods[source][-1] < rods[target][-1]:
              forward = True
          if forward:
              print(f'Moving disk {rods[source][-1]} from {source} to {target}')
              rods[target].append(rods[source].pop())
          else:
              print(f'Moving disk {rods[target][-1]} from {target} to {source}')
              rods[source].append(rods[target].pop())
          # display our progress
          print(rods)

    def move(n, source, auxiliary, target):
        # display starting configuration
        print(rods)
        for i in range(number_of_moves):
            remainder = (i + 1) % 3
            if remainder == 1:
                print(f'Move {i + 1} allowed between {source} and {target}')
    # Región editable por el usuario
  
            elif remainder == 2:
                print(f"Move {i + 1} allowed between {source} and {auxiliary}")
            elif remainder == 0:
                print(f'Move {i + 1} allowed between {auxiliary} and {target}')

   # initiate call from source A to target C with auxiliary B
   move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
   # ----Salida esperada----
   # Move 1 allowed between A and C
   # Move 2 allowed between A and B
   # Move 3 allowed between B and C
   # Move 4 allowed between A and C
   # Move 5 allowed between A and B
   # Move 6 allowed between B and C
   # Move 7 allowed between A and C

  ```

---

## Paso 32

> `make_allowed_move()` toma `rod1` y `rod2` como parámetros. Aquí es necesario realizar una pequeña refactorización. Cambie todas las apariciones de `source` por `rod1`.

- **Codigo**
  
  ```py
    NUMBER_OF_DISKS = 3
    number_of_moves = 2**NUMBER_OF_DISKS - 1
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    
    # Región editable por el usuario
    def make_allowed_move(rod1, rod2):
          forward = False
          if not rods[target]:
              forward = True
          elif rods[rod1] and rods[rod1][-1] < rods[target][-1]:
              forward = True
          if forward:
              print(f'Moving disk {rods[rod1][-1]} from {rod1} to {target}')
              rods[target].append(rods[rod1].pop())
          else:
              print(f'Moving disk {rods[target][-1]} from {target} to {rod1}')
              rods[rod1].append(rods[target].pop())
          # display our progress
          print(rods)

    def move(n, source, auxiliary, target):
        # display starting configuration
        print(rods)
        for i in range(number_of_moves):
            remainder = (i + 1) % 3
            if remainder == 1:
                print(f'Move {i + 1} allowed between {source} and {target}')
    # Región editable por el usuario
  
            elif remainder == 2:
                print(f"Move {i + 1} allowed between {source} and {auxiliary}")
            elif remainder == 0:
                print(f'Move {i + 1} allowed between {auxiliary} and {target}')

   # initiate call from source A to target C with auxiliary B
   move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
   # ----Salida esperada----
   # Move 1 allowed between A and C
   # Move 2 allowed between A and B
   # Move 3 allowed between B and C
   # Move 4 allowed between A and C
   # Move 5 allowed between A and B
   # Move 6 allowed between B and C
   # Move 7 allowed between A and C

  ```

---

## Paso 33

> Ahora cambia cada aparición de `target` por `rod2`.

- **Codigo**
  
  ```py
    NUMBER_OF_DISKS = 3
    number_of_moves = 2**NUMBER_OF_DISKS - 1
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    
    # Región editable por el usuario
    def make_allowed_move(rod1, rod2):
          forward = False
          if not rods[rod2]:
              forward = True
          elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
              forward = True
          if forward:
              print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
              rods[rod2].append(rods[rod1].pop())
          else:
              print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
              rods[rod1].append(rods[rod2].pop())
          # display our progress
          print(rods)

    def move(n, source, auxiliary, target):
        # display starting configuration
        print(rods)
        for i in range(number_of_moves):
            remainder = (i + 1) % 3
            if remainder == 1:
                print(f'Move {i + 1} allowed between {source} and {target}')
    # Región editable por el usuario
  
            elif remainder == 2:
                print(f"Move {i + 1} allowed between {source} and {auxiliary}")
            elif remainder == 0:
                print(f'Move {i + 1} allowed between {auxiliary} and {target}')

   # initiate call from source A to target C with auxiliary B
   move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
   # ----Salida esperada----
   # Move 1 allowed between A and C
   # Move 2 allowed between A and B
   # Move 3 allowed between B and C
   # Move 4 allowed between A and C
   # Move 5 allowed between A and B
   # Move 6 allowed between B and C
   # Move 7 allowed between A and C

  ```

---

## Paso 34

> Ahora llama a `make_allowed_move()` y pasa la `source` y `target` como argumentos.

- **Codigo**
  
  ```py
    NUMBER_OF_DISKS = 3
    number_of_moves = 2**NUMBER_OF_DISKS - 1
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    
    def make_allowed_move(rod1, rod2):
          forward = False
          if not rods[rod2]:
              forward = True
          elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
              forward = True
          if forward:
              print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
              rods[rod2].append(rods[rod1].pop())
          else:
              print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
              rods[rod1].append(rods[rod2].pop())
          # display our progress
          print(rods)

    def move(n, source, auxiliary, target):
        # display starting configuration
        print(rods)
        for i in range(number_of_moves):
            remainder = (i + 1) % 3

    # Región editable por el usuario
            if remainder == 1:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
    # Región editable por el usuario
  
            elif remainder == 2:
                print(f"Move {i + 1} allowed between {source} and {auxiliary}")
            elif remainder == 0:
                print(f'Move {i + 1} allowed between {auxiliary} and {target}')

   # initiate call from source A to target C with auxiliary B
   move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
   # ----Salida esperada----
   # Move 1 allowed between A and C
   # Move 2 allowed between A and B
   # Move 3 allowed between B and C
   # Move 4 allowed between A and C
   # Move 5 allowed between A and B
   # Move 6 allowed between B and C
   # Move 7 allowed between A and C

  ```

---

## Paso 35

> Vuelve a llamar a la función `make_allowed_move()` dentro de las dos cláusulas `elif` y pasa los argumentos correctos.

- **Codigo**
  
  ```py
    NUMBER_OF_DISKS = 3
    number_of_moves = 2**NUMBER_OF_DISKS - 1
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    
    def make_allowed_move(rod1, rod2):
          forward = False
          if not rods[rod2]:
              forward = True
          elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
              forward = True
          if forward:
              print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
              rods[rod2].append(rods[rod1].pop())
          else:
              print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
              rods[rod1].append(rods[rod2].pop())
          # display our progress
          print(rods)

    def move(n, source, auxiliary, target):
        # display starting configuration
        print(rods)
        for i in range(number_of_moves):
            remainder = (i + 1) % 3

    # Región editable por el usuario
            if remainder == 1:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
            elif remainder == 2:
                print(f"Move {i + 1} allowed between {source} and {auxiliary}")
                make_allowed_move(source, auxiliary)
            elif remainder == 0:
                print(f'Move {i + 1} allowed between {auxiliary} and {target}')
                make_allowed_move(auxiliary, target)
    # Región editable por el usuario

    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
    # ----Salida esperada----
    # {'A': [3, 2, 1], 'B': [], 'C': []}
    # Move 1 allowed between A and C
    # Moving disk 1 from A to C
    # {'A': [3, 2], 'B': [], 'C': [1]}
    # Move 2 allowed between A and B
    # Moving disk 2 from A to B
    # {'A': [3], 'B': [2], 'C': [1]}
    # Move 3 allowed between B and C
    # Moving disk 1 from C to B
    # {'A': [3], 'B': [2, 1], 'C': []}
    # Move 4 allowed between A and C
    # Moving disk 3 from A to C
    # {'A': [], 'B': [2, 1], 'C': [3]}
    # Move 5 allowed between A and B
    # Moving disk 1 from B to A
    # {'A': [1], 'B': [2], 'C': [3]}
    # Move 6 allowed between B and C
    # Moving disk 2 from B to C
    # {'A': [1], 'B': [], 'C': [3, 2]}
    # Move 7 allowed between A and C
    # Moving disk 1 from A to C
    # {'A': [], 'B': [], 'C': [3, 2, 1]}

  ```

---

## Paso 36

> ¡Parece que funciona! Pero el resultado no es muy legible. Imprima un carácter de nueva línea después de imprimir las barras para solucionarlo.

- **Codigo**
  
  ```py
    NUMBER_OF_DISKS = 3
    number_of_moves = 2**NUMBER_OF_DISKS - 1
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    
    def make_allowed_move(rod1, rod2):
          forward = False
          if not rods[rod2]:
              forward = True
          elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
              forward = True
          if forward:
              print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
              rods[rod2].append(rods[rod1].pop())
          else:
              print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
              rods[rod1].append(rods[rod2].pop())

    # Región editable por el usuario
          # display our progress
          print(rods,'\n')

    def move(n, source, auxiliary, target):
        # display starting configuration
        print(rods,'\n')
    # Región editable por el usuario

        for i in range(number_of_moves):
            remainder = (i + 1) % 3
            if remainder == 1:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
            elif remainder == 2:
                print(f"Move {i + 1} allowed between {source} and {auxiliary}")
                make_allowed_move(source, auxiliary)
            elif remainder == 0:
                print(f'Move {i + 1} allowed between {auxiliary} and {target}')
                make_allowed_move(auxiliary, target)

    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
    # ----Salida esperada----
    # {'A': [3, 2, 1], 'B': [], 'C': []}
    
    # Move 1 allowed between A and C
    # Moving disk 1 from A to C
    # {'A': [3, 2], 'B': [], 'C': [1]}
    
    # Move 2 allowed between A and B
    # Moving disk 2 from A to B
    # {'A': [3], 'B': [2], 'C': [1]}
    
    # Move 3 allowed between B and C
    # Moving disk 1 from C to B
    # {'A': [3], 'B': [2, 1], 'C': []}
    
    # Move 4 allowed between A and C
    # Moving disk 3 from A to C
    # {'A': [], 'B': [2, 1], 'C': [3]}
    
    # Move 5 allowed between A and B
    # Moving disk 1 from B to A
    # {'A': [1], 'B': [2], 'C': [3]}
    
    # Move 6 allowed between B and C
    # Moving disk 2 from B to C
    # {'A': [1], 'B': [], 'C': [3, 2]}
    
    # Move 7 allowed between A and C
    # Moving disk 1 from A to C
    # {'A': [], 'B': [], 'C': [3, 2, 1]}


  ```

---

## Paso 37

> La solución iterativa de *la Torre de Hanoi* podría parecer completa, pero cambia el número de discos a `4` y observa el resultado.

- **Codigo**
  
  ```py
    
    # Región editable por el usuario
    NUMBER_OF_DISKS = 4
    # Región editable por el usuario

    number_of_moves = 2**NUMBER_OF_DISKS - 1
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    
    def make_allowed_move(rod1, rod2):
          forward = False
          if not rods[rod2]:
              forward = True
          elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
              forward = True
          if forward:
              print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
              rods[rod2].append(rods[rod1].pop())
          else:
              print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
              rods[rod1].append(rods[rod2].pop())
          # display our progress
          print(rods,'\n')

    def move(n, source, auxiliary, target):
        # display starting configuration
        print(rods,'\n')
        for i in range(number_of_moves):
            remainder = (i + 1) % 3
            if remainder == 1:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
            elif remainder == 2:
                print(f"Move {i + 1} allowed between {source} and {auxiliary}")
                make_allowed_move(source, auxiliary)
            elif remainder == 0:
                print(f'Move {i + 1} allowed between {auxiliary} and {target}')
                make_allowed_move(auxiliary, target)

    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
    # ----Salida esperada----
    # {'A': [4, 3, 2, 1], 'B': [], 'C': []} 
    
    # Move 1 allowed between A and C
    # Moving disk 1 from A to C
    # {'A': [4, 3, 2], 'B': [], 'C': [1]} 
    
    # Move 2 allowed between A and B
    # Moving disk 2 from A to B
    # {'A': [4, 3], 'B': [2], 'C': [1]} 
    
    # Move 3 allowed between B and C
    # Moving disk 1 from C to B
    # {'A': [4, 3], 'B': [2, 1], 'C': []} 
    
    # Move 4 allowed between A and C
    # Moving disk 3 from A to C
    # {'A': [4], 'B': [2, 1], 'C': [3]} 
    
    # Move 5 allowed between A and B
    # Moving disk 1 from B to A
    # {'A': [4, 1], 'B': [2], 'C': [3]} 
    
    # Move 6 allowed between B and C
    # Moving disk 2 from B to C
    # {'A': [4, 1], 'B': [], 'C': [3, 2]} 
    
    # Move 7 allowed between A and C
    # Moving disk 1 from A to C
    # {'A': [4], 'B': [], 'C': [3, 2, 1]} 
    
    # Move 8 allowed between A and B
    # Moving disk 4 from A to B
    # {'A': [], 'B': [4], 'C': [3, 2, 1]} 
    
    # Move 9 allowed between B and C
    # Moving disk 1 from C to B
    # {'A': [], 'B': [4, 1], 'C': [3, 2]} 
    
    # Move 10 allowed between A and C
    # Moving disk 2 from C to A
    # {'A': [2], 'B': [4, 1], 'C': [3]} 
    
    # Move 11 allowed between A and B
    # Moving disk 1 from B to A
    # {'A': [2, 1], 'B': [4], 'C': [3]} 
    
    # Move 12 allowed between B and C
    # Moving disk 3 from C to B
    # {'A': [2, 1], 'B': [4, 3], 'C': []} 
    
    # Move 13 allowed between A and C
    # Moving disk 1 from A to C
    # {'A': [2], 'B': [4, 3], 'C': [1]} 
    
    # Move 14 allowed between A and B
    # Moving disk 2 from A to B
    # {'A': [], 'B': [4, 3, 2], 'C': [1]} 
    
    # Move 15 allowed between B and C
    # Moving disk 1 from C to B
    # {'A': [], 'B': [4, 3, 2, 1], 'C': []} 


  ```

---

## Paso 38

Las condiciones que escribiste anteriormente solo son válidas para números impares de discos.

> Agrega un `if` anidado para ejecutar cuando `n` sea impar, y agrega un nivel de sangría a tus llamadas a `print()` y `make_allowed_move()`.

- **Codigo**
  
  ```py
    
    NUMBER_OF_DISKS = 4
    number_of_moves = 2**NUMBER_OF_DISKS - 1
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    
    def make_allowed_move(rod1, rod2):
          forward = False
          if not rods[rod2]:
              forward = True
          elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
              forward = True
          if forward:
              print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
              rods[rod2].append(rods[rod1].pop())
          else:
              print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
              rods[rod1].append(rods[rod2].pop())
          # display our progress
          print(rods,'\n')

    def move(n, source, auxiliary, target):
        # display starting configuration
        print(rods,'\n')
        for i in range(number_of_moves):
            remainder = (i + 1) % 3
            
    # Región editable por el usuario
            if remainder == 1:
                if n % 2 != 0:
                    print(f'Move {i + 1} allowed between {source} and {target}')
                    make_allowed_move(source, target)
    # Región editable por el usuario
            
            elif remainder == 2:
                print(f"Move {i + 1} allowed between {source} and {auxiliary}")
                make_allowed_move(source, auxiliary)
            elif remainder == 0:
                print(f'Move {i + 1} allowed between {auxiliary} and {target}')
                make_allowed_move(auxiliary, target)

    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
    # ----Salida esperada----
    # {'A': [4, 3, 2, 1], 'B': [], 'C': []}
    
    # Move 2 allowed between A and B
    # Moving disk 1 from A to B
    # {'A': [4, 3, 2], 'B': [1], 'C': []}
    
    # Move 3 allowed between B and C
    # Moving disk 1 from B to C
    # {'A': [4, 3, 2], 'B': [], 'C': [1]}
    
    # Move 5 allowed between A and B
    # Moving disk 2 from A to B
    # {'A': [4, 3], 'B': [2], 'C': [1]}
    
    # Move 6 allowed between B and C
    # Moving disk 1 from C to B
    # {'A': [4, 3], 'B': [2, 1], 'C': []}
    
    # Move 8 allowed between A and B
    # Moving disk 1 from B to A
    # {'A': [4, 3, 1], 'B': [2], 'C': []}
    
    # Move 9 allowed between B and C
    # Moving disk 2 from B to C
    # {'A': [4, 3, 1], 'B': [], 'C': [2]}
    
    # Move 11 allowed between A and B
    # Moving disk 1 from A to B
    # {'A': [4, 3], 'B': [1], 'C': [2]}
    
    # Move 12 allowed between B and C
    # Moving disk 1 from B to C
    # {'A': [4, 3], 'B': [], 'C': [2, 1]}
    
    # Move 14 allowed between A and B
    # Moving disk 3 from A to B
    # {'A': [4], 'B': [3], 'C': [2, 1]}
    
    # Move 15 allowed between B and C
    # Moving disk 1 from C to B
    # {'A': [4], 'B': [3, 1], 'C': [2]}


  ```

---

## Paso 39

> Si el número de discos es par y el resto es igual a `1`, se permite el movimiento entre la barra de origen y la barra auxiliar. Agrega una cláusula `else` para imprimir el movimiento permitido y llama a `make_allowed_move()` con los argumentos correctos.
>
> Si observa el resultado, verá que la ejecución se detiene en el tercer movimiento debido a un `IndexError`. Esto ocurre porque el código aún está incompleto y necesita una cláusula `else` que escribirá en breve. Para que funcione, convierta su llamada a `make_allowed_move()` en un comentario.

- **Codigo**
  
  ```py
    
    NUMBER_OF_DISKS = 4
    number_of_moves = 2**NUMBER_OF_DISKS - 1
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    
    def make_allowed_move(rod1, rod2):
          forward = False
          if not rods[rod2]:
              forward = True
          elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
              forward = True
          if forward:
              print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
              rods[rod2].append(rods[rod1].pop())
          else:
              print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
              rods[rod1].append(rods[rod2].pop())
          # display our progress
          print(rods,'\n')

    def move(n, source, auxiliary, target):
        # display starting configuration
        print(rods,'\n')
        for i in range(number_of_moves):
            remainder = (i + 1) % 3
            
    # Región editable por el usuario
            if remainder == 1:
                if n % 2 != 0:
                    print(f'Move {i + 1} allowed between {source} and {target}')
                    <!-- make_allowed_move(source, target) -->
                else:
                    print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                    # make_allowed_move(source, auxiliary)
    # Región editable por el usuario
            
            elif remainder == 2:
                print(f"Move {i + 1} allowed between {source} and {auxiliary}")
                make_allowed_move(source, auxiliary)
            elif remainder == 0:
                print(f'Move {i + 1} allowed between {auxiliary} and {target}')
                make_allowed_move(auxiliary, target)

    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
    # ----Salida esperada----
    # {'A': [4, 3, 2, 1], 'B': [], 'C': []}
    
    # Move 2 allowed between A and B
    # Moving disk 1 from A to B
    # {'A': [4, 3, 2], 'B': [1], 'C': []}
    
    # Move 3 allowed between B and C
    # Moving disk 1 from B to C
    # {'A': [4, 3, 2], 'B': [], 'C': [1]}
    
    # Move 5 allowed between A and B
    # Moving disk 2 from A to B
    # {'A': [4, 3], 'B': [2], 'C': [1]}
    
    # Move 6 allowed between B and C
    # Moving disk 1 from C to B
    # {'A': [4, 3], 'B': [2, 1], 'C': []}
    
    # Move 8 allowed between A and B
    # Moving disk 1 from B to A
    # {'A': [4, 3, 1], 'B': [2], 'C': []}
    
    # Move 9 allowed between B and C
    # Moving disk 2 from B to C
    # {'A': [4, 3, 1], 'B': [], 'C': [2]}
    
    # Move 11 allowed between A and B
    # Moving disk 1 from A to B
    # {'A': [4, 3], 'B': [1], 'C': [2]}
    
    # Move 12 allowed between B and C
    # Moving disk 1 from B to C
    # {'A': [4, 3], 'B': [], 'C': [2, 1]}
    
    # Move 14 allowed between A and B
    # Moving disk 3 from A to B
    # {'A': [4], 'B': [3], 'C': [2, 1]}
    
    # Move 15 allowed between B and C
    # Moving disk 1 from C to B
    # {'A': [4], 'B': [3, 1], 'C': [2]}


  ```

---

## Paso 40

> Ahora debes hacer lo mismo con tu instrucción `elif`: coloca las llamadas a `print()` y `make_allowed_move()` dentro de una instrucción `if` para que se ejecuten cuando `n` sea impar.
>
> Además, convierte el comentario `# make_allowed_move(source, auxiliary)` en código.

- **Codigo**
  
  ```py
    
    NUMBER_OF_DISKS = 4
    number_of_moves = 2**NUMBER_OF_DISKS - 1
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    
    def make_allowed_move(rod1, rod2):
          forward = False
          if not rods[rod2]:
              forward = True
          elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
              forward = True
          if forward:
              print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
              rods[rod2].append(rods[rod1].pop())
          else:
              print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
              rods[rod1].append(rods[rod2].pop())
          # display our progress
          print(rods,'\n')

    def move(n, source, auxiliary, target):
        # display starting configuration
        print(rods,'\n')
        for i in range(number_of_moves):
            remainder = (i + 1) % 3
            
            if remainder == 1:
                if n % 2 != 0:
                    print(f'Move {i + 1} allowed between {source} and {target}')
                    make_allowed_move(source, target)
    
    # Región editable por el usuario
                else:
                    print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                    make_allowed_move(source, auxiliary)
            
            elif remainder == 2:
                if n % 2 != 0:
                    print(f"Move {i + 1} allowed between {source} and {auxiliary}")
                    make_allowed_move(source, auxiliary)
    # Región editable por el usuario

            elif remainder == 0:
                print(f'Move {i + 1} allowed between {auxiliary} and {target}')
                make_allowed_move(auxiliary, target)

    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
    # ----Salida esperada----
    # {'A': [4, 3, 2, 1], 'B': [], 'C': []}
    
    # Move 1 allowed between A and B
    # Moving disk 1 from A to B
    # {'A': [4, 3, 2], 'B': [1], 'C': []}
    
    # Move 3 allowed between B and C
    # Moving disk 1 from B to C
    # {'A': [4, 3, 2], 'B': [], 'C': [1]}
    
    # Move 4 allowed between A and B
    # Moving disk 2 from A to B
    # {'A': [4, 3], 'B': [2], 'C': [1]}
    
    # Move 6 allowed between B and C
    # Moving disk 1 from C to B
    # {'A': [4, 3], 'B': [2, 1], 'C': []}
    
    # Move 7 allowed between A and B
    # Moving disk 1 from B to A
    # {'A': [4, 3, 1], 'B': [2], 'C': []}
    
    # Move 9 allowed between B and C
    # Moving disk 2 from B to C
    # {'A': [4, 3, 1], 'B': [], 'C': [2]}
    
    # Move 10 allowed between A and B
    # Moving disk 1 from A to B
    # {'A': [4, 3], 'B': [1], 'C': [2]}
    
    # Move 12 allowed between B and C
    # Moving disk 1 from B to C
    # {'A': [4, 3], 'B': [], 'C': [2, 1]}
    
    # Move 13 allowed between A and B
    # Moving disk 3 from A to B
    # {'A': [4], 'B': [3], 'C': [2, 1]}
    
    # Move 15 allowed between B and C
    # Moving disk 1 from C to B
    # {'A': [4], 'B': [3, 1], 'C': [2]}


  ```

---

## Paso 41

> Por último, agrega una cláusula `else` que imprima el movimiento permitido y llame a `make_allowed_move`. Intenta averiguar cuáles son los argumentos correctos.

- **Codigo**
  
  ```py
    
    NUMBER_OF_DISKS = 4
    number_of_moves = 2**NUMBER_OF_DISKS - 1
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    
    def make_allowed_move(rod1, rod2):
          forward = False
          if not rods[rod2]:
              forward = True
          elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
              forward = True
          if forward:
              print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
              rods[rod2].append(rods[rod1].pop())
          else:
              print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
              rods[rod1].append(rods[rod2].pop())
          # display our progress
          print(rods,'\n')

    def move(n, source, auxiliary, target):
        # display starting configuration
        print(rods,'\n')
        for i in range(number_of_moves):
            remainder = (i + 1) % 3
            
            if remainder == 1:
                if n % 2 != 0:
                    print(f'Move {i + 1} allowed between {source} and {target}')
                    make_allowed_move(source, target)
                else:
                    print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                    make_allowed_move(source, auxiliary)

    # Región editable por el usuario
            elif remainder == 2:
                if n % 2 != 0:
                    print(f"Move {i + 1} allowed between {source} and {auxiliary}")
                    make_allowed_move(source, auxiliary)
    # Región editable por el usuario

            elif remainder == 0:
                print(f'Move {i + 1} allowed between {auxiliary} and {target}')
                make_allowed_move(auxiliary, target)

    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
    # ----Salida esperada----
    # {'A': [4, 3, 2, 1], 'B': [], 'C': []}
    
    # Move 1 allowed between A and B
    # Moving disk 1 from A to B
    # {'A': [4, 3, 2], 'B': [1], 'C': []}
    
    # Move 2 allowed between A and C
    # Moving disk 2 from A to C
    # {'A': [4, 3], 'B': [1], 'C': [2]}
    
    # Move 3 allowed between B and C
    # Moving disk 1 from B to C
    # {'A': [4, 3], 'B': [], 'C': [2, 1]}
    
    # Move 4 allowed between A and B
    # Moving disk 3 from A to B
    # {'A': [4], 'B': [3], 'C': [2, 1]}
    
    # Move 5 allowed between A and C
    # Moving disk 1 from C to A
    # {'A': [4, 1], 'B': [3], 'C': [2]}
    
    # Move 6 allowed between B and C
    # Moving disk 2 from C to B
    # {'A': [4, 1], 'B': [3, 2], 'C': []}
    
    # Move 7 allowed between A and B
    # Moving disk 1 from A to B
    # {'A': [4], 'B': [3, 2, 1], 'C': []}
    
    # Move 8 allowed between A and C
    # Moving disk 4 from A to C
    # {'A': [], 'B': [3, 2, 1], 'C': [4]}
    
    # Move 9 allowed between B and C
    # Moving disk 1 from B to C
    # {'A': [], 'B': [3, 2], 'C': [4, 1]}
    
    # Move 10 allowed between A and B
    # Moving disk 2 from B to A
    # {'A': [2], 'B': [3], 'C': [4, 1]}
    
    # Move 11 allowed between A and C
    # Moving disk 1 from C to A
    # {'A': [2, 1], 'B': [3], 'C': [4]}
    
    # Move 12 allowed between B and C
    # Moving disk 3 from B to C
    # {'A': [2, 1], 'B': [], 'C': [4, 3]}
    
    # Move 13 allowed between A and B
    # Moving disk 1 from A to B
    # {'A': [2], 'B': [1], 'C': [4, 3]}
    
    # Move 14 allowed between A and C
    # Moving disk 2 from A to C
    # {'A': [], 'B': [1], 'C': [4, 3, 2]}
    
    # Move 15 allowed between B and C
    # Moving disk 1 from B to C
    # {'A': [], 'B': [], 'C': [4, 3, 2, 1]}


  ```

---

## Paso 42

Eso es todo para la solución iterativa. A partir de ahora, vas a crear una función que utilice un enfoque recursivo. La recursividad es cuando una función se llama a sí misma. En este caso, vas a utilizar la recursividad para calcular versiones más pequeñas del mismo problema.

> Elimina todo el cuerpo de la función `move`, excepto el comentario y la primera llamada a `print`. Deja la declaración de la función tal y como está.

- **Codigo**
  
  ```py
    
    NUMBER_OF_DISKS = 4
    number_of_moves = 2**NUMBER_OF_DISKS - 1
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    
    def make_allowed_move(rod1, rod2):
          forward = False
          if not rods[rod2]:
              forward = True
          elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
              forward = True
          if forward:
              print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
              rods[rod2].append(rods[rod1].pop())
          else:
              print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
              rods[rod1].append(rods[rod2].pop())
          # display our progress
          print(rods,'\n')

    # Región editable por el usuario
    def move(n, source, auxiliary, target):
        # display starting configuration
        print(rods,'\n')
    # Región editable por el usuario

    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
    # ----Salida esperada----
    # {'A': [4, 3, 2, 1], 'B': [], 'C': []}

  ```

---

## Paso 43

> Tampoco necesitarás `make_allowed_move` y `number_of_moves`. Elimina toda la función y la variable.

- **Codigo**
  
  ```py
    
    NUMBER_OF_DISKS = 4
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    

    def move(n, source, auxiliary, target):
        # display starting configuration
        print(rods,'\n')
    
    # Región editable por el usuario

    # Región editable por el usuario

    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
    # ----Salida esperada----
    # {'A': [4, 3, 2, 1], 'B': [], 'C': []}

  ```

---

## Paso 44

Para resolver el rompecabezas con recursividad, lo primero que hay que hacer es dividir el problema original en subproblemas más pequeños.

La configuración final con `n` discos apilados en la tercera varilla en orden descendente se puede obtener moviendo:

- `n - 1` discos de la varilla de origen a la varilla auxiliar
- el disco más grande de la varilla de origen a la varilla de destino
- y luego los `n - 1` discos de la varilla auxiliar a la varilla de destino.

Por lo tanto, lo primero que debe hacer la función `move` es llamarse a sí misma con `n - 1` como primer argumento. Pero si intentas hacerlo sin definir un caso base, obtendrás un error `RecursionError`. Esto ocurre porque la función se sigue llamando a sí misma indefinidamente.

> Antes de tu comentario y tu llamada a `print()`, añade la llamada a la función recursiva con `n - 1` como primer argumento y asegúrate de que el cuerpo de la función solo se ejecute cuando `n` sea mayor que cero. Por ahora, deja los demás argumentos en el mismo orden.

- **Codigo**
  
  ```py
    
    NUMBER_OF_DISKS = 4
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    

    def move(n, source, auxiliary, target):
    
    # Región editable por el usuario
        if n > 0:
            move(n - 1, source, auxiliary, target)
    # Región editable por el usuario

            # display starting configuration
            print(rods,'\n')
    
    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
    # ----Salida esperada----
    # {"A": [4, 3, 2, 1], "B": [], "C": []}
    
    # {"A": [4, 3, 2, 1], "B": [], "C": []}
    
    # {"A": [4, 3, 2, 1], "B": [], "C": []}
    
    # {"A": [4, 3, 2, 1], "B": [], "C": []}

  ```

---

## Paso 45

> Antes de la llamada recursiva, agrega un comentario que diga: `move n - 1 disks from source to auxiliary, so they are out of the way`.

- **Codigo**
  
  ```py
    
    NUMBER_OF_DISKS = 4
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    

    def move(n, source, auxiliary, target):
    
    # Región editable por el usuario
        if n > 0:
            # move n - 1 disks from source to auxiliary, so they are out of the way
            move(n - 1, source, auxiliary, target)
    # Región editable por el usuario

            # display starting configuration
            print(rods,'\n')
    
    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
    # ----Salida esperada----
    # {"A": [4, 3, 2, 1], "B": [], "C": []}
    
    # {"A": [4, 3, 2, 1], "B": [], "C": []}
    
    # {"A": [4, 3, 2, 1], "B": [], "C": []}
    
    # {"A": [4, 3, 2, 1], "B": [], "C": []}

  ```

---

## Paso 46

Los pasos para mover `n - 1` discos se pueden desglosar aún más hasta que solo se considere un único disco. Este será el primer movimiento que se realice. Después del primer movimiento, los siguientes movimientos se generan mediante el desarrollo de las llamadas recursivas. Tenga en cuenta que, en cada paso recursivo, la función que desempeñan las varillas cambia entre origen, destino y auxiliar.

> Por ahora, cada llamada recursiva imprime el diccionario `rods` sin realizar ningún cambio en las listas. Antes de la llamada `print()`, elimine el último elemento de la lista `rods[source]` y añádalo a la lista `rods[target]`.

- **Codigo**
  
  ```py
    
    NUMBER_OF_DISKS = 4
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    

    def move(n, source, auxiliary, target):
    
    # Región editable por el usuario
        if n > 0:
            # move n - 1 disks from source to auxiliary, so they are out of the way
            move(n - 1, source, auxiliary, target)
            rods[target].append(rods[source].pop())
    # Región editable por el usuario

            # display starting configuration
            print(rods,'\n')
    
    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
    # ----Salida esperada----
    # {"A": [4, 3, 2, 1], "B": [], "C": []}
    
    # {"A": [4, 3, 2, 1], "B": [], "C": []}
    
    # {"A": [4, 3, 2, 1], "B": [], "C": []}
    
    # {"A": [4, 3, 2, 1], "B": [], "C": []}

  ```

---

## Paso 47

Antes de añadir el último elemento al objetivo, añada un comentario que diga:`move the nth disk from source to target`

- **Codigo**
  
  ```py
    
    NUMBER_OF_DISKS = 4
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    

    def move(n, source, auxiliary, target):
    
    # Región editable por el usuario
        if n > 0:
            # move n - 1 disks from source to auxiliary, so they are out of the way
            move(n - 1, source, auxiliary, target)
            # move the nth disk from source to target
            rods[target].append(rods[source].pop())
    # Región editable por el usuario

            # display starting configuration
            print(rods,'\n')
    
    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
    # ----Salida esperada----
    # {"A": [4, 3, 2, 1], "B": [], "C": []}
    
    # {"A": [4, 3, 2, 1], "B": [], "C": []}
    
    # {"A": [4, 3, 2, 1], "B": [], "C": []}
    
    # {"A": [4, 3, 2, 1], "B": [], "C": []}

  ```

---

## Paso 48

Ahora, cambia el comentario que está encima de la llamada a `print()` para mostrar `display our progress`.

- **Codigo**
  
  ```py
    
    NUMBER_OF_DISKS = 4
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    

    def move(n, source, auxiliary, target):
    
    # Región editable por el usuario
        if n > 0:
            # move n - 1 disks from source to auxiliary, so they are out of the way
            move(n - 1, source, auxiliary, target)
            # move the nth disk from source to target
            rods[target].append(rods[source].pop())
    # Región editable por el usuario

            # display our progress
            print(rods,'\n')
    
    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
    # ----Salida esperada----
    # {'A': [4, 3, 2], 'B': [], 'C': [1]} 

    # {'A': [4, 3], 'B': [], 'C': [1, 2]} 
    
    # {'A': [4], 'B': [], 'C': [1, 2, 3]} 
    
    # {'A': [], 'B': [], 'C': [1, 2, 3, 4]} 

  ```

---

## Paso 49

Al principio, la llamada recursiva que acabas de agregar, se ocupa del subproblema de mover `n - 1` discos a la segunda barra.

Por esa razón, el argumento de `target` corresponde a tu segunda barra, mientras que el argumento `auxiliary` es la tercera barra. Ten en cuenta que estos seguirán intercambiándose a medida que avance la recursión.

> Fija el orden de los argumentos intercambiando el de `target` y el de `auxiliary` en tu llamada recursiva.

- **Codigo**
  
  ```py
    
    NUMBER_OF_DISKS = 4
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    

    # Región editable por el usuario
    def move(n, source, auxiliary, target):
        if n > 0:
            # move n - 1 disks from source to auxiliary, so they are out of the way
            move(n - 1, source, target, auxiliary)
                
            # move the nth disk from source to target
            rods[target].append(rods[source].pop())

            # display our progress
            print(rods,'\n')
    # Región editable por el usuario
    
    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
    # ----Salida esperada----
    # {'A': [4, 3, 2], 'B': [1], 'C': []} 
    
    # {'A': [4, 3], 'B': [1], 'C': [2]} 
    
    # {'A': [4], 'B': [1, 3], 'C': [2]} 
    
    # {'A': [], 'B': [1, 3], 'C': [2, 4]} 

  ```

---

## Paso 50

En un paso anterior, escribiste el código para mover el disco más grande del subproblema a la barra de destino.

> Ahora, todo lo que tienes que hacer es añadir otra llamada recursiva para mover los `n - 1` discos que ya has desplazado. Copia la primera llamada recursiva y pégala al final del bloque `if`.
>
> Ten en cuenta que los argumentos de la función no están en el orden correcto. Intenta averiguar el orden correcto.

- **Codigo**
  
  ```py
    
    NUMBER_OF_DISKS = 4
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    

    # Región editable por el usuario
    def move(n, source, auxiliary, target):
        if n > 0:
            # move n - 1 disks from source to auxiliary, so they are out of the way
            move(n - 1, source, target, auxiliary)

            # move the nth disk from source to target
            rods[target].append(rods[source].pop())

            # display our progress
            print(rods,'\n')

            move(n - 1, auxiliary, source, target)
    # Región editable por el usuario
    
    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
    # ----Salida esperada----
    # {'A': [4, 3, 2], 'B': [1], 'C': []}
    
    # {'A': [4, 3], 'B': [1], 'C': [2]}
    
    # {'A': [4, 3], 'B': [], 'C': [2, 1]}
    
    # {'A': [4], 'B': [3], 'C': [2, 1]}
    
    # {'A': [4, 1], 'B': [3], 'C': [2]}
    
    # {'A': [4, 1], 'B': [3, 2], 'C': []}
    
    # {'A': [4], 'B': [3, 2, 1], 'C': []}
    
    # {'A': [], 'B': [3, 2, 1], 'C': [4]}
    
    # {'A': [], 'B': [3, 2], 'C': [4, 1]}
    
    # {'A': [2], 'B': [3], 'C': [4, 1]}
    
    # {'A': [2, 1], 'B': [3], 'C': [4]}
    
    # {'A': [2, 1], 'B': [], 'C': [4, 3]}
    
    # {'A': [2], 'B': [1], 'C': [4, 3]}
    
    # {'A': [], 'B': [1], 'C': [4, 3, 2]}
    
    # {'A': [], 'B': [], 'C': [4, 3, 2, 1]}

  ```

---

## Paso 51

Por encima de la segunda llamada de `move`, agrega un último comentario que diga: `move the n - 1 disks that we left on auxiliary onto target`.

- **Codigo**
  
  ```py
    
    NUMBER_OF_DISKS = 4
    rods = {
        'A': list(range(NUMBER_OF_DISKS, 0, -1)),
        'B': [],
        'C': []
    }
    

    # Región editable por el usuario
    def move(n, source, auxiliary, target):
        if n > 0:
            # move n - 1 disks from source to auxiliary, so they are out of the way
            move(n - 1, source, target, auxiliary)

            # move the nth disk from source to target
            rods[target].append(rods[source].pop())

            # display our progress
            print(rods,'\n')

            #  move the n - 1 disks that we left on auxiliary onto target
            move(n - 1, auxiliary, source, target)
    # Región editable por el usuario
    
    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, 'A', 'B', 'C')
 
    # ----Salida esperada----
    # {'A': [4, 3, 2], 'B': [1], 'C': []}
    
    # {'A': [4, 3], 'B': [1], 'C': [2]}
    
    # {'A': [4, 3], 'B': [], 'C': [2, 1]}
    
    # {'A': [4], 'B': [3], 'C': [2, 1]}
    
    # {'A': [4, 1], 'B': [3], 'C': [2]}
    
    # {'A': [4, 1], 'B': [3, 2], 'C': []}
    
    # {'A': [4], 'B': [3, 2, 1], 'C': []}
    
    # {'A': [], 'B': [3, 2, 1], 'C': [4]}
    
    # {'A': [], 'B': [3, 2], 'C': [4, 1]}
    
    # {'A': [2], 'B': [3], 'C': [4, 1]}
    
    # {'A': [2, 1], 'B': [3], 'C': [4]}
    
    # {'A': [2, 1], 'B': [], 'C': [4, 3]}
    
    # {'A': [2], 'B': [1], 'C': [4, 3]}
    
    # {'A': [], 'B': [1], 'C': [4, 3, 2]}
    
    # {'A': [], 'B': [], 'C': [4, 3, 2, 1]}

  ```

---

## Paso 52

> Ahora, elimine el diccionario `rods` y convierta sus claves en las variables `A`, `B` y `C`, respectivamente, conservando sus valores. Reestructure su código para reflejar estos cambios. Si ve el resultado en la terminal, ha realizado correctamente este paso.

- **Codigo**

```py
    NUMBER_OF_DISKS = 4
    A = list(range(NUMBER_OF_DISKS, 0, -1))
    B = []
    C = []

    # Región editable por el usuario
    def move(n, source, auxiliary, target):
        if n > 0:
            # move n - 1 disks from source to auxiliary, so they are out of the way
            move(n - 1, source, target, auxiliary)

            # move the nth disk from source to target
            target.append(source.pop())

            # display our progress
            print(A, B, C, '\n')

            #  move the n - 1 disks that we left on auxiliary onto target
            move(n - 1, auxiliary, source, target)
    # Región editable por el usuario

    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, A, B, C)

    # ----Salida esperada----
    # [4, 3, 2] [1] []
    
    # [4, 3] [1] [2]
    
    # [4, 3] [] [2, 1]
    
    # [4] [3] [2, 1]
    
    # [4, 1] [3] [2]
    
    # [4, 1] [3, 2] []
    
    # [4] [3, 2, 1] []
    
    # [] [3, 2, 1] [4]
    
    # [] [3, 2] [4, 1]
    
    # [2] [3] [4, 1]
    
    # [2, 1] [3] [4]
    
    # [2, 1] [] [4, 3]
    
    # [2] [1] [4, 3]
    
    # [] [1] [4, 3, 2]
    
    # [] [] [4, 3, 2, 1]

  ```

---

## Paso 53

Aunque la recursividad a veces puede ser menos fácil de entender, te da el poder de crear código más conciso. En este caso, ni siquiera necesitas diferenciar entre números pares e impares de discos.

Establece `NUMBER_OF_DISKS` en 5 y comprueba el resultado.

- **Codigo**

```py
    NUMBER_OF_DISKS = 5
    A = list(range(NUMBER_OF_DISKS, 0, -1))
    B = []
    C = []

    # Región editable por el usuario
    def move(n, source, auxiliary, target):
        if n > 0:
            # move n - 1 disks from source to auxiliary, so they are out of the way
            move(n - 1, source, target, auxiliary)

            # move the nth disk from source to target
            target.append(source.pop())

            # display our progress
            print(A, B, C, '\n')

            #  move the n - 1 disks that we left on auxiliary onto target
            move(n - 1, auxiliary, source, target)
    # Región editable por el usuario

    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, A, B, C)

    # ----Salida esperada----
    # [5, 4, 3, 2] [] [1]
    
    # [5, 4, 3] [2] [1]
    
    # [5, 4, 3] [2, 1] []
    
    # [5, 4] [2, 1] [3]
    
    # [5, 4, 1] [2] [3]
    
    # [5, 4, 1] [] [3, 2]
    
    # [5, 4] [] [3, 2, 1]
    
    # [5] [4] [3, 2, 1]
    
    # [5] [4, 1] [3, 2]
    
    # [5, 2] [4, 1] [3]
    
    # [5, 2, 1] [4] [3]
    
    # [5, 2, 1] [4, 3] []
    
    # [5, 2] [4, 3] [1]
    
    # [5] [4, 3, 2] [1]
    
    # [5] [4, 3, 2, 1] []
    
    # [] [4, 3, 2, 1] [5]
    
    # [1] [4, 3, 2] [5]
    
    # [1] [4, 3] [5, 2]
    
    # [] [4, 3] [5, 2, 1]
    
    # [3] [4] [5, 2, 1]
    
    # [3] [4, 1] [5, 2]
    
    # [3, 2] [4, 1] [5]
    
    # [3, 2, 1] [4] [5]
    
    # [3, 2, 1] [] [5, 4]
    
    # [3, 2] [] [5, 4, 1]
    
    # [3] [2] [5, 4, 1]
    
    # [3] [2, 1] [5, 4]
    
    # [] [2, 1] [5, 4, 3]
    
    # [1] [2] [5, 4, 3]
    
    # [1] [] [5, 4, 3, 2]
    
    # [] [] [5, 4, 3, 2, 1]

  ```

---

## Paso 54

Todavía hay una cosa que puedes hacer para mejorar la legibilidad de tu código.

Modifica tu `if` para que se ejecute cuando `n` sea menor o igual a cero y añade una instrucción `return` para detener la ejecución de la función.

- **Codigo**

```py
    NUMBER_OF_DISKS = 5
    A = list(range(NUMBER_OF_DISKS, 0, -1))
    B = []
    C = []

    # Región editable por el usuario
    def move(n, source, auxiliary, target):
        if n <= 0:
            return
    # Región editable por el usuario

            # move n - 1 disks from source to auxiliary, so they are out of the way
            move(n - 1, source, target, auxiliary)

            # move the nth disk from source to target
            target.append(source.pop())

            # display our progress
            print(A, B, C, '\n')

            #  move the n - 1 disks that we left on auxiliary onto target
            move(n - 1, auxiliary, source, target)

    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, A, B, C)

    # ----Salida esperada----
    # []

  ```

---

## Paso 55

> Como paso final, reduce el nivel de sangría de todo el código después de la instrucción return.

**Bien hecho. Has completado el proyecto práctico Torre de Hanoi.**

- **Codigo**

```py
    # Región editable por el usuario
    NUMBER_OF_DISKS = 5
    A = list(range(NUMBER_OF_DISKS, 0, -1))
    B = []
    C = []

    def move(n, source, auxiliary, target):
        if n <= 0:
            return
            # move n - 1 disks from source to auxiliary, so they are out of the way
            move(n - 1, source, target, auxiliary)

            # move the nth disk from source to target
            target.append(source.pop())

            # display our progress
            print(A, B, C, '\n')

            #  move the n - 1 disks that we left on auxiliary onto target
            move(n - 1, auxiliary, source, target)

    # initiate call from source A to target C with auxiliary B
    move(NUMBER_OF_DISKS, A, B, C)
    # Región editable por el usuario

    # ----Salida esperada----
    # [5, 4, 3, 2] [] [1]
    
    # [5, 4, 3] [2] [1]
    
    # [5, 4, 3] [2, 1] []
    
    # [5, 4] [2, 1] [3]
    
    # [5, 4, 1] [2] [3]
    
    # [5, 4, 1] [] [3, 2]
    
    # [5, 4] [] [3, 2, 1]
    
    # [5] [4] [3, 2, 1]
    
    # [5] [4, 1] [3, 2]
    
    # [5, 2] [4, 1] [3]
    
    # [5, 2, 1] [4] [3]
    
    # [5, 2, 1] [4, 3] []
    
    # [5, 2] [4, 3] [1]
    
    # [5] [4, 3, 2] [1]
    
    # [5] [4, 3, 2, 1] []
    
    # [] [4, 3, 2, 1] [5]
    
    # [1] [4, 3, 2] [5]
    
    # [1] [4, 3] [5, 2]
    
    # [] [4, 3] [5, 2, 1]
    
    # [3] [4] [5, 2, 1]
    
    # [3] [4, 1] [5, 2]
    
    # [3, 2] [4, 1] [5]
    
    # [3, 2, 1] [4] [5]
    
    # [3, 2, 1] [] [5, 4]
    
    # [3, 2] [] [5, 4, 1]
    
    # [3] [2] [5, 4, 1]
    
    # [3] [2, 1] [5, 4]
    
    # [] [2, 1] [5, 4, 3]
    
    # [1] [2] [5, 4, 3]
    
    # [1] [] [5, 4, 3, 2]
    
    # [] [] [5, 4, 3, 2, 1]

  ```

---
