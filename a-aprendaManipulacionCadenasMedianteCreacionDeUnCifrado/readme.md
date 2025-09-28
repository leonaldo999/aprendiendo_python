# Aprenda la manipulacion de cadenas mediante la creacion de un cifrado

Python es un lenguaje de programación poderoso y popular ampliamente utilizado para ciencia de datos, visualización de datos, desarrollo web, desarrollo de juegos, aprendizaje automático y más.

En este proyecto, aprenderás conceptos fundamentales de programación en Python, como variables, funciones, bucles y sentencias condicionales. Los usarás para codificar tus primeros programas.

---

## Paso 1

Las variables son una parte esencial de Python y de cualquier lenguaje de programación. Una variable es un nombre que hace referencia o apunta a un objeto. Puedes declarar una variable escribiendo el nombre de la variable a la izquierda del operador de asignación `=` y especificando el valor que se le asignará a esa variable a la derecha del operador de asignación:

- *Codigo Ejemplo*

  ```py
  variable_name = value
  ```

> Create a variable called `number` and assign the value `5` to your new variable.

- *Codigo*

  ```py
  number = 5
  ```

---

## Paso 2

Las variables pueden almacenar valores de diferentes tipos de datos. Acabas de asignar un valor `entero`, pero si quieres representar algún texto, necesitas asignar una `cadena`. Las cadenas son secuencias de caracteres entre comillas simples o dobles, pero no puedes comenzar una cadena con una comilla simple y terminarla con una comilla doble, o viceversa:

- *Codigo Ejemplo*

  ```py
  string_1 = "I am a string"
  string_2 = 'I am also a string'
  string_3 = 'This is not valid"
  ```

> Elimine la variable numérica y su valor. A continuación, declare otra variable llamada `text` y asigne la cadena `Hola mundo` a esta variable.

- *Codigo*

  ```py
  #  number = 5
  text = "Hello World"
  ```

---

## Paso 3

Puedes usar la función integrada `print()` para imprimir el resultado de tu código en la terminal.

Las funciones son bloques de código reutilizables que puedes llamar o invocar para ejecutar su código cuando lo necesites. Para llamar a una función, solo tienes que escribir un par de paréntesis junto a su nombre. Muy pronto aprenderás más sobre las funciones.

> Por ahora, vaya a una nueva línea y añada una llamada vacía a la función `print()`. Todavía no debería ver ningún resultado.

- *Codigo*

  ```py
  text = 'Hello World'
  print()
  ```

---

## Paso 4

Un argumento es un objeto o una expresión que se pasa a una función, añadido entre los paréntesis de apertura y cierre, cuando se llama a ella:

- *Codigo Ejemplo*

  ```py
  greet = 'Hello!'
  print(greet)
  ```

El código del ejemplo anterior imprimiría la cadena `¡Hello!`, que es el valor de la variable `greet` pasada a `print()` como argumento.

> Imprime tu variable de `text` en la pantalla pasando la variable de `text` como argumento a la función `print()`.

- *Codigo*

  ```py
  text = 'Hello World'
  print(text)
  ```

---

## Paso 5

Cada carácter de una cadena se puede referenciar mediante un índice numérico. El recuento del índice comienza en cero. Por lo tanto, el primer carácter de una cadena tiene un índice de `0`. Por ejemplo, en la cadena `'Hello World'`, la `'H'` se encuentra en el índice `0`, la `'e'` en el índice `1`, y así sucesivamente.

Se puede acceder a cada carácter de una cadena utilizando la notación entre corchetes. Debe escribir el nombre de la variable seguido de corchetes y añadir el índice del carácter entre los corchetes:

- *Codigo Ejemplo*

  ```py
  text = 'Hello World'
  r = text[8]
  ```

> Ahora, en lugar de imprimir texto, imprima solo el carácter en el índice 6.

- *Codigo*

  ```py
  text = 'Hello World'
  print(text[6])
  ```

---

## Paso 6

También puede acceder a los caracteres de la cadena comenzando por el final de la misma. El último carácter tiene un índice de `-1`, el penúltimo `-2` y así sucesivamente.

> Ahora modifique su llamada `print()` existente para imprimir el último carácter de su cadena.

- *Codigo*

  ```py
  text = 'Hello World'
  print(text[-1])
  ```

---

## Paso 7

Puede acceder al número de caracteres de una cadena con la función integrada `len()`.

> Modifique su llamada `print()` existente pasando `len(text)` en lugar de `text[-1]`.

- *Codigo*

  ```py
  text = 'Hello World'
  print(len(text))
  ```

---

## Paso 8

Verás que en la terminal aparece el número `11`, ya que `Hello World` contiene 11 caracteres.

> Otra función integrada muy útil es `type()`, que devuelve el tipo de datos de una variable. Modifica tu llamada a `print()` para imprimir el tipo de datos del `text`.

- *Codigo*

  ```py
  text = 'Hello World'
  print(type(text))
  ```

---

## Paso 9

Como puede ver, el resultado de imprimir `type(text)` es `<class 'str'>`, lo que significa que su variable es una cadena, indicada como `str`.

> Ahora vaya a una nueva línea y cree otra variable llamada `shift` y asígnele el valor `3` a esta variable.

- *Codigo*

  ```py
  text = "Hello World"
  print(type(text))
  
  shift = 3
  ```

---

## Paso 10

> Ahora imprima su nueva variable.

- *Codigo*

  ```py
  text = "Hello World"
  print(type(text))
  
  shift = 3
  print(shift)
  ```

---

## Paso 11

> Modifique su llamada `print(shift)` para imprimir el `type` de datos de su variable `shift`.

- *Codigo*

  ```py
  text = "Hello World"
  print(type(text))
  
  shift = 3
  print(type(shift))
  ```

---

## Paso 12

**Los aspectos clave del nombramiento de variables en Python son:**

- Algunas palabras son palabras clave reservadas (por ejemplo, `for`, `while`, `True`). Tienen un significado especial en Python, por lo que no se pueden utilizar para nombres de variables.

- Los nombres de las variables no pueden comenzar con un número y solo pueden contener caracteres alfanuméricos o guiones bajos.

- Los nombres de las variables distinguen entre mayúsculas y minúsculas, es decir, `my_var` es diferente de `my_Var` y `MY_VAR`.

- Por último, es una convención común escribir los nombres de las variables utilizando `snake_case`, donde cada espacio se sustituye por un carácter de subrayado y las palabras se escriben en minúsculas.

> Elimine ambas llamadas a `print()` y declare otra variable llamada `alphabet`. Asigne la cadena `abcdefghijklmnopqrstuvwxyz` a esta variable.

- *Codigo*

  ```py
  text = "Hello World"
  shift = 3
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  ```

---

## Paso 13

Vas a utilizar el método `.find()` para encontrar la posición en el **alfabeto** de cada letra de tu mensaje. Un método es similar a una función, pero pertenece a un objeto.

- *Codigo Ejemplo*

  ```py
  sentence = 'My brain hurts!'
  sentence.find('r')
  ```

