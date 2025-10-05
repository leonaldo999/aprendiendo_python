# Aprenda las funciones Lambda creando un registro de gastos

- Las funciones **Lambda** te ofrecen una forma concisa de escribir funciones pequeñas y desechables en tu código.

- En este proyecto, explorarás el poder de las funciones **Lambda** mediante la creación de un rastreador de gastos. La aplicación resultante demostrará cómo puedes utilizar las funciones **Lambda** para realizar operaciones eficientes y optimizadas.

---

## Paso 1

**Antes de comenzar con el proyecto, aprenderás sobre las *listas***.

A diferencia de los números(*numbers*) y las cadenas(*strings*), una lista es un tipo de datos que funciona como contenedor de otros valores:

- *Codigo Ejemplo*

  ```py
  example_list = [1, 2, 3, 4]
  empty_list = []
  ```

La lista se caracteriza por los corchetes que rodean todos los valores y una coma entre ellos, como: `["A", "happy", "list"]`. Si la lista no contiene ningún valor, entonces es una lista vacía: `[]`.

Una lista puede contener diferentes tipos de datos: `[1, "Up", ["Down", "Twice"]]`. Eso incluye todos los tipos de datos posibles. ¡También puede contener otra lista!

> Cree una variable llamada `my_list` y asígnele una lista vacía.

- *Codigo*

  ```py
  my_list = []
  ```

---

## Paso 2

Para agregar elementos a una lista, puedes escribirlos entre corchetes, separando los valores con comas.

> Agrega los números `1` y `2` dentro de la lista.

- *Codigo*

  ```py
  my_list = [1, 2]
  ```

---

## Paso 3

Python tiene varios métodos para listas. Por ejemplo, métodos para añadir o eliminar elementos de una lista.

Puedes añadir un elemento al final de una lista utilizando el método `append()`.

- *Codigo Ejemplo*

  ```py
  example_list = [4, 5, 6]

  example_list.append(7)
  ```

`example_list` ahora es `[4, 5, 6, 7]`.

> Intenta usar el método `append()` para añadir `3` a `my_list`. A continuación, imprime la lista.

- *Codigo*

  ```py
  my_list = [1, 2]
  my_list.append(3)

  print(my_list)
  ```

---

## Paso 4

También puede acceder a un solo elemento para obtener su valor.

Las listas están indexadas desde cero, al igual que las cadenas. Eso significa que el primer elemento está en el índice `0`, el segundo elemento está en el índice `1` y así sucesivamente.

Para acceder a un elemento, utilice la notación entre corchetes. Por ejemplo, `example_list[1]` accede al elemento del índice `1`, el segundo elemento, de `example_list`.

> Imprima el primer elemento de `my_list`.

- *Codigo*

  ```py
  my_list = [1, 2]

  my_list.append(3)
  print(my_list)

  print(my_list[0])
  print(my_list)
  ```

---

## Paso 5

Las listas de Python son mutables, lo que significa que el valor de los elementos de la lista se puede cambiar. Puedes cambiar el valor de un elemento utilizando la notación entre corchetes.

- *Codigo Ejemplo*

  ```py
  example_list = [4, 5, 6, 7]
  example_list[1] = 'oh'
  ```

Esto hará que `example_list` tenga el valor `[4, 'oh', 6, 7]`.

> Cambie el primer elemento de `my_list` a `0` y, a continuación, imprima la lista para comprobar el valor.

- *Codigo*

  ```py
  my_list = [1, 2]

  my_list.append(3)
  print(my_list)
  
  print(my_list[0])

  my_list[0] = 0
  print(my_list)
  ```

---

## Paso 6

El método `insert` puede añadir un elemento en cualquier posición de una lista. El primer argumento es la posición en la que se debe añadir el elemento y el segundo argumento es el elemento que se va a añadir. Por ejemplo, así es como se añade un nuevo elemento en la tercera posición de `example_list`:

- *Codigo Ejemplo*

  ```py
  example_list = [4, 5, 6, 7]

  example_list.insert(2, 5.5)

  print(example_list) # [4, 5, 5.5, 6, 7]
  ```

