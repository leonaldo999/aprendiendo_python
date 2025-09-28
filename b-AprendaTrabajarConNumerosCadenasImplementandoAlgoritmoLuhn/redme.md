# Aprenda a trabajar con números y cadenas implementando el algoritmo de Luhn

El algoritmo de Luhn se utiliza ampliamente para la verificación de errores en diversas aplicaciones, como la verificación de números de tarjetas de crédito.

Al desarrollar este proyecto, adquirirás experiencia en el manejo de cálculos numéricos y la manipulación de cadenas de caracteres.

---

## Paso 1

En este proyecto, implementarás el algoritmo de **Luhn**. Este algoritmo es una fórmula para validar una variedad de números de identificación.

> Comienza declarando una función llamada `main`, que servirá como punto de entrada del programa. Utiliza la palabra clave `pass` para evitar un error.

- *Codigo*

  ```py
  def main():
      pass
  ```

---

## Paso 2

> Reemplaza la instrucción pass por una variable llamada `card_number` y un valor de `'4111-1111-4555-1142'`.

- *Codigo*

  ```py
  def main():
      card_number = "4111-1111-4555-1142"
  ```

---

## Paso 3

Python incluye clases integradas que nos pueden ayudar a manipular cadenas. Una de ellas es la clase `str`. Tiene un método llamado `maketrans` que nos puede ayudar a crear una **tabla de traducción**. Esta tabla se puede utilizar para sustituir caracteres en una cadena:

- *Codigo Ejemplo*

  ```py
  str.maketrans({'t': 'c', 'l': 'b'})
  ```

Lo anterior, cuando se llama en una cadena, reemplazará todos los caracteres `t` por `c` y todos los caracteres `l` por `b`.

> Cree una variable llamada `card_translation` y asígnele una *tabla de traducción* para reemplazar todos los caracteres `-` y ` ` por una cadena vacía.

- *Codigo*

  ```py
  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
  ```

---

## Paso 4

Definir la traducción no traduce por sí solo la cadena. Se debe llamar al método translate sobre la cadena que se va a traducir con la tabla de traducción como argumento:

- *Codigo Ejemplo*

  ```py
  my_string = "tamperlot"
  translation_table = str.maketrans({'t': 'c', 'l': 'b'})
  translated_string = my_string.translate(translation_table)
  ```

> Cree una variable llamada `translated_card_number` y asígnele el resultado de llamar al método `translate` en `card_number` con `card_translation` como argumento.

- *Codigo*

  ```py
  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)
  ```

---

## Paso 5

> Imprima el número de tarjeta traducido=(`translated card`) en la consola.

- *Codigo*

  ```py
  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)
      print(translated_card_number)
  ```

---

## Paso 6

> Llama a la función `main` al final de tu script.

- *Codigo*

  ```py
  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      print(translated_card_number)
  main()
  ```

---

## Paso 7

> Defina una función `verify_card_number` con un parámetro `card_number` y utilice la palabra clave `pass` para que la función no haga nada.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    pass

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      print(translated_card_number)
  main()
  ```

---

## Paso 8

> Dentro de la función `main`, llame a la función `verify_card_number` y pase la variable `translated_card_number` como argumento.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    pass

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      print(translated_card_number)
      
      verify_card_number = translated_card_number
  main()
  ```

---

## Paso 9

El algoritmo de Luhn es el siguiente:

- De derecha a izquierda, duplique el valor de cada segundo dígito; si el producto es mayor que 9, sume los dígitos de los productos.

- Suma todos los dígitos.

- Si la suma de todos los dígitos es múltiplo de 10, el número es válido; de lo contrario, no lo es.

Supongamos un ejemplo de un número de cuenta `'799273987'` al que se le añadirá un dígito de control, quedando en el formato `7992739871x`:

| | | | | | | | | | | | |
|:---|:---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Account number** | 7 | 9 | 9 | 2 | 7 | 3 | 9 | 8 | 7 | 1 | x |
| **Double every other** | 7 | 18 | 9 | 4 | 7 | 6 | 9 | 16 | 7 | 2 | x |
| **Sum 2-char digits** | 7 | 9 | 9 | 2 | 7 | 6 | 9 | 7 | 7 | 2 | x |