Arriba, se llama al método `.find()` en `sentence` (la cadena en la que se va a buscar) y se pasa «`'r'`» (el carácter que se va a localizar) como argumento. La llamada `sentence.find('r')` devolverá `4`, que es el índice de la primera aparición de `'r'` en `sentence`.

> Al final del código, llame a `.find()` en `alphabet` y pase `'z'` como argumento al método.

- *Codigo*

  ```py
  text = "Hello World"
  shift = 3
  alphabet = "abcdefghijklmnopqrstuvwxyz"

  alphabet.find("z")
  ```

---

## Paso 14

El primer tipo de cifrado que vas a crear se llama cifrado *Caesar*. En concreto, tomarás cada letra de tu mensaje, buscarás su posición en el alfabeto, tomarás la letra situada tres posiciones más adelante en el alfabeto y sustituirás la letra original por la nueva.

> Para implementar esto, utilizará el método `.find()` que se ha explicado en el paso anterior. Modifique su llamada `.find()` existente pasándole `text[0]` como argumento en lugar de `'z'`.

- *Codigo*

  ```py
  text = "Hello World"
  shift = 3
  alphabet = "abcdefghijklmnopqrstuvwxyz"

  alphabet.find(text[0])
  ```

---

## Paso 15

La función `print()` solo te da un resultado en la consola, pero las funciones y los métodos pueden tener un valor de retorno que puedes usar en tu código.

> Ahora asigna `alphabet.find(text[0])` a una variable llamada `index`. De esta manera, `index` almacenará el valor devuelto por `alphabet.find(text[0])`.

- *Codigo*

  ```py
  text = "Hello World"
  shift = 3
  alphabet = "abcdefghijklmnopqrstuvwxyz"

  index = alphabet.find(text[0])
  ```

---

## Paso 16

> A continuación, imprima la variable `index` en la consola.

- *Codigo*

  ```py
  text = "Hello World"
  shift = 3
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  index = alphabet.find(text[0])

  print("index")
  ```

---

## Paso 17

`.find()` devuelve el índice del carácter coincidente dentro de la cadena. Si no se encuentra el carácter, devuelve `-1`. Como puede ver, el primer carácter del `text`, la `'H'` mayúscula, no se encuentra, ya que el `alphabet` solo contiene letras minúsculas.

> Puede transformar una cadena en su equivalente en minúsculas con el método `.lower()`. Añada otra llamada a `print()` para imprimir `text.lower()` y vea el resultado.

- *Codigo*

  ```py
  text = "Hello World"
  shift = 3
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  index = alphabet.find(text[0])

  print("index")
  print(text.lower())
  ```

---

## Paso 18

> Elimine la última llamada a `print()`. A continuación, en lugar de `text[0]`, pase `text[0].lower()` como argumento a su llamada a `.find()` y observe el resultado.

- *Codigo*

  ```py
  text = "Hello World"
  shift = 3
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  index = alphabet.find(text[0].lower())

  print("index")
  ```

---

## Paso 19

> Declare una nueva variable llamada `shifted`. Utilice la notación entre corchetes para acceder al valor de `alphabet` en el índice `index` y asígnelo a su nueva variable.

- *Codigo*

  ```py
  text = "Hello World"
  shift = 3
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  index = alphabet.find(text[0].lower())
  print("index")

  shifted = alphabet[index]
  ```

---

## Paso 20

> Imprima la variable `shifted`.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  index = alphabet.find(text[0].lower())
  print(index)

  shifted = alphabet[index]
  print(shifted)
  ```

---

## Paso 21

Como puede ver en el resultado, `'h'` se encuentra en el índice `7` de la cadena `alphabet`. Ahora debe encontrar la letra que se encuentra en el índice `7` más el valor del `shift`. Para ello, puede utilizar el operador de suma, `+`, del mismo modo que lo utilizaría para una suma matemática.

> Modifique su variable `shifted` para que almacene el valor del `alphabet` en el índice `index + shift`.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  index = alphabet.find(text[0].lower())
  print(index)

  shifted = alphabet[index + shift]
  print(shifted)
  ```

---

## Paso 22

Repetir el proceso de localizar la letra dentro del alfabeto y determinar la letra desplazada para cada carácter del `text` puede resultar tedioso. Afortunadamente, puedes simplificarlo utilizando un bucle.

> Por ahora, elimina todas las líneas de código que se encuentran debajo de la declaración de la variable del `alphabet`.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  ```

---

## Paso 23

Un bucle te permite recorrer sistemáticamente una secuencia de elementos y ejecutar acciones en cada uno de ellos.

En este caso, emplearás un bucle `for`. A continuación te mostramos cómo puedes iterar sobre un `text`:

- *Codigo Ejemplo*

  ```py
  for i in text:
  ```

`for` es la palabra clave que indica el tipo de bucle. `i` es una variable que toma secuencialmente el valor de los elementos del `text`. La instrucción termina con dos puntos, `:`.

> Debajo de la línea donde declaraste `alphabet`, escribe un bucle `for` para iterar sobre el `text`. Utiliza `i` como variable del bucle.
>
> Al hacerlo, se produce un error en la terminal. Lo aprenderás en el siguiente paso.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  for i in text:
  ```

---

## Paso 24

El código que se ejecutará en cada iteración, --situado después de los dos puntos `:`--, constituye el cuerpo del bucle. Este código debe estar sangrado. En Python, se recomienda utilizar cuatro espacios por nivel de sangría. Este nivel sangrado es un bloque de código.

- *Codigo Ejemplo*

  ```py
  for i in text:
    print(i)
  ```

Python utiliza la sangría para indicar bloques de código. Dos puntos al final de una línea indican que a continuación habrá un nuevo bloque de código sangrado.

Por lo tanto, cuando no se encuentra ningún bloque sangrado después de los dos puntos finales, la ejecución del código se detiene y se genera un error `IndentationError`. Este código no mostrará el resultado y, en su lugar, generará un error `IndentationError`:

- *Codigo Ejemplo*

  ```py
  for i in text:
  print(i)
  ```

> Dale un cuerpo a tu bucle `for` añadiendo una llamada a `print(i)`. Recuerda sangrar el cuerpo del bucle.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  for i in text:
    print(i)
  ```

---

## Paso 25

La variable de iteración puede tener cualquier nombre válido, pero es conveniente darle un nombre significativo.

> Cambie el nombre de su variable `i` a `char`.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'

  for char in text:
    print(char)
  ```

---

## Paso 26

> Dentro del bucle `for`, antes de imprimir el carácter actual, declare una variable llamada `index` y asigne el valor devuelto por `alphabet.find(char)` a esta variable.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'

  for char in text:
      index = alphabet.find(char)
      print(char)
  ```

---

## Paso 27

Actualmente, la función `print()` toma un único argumento `char`, pero puede tomar varios argumentos, separados por una coma.

> Agrega un segundo argumento a `print(char)` para que imprima el carácter y su índice dentro del alfabeto.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'

  for char in text:
      index = alphabet.find(char)
      print(char, index)
  ```

---

## Paso 28

`find` vuelve a devolver `-1` para las letras mayúsculas y también para el carácter de espacio. Más adelante se ocupará del espacio.