> Usando `insert()`, agregue `1` a `my_list` en la posición adecuada para que cuente hacia arriba, luego imprima la lista.

- *Codigo*

  ```py
  my_list = [1, 2]

  my_list.append(3)
  print(my_list)
  
  print(my_list[0])

  my_list[0] = 0
  print(my_list)

  my_list.insert(1, 1)
  print(my_list)
  ```

---

## Paso 7

El método `pop()` se puede utilizar para eliminar un elemento de una lista. De forma predeterminada, elimina el último elemento de la lista. Se puede pasar un índice como argumento al método y este eliminará el elemento en el índice dado.

- *Codigo Ejemplo*

  ```py
  fruits_list = ["cherry", "lemon", "tomato", "apple", "orange"]

  fruits_list.pop(2)

  print(fruits_list) # ["cherry", "lemon", "apple", "orange"]
  ```

En este caso, `fruits_list.pop(2)` elimina el elemento del índice `2` de la lista.

> Utilice `pop()` para eliminar el último elemento de `my_list` y, a continuación, imprima `my_list`.

- *Codigo*

  ```py
  my_list = [1, 2]

  my_list.append(3)
  print(my_list)
  
  print(my_list[0])

  my_list[0] = 0
  print(my_list)

  my_list.insert(1, 1)
  print(my_list)

  my_list.pop()
  print(my_list)
  ```

---

## Paso 8

> Ahora que ya ha explorado las listas, elimine todo el código que escribió para su revisión y así podrá comenzar el proyecto.

- *Codigo*

  ```py
  # se elimino todo el codigo
  ```

---

## Paso 9

En este proyecto, vas a crear un sencillo pero funcional registro de gastos en Python.

> Empieza definiendo una función llamada `add_expense` que tome tres parámetros: `expenses`, `amount` y `category`. Utiliza la palabra clave `pass` para rellenar el cuerpo de la función.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      pass
  ```

---

## Paso 10

> Cree una lista vacía llamada `expenses`. La utilizará para almacenar cada uno de sus gastos.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      pass
  
  expenses = []
  ```

---

## Paso 11

El parámetro de `expenses` de tu función `add_expense` será una lista de gastos. Quieres poder añadir elementos al final de tu lista. Para ello, utilizarás el método de lista `.append()`.

> Añade una llamada al método `.append()` en la lista de `expenses`. Por ahora, no pases ningún argumento a `.append()`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append()
  
  expenses = []
  ```

---

## Paso 12

Un diccionario es otro tipo de datos integrado en Python. Un diccionario es una colección de datos en forma de pares clave-valor. Los diccionarios se definen con llaves (`{}`) y contienen pares clave-valor separados por comas. Cada clave va seguida de dos puntos (`:`) y del valor:

- *Codigo Ejemplo*

  ```py
  {'amount': 50.0, 'category': 'Food'}
  ```

En el ejemplo anterior, `'amount'` y `'category'` son claves, y `50.0` y `'Food'` son sus valores correspondientes.

> Cree un diccionario con la clave `'amount'` y el valor del parámetro `amount` y pase su nuevo diccionario a la llamada `.append()`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount})
  
  expenses = []
  ```

---

## Paso 13

> Agregue otro par clave-valor al diccionario que está añadiendo a la lista de `expense`. Utilice la cadena `'category'` como clave y el parámetro de `category` como valor.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})
  
  expenses = []
  ```

---

## Paso 14

> A continuación, define una función llamada `print_expenses` que tome un parámetro `expenses`. Esta función se utilizará más adelante para mostrar cada gasto de tu lista.
>
> Rellena el cuerpo de tu nueva función con una instrucción `pass`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      pass

  expenses = []
  ```

---

## Paso 15

