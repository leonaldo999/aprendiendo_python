# Aprenda expresiones regulares creando un generador de contraseñas

Un módulo Python es un archivo que contiene un conjunto de instrucciones y definiciones que puedes utilizar en tu código.

En este proyecto, aprenderás a importar módulos desde la biblioteca estándar de Python. También aprenderás a utilizar expresiones regulares creando tu propio programa generador de contraseñas.

---

## Paso 1

Un módulo de Python es un archivo que contiene código diseñado para realizar tareas específicas. La biblioteca estándar de Python contiene muchos módulos que puedes importar y utilizar en tu código. Para ello, utiliza la instrucción `import` seguida del nombre del módulo.

> Comienza este proyecto importando(`import`) el módulo `string`.

- **Codigo**
  
  ```py
  # Región editable por el usuario
  import string
  # Región editable por el usuario
  ```

---

## Paso 2

Puede acceder a las utilidades definidas dentro del módulo importado mediante la notación de puntos. La notación de puntos funciona añadiendo un punto seguido del nombre de la utilidad al nombre del módulo. Por ejemplo, así es como se accede a la constante `ascii_lowercase`:

- **Codigo Ejemplo**
  
  ```py
  import string

  print(string.ascii_lowercase)
  # Output: abcdefghijklmnopqrstuvwxyz
  ```

En este proyecto, vas a utilizar diferentes constantes del módulo `string`.

> Declara una nueva variable llamada `letters` y asigna `string.ascii_letters` a esta variable.

- **Codigo**
  
  ```py
  # Región editable por el usuario
  import string

  letters = string.ascii_letters
  # Región editable por el usuario
  ```

---

## Paso 3

> Declare dos nuevas variables llamadas `digits` y `symbols` y asígneles `string.digits` y `string.punctuation`, respectivamente.

- **Codigo**
  
  ```py
  import string

  letters = string.ascii_letters
  # Región editable por el usuario
  digits = string.digits
  symbols = string.punctuation
  # Región editable por el usuario
  ```

---

## Paso 4

Estas tres variables constituyen los posibles caracteres entre los que elegir al generar la contraseña.

> Justo antes de ellas, añada un comentario que diga `Define the possible characters for the password`.

- **Codigo**
  
  ```py
  import string
  # Región editable por el usuario

  # Define the possible characters for the password

  # Región editable por el usuario

  letters = string.ascii_letters
  digits = string.digits
  symbols = string.punctuation
  ```

---

## Paso 5

> Ahora declare una variable llamada `all_characters` y asígnele el resultado de concatenar sus variables existentes.

- **Codigo**
  
  ```py
  import string

  # Define the possible characters for the password
  letters = string.ascii_letters
  digits = string.digits
  symbols = string.punctuation
  # Región editable por el usuario
  all_characters = letters + digits + symbols
  # Región editable por el usuario
  ```

---

## Paso 6

Tu variable `all_characters` es una cadena formada por todas las letras minúsculas y mayúsculas, los 10 dígitos y varios caracteres especiales.

> Justo antes de ella, añade un comentario que diga `Combine all characters`.

- **Codigo**
  
  ```py
  import string

  # Define the possible characters for the password
  letters = string.ascii_letters
  digits = string.digits
  symbols = string.punctuation
  
  # Región editable por el usuario
  # Combine all characters
  # Región editable por el usuario
  all_characters = letters + digits + symbols
  ```

---

## Paso 7

> Ahora imprima la variable `all_characters` para ver cómo se ve.

- **Codigo**
  
  ```py
  import string

  # Define the possible characters for the password
  letters = string.ascii_letters
  digits = string.digits
  symbols = string.punctuation
  
  # Combine all characters
  all_characters = letters + digits + symbols
  # Región editable por el usuario
  print(all_characters)
  # Región editable por el usuario

  # ----Salida esperada----
  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
  ```

---

## Paso 8

Es habitual colocar las declaraciones de `import` al principio del código. Además, en caso de que haya varias declaraciones de `import`, ordénelas alfabéticamente para mejorar la legibilidad.

> Al principio del código, `import` el módulo `random`.

- **Codigo**
  
  ```py
  # Región editable por el usuario
  import random
  # Región editable por el usuario
  import string

  # Define the possible characters for the password
  letters = string.ascii_letters
  digits = string.digits
  symbols = string.punctuation
  
  # Combine all characters
  all_characters = letters + digits + symbols
  print(all_characters)

  # ----Salida esperada----
  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
  ```

---

## Paso 9

El módulo `random` contiene un generador de números pseudoaleatorios. La mayoría de sus funcionalidades dependen de la función `random()`, que devuelve un número de coma flotante en el rango entre `0.0` (incluido) y `1.0` (excluido).

> Llama a la función `random()` del módulo `random` e imprime el resultado.

- **Codigo**
  
  ```py
  import random
  import string

  # Define the possible characters for the password
  letters = string.ascii_letters
  digits = string.digits
  symbols = string.punctuation
  
  # Combine all characters
  all_characters = letters + digits + symbols
  print(all_characters)
  
  # Región editable por el usuario
  print(random.random())
  # Región editable por el usuario
  
  # ----Salida esperada----
  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
  # 0.18521323409694668
  ```

---

## Paso 10