> Por ahora, en lugar de iterar sobre el `text`, cambie el bucle `for` para iterar sobre `text.lower()`.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'

  for char in text.lower():
      index = alphabet.find(char)
      print(char, index)
  ```

---

## Paso 29

> Al final del cuerpo del bucle, declare una variable llamada `new_index` y asigne el valor de `index + shift` a esta variable.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'

  for char in text.lower():
      index = alphabet.find(char)
      print(char, index)
      
      new_index = index + shift
  ```

---

## Paso 30

Las cadenas son inmutables, lo que significa que no se pueden cambiar una vez creadas. Por ejemplo, podría pensarse que el siguiente código cambia el valor de `my_string` por la cadena `train`, pero esto no es válido:

- *Codigo Ejemplo*

  ```py
  my_string = 'brain'
  my_string[0] = 't'
  ```

> Confirme esto utilizando la notación entre corchetes para acceder a la primera letra del `text` e intente cambiarla por el carácter que desee. Verá que el resultado desaparece y aparece un error.

- *Codigo*

  ```py
  text = 'Hello World'
  text[0] = "C"
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'

  for char in text.lower():
      index = alphabet.find(char)
      print(char, index)
      
      new_index = index + shift
  ```

---

## Paso 31

Cuando intentas cambiar los caracteres individuales de una cadena como lo hiciste en el paso anterior, obtienes un error `TypeError`, que se produce cuando se utiliza un objeto de tipo inadecuado en tu código.

Como puedes ver en el mensaje de error, las cadenas no admiten la asignación de elementos, ya que son inmutables. Sin embargo, a una variable se le puede reasignar otra cadena:

- *Codigo Ejemplo*

  ```py
  message = 'Hello World'
  message = 'Hello there!'
  ```

> Elimine la línea de `texto[0]` y reasigne al `text` la cadena `Albatross`.

- *Codigo*

  ```py
  text = 'Hello World'
  text = "Albatross"
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'

  for char in text.lower():
      index = alphabet.find(char)
      print(char, index)
      
      new_index = index + shift
  ```

---

## Paso 32

Como puede ver, cada carácter de la cadena reasignada se imprime dentro del bucle.

> Vuelva a la cadena original eliminando la reasignación de `text`.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'

  for char in text.lower():
      index = alphabet.find(char)
      print(char, index)
      
      new_index = index + shift
  ```

---

## Paso 33

> Ahora debe crear una variable new_char al final del cuerpo del bucle. Establezca su valor en alphabet[new_index].

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'

  for char in text.lower():
      index = alphabet.find(char)
      print(char, index)
      
      new_index = index + shift
      new_char = alphabet[new_index]
  ```

---

## Paso 34

> A continuación, imprima `new_char` y vea el resultado.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'

  for char in text.lower():
      index = alphabet.find(char)
      print(char, index)
      
      new_index = index + shift
      new_char = alphabet[new_index]
      print(new_char)
  ```

---

## Paso 35

> Limpia un poco la salida. Elimina `print(char, index)` y convierte la última llamada a `print()` en `print('char:', char, 'new char:', new_char)`.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'

  for char in text.lower():
      index = alphabet.find(char)
      
      new_index = index + shift
      new_char = alphabet[new_index]
      print("char:", char, "new char:", new_char)
  ```

---

## Paso 36

> En este momento, el carácter cifrado se actualiza en cada iteración. Sería mejor almacenar la cadena cifrada en una nueva variable. Antes del bucle `for`, declare una variable llamada `encrypted_text` y asígnele una cadena vacía (`""`).

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  encrypted_text = ""

  for char in text.lower():
      index = alphabet.find(char)
      
      new_index = index + shift
      new_char = alphabet[new_index]
      print("char:", char, "new char:", new_char)
  ```

---

## Paso 37

> Ahora, reemplaza `new_char` por `encrypted_text`. Además, modifica la llamada a `print()` por `print('char:', char, 'encrypted text:', encrypted_text)` para reflejar este cambio.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  encrypted_text = ""

  for char in text.lower():
      index = alphabet.find(char)
      
      new_index = index + shift
      encrypted_text = alphabet[new_index]
      print('char:', char, 'encrypted text:', encrypted_text)
  ```

---

## Paso 38

> En lugar de asignar `alphabet[new_index]` a `encrypted_text`, asigne el valor actual de `encrypted_text` más(`+`) `alphabet[new_index]` a esta variable.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  encrypted_text = ""

  for char in text.lower():
      index = alphabet.find(char)
      
      new_index = index + shift
      encrypted_text = encrypted_text + alphabet[new_index]
      print("char:", char, "encrypted text:", encrypted_text)
  ```

---

## Paso 39

Puede obtener el mismo efecto de `a = a + b` utilizando el operador de asignación de suma:

- *Codigo Ejemplo*

  ```py
  a += b
  ```

El operador de asignación de suma le permite sumar un valor a una variable y luego asignar el resultado a esa variable.

> Utilice el operador `+=` para sumar un valor y asignarlo al mismo tiempo a `encrypted_text`.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  encrypted_text = ""

  for char in text.lower():
      index = alphabet.find(char)
      
      new_index = index + shift
      encrypted_text += alphabet[new_index]
      print("char:", char, "encrypted text:", encrypted_text)
  ```

---

## Paso 40

Los operadores de comparación permiten comparar dos objetos en función de sus valores. Para utilizar un operador de comparación, colóquelo entre los objetos que desea comparar. Estos operadores devuelven un valor booleano (`True` o `False`) en función de la veracidad de la expresión.

**Python cuenta con los siguientes operadores de comparación**:

| Operator | Significado |
|:---|:---:|
| == | Igual |
| != | No igual |
| > | Mayou que |
| < | Menor que |
| >= | Mayor o igual que |
| <= | Menor o igual que |

> Al principio del cuerpo del bucle, imprima el resultado de comparar `char` con un espacio `(' ')`. Utilice el operador de igualdad `==` para ello.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  encrypted_text = ""


  for char in text.lower():
      print(char == " ")
      
      index = alphabet.find(char)
      new_index = index + shift
      encrypted_text += alphabet[new_index]
      print("char:", char, "encrypted text:", encrypted_text)
  ```

---

## Paso 41

Actualmente, los espacios se cifran como `c`. Para mantener el espaciado original en el mensaje sin formato, necesitarás una instrucción condicional `if`. Esta se compone de la palabra clave `if`, una condición y dos puntos `:`.

- *Codigo Ejemplo*

  ```py
  if x != 0:
    print(x)
  ```

En el ejemplo anterior, la condición de la instrucción `if` es `x != 0`. El código `print(x)`, dentro del cuerpo de la instrucción `if`, solo se ejecuta cuando la condición se evalúa como `True` (en este ejemplo, lo que significa que `x` es diferente de cero).

> En la parte superior del bucle for, reemplaza `print(char == ' ')` por una instrucción `if`. La condición de esta instrucción `if` debe evaluarse como `True` si `char` es un espacio en blanco y `False` en caso contrario. Dentro del cuerpo de la instrucción `if`, imprime la cadena `space!`. Recuerda sangrar esta línea.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  encrypted_text = ""


  for char in text.lower():
      if char == " ":
        print("space!")
      
      index = alphabet.find(char)
      new_index = index + shift
      encrypted_text += alphabet[new_index]
      print("char:", char, "encrypted text:", encrypted_text)
  ```