> Reemplaza la instrucción `pass` por una variable `sum_of_odd_digits` y un valor de `0`.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      print(translated_card_number)

      verify_card_number = translated_card_number
      
  main()
  ```

---

## Paso 10

Ya ha accedido a elementos (caracteres) de una cadena utilizando el operador de índice `[]`. También puede utilizar el operador de índice para acceder a un rango de caracteres en una cadena con `string[start:stop:step]`:

- *Codigo Ejemplo*

  ```py
  my_string = 'camperbot'
  my_string[0:6] == 'camper' # True
  my_string[0:6:3] == 'cp' # True
  ```

Donde `start` es el índice inicial (incluido), `stop` es el índice final (excluido) y `step` es la cantidad de caracteres que se deben omitir. Si no se especifica, el valor predeterminado de `step` es 1.

> Cree una variable llamada `card_number_reversed` y asígnele el valor de los primeros 4 caracteres de `card_number`.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[0:4]

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      print(translated_card_number)

      verify_card_number = translated_card_number
      
  main()
  ```

---

## Paso 11

> Imprima el valor de la variable `card_number_reversed` en la consola.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[0:4]
    print(card_number_reversed)

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      print(translated_card_number)

      verify_card_number = translated_card_number
      
  main()
  ```

---

## Paso 12

> Cambie `card_number_reversed` para que sea cada segundo dígito de los primeros cuatro dígitos de `card_number`.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[0:4:2]
    print(card_number_reversed)

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      print(translated_card_number)

      verify_card_number = translated_card_number
      
  main()
  ```

---

## Paso 13

> Invierta el orden de los dígitos de los últimos cuatro dígitos del `card_number`, utilizando un segmento con un paso de `-1`. Puede utilizar índices negativos o positivos para los índices inicial y final.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[-1:-5:-1]
    print(card_number_reversed)

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      print(translated_card_number)

      verify_card_number = translated_card_number
      
  main()
  ```

---

## Paso 14

Al igual que el paso es opcional, también lo son el inicio en `0` y el final al final del segmento:

- *Codigo Ejemplo*

  ```py
  my_string = 'camperbot'
  camperbot = my_string[::]
  ```

> Asigna el reverso de la cadena `card_number` completa a la variable `card_number_reversed`.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    print(card_number_reversed)

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      print(translated_card_number)

      verify_card_number = translated_card_number
      
  main()
  ```

---

## Paso 15

> Elimine la llamada de `print` de la función `verify_card_number`.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      print(translated_card_number)

      verify_card_number = translated_card_number
      
  main()
  ```

---

## Paso 16

> Elimine la llamada de `print` de la función `main`.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      verify_card_number = translated_card_number
      
  main()
  ```

---

## Paso 17

> Dentro de la función `verify_card_number`, cree una variable `odd_digits` que contenga cada dos dígitos de la cadena `card_number_reversed`.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      verify_card_number = translated_card_number
      
  main()
  ```

---

## Paso 18

> Imprima el valor de la variable `odd_digits` en la consola.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    print(odd_digits)

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      verify_card_number = translated_card_number
      
  main()
  ```

---

## Paso 19

> Utilice un bucle `for` para iterar sobre cada dígito de la lista `odd_digits`. Mueva la llamada a `print` del paso anterior al bucle `for` y cámbiela para imprimir cada dígito.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    
    for digit in odd_digits:
    print(digit)

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      verify_card_number = translated_card_number
      
  main()
  ```

---

## Paso 20

> Dentro del bucle `for`, usa el operador `+=` para sumar el `digit` a la variable `sum_of_odd_digits`.

Al hacer esto, tu script generará un error `TypeError` porque estás intentando sumar una cadena a un entero, pero no te preocupes, en el siguiente paso aprenderás más sobre cómo hacer que funcione.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    
    for digit in odd_digits:
        sum_of_odd_digits += digit
    print(digit)

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      verify_card_number = translated_card_number
      
  main()
  ```

---

## Paso 21

Actualmente, tu script genera un error `TypeError` porque estás intentando sumar una cadena a un entero. Puedes solucionarlo convirtiendo la variable `digit` en un entero antes de sumarla a `sum_of_odd_digits`, utilizando la función `int` integrada:

- *Codigo Ejemplo*

  ```py
  my_string = '123'
  my_int = int(my_string)
  ```

> Convierte la variable `digit` en un entero antes de añadirla a `sum_of_odd_digits`. A continuación, mueve la llamada a `print` al final de la función `verify_card_number` para imprimir el valor de `sum_of_odd_digits`.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    print(sum_of_odd_digits)

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      verify_card_number = translated_card_number
      
  main()
  ```

---

## Paso 22

Debajo de la llamada de `print`, crea una variable llamada `sum_of_even_digits` y asígnale el valor `0`.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    print(sum_of_odd_digits)
    sum_of_even_digits = 0

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      verify_card_number = translated_card_number
      
  main()
  ```

---

## Paso 23

> Cree una variable `even_digits` y asígnele los dígitos pares del número de tarjeta invertido=(`card_number_reversed`).

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    print(sum_of_odd_digits)

    sum_of_even_digits = 0
    # solucion
    even_digits = card_number_reversed[1::2]
    # solucion

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      verify_card_number = translated_card_number
      
  main()
  ```

---

## Paso 24

> Recorra los `digit` pares e imprima cada uno de ellos en la consola.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
    print(sum_of_odd_digits)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    # solucion
    for digit in even_digits:
        print(digit)
    # solucion


  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      verify_card_number = translated_card_number
      
  main()
  ```

---

## Paso 25

> Elimine la llamada de `print` para la "suma de los dígitos impares"=(`sum_of_odd_digits`).

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)
      # solucion

      # solucion


    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        print(digit)

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      verify_card_number = translated_card_number
      
  main()
  ```

---

## Paso 26

La siguiente parte del algoritmo de Luhn consiste en multiplicar por `2` todos los dígitos pares.

> Dentro del bucle `for` del `digit`, reemplaza la llamada a `print` por una variable llamada `number` y asígnale el valor del `digit` multiplicado por `2`.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
      # solucion
        number = int(digit) * 2
      # solucion

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      verify_card_number = translated_card_number
      
  main()
  ```

---

## Paso 27

> Para evitar que la multiplicación de un dígito sea mayor que `9`, dentro del bucle de dígitos pares, agrega una instrucción `if` que compruebe si el `number` es mayor o igual que `10`. Si lo es, imprime el `number`.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2

  def main():
      card_number = "4111-1111-4555-1142"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      # solucion
      if verify_card_number = translated_card_number:
          print('VALID!')
      else:
          print('INVALID!')
      # solucion
      
  main()
  ```

---

## Paso 34

> Cambie el valor de `card_number` de modo que se imprima `'INVALID!'` en la consola.

- *Codigo*

  ```py
  def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]
    
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2

  def main():
      card_number = "4111-1111-4555-1141"
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)

      # solucion
      if verify_card_number = translated_card_number:
          print('VALID!')
      else:
          print('INVALID!')
      # solucion
      
  main()
  ```

---

## Paso 35

**Enhorabuena por completar este proyecto.**

> Como paso final, elimine la llamada `print` de la función `verify_card_number` y cambie el "número de tarjeta"=(`card_number`) por uno válido.

- *Codigo*

  ```py
  def verify_card_number(card_number):
      sum_of_odd_digits = 0
      card_number_reversed = card_number[::-1]
      odd_digits = card_number_reversed[::2]
  
      for digit in odd_digits:
          sum_of_odd_digits += int(digit)
  
      sum_of_even_digits = 0
      even_digits = card_number_reversed[1::2]
      for digit in even_digits:
          number = int(digit) * 2
          if number >= 10:
              number = (number // 10) + (number % 10)
          sum_of_even_digits += number
      total = sum_of_odd_digits + sum_of_even_digits
      # solucion
      
      # solucion
      return total % 10 == 0
  
  def main():
      # solucion
      card_number = '4111-1111-4555-1142'
      # solucion
      card_translation = str.maketrans({'-': '', ' ': ''})
      translated_card_number = card_number.translate(card_translation)
  
      if verify_card_number(translated_card_number):
          print('VALID!')
      else:
          print('INVALID!')
  
  main()
  ```

---