La función `choice()` del módulo `random` toma una secuencia y devuelve un elemento aleatorio de la secuencia.

> Modifique su llamada a `print()` para utilizar la función `choice()` y pase `all_characters` como argumento.

- **Codigo**
  
  ```py
  import random
  import string

  # Define the possible characters for the password
  letters = string.ascii_letters
  digits = string.digits
  symbols = string.punctuation
  
  # Combine all characters
  all_characters = letters + digits + symbols
  print(all_characters)
  
  # Región editable por el usuario
  print(random.random())
  # Región editable por el usuario
  
  # ----Salida esperada----
  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
  # 4
  ```

---

## Paso 11

Cada vez que se ejecute el código, deberías ver un carácter aleatorio de la cadena `all_characters`. Esto es exactamente lo que quieres conseguir para crear una contraseña aleatoria.

Sin embargo, el algoritmo en el que se basa `random` hace que los números pseudoaleatorios generados sean predecibles. Por lo tanto, aunque el módulo `random` es adecuado para las aplicaciones más comunes, no se puede utilizar con fines criptográficos, debido a su naturaleza determinista.

> En lugar de importar `random`, importe el módulo `secrets`. A continuación, cambie la llamada a `print()` para utilizar `secrets.choice(all_characters)`.

- **Codigo**
  
  ```py
  # Región editable por el usuario
  import secrets
  # Región editable por el usuario
  import string

  # Define the possible characters for the password
  letters = string.ascii_letters
  digits = string.digits
  symbols = string.punctuation
  
  # Combine all characters
  all_characters = letters + digits + symbols
  print(all_characters)
  
  # Región editable por el usuario
  print(secrets.choice(all_characters))
  # Región editable por el usuario
  
  # ----Salida esperada----
  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
  # z
  ```

---

## Paso 12

Aunque el efecto pueda parecer igual al de `random.choice()`, `secrets` te garantiza la fuente de aleatoriedad más segura que puede proporcionar tu sistema operativo.

> Ahora, elimina tus dos llamadas a `print()`.

- **Codigo**
  
  ```py
  import secrets
  import string

  # Define the possible characters for the password
  letters = string.ascii_letters
  digits = string.digits
  symbols = string.punctuation
  
  # Combine all characters
  all_characters = letters + digits + symbols
  
  # Región editable por el usuario
  # Región editable por el usuario
  
  # ----Salida esperada----
  
  ```

---

## Paso 13

> Declare una función `generate_password` y escriba todo el código, excepto las líneas de `import`, dentro del cuerpo de la función.

- **Codigo**
  
  ```py
  import secrets
  import string

  # Región editable por el usuario
  def generate_password():
  # Región editable por el usuario

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
  
  # ----Salida esperada----
  
  ```

---

## Paso 14

> La función `generate_password` necesita algunos parámetros. Comience agregando un parámetro de `length`.

- **Codigo**
  
  ```py
  import secrets
  import string

  # Región editable por el usuario
  def generate_password(length):
  # Región editable por el usuario

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
  
  # ----Salida esperada----
  
  ```

---

## Paso 15

> En la parte inferior de la función, declare una variable de `password` y asígnele una cadena vacía.

- **Codigo**
  
  ```py
  import secrets
  import string

  def generate_password(length):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      # Región editable por el usuario
      password = ''
      # Región editable por el usuario
  
  # ----Salida esperada----
  
  ```

---

## Paso 16

> Debajo de tu nueva variable, añade un comentario que diga `Generate password`.

- **Codigo**
  
  ```py
  import secrets
  import string

  def generate_password(length):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      password = ''
      # Región editable por el usuario
      # Generate password
      # Región editable por el usuario
  
  # ----Salida esperada----
  
  ```

---

## Paso 17

>A continuación, escribe un bucle `for` con `i` como variable del bucle. Utiliza la función `range()` para iterar hasta el valor de la `length`.
>
> Dentro del bucle, utiliza el operador de asignación de suma para añadir un carácter aleatorio de `all_characters` al valor actual de `password`. Utiliza la función `choice()` del módulo `secrets` para ello.

- **Codigo**
  
  ```py
  import secrets
  import string

  def generate_password(length):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      password = ''
      # Generate password
      # Región editable por el usuario
      for i in range(length):
          password += secrets.choice(all_characters)
      # Región editable por el usuario
  
  # ----Salida esperada----
  
  ```

---

## Paso 18

Se utiliza un solo guión bajo independiente para representar un valor que no te interesa o que no se utilizará en tu código. Tu variable de iteración no se utiliza realmente.

> Modifica tu variable `i` en un guión bajo`_`.

- **Codigo**
  
  ```py
  import secrets
  import string

  def generate_password(length):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      password = ''
      # Generate password
      # Región editable por el usuario
      for _ in range(length):
      # Región editable por el usuario
          password += secrets.choice(all_characters)
  
  # ----Salida esperada----
  
  ```

---

## Paso 19

> Después del bucle, agrega una instrucción `return` a tu función para que devuelva la variable `password`.

- **Codigo**
  
  ```py
  import secrets
  import string

  def generate_password(length):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      password = ''
      # Generate password
      for _ in range(length):
          password += secrets.choice(all_characters)
      # Región editable por el usuario
      return password
      # Región editable por el usuario
  
  # ----Salida esperada----
  
  ```