---

## Paso 42

> Ahora, en lugar de imprimir `space!`, usa el operador de asignación de suma para añadir el espacio (actualmente almacenado en `char`) al valor actual de `encrypted_text`.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  encrypted_text = ""


  for char in text.lower():
      if char == " ":
        encrypted_text += char
      
      index = alphabet.find(char)
      new_index = index + shift
      encrypted_text += alphabet[new_index]
      print("char:", char, "encrypted text:", encrypted_text)
  ```

---

## Paso 43

Una instrucción condicional también puede tener una cláusula `else`. Esta cláusula se puede añadir al final de una instrucción `if` para ejecutar código alternativo si la condición de la instrucción `if` es falsa:

- *Codigo Ejemplo*

  ```py
  if x != 0:
      print(x)
  else:
      print('x = 0')
  ```

Como puede ver en el resultado, cuando las iteraciones del bucle llegan al espacio, se añade un espacio a la cadena cifrada. A continuación, se ejecuta el código fuera del bloque `if` y se añade una `c` a la cadena cifrada.

> Para solucionarlo, añada una cláusula `else` después de `encrypted_text += char` y sangra todas las líneas de código siguientes, excepto la llamada a `print()`.

- *Codigo*

  ```py
  text = 'Hello World'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  encrypted_text = ""


  for char in text.lower():
      if char == " ":
          encrypted_text += char
      else:
          index = alphabet.find(char)
          new_index = index + shift
          encrypted_text += alphabet[new_index]
      print("char:", char, "encrypted text:", encrypted_text)
  ```

---

## Paso 44

> Intenta asignar la cadena `Hello Zaira` a tu variable de `text` y observa qué sucede en la terminal.
>
> Verás una excepción de `índice de cadena fuera de rango`. No te preocupes, ¡pronto descubrirás cómo solucionarlo!

- *Codigo*

  ```py
  text = 'Hello Zaira'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  encrypted_text = ""


  for char in text.lower():
      if char == " ":
          encrypted_text += char
      else:
          index = alphabet.find(char)
          new_index = index + shift
          encrypted_text += alphabet[new_index]
      print("char:", char, "encrypted text:", encrypted_text)
  ```

---

## Paso 45

Cuando el bucle llega a la letra `Z`, la suma `index + shift` supera el último índice de la cadena del `alphabet` . Por lo tanto, `alphabet[new_index]` intenta utilizar un índice no válido, lo que provoca que se genere un `IndexError`.

Se puede observar que la salida en la terminal se detiene en el espacio inmediatamente anterior a la `Z`, del ultimo `print` antes de que se genere el error.

En este caso, se puede utilizar el operador módulo (`%`) para devolver el resto de la división entre dos números. Por ejemplo: `5 % 2` es igual a `1`, porque 5 dividido por 2 tiene un cociente de 2 y un resto de 1.

> Rodee el `index + shift` con paréntesis y aplique el módulo a la expresión con `26`, que es la longitud del `alphabet`.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  encrypted_text = ""


  for char in text.lower():
      if char == " ":
          encrypted_text += char
      else:
          index = alphabet.find(char)
          new_index = (index + shift) % 26
          encrypted_text += alphabet[new_index]
      print("char:", char, "encrypted text:", encrypted_text)
  ```

---

## Paso 46

Si desea incorporar caracteres adicionales a la cadena `alphabet`, como dígitos o caracteres especiales, verá que es necesario modificar manualmente el operando derecho de la operación módulo.

> Reemplace `26` por `len(alphabet)` para evitar este problema.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  encrypted_text = ""


  for char in text.lower():
      if char == " ":
          encrypted_text += char
      else:
          index = alphabet.find(char)
          new_index = (index + shift) % len(alphabet)
          encrypted_text += alphabet[new_index]
      print("char:", char, "encrypted text:", encrypted_text)
  ```

---

## Paso 47

> A continuación, modifique su llamada a `print()` para imprimir `encrypted text:, encrypted_text` y colóquela fuera del bucle `for`, de modo que la cadena cifrada se imprima una sola vez.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  encrypted_text = ""


  for char in text.lower():
      if char == " ":
          encrypted_text += char
      else:
          index = alphabet.find(char)
          new_index = (index + shift) % len(alphabet)
          encrypted_text += alphabet[new_index]
  print("encrypted text:", encrypted_text)
  ```

---

## Paso 48

> Justo antes de la llamada a `print`, agrega otra y pasa `plain text:, text` como argumentos a `print()`. Utiliza la misma sangría.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  shift = 3
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  encrypted_text = ""


  for char in text.lower():
      if char == " ":
          encrypted_text += char
      else:
          index = alphabet.find(char)
          new_index = (index + shift) % len(alphabet)
          encrypted_text += alphabet[new_index]
  print("plain text:", text)
  print("encrypted text:", encrypted_text)
  ```

---

## Paso 49

Una función es básicamente un bloque de código reutilizable. Ya has visto algunas funciones integradas, como `print()`, `find()` y `len()`. Pero también puedes definir funciones personalizadas como esta:

- *Codigo Ejemplo*

  ```py
  def function_name():
      <code>
  ```

Una declaración de función comienza con la palabra clave `def` seguida del nombre de la función (un nombre de variable válido) y un par de paréntesis. La declaración termina con dos puntos.

> Justo después de la variable `shift`, declare una función llamada `caesar` y sangra todas las líneas siguientes para darle cuerpo a su nueva función.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  shift = 3

  def caesar():
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in text.lower():
          if char == " ":
              encrypted_text += char
          else:
              index = alphabet.find(char)
              new_index = (index + shift) % len(alphabet)
              encrypted_text += alphabet[new_index]
      print("plain text:", text)
      print("encrypted text:", encrypted_text)
  ```

---

## Paso 50

En Python, el ámbito de una variable determina dónde se puede acceder a ella:

- Las variables definidas fuera de una función tienen un ámbito global y se puede acceder a ellas desde cualquier parte del código.

- Las variables definidas dentro de una función son locales a esa función y no se puede acceder a ellas fuera de ella.

> Para ver esto en acción, intenta imprimir la variable `alphabet` al final de tu código. Esto generará una excepción `NameError`.
>
> Deberías ver un mensaje de error indicando que `alphabet` no está definida. Esto se debe a que `alphabet` está definida dentro de la función `caesar` y no es accesible fuera de ella.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  shift = 3

  def caesar():
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in text.lower():
          if char == " ":
              encrypted_text += char
          else:
              index = alphabet.find(char)
              new_index = (index + shift) % len(alphabet)
              encrypted_text += alphabet[new_index]
      print("plain text:", text)
      print("encrypted text:", encrypted_text)
  print(alphabet)
  ```

---

## Paso 51

> Ahora, corrija el error eliminando la línea que intenta imprimir la variable `alphabet` fuera de la función `caesar`.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  shift = 3

  def caesar():
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in text.lower():
          if char == " ":
              encrypted_text += char
          else:
              index = alphabet.find(char)
              new_index = (index + shift) % len(alphabet)
              encrypted_text += alphabet[new_index]
      print("plain text:", text)
      print("encrypted text:", encrypted_text)
  ```