> Dentro de la función `print_expenses`, crea un bucle `for` que itere sobre cada elemento de la lista de gastos(`expenses`). Utiliza `expense` como variable del bucle y mueve `pass` dentro del cuerpo del bucle.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          pass

  expenses = []
  ```

---

## Paso 16

A continuación, vas a mostrar los detalles de cada gasto.

> Dentro del bucle `for`, sustituye `pass` por una llamada a `print()` y pásale la siguiente cadena `f'Amount: {expense}, Category: {expense}'`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f"Amount: {expense}, Category: {expense}")

  expenses = []
  ```

---

## Paso 17

En Python, es importante saber que el mismo tipo de comillas que se utiliza para definir una cadena no se puede utilizar dentro de ella. Por ejemplo, la cadena `'I'm a string!'` no es válida. Para utilizar comillas simples dentro de esa cadena, debes hacer una de estas dos cosas:

- Escapar las comillas anteponiéndoles una barra invertida: `'I\'m a string!'`
- O utilizar comillas dobles para definir la cadena: `"I'm a string!"` (*preferible*).

Puede acceder a los valores de un diccionario a través de sus claves. Debe utilizar la notación de corchetes e incluir la clave entre corchetes:

- *Codigo Ejemplo*

  ```py
  my_dict = {'amount': 50.0, 'category': 'Food'}
  my_dict['amount'] # 50.0
  ```

> Actualmente estás interpolando el diccionario de `expense` en tu `f-string`. Modifica la expresión de la `f-string` para acceder al valor de la clave `amount` y la clave `category` en el diccionario de `expense`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  expenses = []
  ```

---

## Paso 18

Necesitarás una función para calcular el importe total de los gastos.

> Define una función llamada `total_expenses` que tome un parámetro `expenses`. Por ahora, rellena el cuerpo de la función con una instrucción `pass`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      pass

  expenses = []
  ```

---

## Paso 19

Las funciones `lambda` son funciones breves y anónimas en Python, ideales para tareas sencillas y puntuales. Se definen mediante la palabra clave `lambda` y utilizan la siguiente sintaxis:

- *Codigo Ejemplo*

  ```py
  lambda x: expr
  ```

En el ejemplo anterior, `x` representa un parámetro que se utilizará en la expresión `expr` y actúa como cualquier parámetro en una función tradicional. `expr` es la expresión que se evalúa y devuelve cuando se llama a la función lambda.

> Cree una variable llamada `test` y asígnele una función `lambda` que tome un parámetro `x` y devuelva `x * 2`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      pass

  test = lambda x: x * 2

  expenses = []
  ```

---

## Paso 20

Para llamar a una función lambda, puede utilizar la sintaxis habitual de las funciones con un par de paréntesis después del nombre de la variable.

> Llame a su función lambda de `test` y pase `3` como argumento. A continuación, imprima el resultado.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      pass

  test = lambda x: x * 2

  expenses = []
  ```

---

## Paso 21

Las funciones lambda se pueden combinar de forma muy útil con la función `map()`, que ejecuta una función específica para cada elemento de una colección de objetos, como una lista:

- *Codigo Ejemplo*

  ```py
  map(lambda x: x * 2, [1, 2, 3])
  ```

La función que se va a ejecutar se pasa como primer argumento, y el iterable se pasa como segundo argumento.

El resultado del ejemplo anterior sería `[2, 4, 6]`, donde cada elemento de la lista pasada a `map()` se ha duplicado por la acción de la función lambda.

> Modifica tu llamada a `print()` para imprimir el resultado de llamar a `map()` con `test` como primer argumento y `[2, 3, 5, 8]` como segundo argumento. Todavía no podrás ver un resultado legible.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      pass

  test = lambda x: x * 2
  print(map(test, [2, 3, 5, 8]))

  expenses = []
  ```

---

## Paso 22

Debería ver algo parecido a `<objeto mapa en 0xd273a8>` impreso en la consola, que es la representación en cadena del objeto mapa devuelto por `mapa()`.

> Para obtener un resultado legible, debe convertir el objeto mapa en una lista. Para ello, pase la llamada a`mapa()` como argumento a la función `lista()`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      pass

  test = lambda x: x * 2
  print(list(map(test, [2, 3, 5, 8])))

  expenses = []
  ```

