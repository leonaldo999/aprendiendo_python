# Aprenda estructuras de datos mediante la creación del algoritmo de ordenación por mezcla

El algoritmo de ordenación por fusión es un algoritmo de ordenación basado en el principio de divide y vencerás.

En este proyecto, aprenderás a interactuar con estructuras de datos ordenando una lista de números aleatorios mediante el algoritmo de ordenación por fusión.

---

## Paso 1

En este proyecto, aprenderás estructuras de datos mediante la creación del algoritmo de ordenación por fusión.

Se trata de un algoritmo de ordenación que utiliza el principio de `'divide y vencerás'` para ordenar colecciones de datos. Es decir, `'divide'` una colección en subpartes más pequeñas y `'vence'` a las subpartes ordenándolas de forma independiente, para luego fusionar las subpartes ordenadas.

> Crea una función llamada `merge_sort`. Esta función se encargará de ordenar una lista de números.
>
> Utiliza la palabra clave `pass` en el cuerpo de la función.

- **Codigo**

  ```py
  def merge_sort():
      pass
  ```

---

## Paso 2

> Necesitarás un parámetro que indique los datos que se van a ordenar. Crea un parámetro llamado `array` en la función `merge_sort`.

- **Codigo**

  ```py
  def merge_sort(array):
      pass
  ```

---

## Paso 3

El algoritmo de ordenación por mezcla realiza principalmente tres acciones:

- Dividir una secuencia de elementos sin ordenar en subpartes.
- Ordenar los elementos de las subpartes.
- Combinar las subpartes ordenadas.

Lo anterior se repite de forma recursiva hasta que las subpartes se combinan en una secuencia ordenada completa. Comencemos por dividir la secuencia.

> Primero, reemplaza la palabra clave `pass` por una variable `middle_point`. Utiliza el operador de división entera (`//`) para dividir la longitud de la lista del `array` por 2 y asigna el resultado a tu nueva variable `middle_point`. Recuerda sangrar tu código.

- **Codigo**

  ```py
  def merge_sort(array):
      middle_point = len(array) // 2
  ```

---

## Paso 4

En el paso anterior, obtuviste el punto medio. Puedes utilizarlo para dividir el `array` en dos y asignar cada parte a nuevas variables.

> Utiliza la sintaxis de corte para extraer la mitad izquierda del `array` y asignarla a una variable llamada `left_part`.

- **Codigo**

  ```py
  def merge_sort(array):
      middle_point = len(array) // 2
      left_part = array[:middle_point]
  ```

---

## Paso 5

> Utilice la sintaxis de corte para extraer la mitad derecha del `array` y asígnela a una variable llamada `right_part`.

- **Codigo**

  ```py
  def merge_sort(array):
      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]
  ```

---

## Paso 6

Ahora que ha dividido la lista de `array` en dos listas separadas, seguirá dividiendo cada lista hasta que cada elemento quede solo en su propia lista. Una lista con un solo número siempre está ordenada.

> Para ello, llame recursivamente a `merge_sort` dentro de su función. Por ahora, no pase ningún argumento.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort()
  ```

---

## Paso 7

> Pase `left_part` como argumento a la llamada `merge_sort()` que ha añadido en el último paso.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
  ```

---

## Paso 8

> Vuelve a llamar a la función `merge_sort()`. Por ahora, no le pases ningún argumento.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort()
  ```

---

## Paso 9

> Pase `right_part` como argumento a la llamada `merge_sort()` que ha añadido en el último paso.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  ```

---

## Paso 10

Ahora es el momento de ordenar y fusionar las listas (`left_part` y `right_part`) en el `array` original.

Puede hacerlo comparando los elementos de ambas listas y fusionando el elemento más pequeño con la lista principal. Va a realizar esta comparación para todos los índices de `left_part` y `right_part`.

> Cree tres variables: `left_array_index`, `right_array_index` y `sorted_index`, y establezca sus valores en `0`. Estas variables le ayudarán a realizar un seguimiento de cada índice durante el proceso de clasificación.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0
  ```

---

## Paso 11

> Dentro de la función, cree un bucle `while` que compare un elemento de `left_part` con un elemento de `right_part` y fusione el elemento más pequeño con la lista del `array` principal.
>
> Cree dos condiciones para el bucle: una que compruebe si `left_array_index` es menor que la longitud de `left_part` y otra que compruebe si `right_array_index` es menor que la longitud de `right_part`.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0

      while left_array_index < len(left_part) and right_array_index < len(right_part):
          pass
  ```