---

## Paso 20

> Por último, declare una variable `new_password` y asígnele el resultado de llamar a `generate_password`. Pase `8` como argumento a su llamada a `generate_password`.

- **Codigo**
  
  ```py
  import secrets
  import string

  def generate_password(length):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      password = ''
      # Generate password
      for _ in range(length):
          password += secrets.choice(all_characters)
      return password
  
  # Región editable por el usuario
  new_password = generate_password(8)
  # Región editable por el usuario
  
  # ----Salida esperada----
  
  ```

---

## Paso 21

> Comprueba el resultado imprimiendo tu nueva variable.

- **Codigo**
  
  ```py
  import secrets
  import string

  def generate_password(length):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      password = ''
      # Generate password
      for _ in range(length):
          password += secrets.choice(all_characters)
      return password
  
  # Región editable por el usuario
  new_password = generate_password(8)
  print(new_password)
  # Región editable por el usuario
  
  # ----Salida esperada----
  # t;u\N}4w
  ```

---

## Paso 22

Todo parece estar bien, pero sería bueno tener una forma de verificar que la contraseña generada cumpla con ciertas características específicas. Por ejemplo, un número mínimo de caracteres especiales, dígitos o letras mayúsculas/minúsculas. Te encargarás de eso muy pronto.

> Por ahora, comenta las dos últimas líneas de tu código.

- **Codigo**
  
  ```py
  import secrets
  import string

  def generate_password(length):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      password = ''
      # Generate password
      for _ in range(length):
          password += secrets.choice(all_characters)
      return password
  
  # Región editable por el usuario
  # new_password = generate_password(8)
  # print(new_password)
  # Región editable por el usuario
  
  # ----Salida esperada----
  ```

---

## Paso 23

A continuación, vas a dar a tu función más parámetros que actuarán como restricciones para la contraseña generada.

> Modifica la declaración de tu función añadiendo `nums`, `special_chars`, `uppercase` y `lowercase` en este orden después del parámetro `length` ya existente.

- **Codigo**
  
  ```py
  import secrets
  import string

  # Región editable por el usuario
  def generate_password(length, nums, special_chars, uppercase, lowercase):
  # Región editable por el usuario

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      password = ''
      # Generate password
      for _ in range(length):
          password += secrets.choice(all_characters)
      return password
  
  # new_password = generate_password(8)
  # print(new_password)
  
  # ----Salida esperada----
  ```

---

## Paso 24

> Coloque la declaración de la variable de `password` y el siguiente bucle `for` dentro de un bucle `while`. Utilice `True` como condición para el nuevo bucle.

- **Codigo**
  
  ```py
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
  # Región editable por el usuario
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)
  
  # ----Salida esperada----
  ```

---

## Paso 25

> Después del bucle `for`, cree una variable `constraints` y asígnele una lista vacía.

- **Codigo**
  
  ```py
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
  # Región editable por el usuario
          constraints = []
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)
  
  # ----Salida esperada----
  ```

---

## Paso 26

Una tupla es otra estructura de datos integrada en Python. Las tuplas son muy similares a las listas, pero se definen con paréntesis `()`, en lugar de corchetes`[]`. Además, las tuplas son inmutables, a diferencia de las listas.

- **Codigo Ejemplo**

  ```py
  my_tuple = ('larch', 1, True)
  ```

Tu lista `constraints` almacenará tuplas. El primer elemento de cada tupla será un parámetro de restricción.

> Modifica la asignación de la lista `constraints` añadiendo una tupla a tu lista. Utiliza `nums` como primer elemento y una cadena vacía como segundo elemento.

- **Codigo**
  
  ```py
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
  # Región editable por el usuario
          constraints = [
              (nums, "")
          ]
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)
  
  # ----Salida esperada----
  ```

---

## Paso 27

El módulo `re` te permite utilizar expresiones regulares en tu código. Muy pronto aprenderás más sobre las expresiones regulares.

> Por ahora, añade una instrucción de `import` al principio de tu código para importar el módulo `re`.

- **Codigo**
  
  ```py
  # Región editable por el usuario
  import re
  # Región editable por el usuario
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, "")
          ]
      return password
  
  # new_password = generate_password(8)
  # print(new_password)
  
  # ----Salida esperada----
  ```

---

## Paso 28

Una expresión *regular*, o *regex*, es un patrón que se utiliza para encontrar una combinación específica de caracteres dentro de una cadena. Es una alternativa válida a las sentencias condicionales `if/else` cuando se necesita encontrar patrones dentro de una cadena con fines de validación, sustitución de caracteres y otros.

La función `compile()` del módulo `re` compila la cadena pasada como argumento en un objeto de expresión regular que puede ser utilizado por otros métodos `re`.

> Declare una nueva variable `pattern` y asigne el valor de `re.compile('i')` a esta variable.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, "")
          ]
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  # Región editable por el usuario
  pattern = re.compile('i')
  # Región editable por el usuario
  
  # ----Salida esperada----
  ```

---

## Paso 29

La función `search()` del módulo `re` analiza la cadena pasada como argumento buscando el primer lugar donde el patrón regex coincide con la cadena.

> Declare una variable llamada `quote` y asigne la cadena `'Not all those who wander are lost.'` a esta variable. A continuación, imprima el resultado de `pattern.search(quote)`.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, "")
          ]
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  # Región editable por el usuario
  pattern = re.compile('i')
  quote = 'Not all those who wander are lost.'
  print(pattern.search(quote))
  # Región editable por el usuario
  
  # ----Salida esperada----
  # None
  ```

