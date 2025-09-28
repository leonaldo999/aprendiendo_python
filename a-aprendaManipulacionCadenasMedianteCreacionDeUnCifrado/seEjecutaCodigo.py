# Paso 1
# variable_name = value

# ===========================================

# Paso 2
# number = 5
# text = "Hello World"

# ===========================================

# Paso 3
# text = 'Hello World'
# print()

# ===========================================

# Paso 4
# text = 'Hello World'
# print(text)

# ===========================================

# Paso 5
# text = "Hello World"

# print(text[6])

# W

# ===========================================

# Paso 6
# text = "Hello World"

# print(text[-1])

# d

# ===========================================

# Paso 7
# text = "Hello World"

# print(len(text))

# 11

# ===========================================

# Paso 8
# text = "Hello World"

# print(type(text))

# <class 'str'>

# ===========================================

# Paso 9
# text = "Hello World"
# print(type(text))

# shift = 3

# <class 'str'>

# ===========================================

# Paso 10
# text = "Hello World"
# print(type(text))

# shift = 3
# print(shift)

# <class 'str'>
# 3

# ===========================================

# Paso 11
# text = "Hello World"
# print(type(text))

# shift = 3
# print(type(shift))

# <class 'str'>
# <class 'int'>

# ===========================================

# Paso 12
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# ===========================================

# Paso 13
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# alphabet.find("z")

# ===========================================

# Paso 14
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# alphabet.find(text[0])

# ===========================================

# Paso 15
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# index = alphabet.find(text[0])

# ===========================================

# Paso 16
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# index = alphabet.find(text[0])

# print(index)

# -1

# ===========================================

# Paso 17
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# index = alphabet.find(text[0])

# print(index)
# print(text.lower())

# -1
# hello world

# ===========================================

# Paso 18
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# index = alphabet.find(text[0].lower())

# print(index)

# 7

# ===========================================

# Paso 19
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# index = alphabet.find(text[0].lower())
# print(index)

# shifted = alphabet[index]

# ---- Salida ----
# 7

# ===========================================

# Paso 20
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# index = alphabet.find(text[0].lower())
# print(index)

# shifted = alphabet[index]
# print(shifted)

# ---- Salida ----
# 7
# h

# ===========================================

# Paso 21
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# index = alphabet.find(text[0].lower())
# print(index)

# shifted = alphabet[index + shift]
# print(shifted)

# ---- Salida ----
# 7
# k

# ===========================================

# Paso 22
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# ===========================================

# Paso 23
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for i in text:

# ===========================================

# Paso 24
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for i in text:
#     print(i)

# ---- Salida ----

# H
# e
# l
# l
# o

# W
# o
# r
# l
# d

# ===========================================

# Paso 25
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for char in text:
#     print(char)

# ---- Salida ----

# H
# e
# l
# l
# o

# W
# o
# r
# l
# d

# ===========================================

# Paso 26
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for char in text:
#     index = alphabet.find(char)
#     print(char)

# ---- Salida ----
# H
# e
# l
# l
# o

# W
# o
# r
# l
# d

# ===========================================

# Paso 27
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for char in text:
#     index = alphabet.find(char)
#     print(char, index)

# ---- Salida ----
# H -1
# e 4
# l 11
# l 11
# o 14
#   -1
# W -1
# o 14
# r 17
# l 11
# d 3

# ===========================================

# Paso 28
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for char in text.lower():
#     index = alphabet.find(char)
#     print(char, index)

# ---- Salida ----
# h 7
# e 4
# l 11
# l 11
# o 14
#   -1
# w 22
# o 14
# r 17
# l 11
# d 3

# ===========================================

# Paso 29
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for char in text.lower():
#     index = alphabet.find(char)
#     print(char, index)

#     new_index = index + shift

# ===========================================

# Paso 30
# text = "Hello World"
# text = alphabet
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for char in text.lower():
#     index = alphabet.find(char)
#     print(char, index)

#     new_index = index + shift

# ===========================================

# Paso 31
# text = "Hello World"
# text = "Albatross"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for char in text.lower():
#     index = alphabet.find(char)
#     print(char, index)

#     new_index = index + shift

# ===========================================

# Paso 32
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for char in text.lower():
#     index = alphabet.find(char)
#     print(char, index)

#     new_index = index + shift

# ===========================================

# Paso 33
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for char in text.lower():
#     index = alphabet.find(char)
#     print(char, index)