---

## Paso 12

> Dentro del bucle `while`, reemplaza `pass` por una instrucción `if` que compruebe si el índice de `left_part` es menor que el índice de `right_part`.
>
> Utiliza la palabra clave `pass` en el cuerpo de la instrucción `if`.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0

      while left_array_index < len(left_part) and right_array_index < len(right_part):
          if left_part[left_array_index] < right_part[right_array_index]:
              pass
  ```

---

## Paso 13

Cuando la condición `if` se evalúa como verdadera, significa que el elemento de la lista `left_part` es menor que el elemento con el que se compara en la lista `right_part`.

En ese caso, puede asignar el índice `left_part` al índice correspondiente en la lista del `array` principal.

> Dentro del bloque `if`, elimine `pass` y asigne `left_part[left_array_index]` a `array[sorted_index]`.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0

      while left_array_index < len(left_part) and right_array_index < len(right_part):
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
  ```

---

## Paso 14

> Después de asignar el índice `left_part` al `array` principal, incremente `left_array_index` en `1`.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0

      while left_array_index < len(left_part) and right_array_index < len(right_part):
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
  ```

---

## Paso 15

En un paso anterior, asignaste el elemento de la `left_part` a la lista del `array` porque era más pequeño. Pero esto no siempre será así. En algunos casos de comparación, el elemento de la derecha podría ser más pequeño.

> Crea una cláusula `else` para ejecutar cuando el `left_part` no sea menor que el `right_part`.
>
> Dentro del bloque `else`, asigne `right_part[right_array_index]` a `array[sorted_index]`.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0

      while left_array_index < len(left_part) and right_array_index < len(right_part):
      
      # Región editable por el usuario
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
          else:
              array[sorted_index] = right_part[right_array_index]
      # Región editable por el usuario
  ```

---

## Paso 16

> Sin salir del bloque `else`, incrementa `right_array_index` en `1`.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0
      while left_array_index < len(left_part) and right_array_index < len(right_part):
      
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
      
      # Región editable por el usuario
          else:
              array[sorted_index] = right_part[right_array_index]
              right_array_index += 1
      # Región editable por el usuario
  ```

---

## Paso 17

Las sentencias `if` y `else` que ha creado en los pasos anteriores asignarán elementos al `sorted array.`.

Cada elemento asignado al `sorted array.` ocupa un índice en la lista. Por lo tanto, debe pasar al siguiente índice sin elemento.

> Debajo del bloque `if`/`else`, pero aún dentro del bucle `while`, incremente `sorted_index` en `1`. Esto no debe estar en el cuerpo de la sentencia `if` o `else`.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0
      
      # Región editable por el usuario
      while left_array_index < len(left_part) and right_array_index < len(right_part):
      
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
          else:
              array[sorted_index] = right_part[right_array_index]
              right_array_index += 1
          sorted_index += 1
      # Región editable por el usuario
  ```

---

## Paso 18

El bucle `while` que ha creado compara un elemento de `left_part` con otro de `right_part` y, a continuación, añade el elemento más pequeño a la lista del `array` principal.

Continuará esta operación hasta que no queden elementos por comparar. Sin embargo, es posible que `left_part` aún tenga elementos, mientras que `right_part` no tenga ninguno, y viceversa.

> Cree otro bucle `while` para copiar los elementos restantes de `left_part` en la lista del `array`. Utilice `left_array_index < len(left_part)` para la condición `while`.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0
      
      while left_array_index < len(left_part) and right_array_index < len(right_part):
      
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
          else:
              array[sorted_index] = right_part[right_array_index]
              right_array_index += 1
          sorted_index += 1
      
      # Región editable por el usuario
      while left_array_index < len(left_part):
          pass
      # Región editable por el usuario
  ```

---

## Paso 19

> Elimine la palabra clave `pass`. Para el bloque de código del bucle `while`, asigne `left_part[left_array_index]` a `array[sorted_index]`.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0
      
      while left_array_index < len(left_part) and right_array_index < len(right_part):
      
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
          else:
              array[sorted_index] = right_part[right_array_index]
              right_array_index += 1
          sorted_index += 1
      
      # Región editable por el usuario
      while left_array_index < len(left_part):
          array[sorted_index] = left_part[left_array_index]
      # Región editable por el usuario
  ```

---

## Paso 20