---

## Paso 23

La función `sum()` devuelve la suma de los elementos del iterable que se pasa como argumento. Vas a utilizar `sum()` junto con las funciones `map()` y `lambda` para obtener el importe total de los gastos.

> Por ahora, haz una pequeña prueba y modifica tu llamada actual a `print()` sustituyendo la llamada a `list()` por una llamada a la función `sum()`, pasándole como argumento la llamada actual a `map()`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      pass

  test = lambda x: x * 2
  # solucion
  print(sum(map(test, [2, 3, 5, 8])))
  # solucion

  expenses = []
  ```

---

## Paso 24

A continuación, vas a implementar la misma lógica dentro de la función `total_expenses`.

> Por ahora, elimina tanto la función de `test` como la llamada a `print()`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      pass

  # solucion
  
  # solucion

  expenses = []
  ```

---

## Paso 25

> En la función `total_expenses`, ahora integrará una función lambda. Reemplace `pass` por una función lambda que tenga `expense` como parámetro.
>
> Se espera que `expense` sea un diccionario, y su función lambda debe devolver el valor de la clave `'amount'` en el diccionario `expense`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      # solucion
      lambda expense: expense["amount"]
      # solucion

  expenses = []
  ```

---

## Paso 26

> Ahora, llame a `map()` pasando su función `lambda` como primer argumento y la lista de `expenses` como segundo argumento.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      # solucion
      map(lambda expense: expense['amount'], expenses)
      # solucion

  expenses = []
  ```

---

## Paso 27

> Por último, pasa tu llamada a `map()` a la función `sum()` para obtener el total de gastos y `return` el resultado.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      # solucion
      return sum(map(lambda expense: expense['amount'], expenses))
      # solucion

  expenses = []
  ```

---

## Paso 28

> A continuación, defina una función llamada `filter_expenses_by_category` que tome dos parámetros: `expenses` y `category`. Utilice `pass` para rellenar el cuerpo de la función.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  # solucion
  def filter_expenses_by_category(expenses, category):
      pass
  # solucion

  expenses = []
  ```

---

## Paso 29

> Dentro de la función `filter_expenses_by_category`, reemplaza `pass` por una función `lambda`. Utiliza `expense` como parámetro y evalúa la comparación entre el valor de la clave `'category'` del diccionario `expense` y `category` utilizando el operador de igualdad.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
  # solucion
      lambda expense: expense['category'] == category
  # solucion

  expenses = []
  ```

---

## Paso 30

La función `filter()` permite seleccionar elementos de un iterable, como una lista, basándose en el resultado de una función:

- *Codigo Ejemplo*

  ```py
  filter(my_function, my_list)
  ```

`filter()` toma una función como primer argumento y un iterable como segundo argumento. Devuelve un iterador, que es un objeto especial que permite iterar sobre los elementos de una colección, como una lista.

El resultado del ejemplo anterior es un iterador que contiene los elementos de `my_list` para los que `my_function` devuelve `True`.

Dentro de la función `filter_expenses_by_category`, llame a `filter()` pasando la función `lambda` que escribió en el paso anterior como primer argumento y la lista de `expenses` como segundo argumento.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
  # solucion
      filter(lambda expense: expense['category'] == category, expenses)
  # solucion

  expenses = []
  ```

---

## Paso 31

> Por último, devuelve(`return`) el resultado de la llamada a `filter()`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
  # solucion
      return filter(lambda expense: expense['category'] == category, expenses)
  # solucion

  expenses = []
  ```

---

## Paso 32

El siguiente paso es definir la función principal, que será el punto de entrada del programa interactivo de seguimiento de gastos.

> Defina una función llamada `main` sin parámetros. Rellene el cuerpo de la función con la lista de `expenses` que creó al principio de este proyecto. Utilizará esta lista para almacenar los registros de gastos.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  # solucion
  def main():
      expenses = []
  # solucion

  ```

---

## Paso 33

