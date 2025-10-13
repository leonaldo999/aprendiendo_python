# Aprenda el método de bisección encontrando la raíz cuadrada de un número

Los métodos numéricos se utilizan para aproximar soluciones a problemas matemáticos que son difíciles o imposibles de resolver analíticamente.

En este proyecto, explorarás el método numérico de bisección para hallar la raíz cuadrada de un número, reduciendo iterativamente el rango posible de valores que contienen la raíz cuadrada.

---

## Paso 1

En este proyecto, hallarás la *raíz cuadrada* aproximada de un número dado utilizando el *método de bisección*.

El método de bisección es una técnica para hallar las raíces de una función de valor real. Funciona reduciendo el intervalo en el que se encuentra la raíz cuadrada hasta que converge en un valor dentro de una tolerancia especificada.

> Comienza creando una función llamada `square_root_bisection`. Deja los parámetros vacíos por ahora.

- *Codigo*

  ```py
  # Región editable por el usuario
  def square_root_bisection():
      pass
  # Región editable por el usuario
  ```

---

## Paso 2

> Proporcione a la función `square_root_bisection` los siguientes parámetros:

- `square_target`: El número del que desea hallar la raíz cuadrada.
- `tolerance` (opcional): La diferencia aceptable entre el cuadrado del valor aproximado de la raíz y el valor objetivo real (el valor predeterminado es `1e-7`). La tolerancia `1e-7` implica que la solución tendrá una precisión de `0.0000001` con respecto al valor real y es una buena opción predeterminada que equilibra la precisión y el rendimiento.
- `max_iterations` (opcional): el número máximo de iteraciones que se deben realizar (el valor predeterminado es `100`). Si el método no converge dentro de este límite, se asumirá que no se ha encontrado la solución.

- *Codigo*

  ```py
  # Región editable por el usuario
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      pass
  # Región editable por el usuario
  ```

---

## Paso 3

Si el número del que quieres hallar la raíz cuadrada es negativo, el código debería generar un error, ya que la raíz cuadrada de un número negativo no está definida en los números reales.

> Elimina la instrucción `pass` y crea una instrucción `if` para comprobar si `square_target` es menor que `0`.

- *Codigo*

  ```py
  # Región editable por el usuario
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      if square_target < 0:
          pass
  # Región editable por el usuario
  ```

---

## Paso 4

La instrucción `raise` permite forzar la aparición de una excepción específica. Consiste en la palabra clave `raise` seguida del tipo de excepción y permite proporcionar un mensaje de error personalizado:

- *Codigo Ejemplo*

  ```py
  raise ValueError("Invalid value")
  ```

Cuando se ejecuta el código anterior, se genera un `raise` `ValueError` y se muestra al usuario el mensaje `"Invalid value"`.

> Si `square_target` es menor que `0`, no se puede calcular la raíz cuadrada con valor real. Por lo tanto, genera un `'Square root of negative number is not defined in real numbers'`. No olvides eliminar la palabra clave `pass`.

- *Codigo*

  ```py
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      if square_target < 0:
  # Región editable por el usuario
          raise ValueError(
              "Square root of negative number is not defined in real numbers"
        )
  # Región editable por el usuario
  ```

---

## Paso 5

Crearás casos separados para cuando `square_target` sea `0` o `1`.

> Comienza creando una instrucción `if` para comprobar si `square_target` es igual a `1`.

- *Codigo*

  ```py
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      if square_target < 0:
          raise ValueError(
              "Square root of negative number is not defined in real numbers"
        )
  # Región editable por el usuario
      if square_target == 1:
        pass
  # Región editable por el usuario
  ```

---

## Paso 6

> Si `square_target` es igual a `1`, declara una variable `root` y asígnale el valor `1`. Además, imprime el mensaje `'The square root of {square_target} is 1'`. Recuerda dar formato al mensaje utilizando una f-string.

- *Codigo*

  ```py
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      if square_target < 0:
          raise ValueError(
              "Square root of negative number is not defined in real numbers"
        )
      if square_target == 1:
  # Región editable por el usuario
          root = 1
          print(f"The square root of {square_target} is 1")
  # Región editable por el usuario
  ```

---

## Paso 7

> Cree una instrucción `elif` para comprobar si `square_target` es igual a `0`. Si lo es, asigne el valor `0` a la variable `root`. Además, imprima el mensaje `'The square root of {square_target} is 0'`. Recuerde dar formato al mensaje utilizando una *f-string*.

- *Codigo*

  ```py
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      if square_target < 0:
          raise ValueError(
              "Square root of negative number is not defined in real numbers"
        )
      if square_target == 1:
        root = 1
        print(f"The square root of {square_target} is 1")
  # Región editable por el usuario
      elif square_target == 0:
          root = 0
          print(f"The square root of {square_target} is 0")
  # Región editable por el usuario
  ```

