# Aprenda la comprensión de listas en Python creando un programa convertidor de mayúsculas y minúsculas

La comprensión de listas es una forma de construir una nueva lista de Python a partir de tipos iterables: listas(`lists`), tuplas(`tuples`) y cadenas(`strings`). Todo ello sin utilizar un bucle `for` ni el método de lista `.append()`.

En este proyecto, escribirás un programa que toma una cadena formateada en `Camel Case` o `Pascal Case` y la convierte en `Snake Case`.

El proyecto tiene dos fases: primero usarás un bucle `for` para implementar el programa. Luego aprenderás a usar la comprensión de listas en lugar de un bucle para lograr los mismos resultados.

---

## Paso 1

En este proyecto, vas a crear un programa que tome como entrada una cadena con formato `camelCase` o `PascalCase` y la convierta en una cadena con formato `snake_case` utilizando dos enfoques. Primero, usarás un bucle `for` y luego una comprensión de lista para lograr los mismos resultados. Verás cómo la comprensión de lista puede hacer que tu código sea más conciso.

> Comienza definiendo una nueva función llamada `convert_to_snake_case()` que acepte como entrada una cadena llamada `pascal_or_camel_cased_string`. Por ahora, añade una instrucción `pass` dentro de la función.

- *Codigo*

  ```py
  # solucion
  def convert_to_snake_case(pascal_or_camel_cased_string):
      pass
  # solucion
  ```

---

## Paso 2

Debes agregar una lista vacía que contenga los caracteres de la cadena después de haberlos convertido a *snake case*.

> Dentro de la función, reemplaza la instrucción `pass` creando una lista vacía llamada `snake_cased_char_list.`

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
    # solucion
      snake_cased_char_list = []"
    # solucion
  ```

---

## Paso 3

Con la lista vacía en su lugar, ahora puede comenzar a iterar a través de la cadena de entrada y convertirla a snake case.

> Dentro de la función, debajo de la lista que acaba de crear, agregue un bucle `for` para iterar a través de `pascal_or_camel_cased_string`. Asegúrese de nombrar la variable de destino `char`. Por ahora, agregue una instrucción `pass` como marcador de posición en el cuerpo del bucle.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
      snake_cased_char_list = []"
      # solucion
      for char in pascal_or_camel_cased_string:
          pass
      # solucion
  ```

---

## Paso 4

Tanto en camel case como en pascal case, las letras mayúsculas marcan el comienzo de nuevas palabras. Para convertir la cadena de entrada a snake case, deberá comprobar si los caracteres de la cadena de entrada están en mayúscula.

Puede utilizar el método de cadena `.isupper()` para comprobar si un carácter está en mayúscula. Este método devuelve `True` si el carácter está en mayúscula y `False` si no lo está.

*> Dentro del bucle `for`, agrega una instrucción `if` para verificar si el carácter actual está en mayúscula. Mueve la instrucción `pass` dentro de la nueva instrucción `if`.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
      snake_cased_char_list = []"
      for char in pascal_or_camel_cased_string:
        # solucion
          if char.isupper():
              pass
        # solucion
  ```

---

## Paso 5

Dentro del cuerpo de la instrucción `if`, debes convertir cualquier carácter en mayúscula a minúscula y anteponer un guión bajo a este carácter en minúscula.

> Utiliza el método de cadena `.lower()` para convertir los caracteres en mayúscula a minúscula. A continuación, antepone un guión bajo al carácter. Asigna los resultados a una variable denominada `converted_character`.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
      snake_cased_char_list = []"
      for char in pascal_or_camel_cased_string:
          if char.isupper():
        # Región editable por el usuario
              converted_character = "_" + char.lower()
        # Región editable por el usuario
  ```

---

## Paso 6

Dentro del cuerpo de la instrucción `if`, vas a agregar el carácter convertido a la lista que creaste anteriormente.

Para ello, se utilizará el método `.append()`. Este método agrega un objeto dado al final de la lista en la que se invoca.