---

## Paso 52

Para ejecutar una función, es necesario llamarla (o invocarla) añadiendo un par de paréntesis después de su nombre, de la siguiente manera:

- *Codigo Ejemplo*

  ```py
  function_name()
  ```

> Al final de tu código, llama a tu función `caesar`. Presta atención a la sangría.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  shift = 3

  def caesar():
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in text.lower():
          if char == " ":
              encrypted_text += char
          else:
              index = alphabet.find(char)
              new_index = (index + shift) % len(alphabet)
              encrypted_text += alphabet[new_index]
      print("plain text:", text)
      print("encrypted text:", encrypted_text)

  caesar()
  ```

---

## Paso 53

Ahora debería ver el resultado de nuevo. Aunque este enfoque funciona, no mejora significativamente la reutilización del código. Llamar repetidamente a su función dará el mismo resultado. Sin embargo, las funciones se pueden declarar con parámetros para introducir versatilidad y personalización:

- *Codigo Ejemplo*

  ```py
  def function_name(param_1, param_2):
      <code>
  ```

Los parámetros son variables que puedes utilizar dentro de tu función. Una función se puede declarar con diferentes números de parámetros. En el ejemplo anterior, `param_1` y `param_2` son parámetros.

>Modifica la declaración de tu función para que tome dos parámetros llamados `message` y `offset`.
>
>Después de eso, verás que aparece un error en la terminal. Verás cómo resolverlo en los siguientes pasos.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  shift = 3

  def caesar(message, offset):
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in text.lower():
          if char == " ":
              encrypted_text += char
          else:
              index = alphabet.find(char)
              new_index = (index + shift) % len(alphabet)
              encrypted_text += alphabet[new_index]
      print("plain text:", text)
      print("encrypted text:", encrypted_text)

  caesar()
  ```

---

## Paso 54

> Dentro del cuerpo de la función, cambie el nombre de las variables `text` y `shift` a `message` y `offset`, respectivamente.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  shift = 3

  def caesar(message, offset):
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          if char == " ":
              encrypted_text += char
          else:
              index = alphabet.find(char)
              new_index = (index + offset) % len(alphabet)
              encrypted_text += alphabet[new_index]
      print("plain text:", message)
      print("encrypted text:", encrypted_text)

  caesar()
  ```

---

## Paso 55

Actualmente, tu código genera un error `TypeError`, ya que la función `caesar` está definida con dos parámetros (`message` y `offset`), por lo que espera ser llamada con dos argumentos.

Llamar a `caesar()` sin los argumentos necesarios detiene la ejecución del código.

>Proporciona valores para `message` y `offset`, pasando `text` y `shift` como argumentos a la llamada a la función `caesar`.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  shift = 3

  def caesar(message, offset):
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          if char == " ":
              encrypted_text += char
          else:
              index = alphabet.find(char)
              new_index = (index + offset) % len(alphabet)
              encrypted_text += alphabet[new_index]
      print("plain text:", message)
      print("encrypted text:", encrypted_text)

  caesar(text, shift)
  ```

---

## Paso 56

> En la parte inferior de tu código, después de la llamada `caesar(text, shift)` existente, vuelve a llamar a tu función.
>
> Esta vez, pasa la variable `text` y el entero `13` como argumentos.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  shift = 3

  def caesar(message, offset):
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          if char == " ":
              encrypted_text += char
          else:
              index = alphabet.find(char)
              new_index = (index + offset) % len(alphabet)
              encrypted_text += alphabet[new_index]
      print("plain text:", message)
      print("encrypted text:", encrypted_text)

  caesar(text, shift)
  caesar(text, 13)
  ```

---

## Paso 57

Actualmente, cada letra se cifra siempre con la misma letra, dependiendo del desplazamiento especificado. ¿Qué pasaría si el desplazamiento fuera diferente para cada letra? Sería mucho más difícil de descifrar. Este algoritmo se conoce como cifrado de Vigenère, en el que el desplazamiento de cada letra viene determinado por otro texto, llamado clave.

> Empieza a transformar tu cifrado Caesar en un cifrado Vigenère eliminando las dos llamadas a la función.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  shift = 3

  def caesar(message, offset):
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          if char == " ":
              encrypted_text += char
          else:
              index = alphabet.find(char)
              new_index = (index + offset) % len(alphabet)
              encrypted_text += alphabet[new_index]
      print("plain text:", message)
      print("encrypted text:", encrypted_text)

  ```

---

## Paso 58

> Ahora modifique la declaración de la función: cambie el nombre de la función a `vigenere` y el segundo parámetro a `key`.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  shift = 3

  def vigenere(message, key):
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          if char == " ":
              encrypted_text += char
          else:
              index = alphabet.find(char)
              new_index = (index + offset) % len(alphabet)
              encrypted_text += alphabet[new_index]
      print("plain text:", message)
      print("encrypted text:", encrypted_text)

  ```

---

## Paso 59

> Elimine la variable `shift`. A continuación, declare una nueva variable llamada `custom_key` y asígnele el valor de la cadena `'python'`.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key):
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          if char == " ":
              encrypted_text += char
          else:
              index = alphabet.find(char)
              new_index = (index + offset) % len(alphabet)
              encrypted_text += alphabet[new_index]
      print("plain text:", message)
      print("encrypted text:", encrypted_text)

  ```

---

## Paso 60

> Dado que la clave es más corta que el texto que va a cifrar, tendrá que repetirla para generar todo el texto cifrado. Al principio del cuerpo de la función, declare una variable `key_index` y establézcala en `cero`.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          if char == " ":
              encrypted_text += char
          else:
              index = alphabet.find(char)
              new_index = (index + offset) % len(alphabet)
              encrypted_text += alphabet[new_index]
      print("plain text:", message)
      print("encrypted text:", encrypted_text)

  ```

---

## Paso 61

Al programar, la legibilidad es fundamental. Los comentarios sirven como notas eficaces que explican la lógica detrás de tu código. Son muy valiosos cuando vuelves a un proyecto después de un tiempo y también ayudan a tus colegas a comprender el código.

En Python, puedes escribir un comentario utilizando un `#`. Todo lo que venga después del `#` no se ejecutará.

> Antes de tu instrucción `if`, añade un comentario que diga `Append space to the message`.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          #  Append space to the message
          if char == " ":
              encrypted_text += char
          else:
              index = alphabet.find(char)
              new_index = (index + offset) % len(alphabet)
              encrypted_text += alphabet[new_index]
      print("plain text:", message)
      print("encrypted text:", encrypted_text)

  ```

---

## Paso 62

> A continuación, dentro del bloque `else`, declare una variable llamada `key_char` y asígnele el valor de `key` en el índice `key_index` mod(`%`) la longitud de `key`.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          #  Append space to the message
          if char == " ":
              encrypted_text += char
          else:
              key_char = key[key_index % len(key)]
              index = alphabet.find(char)
              new_index = (index + offset) % len(alphabet)
              encrypted_text += alphabet[new_index]
      print("plain text:", message)
      print("encrypted text:", encrypted_text)

  ```