---

## Paso 30

Se devuelve el valor `None`, ya que no se encuentra `i` dentro de la cadena analizada.

> Ahora, modifique la cadena pasada a `re.compile()` en `l` y vea el resultado.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, "")
          ]
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  # Región editable por el usuario
  pattern = re.compile('l')
  quote = 'Not all those who wander are lost.'
  print(pattern.search(quote))
  # Región editable por el usuario
  
  # ----Salida esperada----
  # <re.Match object; span=(5, 6), match='l'>
  ```

---

## Paso 31

Como puede ver en el resultado, ahora su expresión regular coincide con la primera `l` dentro de la cadena.

En su patrón, puede agregar un cuantificador después de un carácter para especificar cuántas veces debe repetirse ese carácter. Por ejemplo, el cuantificador `+` significa que debe repetirse una o más veces.

> Agregue un cuantificador `+`a su patrón.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, "")
          ]
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  # Región editable por el usuario
  pattern = re.compile('l+')
  quote = 'Not all those who wander are lost.'
  print(pattern.search(quote))
  # Región editable por el usuario
  
  # ----Salida esperada----
  # <re.Match object; span=(5, 6), match='l'>
  ```

---

## Paso 32

> Puede obtener el mismo resultado sin utilizar la función `compile()`. Modifique su variable `pattern` a la cadena literal `'l+'`. A continuación, cambie la llamada a `print()` por print `re.search(pattern, quote)`.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, "")
          ]
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  # Región editable por el usuario
  pattern = 'l+'
  quote = 'Not all those who wander are lost.'
  print(re.search(pattern, quote))
  # Región editable por el usuario
  
  # ----Salida esperada----
  # <re.Match object; span=(5, 6), match='l'>
  ```

---

## Paso 33

Para comprobar que la contraseña generada cumple con las características requeridas, vas a utilizar la función `findall()` del módulo `re`. Es similar a `search`, pero devuelve una lista con todas las ocurrencias del patrón coincidente.

> Reemplaza la llamada a `search()` por `findall()` y comprueba el resultado.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, "")
          ]
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  # Región editable por el usuario
  pattern = 'l+'
  quote = 'Not all those who wander are lost.'
  print(re.findall(pattern, quote))
  # Región editable por el usuario
  
  # ----Salida esperada----
  # ['ll', 'l']
  ```

---

## Paso 34

Una clase de caracteres se indica mediante corchetes y coincide con un carácter de entre los especificados entre corchetes. Por ejemplo, `ma[dnt]` coincide con `mad`, `man` o `mat`.

> Modifique su `patter` para que coincida con una `w` seguida de una `h` o una `a`.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, "")
          ]
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  # Región editable por el usuario
  pattern = 'w[ha]'
  quote = 'Not all those who wander are lost.'
  print(re.findall(pattern, quote))
  # Región editable por el usuario
  
  # ----Salida esperada----
  # ['wh', 'wa']
  ```

---

## Paso 35

> Ahora, convierta la cadena vacía de la tupla de restricciones en un patrón de expresión regular que coincida con un solo dígito. Utilice una clase de caracteres que especifique cada dígito del `0` al `9`.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
  # Región editable por el usuario
          constraints = [
              (nums, "[0123456789]")
          ]
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  pattern = 'w[ha]'
  quote = 'Not all those who wander are lost.'
  print(re.findall(pattern, quote))
  
  # ----Salida esperada----
  # ['wh', 'wa']
  ```

---

## Paso 36

Las clases de caracteres también le permiten indicar un rango de caracteres que deben coincidir. Debe especificar los caracteres inicial y final separados por un guión `-`. Los caracteres siguen el orden Unicode.

> Modifique su variable `pattern` para que coincida con cualquier letra `t` precedida por una letra minúscula en la variable `quote`. Utilice el rango de caracteres de la `a` la `z` para ello.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, "[0123456789]")
          ]
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  # Región editable por el usuario
  pattern = '[a-z]t'
  quote = 'Not all those who wander are lost.'
  print(re.findall(pattern, quote))
  # Región editable por el usuario
  
  # ----Salida esperada----
  # ['wh', 'wa']
  ```

---

## Paso 37

> Ahora, modifique el patrón en su tupla de restricciones para indicar el rango de todos los dígitos utilizando corchetes.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
  # Región editable por el usuario
          constraints = [
              (nums, "[0-9]")
          ]
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  pattern = '[a-z]t'
  quote = 'Not all those who wander are lost.'
  print(re.findall(pattern, quote))
  
  # ----Salida esperada----
  # ['ot', 'st']
  ```

---

## Paso 38

El símbolo `^`, colocado al principio de la clase de caracteres, coincide con todos los caracteres excepto los especificados en la clase.