> Utiliza el método `.append()` en `snake_cased_char_list` para agregar `converted_character` a la lista.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
      snake_cased_char_list = []"
      for char in pascal_or_camel_cased_string:
          if char.isupper():
              converted_character = "_" + char.lower()
        # Región editable por el usuario
              snake_cased_char_list.append(converted_character)
        # Región editable por el usuario
  ```

---

## Paso 7

Debes manejar los caracteres que ya están en minúscula añadiéndolos a la lista de caracteres convertidos.

> Justo después de la instrucción `if` dentro del bucle `for`, añade una cláusula `else` y utiliza el método `.append()` para añadir `char` a la variable `snake_cased_char_list`.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
      snake_cased_char_list = []"
      for char in pascal_or_camel_cased_string:
          if char.isupper():
              converted_character = "_" + char.lower()
              snake_cased_char_list.append(converted_character)
        # Región editable por el usuario
          else:
            snake_cased_char_list.append(char)
        # Región editable por el usuario
  ```

---

## Paso 8

En este punto, la variable `snake_cased_char_list` contiene la lista de caracteres convertidos. Para combinar estos caracteres en una sola cadena, puede utilizar el método `.join()`.

El método `join` funciona concatenando cada elemento de una lista en una cadena, separados por una cadena designada, conocida como separador.

- *Codigo Ejemplo*

  ```py
  result_string = ''.join(characters)
  ```

El ejemplo anterior une los elementos de la lista de `characters` en una sola cadena, donde cada elemento se concatena utilizando una cadena vacía como separador.

> Ahora, justo después del bucle `for`, utiliza el método `.join()` para unir los elementos de `snake_cased_char_list` utilizando una cadena vacía como separador. Asigna el resultado a una nueva variable llamada `snake_cased_string`.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
      snake_cased_char_list = []"
      for char in pascal_or_camel_cased_string:
          if char.isupper():
              converted_character = "_" + char.lower()
              snake_cased_char_list.append(converted_character)
          else:
            snake_cased_char_list.append(char)
      
      # Región editable por el usuario
      snake_cased_string = "".join(snake_cased_char_list)
      # Región editable por el usuario
  ```

---

## Paso 9

En el caso de Pascal, las cadenas comienzan con una letra mayúscula. Después de convertir todos los caracteres a minúsculas y añadirles un guión bajo, existe la posibilidad de que haya un guión bajo adicional al principio de la cadena.

La forma más fácil de solucionar esto es utilizando el método de cadena `.strip()`, que elimina de una cadena cualquier carácter inicial o final de entre un conjunto de caracteres pasados como argumento. Por ejemplo:

- *Codigo Ejemplo*

  ```py
  original_string = "_example_string_"

  clean_string = original_string.strip('_')
  ```

El método `strip()` se aplica a `original_string`. Esto elimina cualquier guión bajo inicial y final. El resultado del ejemplo anterior sería la cadena `'example_string'`.

> Declare una nueva variable llamada `clean_snake_cased_string` y asígnele el resultado del método `.strip()` aplicado a `snake_cased_string`, pasando `'_'` como argumento al método.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
      snake_cased_char_list = []"
      for char in pascal_or_camel_cased_string:
          if char.isupper():
              converted_character = "_" + char.lower()
              snake_cased_char_list.append(converted_character)
          else:
            snake_cased_char_list.append(char)
      
      snake_cased_string = "".join(snake_cased_char_list)
      # Región editable por el usuario
      clean_snake_cased_string = snake_cased_string.strip('_')
      # Región editable por el usuario
  ```

---

## Paso 10

Para finalizar la función, devuelve la cadena `clean_snake_cased_string`. Esto completará la función y te permitirá utilizarla para convertir cadenas de Pascal o Camel Case a Snake Case.

> Añade una instrucción `return` al final de la función para devolver la cadena `clean_snake_cased_string`.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
      snake_cased_char_list = []"
      for char in pascal_or_camel_cased_string:
          if char.isupper():
              converted_character = "_" + char.lower()
              snake_cased_char_list.append(converted_character)
          else:
            snake_cased_char_list.append(char)
      
      snake_cased_string = "".join(snake_cased_char_list)
      clean_snake_cased_string = snake_cased_string.strip('_')
      # Región editable por el usuario
      return clean_snake_cased_string
      # Región editable por el usuario
  ```

---

## Paso 11

Una vez completada la función, ya puede utilizarla dentro de otra función.

> Cree una nueva función llamada `main()` con `pass` como cuerpo de la función.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
      snake_cased_char_list = []"
      for char in pascal_or_camel_cased_string:
          if char.isupper():
              converted_character = "_" + char.lower()
              snake_cased_char_list.append(converted_character)
          else:
            snake_cased_char_list.append(char)
      snake_cased_string = "".join(snake_cased_char_list)
      clean_snake_cased_string = snake_cased_string.strip('_')
      return clean_snake_cased_string

  # Región editable por el usuario
  def main():
    pass
  # Región editable por el usuario
  ```