---

## Paso 63

> Deberá aumentar el recuento de `key_index` para la siguiente iteración. Para ello, después de la línea que acaba de añadir y en el mismo bloque de código, utilice el operador de asignación de suma para incrementar `key_index` en uno.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          #  Append space to the message
          if char == " ":
              encrypted_text += char
          else:
              key_char = key[key_index % len(key)]
              key_index += 1
              index = alphabet.find(char)
              new_index = (index + offset) % len(alphabet)
              encrypted_text += alphabet[new_index]

      print("plain text:", message)
      print("encrypted text:", encrypted_text)

  ```

---

## Paso 64

> Dentro de la cláusula `else`, escribe un comentario que diga: `Find the right key character to encode`.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          #  Append space to the message
          if char == " ":
              encrypted_text += char
          else:
              #  Find the right key character to encode
              key_char = key[key_index % len(key)]
              key_index += 1
              index = alphabet.find(char)
              new_index = (index + offset) % len(alphabet)
              encrypted_text += alphabet[new_index]
      
      print("plain text:", message)
      print("encrypted text:", encrypted_text)

  ```

---

## Paso 65

El método `.index()` es idéntico al método `.find()`, pero lanza una excepción `ValueError` si no puede encontrar la subcadena.

`ValueError` es una excepción integrada que se genera cuando se pasa a una función un argumento con el tipo correcto pero con un valor inadecuado.

> Después de incrementar `key_index`, declare una variable llamada `offset`. Busque el índice que tiene `key_char` en el `alphabet` y asígnelo a `offset`. Utilice `.index()` para buscar el índice.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          #  Append space to the message
          if char == " ":
              encrypted_text += char
          else:
              #  Find the right key character to encode
              key_char = key[key_index % len(key)]
              key_index += 1
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset) % len(alphabet)
              encrypted_text += alphabet[new_index]
      
      print("plain text:", message)
      print("encrypted text:", encrypted_text)

  ```

---

## Paso 66

> Por encima de la variable de desplazamiento, cree otro comentario que diga `Define the offset and the encrypted letter`.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          #  Append space to the message
          if char == " ":
              encrypted_text += char
          else:
              #  Find the right key character to encode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted letter
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset) % len(alphabet)
              encrypted_text += alphabet[new_index]
      
      print("plain text:", message)
      print("encrypted text:", encrypted_text)

  ```

---

## Paso 67

Por el momento, su función imprime algunas cadenas, pero estos valores no pueden ser utilizados por otras partes del código para realizar ninguna acción.

Para ello, debe utilizar una instrucción de `return`:

- *Codigo Ejemplo*

  ```py
  def foo():
    return 'spam'
  ```

Debes escribir `return` seguido de un espacio y el valor que la función debe devolver. Una vez que se encuentra la instrucción `return`, se devuelve ese valor y se detiene la ejecución de la función, pasando a la siguiente línea de código después de la llamada a la función. En el ejemplo anterior, la función `foo` devuelve la cadena `'spam'`.

> Elimina las dos llamadas a `print()` de tu función y devuelve `encrypted_text`.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          #  Append space to the message
          if char == " ":
              encrypted_text += char
          else:
              #  Find the right key character to encode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted letter
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset) % len(alphabet)
              encrypted_text += alphabet[new_index]
      
      return encrypted_text

  ```

---

## Paso 68

> Llama a tu función pasando `text` y `custom_key` como argumentos. Almacena el valor de retorno de la llamada a la función en una variable llamada `encryption`.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          #  Append space to the message
          if char == " ":
              encrypted_text += char
          else:
              #  Find the right key character to encode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted letter
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset) % len(alphabet)
              encrypted_text += alphabet[new_index]
      
      return encrypted_text

  encryption = vigenere(text, custom_key)
  ```

---

## Paso 69

> Ahora, intenta imprimir el `encryption` para ver el resultado real en la terminal.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          #  Append space to the message
          if char == " ":
              encrypted_text += char
          else:
              #  Find the right key character to encode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted letter
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset) % len(alphabet)
              encrypted_text += alphabet[new_index]
      
      return encrypted_text

  encryption = vigenere(text, custom_key)
  print(encryption)
  ```

---

## Paso 70

El cifrado y el descifrado son procesos opuestos, y tu función puede realizar ambos con un par de ajustes.

> Agrega un tercer parámetro llamado `direction` a la definición de tu función. Además, comenta las dos últimas líneas de código para evitar errores en la consola.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key, direction):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          #  Append space to the message
          if char == " ":
              encrypted_text += char
          else:
              #  Find the right key character to encode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted letter
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset) % len(alphabet)
              encrypted_text += alphabet[new_index]
      
      return encrypted_text

  #  encryption = vigenere(text, custom_key)
  #  print(encryption)
  ```

---

## Paso 71

> Todo lo que tienes que hacer es multiplicar el `offset` por la `direction` en la asignación `new_index`. El operador de multiplicación en Python es `*`.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key, direction):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          #  Append space to the message
          if char == " ":
              encrypted_text += char
          else:
              #  Find the right key character to encode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted letter
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              encrypted_text += alphabet[new_index]
      
      return encrypted_text

  #  encryption = vigenere(text, custom_key)
  #  print(encryption)
  ```

---

## Paso 72

> Ahora puede descomentar las dos últimas líneas y modificar la llamada a la función pasando `1` como tercer argumento.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key, direction):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          #  Append space to the message
          if char == " ":
              encrypted_text += char
          else:
              #  Find the right key character to encode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted letter
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              encrypted_text += alphabet[new_index]
      
      return encrypted_text

  encryption = vigenere(text, custom_key, 1)
  print(encryption)
  ```

---

## Paso 73

Comprueba si la función puede descifrar la cadena y convertirla de nuevo en texto sin formato.

> Declara otra variable llamada `decryption` y asígnale `vigenere(encryption, custom_key, -1)`.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key, direction):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          #  Append space to the message
          if char == " ":
              encrypted_text += char
          else:
              #  Find the right key character to encode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted letter
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              encrypted_text += alphabet[new_index]
      
      return encrypted_text

  encryption = vigenere(text, custom_key, 1)
  print(encryption)
  decryption = vigenere(encryption, custom_key, -1)
  ```

---

## Paso 74

>Ahora imprima su variable de `decryption`.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key, direction):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      encrypted_text = ""
      for char in message.lower():
          #  Append space to the message
          if char == " ":
              encrypted_text += char
          else:
              #  Find the right key character to encode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted letter
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              encrypted_text += alphabet[new_index]
      
      return encrypted_text

  encryption = vigenere(text, custom_key, 1)
  print(encryption)
  decryption = vigenere(encryption, custom_key, -1)
  print(decryption)
  ```

---

## Paso 75

Ahora, tu función se puede utilizar tanto para cifrar como para descifrar un mensaje. Limpia tu código con nombres de variables más adecuados.