#     new_index = index + shift
#     new_char = alphabet[new_index]

# ---- Salida ----
# h 7
# e 4
# l 11
# l 11
# o 14
#   -1
# w 22
# o 14
# r 17
# l 11
# d 3

# ===========================================

# Paso 34
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for char in text.lower():
#     index = alphabet.find(char)
#     print(char, index)

#     new_index = index + shift
#     new_char = alphabet[new_index]
#     print(new_char)

# ---- Salida ----
# h 7
# k
# e 4
# h
# l 11
# o
# l 11
# o
# o 14
# r
#   -1
# c
# w 22
# z
# o 14
# r
# r 17
# u
# l 11
# o
# d 3
# g

# ===========================================

# Paso 35
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"

# for char in text.lower():
#     index = alphabet.find(char)

#     new_index = index + shift
#     new_char = alphabet[new_index]
#     print("char:", char, "new char:", new_char)

# ---- Salida ----
# char: h new char: k
# char: e new char: h
# char: l new char: o
# char: l new char: o
# char: o new char: r
# char:   new char: c
# char: w new char: z
# char: o new char: r
# char: r new char: u
# char: l new char: o
# char: d new char: g

# ===========================================

# Paso 36
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# encrypted_text = ""

# for char in text.lower():
#     index = alphabet.find(char)

#     new_index = index + shift
#     new_char = alphabet[new_index]
#     print("char:", char, "new char:", new_char)

# ===========================================

# Paso 37
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# encrypted_text = ""

# for char in text.lower():
#     index = alphabet.find(char)

#     new_index = index + shift
#     encrypted_text = alphabet[new_index]
#     print("char:", char, "encrypted text:", encrypted_text)

# ---- Salida ----
# har: h encrypted text: k
# char: e encrypted text: h
# char: l encrypted text: o
# char: l encrypted text: o
# char: o encrypted text: r
# char:   encrypted text: c
# char: w encrypted text: z
# char: o encrypted text: r
# char: r encrypted text: u
# char: l encrypted text: o
# char: d encrypted text: g

# ===========================================

# Paso 38
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# encrypted_text = ""

# for char in text.lower():
#     index = alphabet.find(char)

#     new_index = index + shift
#     encrypted_text = encrypted_text + alphabet[new_index]
#     print("char:", char, "encrypted text:", encrypted_text)

# ---- Salida ----
# char: h encrypted text: k
# char: e encrypted text: kh
# char: l encrypted text: kho
# char: l encrypted text: khoo
# char: o encrypted text: khoor
# char:   encrypted text: khoorc
# char: w encrypted text: khoorcz
# char: o encrypted text: khoorczr
# char: r encrypted text: khoorczru
# char: l encrypted text: khoorczruo
# char: d encrypted text: khoorczruog

# ===========================================

# Paso 39
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# encrypted_text = ""

# for char in text.lower():
#     index = alphabet.find(char)

#     new_index = index + shift
#     encrypted_text += alphabet[new_index]
#     print("char:", char, "encrypted text:", encrypted_text)

# ---- Salida ----
# char: h encrypted text: k
# char: e encrypted text: kh
# char: l encrypted text: kho
# char: l encrypted text: khoo
# char: o encrypted text: khoor
# char:   encrypted text: khoorc
# char: w encrypted text: khoorcz
# char: o encrypted text: khoorczr
# char: r encrypted text: khoorczru
# char: l encrypted text: khoorczruo
# char: d encrypted text: khoorczruog

# ===========================================

# Paso 40
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# encrypted_text = ""

# for char in text.lower():
#     print(char == " ")

#     index = alphabet.find(char)
#     new_index = index + shift
#     encrypted_text += alphabet[new_index]
#     print("char:", char, "encrypted text:", encrypted_text)

# ---- Salida ----
# False
# char: h encrypted text: k
# False
# char: e encrypted text: kh
# False
# char: l encrypted text: kho
# False
# char: l encrypted text: khoo
# False
# char: o encrypted text: khoor
# True
# char:   encrypted text: khoorc
# False
# char: w encrypted text: khoorcz
# False
# char: o encrypted text: khoorczr
# False
# char: r encrypted text: khoorczru
# False
# char: l encrypted text: khoorczruo
# False
# char: d encrypted text: khoorczruog

# ===========================================

# Paso 41
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# encrypted_text = ""

# for char in text.lower():
#     if char == " ":
#         print("space!")