> Agrega un `^` como primer carácter dentro de tu clase de caracteres y observa qué sucede.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, "[0-9]")
          ]
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  # Región editable por el usuario
  pattern = '[^a-z]t'
  quote = 'Not all those who wander are lost.'
  print(re.findall(pattern, quote))
  # Región editable por el usuario
  
  # ----Salida esperada----
  # [' t']
  ```

---

## Paso 39

> Agregue una nueva tupla a la lista `constraints`. Utilice `lowercase` como primer elemento y un patrón de expresión regular `a-z` que coincida con una sola letra minúscula como segundo elemento.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
  # Región editable por el usuario
              (nums, "[0-9]"), (lowercase, "[a-z]")
          ]
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  pattern = '[^a-z]t'
  quote = 'Not all those who wander are lost.'
  print(re.findall(pattern, quote))

  # ----Salida esperada----
  # [' t']

  ```

---

## Paso 40

> Agregue una tercera tupla a la lista `constraints`. Utilice el parámetro `uppercase` como primer elemento y un patrón de expresión regular `'[A-Z]'` que coincida con una sola letra mayúscula como segundo elemento.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
  # Región editable por el usuario
          constraints = [
              (nums, "[0-9]"), 
              (lowercase, "[a-z]"),
              (uppercase, '[A-Z]')
          ]
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  pattern = '[^a-z]t'
  quote = 'Not all those who wander are lost.'
  print(re.findall(pattern, quote))
  
  # ----Salida esperada----
  # [' t']
  ```

---

## Paso 41

> Agregue una última tupla a su lista. Utilice el parámetro `special_chars` como primer elemento y una cadena vacía como segundo elemento.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
  # Región editable por el usuario
          constraints = [
              (nums, "[0-9]"), 
              (lowercase, "[a-z]"),
              (uppercase, '[A-Z]'),
              (special_chars, '')
          ]
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  pattern = '[^a-z]t'
  quote = 'Not all those who wander are lost.'
  print(re.findall(pattern, quote))
  
  # ----Salida esperada----
  # [' t']
  ```

---

## Paso 42

> El carácter *punto* es un comodín que coincide con cualquier carácter de una *cadena*, excepto con el carácter de nueva línea por defecto. Modifique el `pattern` para que coincida con toda la cadena sustituyendo el patrón actual por el carácter comodín punto `.` seguido del cuantificador más `+`.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, "[0-9]"), 
              (lowercase, "[a-z]"),
              (uppercase, '[A-Z]'),
              (special_chars, '')
          ]
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  # Región editable por el usuario
  pattern = '.+'
  quote = 'Not all those who wander are lost.'
  print(re.findall(pattern, quote))
  # Región editable por el usuario
  
  # ----Salida esperada----
  # ['Not all those who wander are lost.']
  ```

---

## Paso 43

Si necesita hacer coincidir un carácter que tiene un significado especial en el patrón, como `.` o `+`, puede escapar de él anteponiéndole un carácter de barra invertida, `\`. Por ejemplo, esto coincide con un signo más: `\+`.

> Modifique el `pattern` para que coincida con un solo punto literal.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, "[0-9]"), 
              (lowercase, "[a-z]"),
              (uppercase, '[A-Z]'),
              (special_chars, '')
          ]
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  # Región editable por el usuario
  pattern = '\.'
  quote = 'Not all those who wander are lost.'
  print(re.findall(pattern, quote))
  # Región editable por el usuario
  
  # ----Salida esperada----
  # ['Not all those who wander are lost.']
  ```

---

## Paso 44

Python proporciona un tipo particular de cadena llamada cadena sin formato(*raw string*). Las cadenas sin formato (*raw string*) tienen el prefijo `r`. La diferencia clave con respecto a las cadenas normales radica en cómo manejan el carácter de barra invertida: en las cadenas sin formato(*raw string*), las barras invertidas se tratan como caracteres literales en lugar de caracteres de escape. Al escribir expresiones regulares, es recomendable utilizar cadenas sin formato(*raw string*), ya que suelen contener muchos caracteres `\`.

> Convierta su cadena de `pattern` en una cadena sin formato añadiéndole el prefijo `r`.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, "[0-9]"), 
              (lowercase, "[a-z]"),
              (uppercase, '[A-Z]'),
              (special_chars, '')
          ]
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  # Región editable por el usuario
  pattern = r'\.'
  quote = 'Not all those who wander are lost.'
  print(re.findall(pattern, quote))
  # Región editable por el usuario
  
  # ----Salida esperada----
  # ['.']

  ```

---

## Paso 45

> Ahora, convierta los cuatro patrones de la lista `constraints` en cadenas sin formato.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
  # Región editable por el usuario
          constraints = [
              (nums, r"[0-9]"), 
              (lowercase, r"[a-z]"),
              (uppercase, r'[A-Z]'),
              (special_chars, r'')
          ]
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  pattern = r'\.'
  quote = 'Not all those who wander are lost.'
  print(re.findall(pattern, quote))
  
  # ----Salida esperada----
  # ['.']

  ```

---

## Paso 46

> La clase de caracteres `\d` es una abreviación de `[0-9]`. Reemplace esta clase de caracteres por la abreviación dentro de su primera tupla de restricciones.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
  # Región editable por el usuario
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r'[A-Z]'),
              (special_chars, r'')
          ]
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  pattern = r'\.'
  quote = 'Not all those who wander are lost.'
  print(re.findall(pattern, quote))
  
  # ----Salida esperada----
  # ['.']

  ```