---

## Paso 12

> Dentro de la función `main()`, reemplaza la instrucción `pass` por una llamada a la función `convert_to_snake_case()`, pasando la cadena `'aLongAndComplexString'` como entrada.
>
> Para mostrar el resultado, pasa la llamada a la función como argumento a la función `print()`.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
      snake_cased_char_list = []"
      for char in pascal_or_camel_cased_string:
          if char.isupper():
              converted_character = "_" + char.lower()
              snake_cased_char_list.append(converted_character)
          else:
            snake_cased_char_list.append(char)
      snake_cased_string = "".join(snake_cased_char_list)
      clean_snake_cased_string = snake_cased_string.strip('_')
      return clean_snake_cased_string

  def main():
  # Región editable por el usuario
      print(convert_to_snake_case('aLongAndComplexString'))
  # Región editable por el usuario
  ```

---

## Paso 13

Para mostrar el resultado de la función `convert_to_snake_case()`, debes llamar a la función `main()`.

> En el mismo nivel que las dos funciones existentes, añade una llamada a la función `main()`. Al ejecutarla, deberías ver la cadena en camel case o pascal case convertida a snake case.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
      snake_cased_char_list = []"
      for char in pascal_or_camel_cased_string:
          if char.isupper():
              converted_character = "_" + char.lower()
              snake_cased_char_list.append(converted_character)
          else:
            snake_cased_char_list.append(char)
      snake_cased_string = "".join(snake_cased_char_list)
      clean_snake_cased_string = snake_cased_string.strip('_')
      return clean_snake_cased_string

  def main():
      print(convert_to_snake_case('aLongAndComplexString'))

  # Región editable por el usuario
  main()
  # Región editable por el usuario
  ```

---

## Paso 14

Hasta ahora, en este proyecto has utilizado un bucle `for` para iterar sobre la cadena de entrada y convertirla en la salida deseada. Ahora comenzarás la transición de un bucle `for` a una comprensión de lista.

> Comienza por comentar todas las líneas de código dentro de la función `convert_to_snake_case()`. No las elimines, ya que te serán útiles cuando implementes la lógica utilizando una comprensión de lista.
>
> Recuerda añadir la palabra clave `pass` al cuerpo de la función para evitar que el código falle durante las pruebas.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
  # Región editable por el usuario
      # snake_cased_char_list = []"
      # for char in pascal_or_camel_cased_string:
      #     if char.isupper():
      #         converted_character = "_" + char.lower()
      #         snake_cased_char_list.append(converted_character)
      #     else:
      #       snake_cased_char_list.append(char)
      # snake_cased_string = "".join(snake_cased_char_list)
      # clean_snake_cased_string = snake_cased_string.strip('_')
      # return clean_snake_cased_string
      pass
  # Región editable por el usuario

  def main():
      print(convert_to_snake_case('aLongAndComplexString'))

  main()
  ```

---

## Paso 15

> Reemplaza la palabra clave `pass` por la variable `snake_cased_char_list` y asígnale una lista vacía. Utiliza la notación de llaves para crear la lista.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
      # snake_cased_char_list = []"
      # for char in pascal_or_camel_cased_string:
      #     if char.isupper():
      #         converted_character = "_" + char.lower()
      #         snake_cased_char_list.append(converted_character)
      #     else:
      #       snake_cased_char_list.append(char)
      # snake_cased_string = "".join(snake_cased_char_list)
      # clean_snake_cased_string = snake_cased_string.strip('_')
      # return clean_snake_cased_string

  # Región editable por el usuario
      snake_cased_char_list = []
  # Región editable por el usuario

  def main():
      print(convert_to_snake_case('aLongAndComplexString'))

  main()
  ```

---

## Paso 16

Deberás convertir los caracteres en mayúscula a minúscula y añadir un guión bajo delante de ellos.

Antes de continuar con la comprensión de listas, le darás a tu función un valor de retorno. De esta manera, podrás comprobar el resultado.