#     index = alphabet.find(char)
#     new_index = index + shift
#     encrypted_text += alphabet[new_index]
#     print("char:", char, "encrypted text:", encrypted_text)

# ---- Salida ----
# char: h encrypted text: k
# char: e encrypted text: kh
# char: l encrypted text: kho
# char: l encrypted text: khoo
# char: o encrypted text: khoor
# space!
# char:   encrypted text: khoorc
# char: w encrypted text: khoorcz
# char: o encrypted text: khoorczr
# char: r encrypted text: khoorczru
# char: l encrypted text: khoorczruo
# char: d encrypted text: khoorczruog

# ===========================================

# Paso 42
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# encrypted_text = ""

# for char in text.lower():
#     if char == " ":
#         encrypted_text += char

#     index = alphabet.find(char)
#     new_index = index + shift
#     encrypted_text += alphabet[new_index]
#     print("char:", char, "encrypted text:", encrypted_text)

# ---- Salida ----
# char: h encrypted text: k
# char: e encrypted text: kh
# char: l encrypted text: kho
# char: l encrypted text: khoo
# char: o encrypted text: khoor
# char:   encrypted text: khoor c
# char: w encrypted text: khoor cz
# char: o encrypted text: khoor czr
# char: r encrypted text: khoor czru
# char: l encrypted text: khoor czruo
# char: d encrypted text: khoor czruog

# ===========================================

# Paso 43
# text = "Hello World"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# encrypted_text = ""

# for char in text.lower():
#     if char == " ":
#         encrypted_text += char
#     else:
#         index = alphabet.find(char)
#         new_index = index + shift
#         encrypted_text += alphabet[new_index]
#     print("char:", char, "encrypted text:", encrypted_text)

# ---- Salida ----
# char: h encrypted text: k
# char: e encrypted text: kh
# char: l encrypted text: kho
# char: l encrypted text: khoo
# char: o encrypted text: khoor
# char:   encrypted text: khoor
# char: w encrypted text: khoor z
# char: o encrypted text: khoor zr
# char: r encrypted text: khoor zru
# char: l encrypted text: khoor zruo
# char: d encrypted text: khoor zruog

# ===========================================

# Paso 44
# text = "Hello Zaira"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# encrypted_text = ""

# for char in text.lower():
#     if char == " ":
#         encrypted_text += char
#     else:
#         index = alphabet.find(char)
#         new_index = index + shift
#         encrypted_text += alphabet[new_index]
#     print("char:", char, "encrypted text:", encrypted_text)

# ---- Salida ----
# char: h encrypted text: k
# char: e encrypted text: kh
# char: l encrypted text: kho
# char: l encrypted text: khoo
# char: o encrypted text: khoorTraceback (most recent call last):
# char:   encrypted text: khoor
#     encrypted_text += alphabet[new_index]
# IndexError: string index out of range

# ===========================================

# Paso 45
# text = "Hello Zaira"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# encrypted_text = ""

# for char in text.lower():
#     if char == " ":
#         encrypted_text += char
#     else:
#         index = alphabet.find(char)
#         new_index = (index + shift) % 26
#         encrypted_text += alphabet[new_index]
#     print("char:", char, "encrypted text:", encrypted_text)

# ---- Salida ----
# char: h encrypted text: k
# char: e encrypted text: kh
# char: l encrypted text: kho
# char: l encrypted text: khoo
# char: o encrypted text: khoor
# char:   encrypted text: khoor
# char: z encrypted text: khoor c
# char: a encrypted text: khoor cd
# char: i encrypted text: khoor cdl
# char: r encrypted text: khoor cdlu
# char: a encrypted text: khoor cdlud

# ===========================================

# Paso 46
# text = "Hello Zaira"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# encrypted_text = ""

# for char in text.lower():
#     if char == " ":
#         encrypted_text += char
#     else:
#         index = alphabet.find(char)
#         new_index = (index + shift) % len(alphabet)
#         encrypted_text += alphabet[new_index]
#     print("char:", char, "encrypted text:", encrypted_text)

# ---- Salida ----
# char: h encrypted text: k
# char: e encrypted text: kh
# char: l encrypted text: kho
# char: l encrypted text: khoo
# char: o encrypted text: khoor
# char:   encrypted text: khoor
# char: z encrypted text: khoor c
# char: a encrypted text: khoor cd
# char: i encrypted text: khoor cdl
# char: r encrypted text: khoor cdlu
# char: a encrypted text: khoor cdlud