> Cambia cada aparición de `encrypted_text` por `final_message`.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key, direction):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append space to the message
          if char == " ":
              final_message += char
          else:
              #  Find the right key character to encode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted letter
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  encryption = vigenere(text, custom_key, 1)
  print(encryption)
  decryption = vigenere(encryption, custom_key, -1)
  print(decryption)
  ```

---

## Paso 76

> Actualice también sus comentarios. Su segundo comentario debería decir `encode/decode` en lugar de `encode`. Su tercer comentario debería decir `encrypted/decrypted` en lugar de `encrypted`.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key, direction):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append space to the message
          if char == " ":
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  encryption = vigenere(text, custom_key, 1)
  print(encryption)
  decryption = vigenere(encryption, custom_key, -1)
  print(decryption)
  ```

---

## Paso 77

Las funciones se pueden llamar con argumentos predeterminados. Un argumento predeterminado indica el valor que debe tomar la función si no se pasa el argumento. Por ejemplo, la función siguiente acepta tres argumentos, pero se puede llamar pasando dos argumentos. El tercero asumirá el valor especificado de forma predeterminada:

- *Codigo Ejemplo*

  ```py
  def foo(a, b, c=value):
      <code>
  ```

> Modifique la función `vigenere` para que su parámetro de `direction` tenga un valor predeterminado de `1`.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append space to the message
          if char == " ":
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  encryption = vigenere(text, custom_key, 1)
  print(encryption)
  decryption = vigenere(encryption, custom_key, -1)
  print(decryption)
  ```

---

## Paso 78

> Ahora puede eliminar el tercer argumento de su primera llamada a la función.

- *Codigo*

  ```py
  text = 'Hello Zaira'
  custom_key = 'python'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append space to the message
          if char == " ":
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  encryption = vigenere(text, custom_key)
  print(encryption)
  decryption = vigenere(encryption, custom_key, -1)
  print(decryption)
  ```

---

## Paso 79

En este momento, los signos de puntuación, los caracteres especiales o los dígitos no se codifican/decodifican correctamente.

> Compruébelo añadiendo un signo de exclamación al final de la cadena de `text`.

- *Codigo*

  ```py
  text = 'Hello Zaira!'
  custom_key = 'python'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append space to the message
          if char == " ":
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  encryption = vigenere(text, custom_key)
  print(encryption)
  decryption = vigenere(encryption, custom_key, -1)
  print(decryption)
  ```

---

## Paso 80

El método `.isalpha()` devuelve `True` si todos los caracteres de la cadena en la que se invoca son letras. Por ejemplo, el código siguiente devuelve `True`:

- *Codigo Ejemplo*

  ```py
  'freeCodeCamp'.isalpha()
  # True
  ```

> Elimine la condición `char == ' '` y sustitúyala llamando al método `.isalpha()` en `char`.

- *Codigo*

  ```py
  text = 'Hello Zaira!'
  custom_key = 'python'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append space to the message
          if char.isalpha():
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  encryption = vigenere(text, custom_key)
  print(encryption)
  decryption = vigenere(encryption, custom_key, -1)
  print(decryption)
  ```

---

## Paso 81

El operador `not` se utiliza para negar una expresión. Cuando se coloca antes de un valor verdadero -un valor que se evalúa como `True`-, devuelve `False` y viceversa.

>Agregue el operador `not` al principio de la condición `if` para comprobar si el carácter no es alfabético.

- *Codigo*

  ```py
  text = 'Hello Zaira!'
  custom_key = 'python'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append space to the message
          if not char.isalpha():
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  encryption = vigenere(text, custom_key)
  print(encryption)
  decryption = vigenere(encryption, custom_key, -1)
  print(decryption)
  ```

---

## Paso 82

> Modifique su comentario añadiendo `Append any non-letter character to the message`.

- *Codigo*

  ```py
  text = 'Hello Zaira!'
  custom_key = 'python'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append any non-letter character to the message
          if not char.isalpha():
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  encryption = vigenere(text, custom_key)
  print(encryption)
  decryption = vigenere(encryption, custom_key, -1)
  print(decryption)
  ```

---

## Paso 83

La palabra clave `pass` se puede utilizar como marcador de posición para código futuro. No tiene ningún efecto en el código, pero puede evitar errores que se producirían en caso de código incompleto:

- *Codigo Ejemplo*

  ```py
  def foo():
      pass
  ```

> Llamar a `vigenere` con `1` para cifrar y `-1` para descifrar está bien, pero puede resultar un poco críptico. Crea una nueva función llamada `encrypt` que tome los parámetros `message` y `key`, y utiliza `pass` para rellenar el cuerpo de la función.

- *Codigo*

  ```py
  text = 'Hello Zaira!'
  custom_key = 'python'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append any non-letter character to the message
          if not char.isalpha():
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  def encrypt(message, key):
    pass
  encryption = vigenere(text, custom_key)
  print(encryption)
  decryption = vigenere(encryption, custom_key, -1)
  print(decryption)
  ```

---

## Paso 84

> Elimine la palabra clave `pass` y devuelva `vigenere(message, key)` desde su nueva función.

- *Codigo*

  ```py
  text = 'Hello Zaira!'
  custom_key = 'python'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append any non-letter character to the message
          if not char.isalpha():
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  def encrypt(message, key):
    return vigenere(message, key)

  encryption = vigenere(text, custom_key)
  print(encryption)
  decryption = vigenere(encryption, custom_key, -1)
  print(decryption)
  ```

---

## Paso 85

> Defina otra función llamada `decrypt` con los mismos parámetros que `encrypt`. Esta vez, devuelva `vigenere(message, key, -1)`.

- *Codigo*

  ```py
  text = 'Hello Zaira!'
  custom_key = 'python'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append any non-letter character to the message
          if not char.isalpha():
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  def encrypt(message, key):
    return vigenere(message, key)

  def decrypt(message, key):
    return vigenere(message, key,-1)

  encryption = vigenere(text, custom_key)
  print(encryption)
  decryption = vigenere(encryption, custom_key, -1)
  print(decryption)
  ```

---

## Paso 86

> A continuación, modifique sus variables de `encryption y decryption` llamando a `encrypt` y `decrypt`, respectivamente, en lugar de `vigenere`.

- *Codigo*

  ```py
  text = 'Hello Zaira!'
  custom_key = 'python'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append any non-letter character to the message
          if not char.isalpha():
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  def encrypt(message, key):
    return vigenere(message, key)

  def decrypt(message, key):
    return vigenere(message, key,-1)

  encryption = encrypt(text, custom_key)
  print(encryption)
  decryption = decrypt(encryption, custom_key)
  print(decryption)
  ```

---

## Paso 87

¡Funciona! Ahora, vas a empezar con un mensaje cifrado que hay que descifrar.

> Cambia el valor del `text` por la cadena `'mrttaqrhknsw ih puggrur'`.

- *Codigo*

  ```py
  text = 'mrttaqrhknsw ih puggrur'
  custom_key = 'python'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append any non-letter character to the message
          if not char.isalpha():
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  def encrypt(message, key):
    return vigenere(message, key)

  def decrypt(message, key):
    return vigenere(message, key,-1)

  encryption = encrypt(text, custom_key)
  print(encryption)
  decryption = decrypt(encryption, custom_key)
  print(decryption)
  ```

---

## Paso 88

Dado que en esta ocasión se parte de una cadena cifrada para descifrarla, ya no se necesitará la variable de `encryption`.

> Elimine el `encryption` y la llamada `print(encryption)`. Además, comente las dos últimas líneas del código.

- *Codigo*

  ```py
  text = 'mrttaqrhknsw ih puggrur'
  custom_key = 'python'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append any non-letter character to the message
          if not char.isalpha():
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  def encrypt(message, key):
    return vigenere(message, key)

  def decrypt(message, key):
    return vigenere(message, key,-1)

  # decryption = decrypt(encryption, custom_key)
  print(decryption)
  ```

---

## Paso 89

Se pueden concatenar dos o más cadenas utilizando el operador +. Por ejemplo: `'Hello' + ' there!'` da como resultado `'Hello there!'`.

> Llama a la función `print()` y utiliza el operador `+` para concatenar la variable de `text` con la cadena `'Encrypted text: '`. Presta atención al espaciado.

- *Codigo*

  ```py
  text = 'mrttaqrhknsw ih puggrur'
  custom_key = 'python'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append any non-letter character to the message
          if not char.isalpha():
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  def encrypt(message, key):
    return vigenere(message, key)

  def decrypt(message, key):
    return vigenere(message, key,-1)

  print("Encrypted text: " + text)
  # decryption = decrypt(encryption, custom_key)
  # print(decryption)
  ```

---

## Paso 90

> Debajo de la llamada `print()` que acaba de agregar, agregue otra llamada `print()` para imprimir `Key: python` concatenando la cadena `'Key: '` y el valor de la variable `custom_key`.

- *Codigo*

  ```py
  text = 'mrttaqrhknsw ih puggrur'
  custom_key = 'python'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append any non-letter character to the message
          if not char.isalpha():
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  def encrypt(message, key):
    return vigenere(message, key)

  def decrypt(message, key):
    return vigenere(message, key,-1)

  print("Encrypted text: " + text)
  print('Key: ' + custom_key)
  # decryption = decrypt(encryption, custom_key)
  # print(decryption)
  ```

---

## Paso 91

En Python, hay una forma fácil de dar formato a las cadenas. Las cadenas `f` te permiten interpolar valores en tus cadenas.

La interpolación consiste en escribir marcadores de posición que serán sustituidos por los valores especificados cuando se ejecute el programa. Por ejemplo, puedes obtener el mismo resultado que con `'Encrypted text: ' + text` con `f'Encrypted text: {text}'`. Debes poner una `f` antes de las comillas para crear la `f-string` y escribir las variables o expresiones que deseas interpolar entre llaves.

> Modifica la primera llamada a `print()` para utilizar una `f-string`.

- *Codigo*

  ```py
  text = 'mrttaqrhknsw ih puggrur'
  custom_key = 'python'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append any non-letter character to the message
          if not char.isalpha():
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  def encrypt(message, key):
    return vigenere(message, key)

  def decrypt(message, key):
    return vigenere(message, key,-1)

  print(f'Encrypted text: {text}')
  print('Key: ' + custom_key)
  # decryption = decrypt(encryption, custom_key)
  # print(decryption)
  ```

---

## Paso 92

> A continuación, modifique `print('Key: ' + custom_key)` para utilizar una `cadena f`.

- *Codigo*

  ```py
  text = 'mrttaqrhknsw ih puggrur'
  custom_key = 'python'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append any non-letter character to the message
          if not char.isalpha():
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  def encrypt(message, key):
    return vigenere(message, key)

  def decrypt(message, key):
    return vigenere(message, key,-1)

  print(f'Encrypted text: {text}')
  print(f"Key: {custom_key}")
  # decryption = decrypt(encryption, custom_key)
  # print(decryption)
  ```

---

## Paso 93

El carácter de nueva línea `\n` es una secuencia especial que se utiliza para representar una nueva línea. Puede escribir una barra invertida `\` seguida de una `n` como una secuencia normal de caracteres en una cadena y se sustituirá por una nueva línea en la salida cuando se ejecute el programa.

> Coloque un carácter de nueva línea al principio de su primera llamada de `print` y vea el resultado.

- *Codigo*

  ```py
  text = 'mrttaqrhknsw ih puggrur'
  custom_key = 'python'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append any non-letter character to the message
          if not char.isalpha():
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  def encrypt(message, key):
    return vigenere(message, key)

  def decrypt(message, key):
    return vigenere(message, key,-1)

  print(f'Encrypted text: {text}')
  print(f"Key: {custom_key}")
  # decryption = decrypt(encryption, custom_key)
  # print(decryption)
  ```

---

## Paso 94

> Descomente la variable de `decryption` y cambie su valor pasando `text` como primer argumento para `decrypt`.

- *Codigo*

  ```py
  text = 'mrttaqrhknsw ih puggrur'
  custom_key = 'python'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append any non-letter character to the message
          if not char.isalpha():
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  def encrypt(message, key):
    return vigenere(message, key)

  def decrypt(message, key):
    return vigenere(message, key,-1)

  print(f'Encrypted text: {text}')
  print(f"Key: {custom_key}")
  decryption = decrypt(text, custom_key)
  # print(decryption)
  ```

---

## Paso 95

> Descomente su última llamada a`print()` y cámbiela para que utilice la (`cadena f`) `f'\nDecrypted text: {decryption}\n'` como argumento.

- *Codigo*

  ```py
  text = 'mrttaqrhknsw ih puggrur'
  custom_key = 'python'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append any non-letter character to the message
          if not char.isalpha():
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  def encrypt(message, key):
    return vigenere(message, key)

  def decrypt(message, key):
    return vigenere(message, key,-1)

  print(f'Encrypted text: {text}')
  print(f"Key: {custom_key}")
  decryption = decrypt(text, custom_key)
  print(f'\nDecrypted text: {decryption}\n')
  ```

---

## Paso 96

> ¡Espera un momento! No puedes descifrar nada con una clave incorrecta. Prueba con `'happycoding'`.

**Con eso, tu proyecto de cifrado está completo.**

- *Codigo*

  ```py
  text = 'mrttaqrhknsw ih puggrur'
  custom_key = 'happycoding'

  def vigenere(message, key, direction= 1):
      key_index = 0
      alphabet = 'abcdefghijklmnopqrstuvwxyz'
      final_message = ""
      for char in message.lower():
          #  Append any non-letter character to the message
          if not char.isalpha():
              final_message += char
          else:
              #  Find the right key character to encode/decode
              key_char = key[key_index % len(key)]
              key_index += 1
              #  Define the offset and the encrypted/decrypted letter 
              offset = alphabet.index(key_char)
              index = alphabet.find(char)
              new_index = (index + offset * direction) % len(alphabet)
              final_message += alphabet[new_index]
      
      return final_message

  def encrypt(message, key):
    return vigenere(message, key)

  def decrypt(message, key):
    return vigenere(message, key,-1)

  print(f'Encrypted text: {text}')
  print(f"Key: {custom_key}")
  decryption = decrypt(text, custom_key)
  print(f'\nDecrypted text: {decryption}\n')
  ```

---