---

## Paso 47

En una clase de caracteres, puede combinar varios rangos escribiendo un rango tras otro entre corchetes (sin caracteres adicionales). Por ejemplo: `[a-d3-6]` es la combinación de `[a-d]` y `[3-6]`.

> Ahora, modifique el último patrón de expresión regular para que coincida con cualquier carácter no alfanumérico. Combine los rangos `a-z`, `A-Z` y `0-9` en una sola clase de caracteres y añada un `^` como primer carácter para negar el patrón.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
  # Región editable por el usuario
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, r"[^a-zA-Z0-9]")
          ]
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  pattern = r'\.'
  quote = 'Not all those who wander are lost.'
  print(re.findall(pattern, quote))
  
  # ----Salida esperada----
  # ['.']

  ```

---

## Paso 48

Del mismo modo que la clase `[0-9]` es equivalente a `\d`, la clase `[^0-9]` es equivalente a `\D`. Los caracteres alfanuméricos se pueden hacer coincidir con `\w` y los caracteres no alfanuméricos se pueden hacer coincidir con `\W`.

> Reemplace la clase de caracteres `[^a-zA-Z0-9]` por `\W`.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
  # Región editable por el usuario
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, r"\W")
          ]
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  pattern = r'\.'
  quote = 'Not all those who wander are lost.'
  print(re.findall(pattern, quote))
  
  # ----Salida esperada----
  # ['.']

  ```

---

## Paso 49

> Ahora, convierta el `pattern` en la clase abreviada para caracteres no alfanuméricos.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, r"\W")
          ]
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  # Región editable por el usuario
  pattern = r'\W'
  quote = 'Not all those who wander are lost.'
  print(re.findall(pattern, quote))
  # Región editable por el usuario
  
  # ----Salida esperada----
  # [' ', ' ', ' ', ' ', ' ', ' ', '.']

  ```

---

## Paso 50

Los caracteres de espacio y el punto final coinciden, ya que son los únicos caracteres no alfanuméricos de la cadena.

> Ahora convierte la cadena `quote` en un solo carácter de guión bajo.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, r"\W")
          ]
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  # Región editable por el usuario
  pattern = r'\W'
  quote = '_'
  print(re.findall(pattern, quote))
  # Región editable por el usuario
  
  # ----Salida esperada----
  # []

  ```

---

## Paso 51

Dado que el carácter de subrayado es un carácter válido para los nombres de variables, se incluye en la clase de caracteres `\w` (equivalente a `[a-zA-Z0-9_]`), que se puede utilizar cómodamente para buscar nombres de variables.

Por lo tanto, la clase de caracteres `\W` es equivalente a `[^a-zA-Z0-9_]` sin el carácter de subrayado. Por este motivo, no se puede utilizar para buscar todos los caracteres especiales.

>Elimine las tres últimas líneas del código.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, r"\W")
          ]
      return password
  
  # new_password = generate_password(8)
  # print(new_password)

  # Región editable por el usuario
  
  # Región editable por el usuario
  
  # ----Salida esperada----
  # []

  ```

---

## Paso 52

> Ahora, combine su *cadena sin formato*(`r-string`) con una cadena con una *cadena formateada*(`f-string`) e interponga su variable `symbols` dentro de la clase de caracteres. Recuerde que puede interponer una variable dentro de una con una *cadena formateada*(`f-string`) utilizando llaves `{ }`.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
  # Región editable por el usuario
              (special_chars, rf"[{symbols}]")
  # Región editable por el usuario
          ]
      return password
  
  # new_password = generate_password(8)
  # print(new_password)
  
  
  # ----Salida esperada----
  # []

  ```

---

## Paso 53

> Debajo de la lista `constraints`, agregue un comentario que diga `Check constraint`.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
  # Región editable por el usuario
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
          # Check constraints
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)
  
  
  # ----Salida esperada----
  # []

  ```

---

## Paso 54

> Después de tu nuevo comentario, escribe un bucle `for` para iterar sobre la lista `constraints`. Utiliza `constraint` y `pattern` como variables del bucle.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
  # Región editable por el usuario
          # Check constraints
          for constraint, pattern in constraints:
            pass 
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)
  
  
  # ----Salida esperada----
  # []

  ```

---

## Paso 55

> Dentro del bucle `for`, llame a la función `findall()` pasando `pattern` y `password` como argumentos.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
  # Región editable por el usuario
          # Check constraints
          for constraint, pattern in constraints:
            re.findall(pattern, password)
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)
  
  
  # ----Salida esperada----
  # []

  ```

---

## Paso 56

Te interesa el número de elementos de la lista devuelta por la función `findall()`.

> Pasa tu llamada `findall()` existente a la función `len()`.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
  # Región editable por el usuario
          # Check constraints
          for constraint, pattern in constraints:
            len(re.findall(pattern, password))
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)
  
  
  # ----Salida esperada----
  # []

  ```

---

## Paso 57