> Utiliza la instrucción `return` para devolver la lista `snake_cased_char_list` desde tu función.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
      # snake_cased_char_list = []"
      # for char in pascal_or_camel_cased_string:
      #     if char.isupper():
      #         converted_character = "_" + char.lower()
      #         snake_cased_char_list.append(converted_character)
      #     else:
      #       snake_cased_char_list.append(char)
      # snake_cased_string = "".join(snake_cased_char_list)
      # clean_snake_cased_string = snake_cased_string.strip('_')
      # return clean_snake_cased_string

      snake_cased_char_list = []
  # Región editable por el usuario
      return snake_cased_char_list
  # Región editable por el usuario

  def main():
      print(convert_to_snake_case('aLongAndComplexString'))

  main()
  ```

---

## Paso 17

En lugar de devolver la lista `snake_cased_char_list`, deberá unir(`join`) sus elementos en una sola cadena utilizando una cadena vacía `''` como separador.

> Modifique la instrucción `return` para que devuelva el resultado de unir(`join`) `snake_cased_char_list` con una cadena vacía como separador.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
      # snake_cased_char_list = []"
      # for char in pascal_or_camel_cased_string:
      #     if char.isupper():
      #         converted_character = "_" + char.lower()
      #         snake_cased_char_list.append(converted_character)
      #     else:
      #       snake_cased_char_list.append(char)
      # snake_cased_string = "".join(snake_cased_char_list)
      # clean_snake_cased_string = snake_cased_string.strip('_')
      # return clean_snake_cased_string

      snake_cased_char_list = []
  # Región editable por el usuario
      return ''.join(snake_cased_char_list)
  # Región editable por el usuario

  def main():
      print(convert_to_snake_case('aLongAndComplexString'))

  main()
  ```

---

## Paso 18

Después de unir los elementos de la lista `snake_cased_char_list`, deberá eliminar cualquier guión bajo inicial o final de la cadena resultante. Para ello, utilice el método `strip` con el carácter de guión bajo `_` como argumento.

Las llamadas a métodos se pueden encadenar, lo que significa que el resultado de una llamada a un método se puede utilizar como objeto para otra llamada a un método.

- *Codigo Ejemplo*

  ```py
  words_list = ['hello', 'world', 'this', 'is', 'chained', 'methods']
  result = ' '.join(words_list).upper()
  ```

En el ejemplo anterior, el método `.upper()` se encadena a `' '.join(words_list)`, por lo que `.upper()` se invoca sobre el resultado de la invocación de `.join()`.

> Modifique la instrucción `return` encadenando a `''.join(snake_cased_char_list)` una invocación al método `.strip()` para eliminar cualquier guión bajo inicial o final.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
      # snake_cased_char_list = []"
      # for char in pascal_or_camel_cased_string:
      #     if char.isupper():
      #         converted_character = "_" + char.lower()
      #         snake_cased_char_list.append(converted_character)
      #     else:
      #       snake_cased_char_list.append(char)
      # snake_cased_string = "".join(snake_cased_char_list)
      # clean_snake_cased_string = snake_cased_string.strip('_')
      # return clean_snake_cased_string

      snake_cased_char_list = []
  # Región editable por el usuario
      return ''.join(snake_cased_char_list).strip("_")
  # Región editable por el usuario

  def main():
      print(convert_to_snake_case('aLongAndComplexString'))

  main()
  ```

---

## Paso 19

En Python, una *comprensión de lista* es una construcción que permite generar una nueva lista aplicando una expresión a cada elemento de un iterable existente y, opcionalmente, filtrando los elementos con una condición. Además de ser más breves, las comprensiones de lista suelen ejecutarse más rápido.

*Una comprensión de lista básica consiste en una expresión seguida de una cláusula `for`:*

- *Codigo Ejemplo*

  ```py
  spam = [i * 2 for i in iterable]
  ```

Lo anterior utiliza la variable `i` para iterar sobre `iterable`. Cada elemento de la lista resultante se obtiene evaluando la expresión `i * 2` en la iteración actual.

> En este paso, debes llenar la lista vacía `snake_cased_char_list` utilizando la sintaxis de comprensión de listas.
>
> Convierta su lista vacía en una comprensión de lista que convierta cada carácter de `pascal_or_camel_cased_string` en un carácter minúsculo y le anteponga un guión bajo (el código que comentó anteriormente puede ayudarle a escribir la expresión). Utilice char `para` iterar sobre `pascal_or_camel_cased_string`.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
      # snake_cased_char_list = []"
      # for char in pascal_or_camel_cased_string:
      #     if char.isupper():
      #         converted_character = "_" + char.lower()
      #         snake_cased_char_list.append(converted_character)
      #     else:
      #       snake_cased_char_list.append(char)
      # snake_cased_string = "".join(snake_cased_char_list)
      # clean_snake_cased_string = snake_cased_string.strip('_')
      # return clean_snake_cased_string

  # Región editable por el usuario
      snake_cased_char_list = [("_" + char.lower()) for char in pascal_or_camel_cased_string]
  # Región editable por el usuario
      return ''.join(snake_cased_char_list).strip("_")

  def main():
      print(convert_to_snake_case('aLongAndComplexString'))

  main()
  ```