# ===========================================

# Paso 47
# text = "Hello Zaira"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# encrypted_text = ""

# for char in text.lower():
#     if char == " ":
#         encrypted_text += char
#     else:
#         index = alphabet.find(char)
#         new_index = (index + shift) % len(alphabet)
#         encrypted_text += alphabet[new_index]
# print("encrypted text:", encrypted_text)

# ===========================================

# Paso 48
# text = "Hello Zaira"
# shift = 3
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# encrypted_text = ""

# for char in text.lower():
#     if char == " ":
#         encrypted_text += char
#     else:
#         index = alphabet.find(char)
#         new_index = (index + shift) % len(alphabet)
#         encrypted_text += alphabet[new_index]

# print("plain text:", text)
# print("encrypted text:", encrypted_text)
# ---- Salida ----
# plain text: Hello Zaira
# encrypted text: khoor cdlud

# ===========================================

# Paso 49
# text = "Hello Zaira"
# shift = 3


# def caesar():
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in text.lower():
#         if char == " ":
#             encrypted_text += char
#         else:
#             index = alphabet.find(char)
#             new_index = (index + shift) % len(alphabet)
#             encrypted_text += alphabet[new_index]

#     print("plain text:", text)
#     print("encrypted text:", encrypted_text)


# ===========================================

# Paso 50
# text = "Hello Zaira"
# shift = 3


# def caesar():
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in text.lower():
#         if char == " ":
#             encrypted_text += char
#         else:
#             index = alphabet.find(char)
#             new_index = (index + shift) % len(alphabet)
#             encrypted_text += alphabet[new_index]

#     print("plain text:", text)
#     print("encrypted text:", encrypted_text)
# print(alphabet)

# ---- Salida ----
# NameError: name 'alphabet' is not defined

# ===========================================

# Paso 51
# text = "Hello Zaira"
# shift = 3


# def caesar():
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in text.lower():
#         if char == " ":
#             encrypted_text += char
#         else:
#             index = alphabet.find(char)
#             new_index = (index + shift) % len(alphabet)
#             encrypted_text += alphabet[new_index]

#     print("plain text:", text)
#     print("encrypted text:", encrypted_text)


# ===========================================

# Paso 52
# text = "Hello Zaira"
# shift = 3


# def caesar():
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in text.lower():
#         if char == " ":
#             encrypted_text += char
#         else:
#             index = alphabet.find(char)
#             new_index = (index + shift) % len(alphabet)
#             encrypted_text += alphabet[new_index]

#     print("plain text:", text)
#     print("encrypted text:", encrypted_text)


# caesar()
# ---- Salida ----
# plain text: Hello Zaira
# encrypted text: khoor cdlud

# ===========================================

# Paso 53
# text = "Hello Zaira"
# shift = 3


# def caesar(message, offset):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in text.lower():
#         if char == " ":
#             encrypted_text += char
#         else:
#             index = alphabet.find(char)
#             new_index = (index + shift) % len(alphabet)
#             encrypted_text += alphabet[new_index]

#     print("plain text:", text)
#     print("encrypted text:", encrypted_text)


# caesar()
# ---- Salida ----
# TypeError: caesar() missing 2 required positional arguments: 'message' and 'offset'

# ===========================================

# Paso 54
# text = "Hello Zaira"
# shift = 3


# def caesar(message, offset):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         if char == " ":
#             encrypted_text += char
#         else:
#             index = alphabet.find(char)
#             new_index = (index + offset) % len(alphabet)
#             encrypted_text += alphabet[new_index]

#     print("plain text:", message)
#     print("encrypted text:", encrypted_text)


# caesar()

# ---- Salida ----
# TypeError: caesar() missing 2 required positional arguments: 'message' and 'offset'

# ===========================================

# Paso 55
# text = "Hello Zaira"
# shift = 3


# def caesar(message, offset):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         if char == " ":
#             encrypted_text += char
#         else:
#             index = alphabet.find(char)
#             new_index = (index + offset) % len(alphabet)
#             encrypted_text += alphabet[new_index]
#     print("plain text:", message)
#     print("encrypted text:", encrypted_text)


# caesar(text, shift)

# ---- Salida ----
# plain text: Hello Zaira
# encrypted text: khoor cdlud

# ===========================================

# Paso 56
# text = "Hello Zaira"
# shift = 3