> Sin salir del bucle `while`, incrementa el valor de `left_array_index` en `1`.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0
      
      while left_array_index < len(left_part) and right_array_index < len(right_part):
      
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
          else:
              array[sorted_index] = right_part[right_array_index]
              right_array_index += 1
          sorted_index += 1
      
      # Región editable por el usuario
      while left_array_index < len(left_part):
          array[sorted_index] = left_part[left_array_index]
          left_array_index += 1
      # Región editable por el usuario
  ```

---

## Paso 21

Lo último que hay que hacer para el bucle `while` es pasar al siguiente índice de la matriz ordenada.

Utilizando el operador de suma con asignación aumentada, suma `1` al valor de `sorted_index`.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0
      
      while left_array_index < len(left_part) and right_array_index < len(right_part):
      
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
          else:
              array[sorted_index] = right_part[right_array_index]
              right_array_index += 1
          sorted_index += 1
      
      # Región editable por el usuario
      while left_array_index < len(left_part):
          array[sorted_index] = left_part[left_array_index]
          left_array_index += 1
          sorted_index += 1
      # Región editable por el usuario
  ```

---

## Paso 22

Ahora, vas a replicar la misma lógica del bucle `while` para `right_part`.

> Crea un bucle `while` que se ejecute cuando `right_array_index` sea menor que `len(right_part)` y utiliza la palabra clave `pass` en el cuerpo del bucle.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0
      
      while left_array_index < len(left_part) and right_array_index < len(right_part):
      
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
          else:
              array[sorted_index] = right_part[right_array_index]
              right_array_index += 1
          sorted_index += 1
      
      while left_array_index < len(left_part):
          array[sorted_index] = left_part[left_array_index]
          left_array_index += 1
          sorted_index += 1
      
      # Región editable por el usuario
      while right_array_index < len(right_part):
          pass
      # Región editable por el usuario
  ```

---

## Paso 23

> Dentro del bucle `while`, asigne `right_part[right_array_index]` a `array[sorted_index]`.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0
      
      while left_array_index < len(left_part) and right_array_index < len(right_part):
      
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
          else:
              array[sorted_index] = right_part[right_array_index]
              right_array_index += 1
          sorted_index += 1
      
      while left_array_index < len(left_part):
          array[sorted_index] = left_part[left_array_index]
          left_array_index += 1
          sorted_index += 1
      
      # Región editable por el usuario
      while right_array_index < len(right_part):
          array[sorted_index] = right_part[right_array_index]
      # Región editable por el usuario
  ```

---

## Paso 24