---

## Paso 8

A continuación, vas a trabajar en los casos en los que `square_target` es un número positivo distinto de `1` o `0`.

> Crea una cláusula `else` para manejar estos casos.

- *Codigo*

  ```py
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      if square_target < 0:
          raise ValueError(
              "Square root of negative number is not defined in real numbers"
        )
      if square_target == 1:
        root = 1
        print(f"The square root of {square_target} is 1")
      elif square_target == 0:
          root = 0
          print(f"The square root of {square_target} is 0")
  # Región editable por el usuario
      else:
         pass
  # Región editable por el usuario
  ```

---

## Paso 9

En Python, la función `max()` devuelve el mayor de los valores introducidos.

- *Codigo Ejemplo*

  ```py
  max(1, 2, 3) # Output: 3
  ```

Las variables `low` y `high` se utilizarán para definir el intervalo inicial en el que se encuentra la raíz cuadrada.

> Dentro de la cláusula `else`, inicializa la variable `low` a `0` y la variable `high` al máximo`max()` entre `1` y `square_target`, ya que la raíz cuadrada de un número siempre es menor o igual que el número en sí.

- *Codigo*

  ```py
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      if square_target < 0:
          raise ValueError(
              "Square root of negative number is not defined in real numbers"
        )
      if square_target == 1:
        root = 1
        print(f"The square root of {square_target} is 1")
      elif square_target == 0:
          root = 0
          print(f"The square root of {square_target} is 0")
  # Región editable por el usuario
      else:
          low = 0
          high = max(1, square_target)
  # Región editable por el usuario
  ```

---

## Paso 10

> Establezca el valor de `root` en `None`, ya que en este momento aún no tiene un valor aproximado.

- *Codigo*

  ```py
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      if square_target < 0:
          raise ValueError(
              "Square root of negative number is not defined in real numbers"
        )
      if square_target == 1:
        root = 1
        print(f"The square root of {square_target} is 1")
      elif square_target == 0:
          root = 0
          print(f"The square root of {square_target} is 0")
  # Región editable por el usuario
      else:
          low = 0
          high = max(1, square_target)
          root = None
  # Región editable por el usuario
  ```

---

## Paso 11

Ahora reducirás repetidamente el intervalo buscando el punto medio del intervalo actual y comparando el cuadrado del punto medio con el valor objetivo.

> Para ello, dentro del bloque `else`, crea un bucle `for` que se ejecute hasta `max_iterations` veces.
>
> Para q tu bucle, utiliza la función `range`, que genera una secuencia de números sobre la que puedes iterar. La sintaxis es `range(start, stop, step)`, donde `start` es el entero inicial (incluido), `stop` es el último entero (no incluido) y `step` es la diferencia entre un número y el anterior en la secuencia.
>
> Además, usa (`_`) como variable de bucle. El (`_`) actúa como un marcador de posición y es útil cuando necesitas usar una variable, pero en realidad no necesitas su valor.

- *Codigo*

  ```py
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      if square_target < 0:
          raise ValueError(
              "Square root of negative number is not defined in real numbers"
        )
      if square_target == 1:
        root = 1
        print(f"The square root of {square_target} is 1")
      elif square_target == 0:
          root = 0
          print(f"The square root of {square_target} is 0")
  # Región editable por el usuario
      else:
          low = 0
          high = max(1, square_target)
          root = None
          for _ in range(max_iterations):
              pass
  # Región editable por el usuario
  ```

---

## Paso 12

> Dentro del bucle `for`, calcula el punto medio del intervalo que va de `low` a `high`. Asigna este valor a una variable `mid`.
>
> Además, calcula el cuadrado del punto medio (`mid`) y guárdalo en la variable `square_mid`.

- *Codigo*

  ```py
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      if square_target < 0:
          raise ValueError(
              "Square root of negative number is not defined in real numbers"
        )
      if square_target == 1:
        root = 1
        print(f"The square root of {square_target} is 1")
      elif square_target == 0:
          root = 0
          print(f"The square root of {square_target} is 0")
  # Región editable por el usuario
      else:
          low = 0
          high = max(1, square_target)
          root = None
          for _ in range(max_iterations):
              mid = (low + high) / 2
              square_mid = mid**2
  # Región editable por el usuario
  ```

---

## Paso 13

La función `abs()` devuelve el valor absoluto de un número, que siempre es positivo, independientemente del signo del número. La utilizará para comprobar que la raíz cuadrada estimada se aproxima lo suficiente al valor real.