# def caesar(message, offset):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         if char == " ":
#             encrypted_text += char
#         else:
#             index = alphabet.find(char)
#             new_index = (index + offset) % len(alphabet)
#             encrypted_text += alphabet[new_index]
#     print("plain text:", message)
#     print("encrypted text:", encrypted_text)


# caesar(text, shift)
# caesar(text, 13)

# ---- Salida ----
# plain text: Hello Zaira
# encrypted text: khoor cdlud
# plain text: Hello Zaira
# encrypted text: uryyb mnven

# ===========================================

# Paso 57
# text = "Hello Zaira"
# shift = 3


# def caesar(message, offset):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         if char == " ":
#             encrypted_text += char
#         else:
#             index = alphabet.find(char)
#             new_index = (index + offset) % len(alphabet)
#             encrypted_text += alphabet[new_index]
#     print("plain text:", message)
#     print("encrypted text:", encrypted_text)

# ===========================================

# Paso 58
# text = "Hello Zaira"
# shift = 3


# def vigenere(message, key):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         if char == " ":
#             encrypted_text += char
#         else:
#             index = alphabet.find(char)
#             new_index = (index + offset) % len(alphabet)
#             encrypted_text += alphabet[new_index]
#     print("plain text:", message)
#     print("encrypted text:", encrypted_text)


# ===========================================

# Paso 59
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         if char == " ":
#             encrypted_text += char
#         else:
#             index = alphabet.find(char)
#             new_index = (index + offset) % len(alphabet)
#             encrypted_text += alphabet[new_index]
#     print("plain text:", message)
#     print("encrypted text:", encrypted_text)


# ===========================================

# Paso 60
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         if char == " ":
#             encrypted_text += char
#         else:
#             index = alphabet.find(char)
#             new_index = (index + offset) % len(alphabet)
#             encrypted_text += alphabet[new_index]
#     print("plain text:", message)
#     print("encrypted text:", encrypted_text)


# ---- Salida ----
# plain text: Hello Zaira
# encrypted text: khoor cdlud
# plain text: Hello Zaira
# encrypted text: uryyb mnven

# ===========================================

# Paso 61
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         # Append space to the message
#         if char == " ":
#             encrypted_text += char
#         else:
#             index = alphabet.find(char)
#             new_index = (index + offset) % len(alphabet)
#             encrypted_text += alphabet[new_index]
#     print("plain text:", message)
#     print("encrypted text:", encrypted_text)


# ===========================================

# Paso 62
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         # Append space to the message
#         if char == " ":
#             encrypted_text += char
#         else:
#             key_char = key[key_index % len(key)]
#             index = alphabet.find(char)
#             new_index = (index + offset) % len(alphabet)
#             encrypted_text += alphabet[new_index]
#     print("plain text:", message)
#     print("encrypted text:", encrypted_text)


# ===========================================

# Paso 63
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         # Append space to the message
#         if char == " ":
#             encrypted_text += char
#         else:
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             index = alphabet.find(char)
#             new_index = (index + offset) % len(alphabet)
#             encrypted_text += alphabet[new_index]

#     print("plain text:", message)
#     print("encrypted text:", encrypted_text)


# ===========================================

# Paso 64
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         # Append space to the message
#         if char == " ":
#             encrypted_text += char
#         else:
#             # Find the right key character to encode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             index = alphabet.find(char)
#             new_index = (index + offset) % len(alphabet)
#             encrypted_text += alphabet[new_index]

#     print("plain text:", message)
#     print("encrypted text:", encrypted_text)

# ===========================================

# Paso 65
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         # Append space to the message
#         if char == " ":
#             encrypted_text += char
#         else:
#             # Find the right key character to encode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset) % len(alphabet)
#             encrypted_text += alphabet[new_index]

#     print("plain text:", message)
#     print("encrypted text:", encrypted_text)

# ===========================================

# Paso 66
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         # Append space to the message
#         if char == " ":
#             encrypted_text += char
#         else:
#             # Find the right key character to encode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset) % len(alphabet)
#             encrypted_text += alphabet[new_index]

#     print("plain text:", message)
#     print("encrypted text:", encrypted_text)

# ===========================================

# Paso 67
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         # Append space to the message
#         if char == " ":
#             encrypted_text += char
#         else:
#             # Find the right key character to encode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset) % len(alphabet)
#             encrypted_text += alphabet[new_index]