Un bucle `while` es otro tipo de bucle que ejecuta una parte del código mientras una condición especificada sea `True`. El bucle termina cuando la condición se vuelve `False`:

- *Codigo Ejemplo*

  ```py
  while condition:
      <code>
  ```

> Debajo de la lista de `expenses`, crea un bucle `while`. Utiliza `True` como condición e imprime la cadena `'\nExpense Tracker'` dentro del cuerpo del bucle para mostrar el título del programa.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
  # solucion
      while True:
          print('\nExpense Tracker')
  # solucion

  ```

---

## Paso 34

El bucle `while` que ha creado en el paso anterior es un bucle infinito que permitirá al programa presentar continuamente las opciones del menú hasta que el usuario decida salir.

> Después de la llamada a `print()`, añada otra llamada a `print()` para imprimir la cadena `'1. Add an expense'`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
      while True:
          print('\nExpense Tracker')
  # solucion
          print('1. Add an expense')
  # solucion

  ```

---

## Paso 35

> A continuación, agrega otra llamada a `print()` y pasa la cadena `'2. List all expenses'`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
      while True:
          print('\nExpense Tracker')
          print('1. Add an expense')
  # solucion
          print('2. List all expenses')
  # solucion

  ```

---

## Paso 36

> Proporcione las demás opciones del menú imprimiendo las siguientes tres cadenas en su bucle `while`: `'3. Show total expenses'`, `'4. Filter expenses by category'` y `'5. Exit'`. Siga añadiendo las llamadas a print() en orden.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
      while True:
          print('\nExpense Tracker')
          print('1. Add an expense')
          print('2. List all expenses')
  # solucion
          print("3. Show total expenses")
          print("4. Filter expenses by category")
          print("5. Exit")
  # solucion

  ```

---

## Paso 37

La función `input()` toma una entrada del usuario y la devuelve en forma de cadena.

> Dentro del bucle `while`, llame a la función `input()` pasando la cadena `'Enter your choice: '` como argumento y asigne el resultado a una variable llamada `choice`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
      while True:
          print('\nExpense Tracker')
          print('1. Add an expense')
          print('2. List all expenses')
          print("3. Show total expenses")
          print("4. Filter expenses by category")
          print("5. Exit")
  # solucion
          choice = input("Enter your choice: ")
  # solucion

  ```

---

## Paso 38

Vas a utilizar sentencias condicionales para comprobar la elección del usuario. Si la elección es `'1'`, significa que el usuario quiere añadir un gasto.

> Sin salir del bucle `while`, debajo de la variable `choice`, escribe una sentencia `if` para comprobar si `choice` es igual a la cadena `'1'`. Si es cierto, será el punto de partida para añadir un nuevo gasto.
>
> Dentro del cuerpo de la instrucción `if`, declara una variable `amount` y asígnale una llamada `input()` vacía.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
      while True:
          print('\nExpense Tracker')
          print('1. Add an expense')
          print('2. List all expenses')
          print("3. Show total expenses")
          print("4. Filter expenses by category")
          print("5. Exit")
          
          choice = input("Enter your choice: ")
  # solucion
          if choice == "1":
              amount = input()
  # solucion

  ```

---

## Paso 39

Dentro de la instrucción `if`, debes pedir al usuario que introduzca el importe del gasto y guardarlo en una variable.

> Pasa la cadena `'Enter amount: '` a tu llamada `input()` vacía, para que puedas guardar el gasto.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
      while True:
          print('\nExpense Tracker')
          print('1. Add an expense')
          print('2. List all expenses')
          print("3. Show total expenses")
          print("4. Filter expenses by category")
          print("5. Exit")
          
          choice = input("Enter your choice: ")
  # solucion
          if choice == "1":
              amount = input('Enter amount: ')
  # solucion

  ```

---

## Paso 40

Es necesario convertir el importe del gasto antes de realizar cualquier cálculo. La función `float()` toma una cadena o un número entero como argumento y devuelve un número de coma flotante.

> Pase `input('Enter amount: ')` a la función `float()`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
      while True:
          print('\nExpense Tracker')
          print('1. Add an expense')
          print('2. List all expenses')
          print("3. Show total expenses")
          print("4. Filter expenses by category")
          print("5. Exit")
          
          choice = input("Enter your choice: ")
  # solucion
          if choice == "1":
              amount = float(input('Enter amount: '))
  # solucion

  ```