> Ahora, cree una instrucción `if` para comprobar si el valor absoluto de la diferencia entre `square_mid` y `square_target` se encuentra dentro de la `tolerance`.

- *Codigo*

  ```py
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      if square_target < 0:
          raise ValueError(
              "Square root of negative number is not defined in real numbers"
        )
      if square_target == 1:
        root = 1
        print(f"The square root of {square_target} is 1")
      elif square_target == 0:
          root = 0
          print(f"The square root of {square_target} is 0")
  # Región editable por el usuario
      else:
          low = 0
          high = max(1, square_target)
          root = None
          for _ in range(max_iterations):
              mid = (low + high) / 2
              square_mid = mid**2
              if abs(square_mid - square_target) < tolerance:
                  pass
  # Región editable por el usuario
  ```

---

## Paso 14

> Si la diferencia está dentro de la `tolerance` especificada, establezca el valor de `root` en `mid` y use `break` para salir del bucle.

- *Codigo*

  ```py
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      if square_target < 0:
          raise ValueError(
              "Square root of negative number is not defined in real numbers"
        )
      if square_target == 1:
        root = 1
        print(f"The square root of {square_target} is 1")
      elif square_target == 0:
          root = 0
          print(f"The square root of {square_target} is 0")
      else:
          low = 0
          high = max(1, square_target)
          root = None
          for _ in range(max_iterations):
              mid = (low + high) / 2
              square_mid = mid**2
  # Región editable por el usuario
              if abs(square_mid - square_target) < tolerance:
                  root = mid
                  break
  # Región editable por el usuario
  ```

---

## Paso 15

> Si la diferencia no está dentro de la `tolerance` especificada, cree una instrucción `elif` para comprobar si `square_mid` es menor que `square_target`.
>
> Asigne el valor de `mid` a `low`, ya que la raíz cuadrada ahora se encontraría entre `low` y `mid`.

- *Codigo*

  ```py
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      if square_target < 0:
          raise ValueError(
              "Square root of negative number is not defined in real numbers"
        )
      if square_target == 1:
        root = 1
        print(f"The square root of {square_target} is 1")
      elif square_target == 0:
          root = 0
          print(f"The square root of {square_target} is 0")
      else:
          low = 0
          high = max(1, square_target)
          root = None
          for _ in range(max_iterations):
              mid = (low + high) / 2
              square_mid = mid**2
  # Región editable por el usuario
              if abs(square_mid - square_target) < tolerance:
                  root = mid
                  break
              elif square_mid < square_target:
                  low = mid
  # Región editable por el usuario
  ```

---

## Paso 16

> Si no se cumplen las condiciones `if` y `elif`, el valor de `mid` sería mayor que `square_target`. En este caso, crea una cláusula `else` y asigna el valor de `mid` a `high`.

- *Codigo*

  ```py
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      if square_target < 0:
          raise ValueError(
              "Square root of negative number is not defined in real numbers"
        )
      if square_target == 1:
        root = 1
        print(f"The square root of {square_target} is 1")
      elif square_target == 0:
          root = 0
          print(f"The square root of {square_target} is 0")
      else:
          low = 0
          high = max(1, square_target)
          root = None
          for _ in range(max_iterations):
              mid = (low + high) / 2
              square_mid = mid**2
  # Región editable por el usuario
              if abs(square_mid - square_target) < tolerance:
                  root = mid
                  break
              elif square_mid < square_target:
                  low = mid
              else:
                  high = mid
  # Región editable por el usuario
  ```

---

## Paso 17

En Python, la palabra clave `is` comprueba la identidad de los objetos. Se utiliza para determinar si dos variables apuntan al mismo objeto en la memoria. A diferencia de `is`, el operador de igualdad (`==`) determina si los valores de dos objetos son iguales, independientemente de si son el mismo objeto en la memoria.

> Fuera del bucle for, crea una instrucción `if` para comprobar si `root es None`. Si lo es, imprime el mensaje `'Failed to converge within {max_iterations} iterations.'`. Recuerda dar formato al mensaje utilizando una cadena f(`f-string`).

- *Codigo*

  ```py
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      if square_target < 0:
          raise ValueError(
              "Square root of negative number is not defined in real numbers"
        )
      if square_target == 1:
        root = 1
        print(f"The square root of {square_target} is 1")
      elif square_target == 0:
          root = 0
          print(f"The square root of {square_target} is 0")
      else:
          low = 0
          high = max(1, square_target)
          root = None
          for _ in range(max_iterations):
              mid = (low + high) / 2
              square_mid = mid**2
              if abs(square_mid - square_target) < tolerance:
                  root = mid
                  break
              elif square_mid < square_target:
                  low = mid
              else:
                  high = mid
  # Región editable por el usuario
          if root is None:
            print(f'Failed to converge within {max_iterations} iterations.')
  # Región editable por el usuario
  ```