> Ahora, usa el operador `+=` para incrementar `right_array_index` en `1`.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0
      
      while left_array_index < len(left_part) and right_array_index < len(right_part):
      
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
          else:
              array[sorted_index] = right_part[right_array_index]
              right_array_index += 1
          sorted_index += 1
      
      while left_array_index < len(left_part):
          array[sorted_index] = left_part[left_array_index]
          left_array_index += 1
          sorted_index += 1
      
      # Región editable por el usuario
      while right_array_index < len(right_part):
          array[sorted_index] = right_part[right_array_index]
          right_array_index += 1
      # Región editable por el usuario
  ```

---

## Paso 25

> Para el último paso del bucle `while`, incrementa `sorted_index` en `1`.

- **Codigo**

  ```py
  def merge_sort(array):

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0
      
      while left_array_index < len(left_part) and right_array_index < len(right_part):
      
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
          else:
              array[sorted_index] = right_part[right_array_index]
              right_array_index += 1
          sorted_index += 1
      
      while left_array_index < len(left_part):
          array[sorted_index] = left_part[left_array_index]
          left_array_index += 1
          sorted_index += 1
      
      # Región editable por el usuario
      while right_array_index < len(right_part):
          array[sorted_index] = right_part[right_array_index]
          right_array_index += 1
          sorted_index += 1
      # Región editable por el usuario
  ```

---

## Paso 26

Antes de probar la función `merge_sort()`, es necesario crear un caso base que detenga la ejecución de la función cuando la longitud de la matriz sea menor o igual a `1`.

Este caso base detendrá la llamada recursiva. Sin él, la operación de ordenación por fusión continuaría ejecutándose incluso cuando la lista ya estuviera ordenada o no tuviera ningún elemento.

> Justo después de la declaración de la función, cree una instrucción `if` con esta condición: `len(array) <= 1`. Utilice la palabra clave `pass` en el cuerpo de la función.

- **Codigo**

  ```py
  # Región editable por el usuario
  def merge_sort(array):
      if len(array) <= 1:
          pass
  # Región editable por el usuario

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0
      
      while left_array_index < len(left_part) and right_array_index < len(right_part):
      
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
          else:
              array[sorted_index] = right_part[right_array_index]
              right_array_index += 1
          sorted_index += 1
      
      while left_array_index < len(left_part):
          array[sorted_index] = left_part[left_array_index]
          left_array_index += 1
          sorted_index += 1
      
      while right_array_index < len(right_part):
          array[sorted_index] = right_part[right_array_index]
          right_array_index += 1
          sorted_index += 1
  ```

---

## Paso 27

> Reemplaza la palabra clave `pass` dentro de la instrucción `if` por una instrucción `return`. Esto detendrá la ejecución de la función `merge_sort` cuando la condición dada sea verdadera.

- **Codigo**

  ```py
  # Región editable por el usuario
  def merge_sort(array):
      if len(array) <= 1:
          return
  # Región editable por el usuario

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0
      
      while left_array_index < len(left_part) and right_array_index < len(right_part):
      
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
          else:
              array[sorted_index] = right_part[right_array_index]
              right_array_index += 1
          sorted_index += 1
      
      while left_array_index < len(left_part):
          array[sorted_index] = left_part[left_array_index]
          left_array_index += 1
          sorted_index += 1
      
      while right_array_index < len(right_part):
          array[sorted_index] = right_part[right_array_index]
          right_array_index += 1
          sorted_index += 1
  ```

---

## Paso 28

Puedes usar la variable `__name__` para determinar si un script de Python se está ejecutando como programa principal o si se está importando como módulo (código escrito en otro archivo Python).

Si el valor de `__name__` se establece en `'__main__'`, significa que el script actual es el programa principal y no un módulo.

En este proyecto, utilizará el script actual como programa principal.

> Cree una instrucción `if` que compruebe si el valor de `__name__` es `'__main__'`.
>
> Utilice la palabra clave `pass` en el cuerpo de la instrucción `if`.

- **Codigo**

  ```py
  def merge_sort(array):
      if len(array) <= 1:
          return

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0
      
      while left_array_index < len(left_part) and right_array_index < len(right_part):
      
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
          else:
              array[sorted_index] = right_part[right_array_index]
              right_array_index += 1
          sorted_index += 1
      
      while left_array_index < len(left_part):
          array[sorted_index] = left_part[left_array_index]
          left_array_index += 1
          sorted_index += 1
      
      while right_array_index < len(right_part):
          array[sorted_index] = right_part[right_array_index]
          right_array_index += 1
          sorted_index += 1
  
  # Región editable por el usuario
  if __name__ == '__main__':
      pass
  # Región editable por el usuario
  ```

---

## Paso 29

¡Es hora de probar la función `merge_sort`!

> Reemplaza `pass` por una lista llamada `numbers` y asígnale esta lista: `[4, 10, 6, 14, 2, 1, 8, 5]`

- **Codigo**

  ```py
  def merge_sort(array):
      if len(array) <= 1:
          return

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0
      
      while left_array_index < len(left_part) and right_array_index < len(right_part):
      
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
          else:
              array[sorted_index] = right_part[right_array_index]
              right_array_index += 1
          sorted_index += 1
      
      while left_array_index < len(left_part):
          array[sorted_index] = left_part[left_array_index]
          left_array_index += 1
          sorted_index += 1
      
      while right_array_index < len(right_part):
          array[sorted_index] = right_part[right_array_index]
          right_array_index += 1
          sorted_index += 1
  
  # Región editable por el usuario
  if __name__ == '__main__':
      numbers = [4, 10, 6, 14, 2, 1, 8, 5]
  # Región editable por el usuario
  ```

---

## Paso 30

> Utilice la función `print()` para imprimir la cadena `'Unsorted array:'`.

- **Codigo**

  ```py
  def merge_sort(array):
      if len(array) <= 1:
          return

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0
      
      while left_array_index < len(left_part) and right_array_index < len(right_part):
      
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
          else:
              array[sorted_index] = right_part[right_array_index]
              right_array_index += 1
          sorted_index += 1
      
      while left_array_index < len(left_part):
          array[sorted_index] = left_part[left_array_index]
          left_array_index += 1
          sorted_index += 1
      
      while right_array_index < len(right_part):
          array[sorted_index] = right_part[right_array_index]
          right_array_index += 1
          sorted_index += 1
  
  # Región editable por el usuario
  if __name__ == '__main__':
      numbers = [4, 10, 6, 14, 2, 1, 8, 5]
      print('Unsorted array:')
  # Región editable por el usuario

  # -------------Salida----------------
  # Unsorted array:
  ```

---

## Paso 31

> Vuelve a llamar a la función `print()` para imprimir la lista de `numbers`. Esto imprimirá la lista sin ordenar en la consola.

- **Codigo**

  ```py
  def merge_sort(array):
      if len(array) <= 1:
          return

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0
      
      while left_array_index < len(left_part) and right_array_index < len(right_part):
      
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
          else:
              array[sorted_index] = right_part[right_array_index]
              right_array_index += 1
          sorted_index += 1
      
      while left_array_index < len(left_part):
          array[sorted_index] = left_part[left_array_index]
          left_array_index += 1
          sorted_index += 1
      
      while right_array_index < len(right_part):
          array[sorted_index] = right_part[right_array_index]
          right_array_index += 1
          sorted_index += 1
  
  # Región editable por el usuario
  if __name__ == '__main__':
      numbers = [4, 10, 6, 14, 2, 1, 8, 5]
      print('Unsorted array:')
      print(numbers)
  # Región editable por el usuario

  # -------------Salida----------------
  # Unsorted array:
  # [4, 10, 6, 14, 2, 1, 8, 5]
  ```

---

## Paso 32

> Después de las llamadas a `print()`, llame a la función `merge_sort` y pase la lista de `numbers` como argumento.

- **Codigo**

  ```py
  def merge_sort(array):
      if len(array) <= 1:
          return

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0
      
      while left_array_index < len(left_part) and right_array_index < len(right_part):
      
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
          else:
              array[sorted_index] = right_part[right_array_index]
              right_array_index += 1
          sorted_index += 1
      
      while left_array_index < len(left_part):
          array[sorted_index] = left_part[left_array_index]
          left_array_index += 1
          sorted_index += 1
      
      while right_array_index < len(right_part):
          array[sorted_index] = right_part[right_array_index]
          right_array_index += 1
          sorted_index += 1
  
  # Región editable por el usuario
  if __name__ == '__main__':
      numbers = [4, 10, 6, 14, 2, 1, 8, 5]
      print('Unsorted array:')
      print(numbers)
      merge_sort(numbers)
  # Región editable por el usuario

  # -------------Salida----------------
  # Unsorted array:
  # [4, 10, 6, 14, 2, 1, 8, 5]
  ```

---

## Paso 33

> En este punto, la lista de `numbers` ya está ordenada. Llame a la función `print` para imprimir la cadena `'Sorted array: '` y la lista ordenada.
>
> Para ello, concatene `'Sorted array: '` y `str(números)` en la llamada a `print()`.

**Con esto, el algoritmo de ordenación por mezcla queda completado.**

- **Codigo**

  ```py
  def merge_sort(array):
      if len(array) <= 1:
          return

      middle_point = len(array) // 2
      left_part = array[:middle_point]
      right_part = array[middle_point:]

      merge_sort(left_part)
      merge_sort(right_part)
  
      left_array_index = 0
      right_array_index = 0
      sorted_index = 0
      
      while left_array_index < len(left_part) and right_array_index < len(right_part):
      
          if left_part[left_array_index] < right_part[right_array_index]:
              array[sorted_index] = left_part[left_array_index]
              left_array_index += 1
          else:
              array[sorted_index] = right_part[right_array_index]
              right_array_index += 1
          sorted_index += 1
      
      while left_array_index < len(left_part):
          array[sorted_index] = left_part[left_array_index]
          left_array_index += 1
          sorted_index += 1
      
      while right_array_index < len(right_part):
          array[sorted_index] = right_part[right_array_index]
          right_array_index += 1
          sorted_index += 1
  
  # Región editable por el usuario
  if __name__ == '__main__':
      numbers = [4, 10, 6, 14, 2, 1, 8, 5]
      print('Unsorted array:')
      print(numbers)
      merge_sort(numbers)
      print('Sorted array: ' + str(numbers))
  # Región editable por el usuario

  # -------------Salida----------------
  # Unsorted array:
  # [4, 10, 6, 14, 2, 1, 8, 5]
  # Sorted array: [1, 2, 4, 5, 6, 8, 10, 14]
  ```

---