> Dentro del bucle `for`, compara `constraint` y la longitud de la lista devuelta por `findall()`. Utiliza el operador `<=` para ello.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
  # Región editable por el usuario
          # Check constraints
          for constraint, pattern in constraints:
            constraint <= len(re.findall(pattern, password))
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)
  
  
  # ----Salida esperada----
  # []

  ```

---

## Paso 58

> Justo antes del bucle `for`, declare una variable `count` y asígnele el valor cero.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
  # Región editable por el usuario
          # Check constraints
          count = 0
          for constraint, pattern in constraints:
            constraint <= len(re.findall(pattern, password))
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)
  
  
  # ----Salida esperada----
  # []

  ```

---

## Paso 59

> Convierta la expresión dentro de su bucle `for` en una instrucción `if`. Utilice la restricción de expresión `constraint <= len(re.findall(pattern, password))` como condición `if`.
>
> Dentro de la nueva instrucción condicional, incremente el `count` del recuento en `1`.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
  # Región editable por el usuario
          # Check constraints
          count = 0
          for constraint, pattern in constraints:
            if constraint <= len(re.findall(pattern, password)):
                count += 1
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)
  
  
  # ----Salida esperada----
  # []

  ```

---

## Paso 60

> Por último, después del bucle `for`, crea una instrucción `if` para comprobar si `count` es igual a `4` y sal del bucle `while` utilizando la instrucción `break`.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
  # Región editable por el usuario
          # Check constraints
          count = 0
          for constraint, pattern in constraints:
            if constraint <= len(re.findall(pattern, password)):
                count += 1
          if count == 4:
              break
  # Región editable por el usuario
      return password
  
  # new_password = generate_password(8)
  # print(new_password)
  
  
  # ----Salida esperada----
  # []

  ```

---

## Paso 61

En lugar de utilizar un bucle y una variable contadora, puede obtener el mismo resultado con un enfoque diferente, que implementará en los siguientes pasos.

`all()` es una función integrada de Python que devuelve `True` si todos los elementos dentro de un iterable dado se evalúan como `True`. De lo contrario, devuelve `False`.

> Reemplaza tu bucle `for` existente y las dos sentencias `if` por una sola sentencia `if`. Para la condición `if`, utiliza una llamada a la función `all()` y pasa una lista vacía como argumento a la llamada a la función.

Traducción realizada con la versión gratuita del traductor DeepL.com

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
          # Check constraints
          count = 0
  # Región editable por el usuario
          if all([]):
  # Región editable por el usuario
              break
      return password
  
  # new_password = generate_password(8)
  # print(new_password)
  
  
  # ----Salida esperada----
  # []

  ```

---

## Paso 62

En este momento, `all()` está tomando una lista vacía como argumento. Rellena esa lista vacía utilizando la sintaxis de comprensión para que la lista almacene los resultados de evaluar la restricción de `constraint <= len(re.findall(pattern, password))` para cada tupla de `constraint-pattern` en la lista `constraint`.

> De esta manera, solo saldrás del bucle `while` después de que se cumplan todos los requisitos.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
          # Check constraints
          count = 0
  # Región editable por el usuario
          if all([constraint <= len(re.findall(pattern, password)) 
                for constraint, pattern in constraints]):
  # Región editable por el usuario
              break
      return password
  
  # new_password = generate_password(8)
  # print(new_password)
  
  
  # ----Salida esperada----
  # []

  ```

---

## Paso 63

`All([expresión para i en iterable])` significa que se crea una nueva lista evaluando la `expression` para cada `i` en `iterable`. Después de que la función `all()` itera sobre la lista recién creada, esta se elimina automáticamente, ya que ya no es necesaria.

Se puede ahorrar memoria utilizando una expresión generadora. Las expresiones generadoras siguen la sintaxis de las comprensiones de lista, pero utilizan paréntesis en lugar de corchetes.

> Cambie su comprensión de lista por una expresión generadora eliminando los corchetes.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
          # Check constraints
          count = 0
  # Región editable por el usuario
          if all(
              constraint <= len(re.findall(pattern, password)) 
              for constraint, pattern in constraints
          ):
  # Región editable por el usuario
              break
      return password
  
  # new_password = generate_password(8)
  # print(new_password)
  
  
  # ----Salida esperada----
  # []

  ```

---

## Paso 64

> Ya no necesita la variable `count`. Elimine esta variable y su valor.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
  # Región editable por el usuario
          # Check constraints
          if all(
              constraint <= len(re.findall(pattern, password)) 
              for constraint, pattern in constraints
          ):
  # Región editable por el usuario
              break
      return password
  
  # new_password = generate_password(8)
  # print(new_password)
  
  
  # ----Salida esperada----
  # []

  ```

---

## Paso 65