---

## Paso 18

> Crea una cláusula `else` para manejar el caso en el que el valor de `root` no sea `None`, lo que indica que se ha encontrado una raíz(*root*). Si no es `None`, imprime el mensaje `'The square root of {square_target} is approximately {root}'`. Recuerda formatear utilizando una cadena f.

- *Codigo*

  ```py
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      if square_target < 0:
          raise ValueError(
              "Square root of negative number is not defined in real numbers"
        )
      if square_target == 1:
        root = 1
        print(f"The square root of {square_target} is 1")
      elif square_target == 0:
          root = 0
          print(f"The square root of {square_target} is 0")
      else:
          low = 0
          high = max(1, square_target)
          root = None
          for _ in range(max_iterations):
              mid = (low + high) / 2
              square_mid = mid**2
              if abs(square_mid - square_target) < tolerance:
                  root = mid
                  break
              elif square_mid < square_target:
                  low = mid
              else:
                  high = mid
  # Región editable por el usuario
          if root is None:
              print(f'Failed to converge within {max_iterations} iterations.')
          else:
              print(f'The square root of {square_target} is approximately {root}')
  # Región editable por el usuario
  ```

---

## Paso 19

> Por último, devuelve el valor de la raíz cuadrada desde la función `square_root_bisection`.

- *Codigo*

  ```py
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      if square_target < 0:
          raise ValueError(
              "Square root of negative number is not defined in real numbers"
        )
      if square_target == 1:
        root = 1
        print(f"The square root of {square_target} is 1")
      elif square_target == 0:
          root = 0
          print(f"The square root of {square_target} is 0")
      else:
          low = 0
          high = max(1, square_target)
          root = None
          for _ in range(max_iterations):
              mid = (low + high) / 2
              square_mid = mid**2
              if abs(square_mid - square_target) < tolerance:
                  root = mid
                  break
              elif square_mid < square_target:
                  low = mid
              else:
                  high = mid
          if root is None:
              print(f'Failed to converge within {max_iterations} iterations.')
          else:
              print(f'The square root of {square_target} is approximately {root}')
  # Región editable por el usuario
      return root
  # Región editable por el usuario
  ```

---

## Paso 20

> Fuera de la definición de la función, cree una variable `N` y asígnele el valor `16`.

- *Codigo*

  ```py
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      if square_target < 0:
          raise ValueError(
              "Square root of negative number is not defined in real numbers"
        )
      if square_target == 1:
        root = 1
        print(f"The square root of {square_target} is 1")
      elif square_target == 0:
          root = 0
          print(f"The square root of {square_target} is 0")
      else:
          low = 0
          high = max(1, square_target)
          root = None
          for _ in range(max_iterations):
              mid = (low + high) / 2
              square_mid = mid**2
              if abs(square_mid - square_target) < tolerance:
                  root = mid
                  break
              elif square_mid < square_target:
                  low = mid
              else:
                  high = mid
          if root is None:
              print(f'Failed to converge within {max_iterations} iterations.')
          else:
              print(f'The square root of {square_target} is approximately {root}')
      return root

  # Región editable por el usuario
  N = 16
  # Región editable por el usuario
  ```

---

## Paso 21

> Llama a la `función square_root_bisection` con la variable `N` como argumento. Esto imprimirá el resultado en la consola.

*Experimenta con valores más grandes.*

**Con esto, has implementado con éxito el método de bisección para encontrar la raíz cuadrada de un número.**

- *Codigo*

  ```py
  def square_root_bisection(square_target, tolerance = 1e-7, max_iterations = 100):
      if square_target < 0:
          raise ValueError(
              "Square root of negative number is not defined in real numbers"
        )
      if square_target == 1:
        root = 1
        print(f"The square root of {square_target} is 1")
      elif square_target == 0:
          root = 0
          print(f"The square root of {square_target} is 0")
      else:
          low = 0
          high = max(1, square_target)
          root = None
          for _ in range(max_iterations):
              mid = (low + high) / 2
              square_mid = mid**2
              if abs(square_mid - square_target) < tolerance:
                  root = mid
                  break
              elif square_mid < square_target:
                  low = mid
              else:
                  high = mid
          if root is None:
              print(f'Failed to converge within {max_iterations} iterations.')
          else:
              print(f'The square root of {square_target} is approximately {root}')
      return root

  N = 16
  # Región editable por el usuario
  square_root_bisection(N)
  # Región editable por el usuario

  # ---- Salida ----
  # The square root of 16 is approximately 4.0
  ```

---