#     return encrypted_text

# ===========================================

# Paso 68
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         # Append space to the message
#         if char == " ":
#             encrypted_text += char
#         else:
#             # Find the right key character to encode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset) % len(alphabet)
#             encrypted_text += alphabet[new_index]

#     return encrypted_text

# encryption = vigenere(text, custom_key)

# ===========================================

# Paso 69
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         # Append space to the message
#         if char == " ":
#             encrypted_text += char
#         else:
#             # Find the right key character to encode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset) % len(alphabet)
#             encrypted_text += alphabet[new_index]

#     return encrypted_text


# encryption = vigenere(text, custom_key)
# print(encryption)

# ===========================================

# Paso 70
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key, direction):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         # Append space to the message
#         if char == " ":
#             encrypted_text += char
#         else:
#             # Find the right key character to encode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset) % len(alphabet)
#             encrypted_text += alphabet[new_index]

#     return encrypted_text


# # encryption = vigenere(text, custom_key)
# # print(encryption)

# ===========================================

# Paso 71
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key, direction):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         # Append space to the message
#         if char == " ":
#             encrypted_text += char
#         else:
#             # Find the right key character to encode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             encrypted_text += alphabet[new_index]

#     return encrypted_text


# # encryption = vigenere(text, custom_key)
# # print(encryption)

# ===========================================

# Paso 72
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key, direction):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         # Append space to the message
#         if char == " ":
#             encrypted_text += char
#         else:
#             # Find the right key character to encode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             encrypted_text += alphabet[new_index]

#     return encrypted_text


# encryption = vigenere(text, custom_key, 1)
# print(encryption)

# ===========================================

# Paso 73
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key, direction):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         # Append space to the message
#         if char == " ":
#             encrypted_text += char
#         else:
#             # Find the right key character to encode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             encrypted_text += alphabet[new_index]

#     return encrypted_text


# encryption = vigenere(text, custom_key, 1)
# print(encryption)
# decryption = vigenere(encryption, custom_key, -1)

# ===========================================

# Paso 74
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key, direction):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     encrypted_text = ""

#     for char in message.lower():
#         # Append space to the message
#         if char == " ":
#             encrypted_text += char
#         else:
#             # Find the right key character to encode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             encrypted_text += alphabet[new_index]

#     return encrypted_text


# encryption = vigenere(text, custom_key, 1)
# print(encryption)
# decryption = vigenere(encryption, custom_key, -1)
# print(decryption)

# ---- Salida ----
# plain text: Hello Zaira
# encrypted text: khoor cdlud
# plain text: Hello Zaira
# encrypted text: uryyb mnven
# wcesc mpgkh
# hello zaira

# ===========================================

# Paso 75
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key, direction):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append space to the message
#         if char == " ":
#             final_message += char
#         else:
#             # Find the right key character to encode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message


# encryption = vigenere(text, custom_key, 1)
# print(encryption)
# decryption = vigenere(encryption, custom_key, -1)
# print(decryption)

# ===========================================

# Paso 76
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key, direction):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append space to the message
#         if char == " ":
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message


# encryption = vigenere(text, custom_key, 1)
# print(encryption)
# decryption = vigenere(encryption, custom_key, -1)
# print(decryption)

# ===========================================

# Paso 77
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key, direction= 1):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append space to the message
#         if char == " ":
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message


# encryption = vigenere(text, custom_key, 1)
# print(encryption)
# decryption = vigenere(encryption, custom_key, -1)
# print(decryption)

# ===========================================

# Paso 78
# text = "Hello Zaira"
# custom_key = "python"


# def vigenere(message, key, direction= 1):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append space to the message
#         if char == " ":
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message


# encryption = vigenere(text, custom_key)
# print(encryption)
# decryption = vigenere(encryption, custom_key, -1)
# print(decryption)

# ===========================================

# Paso 79
# text = "Hello Zaira!"
# custom_key = "python"


# def vigenere(message, key, direction=1):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append space to the message
#         if char == " ":
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message


# encryption = vigenere(text, custom_key)
# print(encryption)
# decryption = vigenere(encryption, custom_key, -1)
# print(decryption)

# ===========================================

# Paso 80
# text = "Hello Zaira!"
# custom_key = "python"


# def vigenere(message, key, direction=1):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append space to the message
#         if char.isalpha():
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message


# encryption = vigenere(text, custom_key)
# print(encryption)
# decryption = vigenere(encryption, custom_key, -1)
# print(decryption)

