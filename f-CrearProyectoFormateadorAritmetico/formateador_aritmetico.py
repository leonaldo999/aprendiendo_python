def arithmetic_arranger(problems, show_answers=False):
    # Si hay más de 5 problemas, retorna un error
    if len(problems) > 5:
        return "Error: Too many problems."

    # Listas para almacenar cada línea de la salida
    first_line = []  # Primer operando de cada problema
    second_line = []  # Operador y segundo operando
    dashes = []  # Línea de guiones
    results = []  # Resultados (si show_answers es True)

    # Procesa cada problema individualmente
    for problem in problems:
        parts = problem.split()
        # Verifica que el problema tenga exactamente 3 partes
        if len(parts) != 3:
            return "Error: Each problem must contain two operands and one operator."
        left, operator, right = parts

        # Solo se permiten suma y resta
        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."
        # Ambos operandos deben ser dígitos
        if not left.isdigit() or not right.isdigit():
            return "Error: Numbers must only contain digits."
        # Ningún operando puede tener más de 4 dígitos
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calcula el ancho necesario para alinear el problema
        width = max(len(left), len(right)) + 2
        # Agrega el primer operando alineado a la derecha
        first_line.append(left.rjust(width))
        # Agrega el operador y el segundo operando alineado
        second_line.append(operator + " " + right.rjust(width - 2))
        # Agrega la línea de guiones
        dashes.append("-" * width)

        # Si se deben mostrar respuestas, calcula y almacena el resultado
        if show_answers:
            if operator == "+":
                answer = str(int(left) + int(right))
            else:
                answer = str(int(left) - int(right))
            results.append(answer.rjust(width))

    # Une cada línea con 4 espacios entre problemas
    arranged = (
        "    ".join(first_line)
        + "\n"
        + "    ".join(second_line)
        + "\n"
        + "    ".join(dashes)
    )
    # Si se piden respuestas, agrega la línea de resultados
    if show_answers:
        arranged += "\n" + "    ".join(results)


    return arranged


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
print(
    f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "143 + 69"])}'
)
print(
    f'\n{arithmetic_arranger(
        [
            "32 + 698",
            "3801 - 2",
            "45 + 43",
            "123 + 49",
            "223 + 19",
            "122 + 48"
            ]
        )}'
)


# -----------------Salida-------------------
#    32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----

#    32      3801      45      123      143
# + 698    -    2    + 43    +  49    +  69
# -----    ------    ----    -----    -----

# Error: Too many problems.