---

## Paso 41

> Dentro de la instrucción `if`, crea una variable llamada `category` para almacenar la categoría de gastos. Asígnale una llamada a `input()` y utiliza «`'Enter category: '`» como argumento.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
      while True:
          print('\nExpense Tracker')
          print('1. Add an expense')
          print('2. List all expenses')
          print("3. Show total expenses")
          print("4. Filter expenses by category")
          print("5. Exit")
          
          choice = input("Enter your choice: ")
          if choice == "1":
              amount = float(input('Enter amount: '))
  # solucion
              category = input("Enter category: ")
  # solucion

  ```

---

## Paso 42

> Una vez que tengas los detalles del gasto, debes llamar a la función `add_expense` para añadir el nuevo gasto a la lista de gastos(`expenses`).
>
> Después de obtener el importe(`amount`) y la categoría(`category`) mediante `input()`, llama a la función `add_expense`, pasando tres argumentos: `expenses`, `amount` y `category`.

- `expenses` es la lista vacía creada en la función principal anteriormente en este proyecto.
- `amount` es el importe del gasto.
- `category` es la categoría del gasto.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
      while True:
          print('\nExpense Tracker')
          print('1. Add an expense')
          print('2. List all expenses')
          print("3. Show total expenses")
          print("4. Filter expenses by category")
          print("5. Exit")
          
          choice = input("Enter your choice: ")
          if choice == "1":
              amount = float(input('Enter amount: '))
              category = input("Enter category: ")
  # solucion
              add_expense(expenses, amount, category)
  # solucion

  ```

---

## Paso 43

Para enumerar todos los gastos, puede utilizar una cláusula `elif` después de una instrucción `if`. La cláusula `elif` comprueba condiciones adicionales y solo funciona después de una instrucción `if`.

> Cree una cláusula `elif` para comprobar si la elección del usuario es igual a la cadena `'2'`. Dentro de la cláusula `elif`, imprima la cadena `'\nAll Expenses:'`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
      while True:
          print('\nExpense Tracker')
          print('1. Add an expense')
          print('2. List all expenses')
          print("3. Show total expenses")
          print("4. Filter expenses by category")
          print("5. Exit")
          
          choice = input("Enter your choice: ")
          if choice == "1":
              amount = float(input('Enter amount: '))
              category = input("Enter category: ")
              add_expense(expenses, amount, category)
  # solucion
          elif choice == "2":
            print("\nAll Expenses:")
  # solucion

  ```

---

## Paso 44

> Después de la llamada a `print()`, llame a la función `print_expenses` para mostrar todos los gastos que se han añadido hasta ahora. Pase la lista de `expenses` como argumento.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
      while True:
          print('\nExpense Tracker')
          print('1. Add an expense')
          print('2. List all expenses')
          print("3. Show total expenses")
          print("4. Filter expenses by category")
          print("5. Exit")
          
          choice = input("Enter your choice: ")
          if choice == "1":
              amount = float(input('Enter amount: '))
              category = input("Enter category: ")
              add_expense(expenses, amount, category)
          elif choice == "2":
            print("\nAll Expenses:")
  # solucion
            print_expenses(expenses)
  # solucion

  ```

---

## Paso 45

