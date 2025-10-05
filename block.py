# cadena = "Estamos aprendiendo " + "Pyton"
# cadena = "Estamos aprendiendo " * 4
# number = 7
# flotante = 7.2
# cadena = "Estamos aprendiendo "
# cadena_numerica = "126"
# cadena_flotante = "12.6"
# numeros = 1, 000, 000
# numeros = 1_000_000
# cadena2 = "Pyton"
# print(cadena)
# print(cadena + cadena2)
# print(len(cadena))
# print(type(cadena))
# print(type(flotante))
# print(type(number))
# print(int(flotante))
# print(float(number))
# print(type(cadena_numerica))
# print(int(cadena_numerica))
# print(int(cadena_numerica) / 3)
# print(float(cadena_flotante))
# print(numeros)


# ==========================


def encontrar_palabra_mas_larga(oracion):
    """
    Dada una oración, devuelve la palabra más larga de la misma.
    Ignora los puntos (.) al determinar la longitud.
    Si hay varias palabras con la misma longitud, devuelve la primera.
    """
    # 1. Limpiar y dividir la oración en palabras
    #    - Reemplazar comas, dos puntos, puntos y comas y signos de exclamación/interrogación
    #      por un espacio para asegurar una buena separación de palabras.
    #    - El punto final se maneja en el paso 2.
    #    - Convertir todo a minúsculas (opcional, pero buena práctica si se considera
    #      que la longitud es la única métrica).
    #
    # Nota: Usaremos 'split()' sin argumentos para manejar múltiples espacios.

    # Pre-limpieza para manejar otros signos de puntuación comunes que no sean el punto
    puntuacion_a_reemplazar = [
        ",",
        ":",
        ";",
        "!",
        "¿",
        "?",
        "¡",
        "(",
        ")",
        "[",
        "]",
        "{",
        "}",
    ]
    for signo in puntuacion_a_reemplazar:
        oracion = oracion.replace(signo, " ")

    palabras = oracion.split()

    # Inicializar la palabra más larga y su longitud
    palabra_mas_larga = ""
    max_longitud = 0

    for palabra in palabras:
        # 2. Limpiar el punto y calcular la longitud
        #    - Crear una versión "limpia" de la palabra (sin puntos).
        palabra_limpia = palabra.replace(".", "")

        longitud_actual = len(palabra_limpia)

        # 3. Comprobar si es la más larga
        #    - El uso de '>' garantiza que solo se reemplace si la palabra actual
        #      es estrictamente más larga. Esto automáticamente maneja el caso de empate
        #      devolviendo la *primera* que se encontró.
        if longitud_actual > max_longitud:
            max_longitud = longitud_actual
            palabra_mas_larga = (
                palabra_limpia  # Usamos la versión limpia para la salida
            )

    return palabra_mas_larga


# ---
## Ejemplos de uso

oracion1 = "El perro salta y corre. La bicicleta es rapidísima."
oracion2 = "Hola. ¿Qué tal estás?"
oracion3 = "Programación es más larga que algoritmo."
oracion4 = "Python es genial."
oracion5 = "Tengo tres palabras: sol, mar, pan."  # Prueba con palabras de longitud 3
oracion6 = "Este ejemplo tiene dos palabras muy, muy, muy largas."  # Prueba con empate (debería devolver la primera "muy")

resultado1 = encontrar_palabra_mas_larga(oracion1)
resultado2 = encontrar_palabra_mas_larga(oracion2)
resultado3 = encontrar_palabra_mas_larga(oracion3)
resultado4 = encontrar_palabra_mas_larga(oracion4)
resultado5 = encontrar_palabra_mas_larga(oracion5)
resultado6 = encontrar_palabra_mas_larga(oracion6)

print(f"Oración 1: '{oracion1}' -> Palabra más larga: '{resultado1}'")
print(f"Oración 2: '{oracion2}' -> Palabra más larga: '{resultado2}'")
print(f"Oración 3: '{oracion3}' -> Palabra más larga: '{resultado3}'")
print(f"Oración 4: '{oracion4}' -> Palabra más larga: '{resultado4}'")
print(f"Oración 5: '{oracion5}' -> Palabra más larga: '{resultado5}'")
print(f"Oración 6: '{oracion6}' -> Palabra más larga: '{resultado6}'")