---

## Paso 20

Las comprensiones de listas aceptan sentencias condicionales para evaluar la expresión proporcionada solo si se cumplen ciertas condiciones:

- *Codigo Ejemplo*

  ```py
  spam = [i * 2 for i in iterable if i > 0]
  ```

Como se puede ver en el resultado, la lista de caracteres generada a partir de `pascal_or_camel_cased_string` se ha unido. Dado que la expresión dentro de la comprensión de lista se evalúa para cada carácter, el resultado es una cadena en minúsculas con todos los caracteres separados por un guión bajo.

> Siga el ejemplo anterior para añadir una cláusula `if` a su comprensión de lista, de modo que la expresión solo se ejecute si el carácter es mayúscula.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
      # snake_cased_char_list = []"
      # for char in pascal_or_camel_cased_string:
      #     if char.isupper():
      #         converted_character = "_" + char.lower()
      #         snake_cased_char_list.append(converted_character)
      #     else:
      #       snake_cased_char_list.append(char)
      # snake_cased_string = "".join(snake_cased_char_list)
      # clean_snake_cased_string = snake_cased_string.strip('_')
      # return clean_snake_cased_string

  # Región editable por el usuario
      snake_cased_char_list = ['_' + char.lower() for char in pascal_or_camel_cased_string if char.isupper()]
  # Región editable por el usuario
      return ''.join(snake_cased_char_list).strip("_")

  def main():
      print(convert_to_snake_case('aLongAndComplexString'))

  main()
  ```

---

## Paso 21

Aun así, el resultado final no es exactamente el que deseas obtener. Necesitas ejecutar una expresión diferente para los caracteres filtrados por la cláusula `if`. Para ello, utilizarás una cláusula `else`:

- *Codigo Ejemplo*

  ```py
  spam = [i * 2 if i > 0 else -1 for i in iterable]
  ```

Ten en cuenta que, a diferencia de la cláusula `if`, la construcción `if`/`else` debe colocarse entre la expresión y la palabra clave `for`.

> Modifica tu comprensión de lista para que, cuando un carácter no sea mayúscula, permanezca sin cambios.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
      # snake_cased_char_list = []"
      # for char in pascal_or_camel_cased_string:
      #     if char.isupper():
      #         converted_character = "_" + char.lower()
      #         snake_cased_char_list.append(converted_character)
      #     else:
      #       snake_cased_char_list.append(char)
      # snake_cased_string = "".join(snake_cased_char_list)
      # clean_snake_cased_string = snake_cased_string.strip('_')
      # return clean_snake_cased_string

  # Región editable por el usuario
      snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]
  # Región editable por el usuario
      return ''.join(snake_cased_char_list).strip("_")

  def main():
      print(convert_to_snake_case('aLongAndComplexString'))

  main()
  ```

---

## Paso 22

Elimine las líneas de código comentadas dentro de la función convert_to_snake_case() para limpiar la definición de la función.

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
  # Región editable por el usuario
      
  # Región editable por el usuario

      snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]
      return ''.join(snake_cased_char_list).strip("_")

  def main():
      print(convert_to_snake_case('aLongAndComplexString'))

  main()
  ```

---

## Paso 23

> Por último, prueba esta nueva implementación ejecutando el programa. Cambia la cadena de entrada a `'IAmAPascalCasedString'` y comprueba si el resultado es `'i_am_a_pascal_cased_string'`, aunque eso sea falso.

Si lo has hecho todo correctamente, deberías ver la cadena de entrada convertida a snake case, como antes.

**¡Felicidades! Ahora tu función `convert_to_snake_case()` está lista.**

- *Codigo*

  ```py
  def convert_to_snake_case(pascal_or_camel_cased_string):
      snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]
      return ''.join(snake_cased_char_list).strip("_")

  def main():
  # Región editable por el usuario
      print(convert_to_snake_case('aLongAndComplexString'))
  # Región editable por el usuario

  main()
  ```

---