> Ahora es el momento de probar tu función. Descomenta las dos últimas líneas de tu código y modifica la llamada a la función pasando 5 argumentos. Utiliza `8` para la longitud y `1` para las otras cuatro restricciones.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
  # Región editable por el usuario
          # Check constraints
          if all(
              constraint <= len(re.findall(pattern, password)) 
              for constraint, pattern in constraints
          ):
  # Región editable por el usuario
              break
      return password
  
  new_password = generate_password(8, 1, 1, 1, 1)
  print(new_password)
  
  
  # ----Salida esperada----
  # PHO:q7BM

  ```

---

## Paso 66

Funciona, pero aún hay un par de cosas que puedes mejorar. En primer lugar, llamar a una función con 5 argumentos puede crear confusión sobre qué valor se asignará a cada parámetro.

Puedes llamar a una función utilizando argumentos clave, es decir, escribiendo el nombre del parámetro explícitamente seguido del operador de asignación y el valor. Por ejemplo:

- **Codigo Ejemplo**
  
  ```py
  def add(x, y):
      return x + y
  
  add(x=1, y=7) # 8
  ```

> Modifique la llamada a la función para utilizar argumentos clave.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
          # Check constraints
          if all(
              constraint <= len(re.findall(pattern, password)) 
              for constraint, pattern in constraints
          ):
              break
      return password
  
  # Región editable por el usuario
  new_password = generate_password(
      length=8,
      nums=1,
      special_chars=1,
      uppercase=1,
      lowercase=1
  )
  print(new_password)
  # Región editable por el usuario
  
  
  # ----Salida esperada----
  # y489n~zK

  ```

---

## Paso 67

Siempre que todos los argumentos de una llamada a una función sean argumentos clave, el orden de los argumentos no importa.

> Para confirmarlo, intenta cambiar el orden de `length=8` y `nums=1` en tu llamada a la función.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length, nums, special_chars, uppercase, lowercase):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
          # Check constraints
          if all(
              constraint <= len(re.findall(pattern, password)) 
              for constraint, pattern in constraints
          ):
              break
      return password
  
  # Región editable por el usuario
  new_password = generate_password(
      nums=1,
      length=8,
      special_chars=1,
      uppercase=1,
      lowercase=1
  )
  print(new_password)
  # Región editable por el usuario
  
  
  # ----Salida esperada----
  # |&7=I(v9

  ```

---

## Paso 68

> Modifique la declaración de la función para que acepte parámetros predeterminados. Utilice `16` para la longitud y `1` para las demás restricciones.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  # Región editable por el usuario
  def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
  # Región editable por el usuario

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
          # Check constraints
          if all(
              constraint <= len(re.findall(pattern, password)) 
              for constraint, pattern in constraints
          ):
              break
      return password
  
  new_password = generate_password(
      nums=1,
      length=8,
      special_chars=1,
      uppercase=1,
      lowercase=1
  )
  print(new_password)
  
  
  # ----Salida esperada----
  # `J])8V3o

  ```

---

## Paso 69

Cuando se combinan argumentos predeterminados con argumentos clave, se pueden pasar explícitamente menos argumentos que los requeridos por la función. Los argumentos que no se pasan explícitamente a la llamada a la función tomarán sus valores predeterminados.

> Modifique su llamada a `generate_password()` para que solo tome `length=8`.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
          # Check constraints
          if all(
              constraint <= len(re.findall(pattern, password)) 
              for constraint, pattern in constraints
          ):
              break
      return password
  
  # Región editable por el usuario
  new_password = generate_password(
      length=8
  )
  print(new_password)
  # Región editable por el usuario
  
  
  # ----Salida esperada----
  # `J])8V3o

  ```

---

## Paso 70

> Ahora, elimine todos los argumentos de la llamada a la función.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
          # Check constraints
          if all(
              constraint <= len(re.findall(pattern, password)) 
              for constraint, pattern in constraints
          ):
              break
      return password
  
  # Región editable por el usuario
  new_password = generate_password()
  print(new_password)
  # Región editable por el usuario
  
  
  # ----Salida esperada----
  # xDF)A/,k]0a-{>)x

  ```

---

## Paso 71

> Modifique su llamada a `print()` para que tome la cadena `'Generated password:'` como primer argumento, antes de `new_password`.

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
          # Check constraints
          if all(
              constraint <= len(re.findall(pattern, password)) 
              for constraint, pattern in constraints
          ):
              break
      return password
  
  # Región editable por el usuario
  new_password = generate_password()
  print('Generated password:', new_password)
  # Región editable por el usuario
  
  
  # ----Salida esperada----
  # Generated password: *!aW!@0mwPC/Mh]%

  ```

---

## Paso 72

> Por último, coloca las dos últimas líneas de tu código dentro de una instrucción `if` que se ejecute cuando `__name__ == '__main__'`. De esta manera, tu código no se ejecutará cuando se importe como módulo. De lo contrario, llamará a `generate_password()` e imprimirá la contraseña generada.

**Con esto, el proyecto del generador de contraseñas está completo.**

- **Codigo**
  
  ```py
  import re
  import secrets
  import string

  def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

      # Define the possible characters for the password
      letters = string.ascii_letters
      digits = string.digits
      symbols = string.punctuation
      
      # Combine all characters
      all_characters = letters + digits + symbols
  
      while True:
          password = ""
          # Generate password
          for _ in range(length):
              password += secrets.choice(all_characters)
          constraints = [
              (nums, r"\d"), 
              (lowercase, r"[a-z]"),
              (uppercase, r"[A-Z]"),
              (special_chars, rf"[{symbols}]")
          ]
          # Check constraints
          if all(
              constraint <= len(re.findall(pattern, password)) 
              for constraint, pattern in constraints
          ):
              break
      return password
  
  # Región editable por el usuario
  if __name__ == '__main__':
      new_password = generate_password()
      print('Generated password:', new_password)
  # Región editable por el usuario
  
  
  # ----Salida esperada----
  # Generated password: '5?k&+XUl!$3^dqV

  ```

---