> Para mostrar los gastos totales, crea una instrucción `elif` que compruebe si `choice == '3'`.
>
> Si es cierto, significa que el usuario quiere ver los gastos totales. Así que llama a `print()` y pasa la cadena `'\nTotal Expenses: '` como primer argumento y `total_expenses(expenses)` como segundo argumento.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
      while True:
          print('\nExpense Tracker')
          print('1. Add an expense')
          print('2. List all expenses')
          print("3. Show total expenses")
          print("4. Filter expenses by category")
          print("5. Exit")
          
          choice = input("Enter your choice: ")
          if choice == "1":
              amount = float(input('Enter amount: '))
              category = input("Enter category: ")
              add_expense(expenses, amount, category)
          elif choice == "2":
            print("\nAll Expenses:")
            print_expenses(expenses)
  # solucion
          elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
  # solucion

  ```

---

## Paso 46

> Cree otra cláusula `elif` que compruebe si `choice == '4'`. Dentro de la nueva cláusula `elif`, cree una variable `category` y asígnele i`nput('Enter category to filter: ')` para filtrar la categoría de gastos.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
      while True:
          print('\nExpense Tracker')
          print('1. Add an expense')
          print('2. List all expenses')
          print("3. Show total expenses")
          print("4. Filter expenses by category")
          print("5. Exit")
          
          choice = input("Enter your choice: ")
          if choice == "1":
              amount = float(input('Enter amount: '))
              category = input("Enter category: ")
              add_expense(expenses, amount, category)
          elif choice == "2":
              print("\nAll Expenses:")
              print_expenses(expenses)
          elif choice == '3':
              print('\nTotal Expenses: ', total_expenses(expenses))
  # solucion
          elif choice == '4':
              category = input('Enter category to filter: ')
  # solucion

  ```

---

## Paso 47

> Después de obtener la categoría, imprima la siguiente f-string `f'\nExpenses for {category}:'`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
      while True:
          print('\nExpense Tracker')
          print('1. Add an expense')
          print('2. List all expenses')
          print("3. Show total expenses")
          print("4. Filter expenses by category")
          print("5. Exit")
          
          choice = input("Enter your choice: ")
          if choice == "1":
              amount = float(input('Enter amount: '))
              category = input("Enter category: ")
              add_expense(expenses, amount, category)
          elif choice == "2":
              print("\nAll Expenses:")
              print_expenses(expenses)
          elif choice == '3':
              print('\nTotal Expenses: ', total_expenses(expenses))
          elif choice == '4':
              category = input('Enter category to filter: ')
  # solucion
              print(f"\nExpenses for {category}:")
  # solucion

  ```

---

## Paso 48

> Después de llamar a `print()`, debes filtrar los gastos e imprimir la lista filtrada. Declara una variable `expenses_from_category` y asígnale una llamada a `filter_expenses_by_category` pasando `expenses` y `category` como argumentos.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
      while True:
          print('\nExpense Tracker')
          print('1. Add an expense')
          print('2. List all expenses')
          print("3. Show total expenses")
          print("4. Filter expenses by category")
          print("5. Exit")
          
          choice = input("Enter your choice: ")
          if choice == "1":
              amount = float(input('Enter amount: '))
              category = input("Enter category: ")
              add_expense(expenses, amount, category)
          elif choice == "2":
              print("\nAll Expenses:")
              print_expenses(expenses)
          elif choice == '3':
              print('\nTotal Expenses: ', total_expenses(expenses))
          elif choice == '4':
              category = input('Enter category to filter: ')
              print(f"\nExpenses for {category}:")
  # solucion
              expenses_from_category = filter_expenses_by_category(expenses, category)
  # solucion

  ```

---

## Paso 49