# ---- Salida ----
# plain text: Hello Zaira
# encrypted text: khoor cdlud
# plain text: Hello Zaira
# encrypted text: uryyb mnven
# helloozairax
# helloozairax

# ===========================================

# Paso 81
# text = "Hello Zaira!"
# custom_key = "python"


# def vigenere(message, key, direction=1):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append space to the message
#         if not char.isalpha():
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message


# encryption = vigenere(text, custom_key)
# print(encryption)
# decryption = vigenere(encryption, custom_key, -1)
# print(decryption)

# ===========================================

# Paso 82
# text = "Hello Zaira!"
# custom_key = "python"


# def vigenere(message, key, direction=1):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append any non-letter character to the message
#         if not char.isalpha():
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message


# encryption = vigenere(text, custom_key)
# print(encryption)
# decryption = vigenere(encryption, custom_key, -1)
# print(decryption)

# ===========================================

# Paso 83
# text = "Hello Zaira!"
# custom_key = "python"


# def vigenere(message, key, direction=1):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append any non-letter character to the message
#         if not char.isalpha():
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message

# def encrypt(message, key):
#     pass
# encryption = vigenere(text, custom_key)
# print(encryption)
# decryption = vigenere(encryption, custom_key, -1)
# print(decryption)

# ===========================================

# Paso 84
# text = "Hello Zaira!"
# custom_key = "python"


# def vigenere(message, key, direction=1):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append any non-letter character to the message
#         if not char.isalpha():
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message

# def encrypt(message, key):
#     return vigenere(message, key)

# encryption = vigenere(text, custom_key)
# print(encryption)
# decryption = vigenere(encryption, custom_key, -1)
# print(decryption)

# ===========================================

# Paso 85
# text = "Hello Zaira!"
# custom_key = "python"


# def vigenere(message, key, direction=1):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append any non-letter character to the message
#         if not char.isalpha():
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message


# def encrypt(message, key):
#     return vigenere(message, key)


# def decrypt(message, key):
#     return vigenere(message, key, -1)


# encryption = vigenere(text, custom_key)
# print(encryption)
# decryption = vigenere(encryption, custom_key, -1)
# print(decryption)

# ===========================================

# Paso 86
# text = "Hello Zaira!"
# custom_key = "python"


# def vigenere(message, key, direction=1):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append any non-letter character to the message
#         if not char.isalpha():
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message


# def encrypt(message, key):
#     return vigenere(message, key)


# def decrypt(message, key):
#     return vigenere(message, key, -1)


# encryption = encrypt(text, custom_key)
# print(encryption)
# decryption = decrypt(encryption, custom_key)
# print(decryption)

# ===========================================

# Paso 87
# text = "mrttaqrhknsw ih puggrur"
# custom_key = "python"


# def vigenere(message, key, direction=1):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append any non-letter character to the message
#         if not char.isalpha():
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message


# def encrypt(message, key):
#     return vigenere(message, key)


# def decrypt(message, key):
#     return vigenere(message, key, -1)


# encryption = encrypt(text, custom_key)
# print(encryption)
# decryption = decrypt(encryption, custom_key)
# print(decryption)

# ---- Salida ----
# plain text: Hello Zaira
# encrypted text: khoor cdlud
# plain text: Hello Zaira
# encrypted text: uryyb mnven
# bpmaodgfdugj xf ibutgsk
# mrttaqrhknsw ih puggrur

# ===========================================

# Paso 88
# text = "mrttaqrhknsw ih puggrur"
# custom_key = "python"


# def vigenere(message, key, direction=1):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append any non-letter character to the message
#         if not char.isalpha():
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message


# def encrypt(message, key):
#     return vigenere(message, key)


# def decrypt(message, key):
#     return vigenere(message, key, -1)


# # decryption = decrypt(encryption, custom_key)
# # print(decryption)

# ===========================================

# Paso 89
# text = "mrttaqrhknsw ih puggrur"
# custom_key = "python"


# def vigenere(message, key, direction=1):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append any non-letter character to the message
#         if not char.isalpha():
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message


# def encrypt(message, key):
#     return vigenere(message, key)


# def decrypt(message, key):
#     return vigenere(message, key, -1)


# print("Encrypted text: " + text)
# # decryption = decrypt(encryption, custom_key)
# # print(decryption)

# ===========================================

