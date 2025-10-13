# Crear un proyecto de formateador aritmético

Los alumnos de primaria suelen organizar los problemas aritméticos verticalmente para que sean más fáciles de resolver. Por ejemplo, `"235 + 52"` se convierte en:

- *Codigo Ejemplo*

  ```py
    235
  +  52
  -----
  ```

Termina la función `arithmetic_arranger` que recibe una lista de cadenas que son problemas aritméticos y devuelve los problemas ordenados verticalmente y uno al lado del otro. La función debe aceptar opcionalmente un segundo argumento. Cuando el segundo argumento se establece en `True`, se deben mostrar las respuestas.

## Ejemplos de uso

*Llamada a función:*

- *Codigo Ejemplo*

  ```py
  arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
  ```

*Resultado:*

- *Codigo Ejemplo*

  ```py
     32      3801      45      123
  + 698    -    2    + 43    +  49
  -----    ------    ----    -----
  ```

*Llamada a función:*

- *Codigo Ejemplo*

  ```py
  arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
  ```

*Resultado:*

- *Codigo Ejemplo*

  ```py
    32         1      9999      523
  +  8    - 3801    + 9999    -  49
  ----    ------    ------    -----
    40     -3800     19998      474
  ```

## Reglas

La función devolverá la conversión correcta si los problemas proporcionados están correctamente formateados; de lo contrario, devolverá una cadena que describe un error significativo para el usuario.

- *Situaciones que devolverán un error:*
  
  - Si se proporcionan demasiados problemas a la función. El límite es cinco, cualquier cantidad superior devolverá: `'Error: Too many problems.'`.
  - Los operadores adecuados que aceptará la función son la suma y la resta. La multiplicación y la división devolverán un error. No será necesario probar otros operadores no mencionados en este punto. El error devuelto será: `"Error: Operator must be '+' or '-'."`.
  - Cada número (operando) solo debe contener dígitos. De lo contrario, la función devolverá: `'Error: Numbers must only contain digits.'`.
  - Cada operando (es decir, el número a cada lado del operador) tiene un máximo de cuatro dígitos de ancho. De lo contrario, la cadena de error devuelta será: `'Error: Numbers cannot be more than four digits.'`.

- *Si el usuario ha proporcionado el formato correcto de los problemas, la conversión que devuelva seguirá estas reglas:*

  - Debe haber un solo espacio entre el operador y el más largo de los dos operandos, el operador estará en la misma línea que el segundo operando, ambos operandos estarán en el mismo orden en que se proporcionaron (el primero será el superior y el segundo será el inferior).
  - Los números deben estar alineados a la derecha.
  - Debe haber cuatro espacios entre cada problema.
  - Debe haber guiones en la parte inferior de cada problema. Los guiones deben extenderse a lo largo de toda la longitud de cada problema individualmente. (El ejemplo anterior muestra cómo debe quedar).

> Nota: abre la consola del navegador con F12 para ver una salida más detallada de las pruebas.

- **Codigo**

  ```py
  def arithmetic_arranger(problems, show_answers=False):
      
      

      return problems

  print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
  ```