> Aún dentro de la cláusula `elif`, pasa el iterador `expenses_from_category` a una llamada `print_expenses`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
      while True:
          print('\nExpense Tracker')
          print('1. Add an expense')
          print('2. List all expenses')
          print("3. Show total expenses")
          print("4. Filter expenses by category")
          print("5. Exit")
          
          choice = input("Enter your choice: ")
          if choice == "1":
              amount = float(input('Enter amount: '))
              category = input("Enter category: ")
              add_expense(expenses, amount, category)
          elif choice == "2":
              print("\nAll Expenses:")
              print_expenses(expenses)
          elif choice == '3':
              print('\nTotal Expenses: ', total_expenses(expenses))
          elif choice == '4':
              category = input('Enter category to filter: ')
              print(f"\nExpenses for {category}:")
              expenses_from_category = filter_expenses_by_category(expenses, category)
  # solucion
              print_expenses(expenses_from_category)
  # solucion

  ```

---

## Paso 50

> Para proporcionar una forma de salir del programa, utilice otra cláusula `elif` para comprobar si `choice` es igual a la cadena `'5'`.
>
> Dentro de la nueva cláusula `elif`, imprima la cadena `'Exiting the program.'` para indicar que el programa está terminando su ejecución.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
      while True:
          print('\nExpense Tracker')
          print('1. Add an expense')
          print('2. List all expenses')
          print("3. Show total expenses")
          print("4. Filter expenses by category")
          print("5. Exit")
          
          choice = input("Enter your choice: ")
          if choice == "1":
              amount = float(input('Enter amount: '))
              category = input("Enter category: ")
              add_expense(expenses, amount, category)
          elif choice == "2":
              print("\nAll Expenses:")
              print_expenses(expenses)
          elif choice == '3':
              print('\nTotal Expenses: ', total_expenses(expenses))
          elif choice == '4':
              category = input('Enter category to filter: ')
              print(f"\nExpenses for {category}:")
              expenses_from_category = filter_expenses_by_category(expenses, category)
              print_expenses(expenses_from_category)
  # solucion
          elif choice == '5':
            print('Exiting the program.')
  # solucion

  ```

---

## Paso 51

> Por último, para detener la ejecución del bucle `while`, agregue la instrucción `break` dentro de su última cláusula `elif`.

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
      while True:
          print('\nExpense Tracker')
          print('1. Add an expense')
          print('2. List all expenses')
          print("3. Show total expenses")
          print("4. Filter expenses by category")
          print("5. Exit")
          
          choice = input("Enter your choice: ")
          if choice == "1":
              amount = float(input('Enter amount: '))
              category = input("Enter category: ")
              add_expense(expenses, amount, category)
          elif choice == "2":
              print("\nAll Expenses:")
              print_expenses(expenses)
          elif choice == '3':
              print('\nTotal Expenses: ', total_expenses(expenses))
          elif choice == '4':
              category = input('Enter category to filter: ')
              print(f"\nExpenses for {category}:")
              expenses_from_category = filter_expenses_by_category(expenses, category)
              print_expenses(expenses_from_category)
          elif choice == '5':
              print('Exiting the program.')
  # solucion
              break
  # solucion

  ```

---

## Paso 52

> Por último, llama a tu función `main()` y prueba el programa de seguimiento de gastos en la consola.

**¡Con esto, el proyecto de seguimiento de gastos está completo!**

- *Codigo*

  ```py
  def add_expense(expenses, amount, category):
      expenses.append({"amount": amount, "category": category})

  def print_expenses(expenses):
      for expense in expenses:
          print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

  def total_expenses(expenses):
      return sum(map(lambda expense: expense['amount'], expenses))

  def filter_expenses_by_category(expenses, category):
      return filter(lambda expense: expense['category'] == category, expenses)

  def main():
      expenses = []
      while True:
          print('\nExpense Tracker')
          print('1. Add an expense')
          print('2. List all expenses')
          print("3. Show total expenses")
          print("4. Filter expenses by category")
          print("5. Exit")
          
          choice = input("Enter your choice: ")
          if choice == "1":
              amount = float(input('Enter amount: '))
              category = input("Enter category: ")
              add_expense(expenses, amount, category)
          elif choice == "2":
              print("\nAll Expenses:")
              print_expenses(expenses)
          elif choice == '3':
              print('\nTotal Expenses: ', total_expenses(expenses))
          elif choice == '4':
              category = input('Enter category to filter: ')
              print(f"\nExpenses for {category}:")
              expenses_from_category = filter_expenses_by_category(expenses, category)
              print_expenses(expenses_from_category)
          elif choice == '5':
              print('Exiting the program.')
              break
  # solucion
  main()
  # solucion

  ```

---