# Paso 90
# text = "mrttaqrhknsw ih puggrur"
# custom_key = "python"


# def vigenere(message, key, direction=1):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append any non-letter character to the message
#         if not char.isalpha():
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message


# def encrypt(message, key):
#     return vigenere(message, key)


# def decrypt(message, key):
#     return vigenere(message, key, -1)


# print("Encrypted text: " + text)
# print("Key: " + custom_key)
# decryption = decrypt(encryption, custom_key)
# print(decryption)

# ===========================================

# Paso 91
# text = "mrttaqrhknsw ih puggrur"
# custom_key = "python"


# def vigenere(message, key, direction=1):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append any non-letter character to the message
#         if not char.isalpha():
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message


# def encrypt(message, key):
#     return vigenere(message, key)


# def decrypt(message, key):
#     return vigenere(message, key, -1)


# print(f"Encrypted text: {text}")
# print("Key: " + custom_key)
# # decryption = decrypt(encryption, custom_key)
# # print(decryption)

# ===========================================

# Paso 92
# text = "mrttaqrhknsw ih puggrur"
# custom_key = "python"


# def vigenere(message, key, direction=1):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append any non-letter character to the message
#         if not char.isalpha():
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message


# def encrypt(message, key):
#     return vigenere(message, key)


# def decrypt(message, key):
#     return vigenere(message, key, -1)


# print(f"\nEncrypted text: {text}")
# print(f"Key: {custom_key}")
# # decryption = decrypt(encryption, custom_key)
# # print(decryption)

# ---- Salida ----
#  Encrypted text: mrttaqrhknsw ih puggrur
# Key: python

# ===========================================

# Paso 93
# text = "mrttaqrhknsw ih puggrur"
# custom_key = "python"


# def vigenere(message, key, direction=1):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append any non-letter character to the message
#         if not char.isalpha():
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message


# def encrypt(message, key):
#     return vigenere(message, key)


# def decrypt(message, key):
#     return vigenere(message, key, -1)


# print(f"\nEncrypted text: {text}")
# print(f"Key: {custom_key}")
# # decryption = decrypt(encryption, custom_key)
# # print(decryption)

# ---- Salida ----

# Encrypted text: mrttaqrhknsw ih puggrur
# Key: python

# ===========================================

# Paso 94
# text = "mrttaqrhknsw ih puggrur"
# custom_key = "python"


# def vigenere(message, key, direction=1):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append any non-letter character to the message
#         if not char.isalpha():
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message


# def encrypt(message, key):
#     return vigenere(message, key)


# def decrypt(message, key):
#     return vigenere(message, key, -1)


# print(f"\nEncrypted text: {text}")
# print(f"Key: {custom_key}")
# decryption = decrypt(text, custom_key)
# # print(decryption)

# ===========================================

# Paso 95
# text = "mrttaqrhknsw ih puggrur"
# custom_key = "python"


# def vigenere(message, key, direction=1):
#     key_index = 0
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     final_message = ""

#     for char in message.lower():
#         # Append any non-letter character to the message
#         if not char.isalpha():
#             final_message += char
#         else:
#             # Find the right key character to encode/decode
#             key_char = key[key_index % len(key)]
#             key_index += 1
#             # Define the offset and the encrypted/decrypted letter
#             offset = alphabet.index(key_char)
#             index = alphabet.find(char)
#             new_index = (index + offset * direction) % len(alphabet)
#             final_message += alphabet[new_index]

#     return final_message


# def encrypt(message, key):
#     return vigenere(message, key)


# def decrypt(message, key):
#     return vigenere(message, key, -1)


# print(f"\nEncrypted text: {text}")
# print(f"Key: {custom_key}")
# decryption = decrypt(text, custom_key)
# print(f"\nDecrypted text: {decryption}\n")

# ==========================================

# Paso 96
text = "mrttaqrhknsw ih puggrur"
custom_key = "happycoding"


def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    final_message = ""

    for char in message.lower():
        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1
            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message


def encrypt(message, key):
    return vigenere(message, key)


def decrypt(message, key):
    return vigenere(message, key, -1)


print(f"\nEncrypted text: {text}")
print(f"Key: {custom_key}")
decryption = decrypt(text, custom_key)
print(f"\nDecrypted text: {decryption}\n")

# ---- Salida ----
# Encrypted text: mrttaqrhknsw ih puggrur
# Key: happycoding

# Decrypted text: freecodecamp is awesome
