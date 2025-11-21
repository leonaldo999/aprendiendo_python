"""
Aprenda sobre clases y objetos creando un solucionador de sudokus
"""

# ===========================================

# Paso 1

# class Board:
#     pass

# ===========================================

# Paso 2

# class Board:
#     pass

# gameboard = Board()

# ===========================================

# Paso 3

# class Board:

#     def spam():
#         pass


# gameboard = Board()

# ===========================================

# Paso 4

# class Board:

#     def spam(self):
#         pass


# gameboard = Board()

# ===========================================

# Paso 5

# class Board:

#     def spam(self):
#         print("Spam!")

# gameboard = Board()

# ===========================================

# Paso 6

# class Board:

#     def spam(self):
#         print("Spam!")

# gameboard = Board()
# gameboard.spam()

# ===========================================

# Paso 7

# class Board:

#     def spam(self):
#         print("Spam!")

# gameboard = Board()

# ===========================================

# Paso 8

# class Board:

#     def __init__(self):
#         pass

# gameboard = Board()

# ===========================================

# Paso 9

# class Board:

#     def __init__(self):
#         pass

# puzzle = [
#       [0, 0, 2, 0, 0, 8, 0, 0, 0],
#       [0, 0, 0, 0, 0, 3, 7, 6, 2],
#       [4, 3, 0, 0, 0, 0, 8, 0, 0],
#       [0, 5, 0, 0, 3, 0, 0, 9, 0],
#       [0, 4, 0, 0, 0, 0, 0, 2, 6],
#       [0, 0, 0, 4, 6, 7, 0, 0, 0],
#       [0, 8, 6, 7, 0, 4, 0, 0, 0],
#       [0, 0, 0, 5, 1, 9, 0, 0, 8],
#       [1, 7, 0, 0, 0, 6, 0, 0, 5]
#     ]

# gameboard = Board()

# ===========================================

# Paso 10

# class Board:

#     def __init__(self, board):
#         pass

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]
# gameboard = Board(puzzle)

# ===========================================

# Paso 11

# class Board:

#     def __init__(self, board):
#         self.board = board

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]
# gameboard = Board(puzzle)

# ===========================================

# Paso 12

# class Board:

#     def __init__(self, board):
#         self.board = board

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]
# gameboard = Board(puzzle)
# print(gameboard.board)

# -------Salida-------
# [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# ===========================================

# Paso 13


# class Board:

#     def __init__(self, board):
#         self.board = board


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]
# gameboard = Board(puzzle)

# -------Salida-------


# ===========================================

# Paso 14

# class Board:

#     def __init__(self, board):
#         self.board = board
#     def find_empty_cell(self):
#         pass

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# -------Salida-------


# ===========================================

# Paso 15

# class Board:

#     def __init__(self, board):
#         self.board = board

#     # ---Región editable por el usuario---
#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             pass
#     # ---Región editable por el usuario---

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# -------Salida-------


# ===========================================

# Paso 16


# class Board:

#     def __init__(self, board):
#         self.board = board

#     # ---Región editable por el usuario---
#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             col = contents.index(0)
#     # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# -------Salida-------


# ===========================================

# Paso 17


# class Board:

#     def __init__(self, board):
#         self.board = board

#     # ---Región editable por el usuario---
#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#             except:
#                 pass
#     # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# -------Salida-------


# ===========================================

# Paso 18


# class Board:

#     def __init__(self, board):
#         self.board = board

#     # ---Región editable por el usuario---
#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except:
#                 pass
#     # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# -------Salida-------


# ===========================================

# Paso 19


# class Board:

#     def __init__(self, board):
#         self.board = board

#     # ---Región editable por el usuario---
#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#     # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# -------Salida-------


# ===========================================

# Paso 20


# class Board:

#     def __init__(self, board):
#         self.board = board

#     # ---Región editable por el usuario---
#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None
#     # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# -------Salida-------


# ===========================================

# Paso 21


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# # ---Región editable por el usuario---
# print(gameboard.find_empty_cell())
# # ---Región editable por el usuario---

# -------Salida-------
# (0, 0)

# ===========================================

# Paso 22


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None


# # ---Región editable por el usuario---
# puzzle = [
#     [1, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]
# # ---Región editable por el usuario---

# gameboard = Board(puzzle)
# print(gameboard.find_empty_cell())

# -------Salida-------
# (0, 1)

# ===========================================

# Paso 23


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None


# # ---Región editable por el usuario---
# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)
# # ---Región editable por el usuario---

# -------Salida-------

# ===========================================

# Paso 24


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     # ---Región editable por el usuario---
#     def valid_in_row(self, row, num):
#         pass
# # ---Región editable por el usuario---

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# -------Salida-------

# ===========================================

# Paso 25


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     # ---Región editable por el usuario---
#     def valid_in_row(self, row, num):
#         num not in self.board[row]
# # ---Región editable por el usuario---

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# -------Salida-------

# ===========================================

# Paso 26


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     # ---Región editable por el usuario---
#     def valid_in_row(self, row, num):
#         return num not in self.board[row]
# # ---Región editable por el usuario---

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# -------Salida-------

# ===========================================

# Paso 27


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# # ---Región editable por el usuario---
# print(gameboard.valid_in_row(0, 8))
# # ---Región editable por el usuario---

# -------Salida-------
# False

# ===========================================

# Paso 28


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# # ---Región editable por el usuario---
# print(gameboard.valid_in_row(0, 7))
# # ---Región editable por el usuario---

# -------Salida-------
# True

# ===========================================

# Paso 29


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# # ---Región editable por el usuario---
# # ---Región editable por el usuario---

# -------Salida-------

# ===========================================

# Paso 30


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     # ---Región editable por el usuario---
#     def valid_in_col(self, col, num):
#         pass
#     # ---Región editable por el usuario---

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 31


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     # ---Región editable por el usuario---
#     def valid_in_col(self, col, num):
#         (self.board[row][col] != num for row in range(9))
#     # ---Región editable por el usuario---

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 32


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     # ---Región editable por el usuario---
#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))
#     # ---Región editable por el usuario---

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 33


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# # ---Región editable por el usuario---
# print(gameboard.valid_in_col(0, 7))
# # ---Región editable por el usuario---

# -------Salida-------
# True

# ===========================================

# Paso 34


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# # ---Región editable por el usuario---
# print(gameboard.valid_in_col(0, 1))
# # ---Región editable por el usuario---

# -------Salida-------
# False

# ===========================================

# Paso 35


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# # ---Región editable por el usuario---
# # ---Región editable por el usuario---

# -------Salida-------

# ===========================================

# Paso 36


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))


# # ---Región editable por el usuario---
#     def valid_in_square(self, row, col, num):
#         pass
# # ---Región editable por el usuario---

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# -------Salida-------

# ===========================================

# Paso 37


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     # ---Región editable por el usuario---
#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
# # ---Región editable por el usuario---

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# -------Salida-------

# ===========================================

# Paso 38


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     # ---Región editable por el usuario---
#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
# # ---Región editable por el usuario---

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# -------Salida-------

# ===========================================

# Paso 39


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     # ---Región editable por el usuario---
#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             pass
# # ---Región editable por el usuario---

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# -------Salida-------

# ===========================================

# Paso 40


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     # ---Región editable por el usuario---
#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 pass
# # ---Región editable por el usuario---

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# -------Salida-------

# ===========================================

# Paso 41


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     # ---Región editable por el usuario---
#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
# # ---Región editable por el usuario---

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# -------Salida-------

# ===========================================

# Paso 42


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     # ---Región editable por el usuario---
#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True
# # ---Región editable por el usuario---

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# -------Salida-------

# ===========================================

# Paso 43


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# # ---Región editable por el usuario---
# print(gameboard.valid_in_square(1, 0, 3))
# # ---Región editable por el usuario---

# -------Salida-------
# False

# ===========================================

# Paso 44


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# # ---Región editable por el usuario---
# print(gameboard.valid_in_square(1, 6, 3))
# # ---Región editable por el usuario---

# -------Salida-------
# True

# ===========================================

# Paso 45


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)

# # ---Región editable por el usuario---
# # ---Región editable por el usuario---

# -------Salida-------

# ===========================================

# Paso 46


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

# # ---Región editable por el usuario---
#     def is_valid(self, empty, num):
#         pass
# # ---Región editable por el usuario---

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 47


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     # ---Región editable por el usuario---
#     def is_valid(self, empty, num):
#         row, col = empty


# # ---Región editable por el usuario---

# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 48


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     # ---Región editable por el usuario---
#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#     # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 49


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     # ---Región editable por el usuario---
#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#     # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 50


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     # ---Región editable por el usuario---
#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#     # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 51


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     # ---Región editable por el usuario---
#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )
#     # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 52


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     # ---Región editable por el usuario---
#     def solver(self):
#         pass
#     # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 53


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     # ---Región editable por el usuario---
#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#     # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 54


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     # ---Región editable por el usuario---
#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#     # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 55


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     # ---Región editable por el usuario---
#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             pass
#     # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 56


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     # ---Región editable por el usuario---
#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 pass
#     # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 57


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     # ---Región editable por el usuario---
#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#     # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 58


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     # ---Región editable por el usuario---
#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#     # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 59


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     # ---Región editable por el usuario---
#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#                 if self.solver():
#                     return True
#     # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 60


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     # ---Región editable por el usuario---
#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#                 if self.solver():
#                     return True
#                 self.board[row][col] = 0
#     # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 61


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     # ---Región editable por el usuario---
#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#                 if self.solver():
#                     return True
#                 self.board[row][col] = 0
#         return False
#     # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 62


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#                 if self.solver():
#                     return True
#                 self.board[row][col] = 0
#         return False

# # ---Región editable por el usuario---
# def solve_sudoku(board):
#     pass
# # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 63


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#                 if self.solver():
#                     return True
#                 self.board[row][col] = 0
#         return False

# # ---Región editable por el usuario---
# def solve_sudoku(board):
#     gameboard = Board(board)
# # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 64


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#                 if self.solver():
#                     return True
#                 self.board[row][col] = 0
#         return False

# # ---Región editable por el usuario---
# def solve_sudoku(board):
#     gameboard = Board(board)
#     print(f"Puzzle to solve:\n{gameboard}")
# # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 65


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#                 if self.solver():
#                     return True
#                 self.board[row][col] = 0
#         return False

# # ---Región editable por el usuario---
# def solve_sudoku(board):
#     gameboard = Board(board)
#     print(f"Puzzle to solve:\n{gameboard}")
#     if gameboard.solver():
#         print(f"Solved puzzle:\n{gameboard}")
# # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 66


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#                 if self.solver():
#                     return True
#                 self.board[row][col] = 0
#         return False

# # ---Región editable por el usuario---
# def solve_sudoku(board):
#     gameboard = Board(board)
#     print(f"Puzzle to solve:\n{gameboard}")
#     if gameboard.solver():
#         print(f"Solved puzzle:\n{gameboard}")
#     else:
#         print("The provided puzzle is unsolvable.")
# # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 67


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#                 if self.solver():
#                     return True
#                 self.board[row][col] = 0
#         return False

# # ---Región editable por el usuario---
# def solve_sudoku(board):
#     gameboard = Board(board)
#     print(f"Puzzle to solve:\n{gameboard}")
#     if gameboard.solver():
#         print(f"Solved puzzle:\n{gameboard}")
#     else:
#         print("The provided puzzle is unsolvable.")
#     return gameboard
# # ---Región editable por el usuario---


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# gameboard = Board(puzzle)


# -------Salida-------

# ===========================================

# Paso 68


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#                 if self.solver():
#                     return True
#                 self.board[row][col] = 0
#         return False

# def solve_sudoku(board):
#     gameboard = Board(board)
#     print(f"Puzzle to solve:\n{gameboard}")
#     if gameboard.solver():
#         print(f"Solved puzzle:\n{gameboard}")
#     else:
#         print("The provided puzzle is unsolvable.")
#     return gameboard


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# # ---Región editable por el usuario---
# gameboard = Board(puzzle)
# print(gameboard)
# # ---Región editable por el usuario---


# -------Salida-------
# <__main__.Board object at 0x000001FDD8F0FFD0>

# ===========================================

# Paso 69


# class Board:

#     def __init__(self, board):
#         self.board = board

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#                 if self.solver():
#                     return True
#                 self.board[row][col] = 0
#         return False

# def solve_sudoku(board):
#     gameboard = Board(board)
#     print(f"Puzzle to solve:\n{gameboard}")
#     if gameboard.solver():
#         print(f"Solved puzzle:\n{gameboard}")
#     else:
#         print("The provided puzzle is unsolvable.")
#     return gameboard


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]

# ---Región editable por el usuario---

# ---Región editable por el usuario---


# -------Salida-------

# ===========================================

# Paso 70


# class Board:

#     def __init__(self, board):
#         self.board = board

#     # ---Región editable por el usuario---
#     def __str__(self):
#         pass
#     # ---Región editable por el usuario---

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#                 if self.solver():
#                     return True
#                 self.board[row][col] = 0
#         return False


# def solve_sudoku(board):
#     gameboard = Board(board)
#     print(f"Puzzle to solve:\n{gameboard}")
#     if gameboard.solver():
#         print(f"Solved puzzle:\n{gameboard}")
#     else:
#         print("The provided puzzle is unsolvable.")
#     return gameboard


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]


# -------Salida-------

# ===========================================

# Paso 71


# class Board:

#     def __init__(self, board):
#         self.board = board

#     # ---Región editable por el usuario---
#     def __str__(self):
#         board_str = ''
#     # ---Región editable por el usuario---

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#                 if self.solver():
#                     return True
#                 self.board[row][col] = 0
#         return False


# def solve_sudoku(board):
#     gameboard = Board(board)
#     print(f"Puzzle to solve:\n{gameboard}")
#     if gameboard.solver():
#         print(f"Solved puzzle:\n{gameboard}")
#     else:
#         print("The provided puzzle is unsolvable.")
#     return gameboard


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]


# -------Salida-------

# ===========================================

# Paso 72


# class Board:

#     def __init__(self, board):
#         self.board = board

#     # ---Región editable por el usuario---
#     def __str__(self):
#         board_str = ''
#         for row in self.board:
#             pass
#     # ---Región editable por el usuario---

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#                 if self.solver():
#                     return True
#                 self.board[row][col] = 0
#         return False


# def solve_sudoku(board):
#     gameboard = Board(board)
#     print(f"Puzzle to solve:\n{gameboard}")
#     if gameboard.solver():
#         print(f"Solved puzzle:\n{gameboard}")
#     else:
#         print("The provided puzzle is unsolvable.")
#     return gameboard


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]


# -------Salida-------

# ===========================================

# Paso 73


# class Board:

#     def __init__(self, board):
#         self.board = board

#     # ---Región editable por el usuario---
#     def __str__(self):
#         board_str = ''
#         for row in self.board:
#             row_str = [str(i) for i in row]
#     # ---Región editable por el usuario---

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#                 if self.solver():
#                     return True
#                 self.board[row][col] = 0
#         return False


# def solve_sudoku(board):
#     gameboard = Board(board)
#     print(f"Puzzle to solve:\n{gameboard}")
#     if gameboard.solver():
#         print(f"Solved puzzle:\n{gameboard}")
#     else:
#         print("The provided puzzle is unsolvable.")
#     return gameboard


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]


# -------Salida-------

# ===========================================

# Paso 74


# class Board:

#     def __init__(self, board):
#         self.board = board

#     # ---Región editable por el usuario---
#     def __str__(self):
#         board_str = ''
#         for row in self.board:
#             row_str = [str(i) if i != 0 else "*" for i in row]
#     # ---Región editable por el usuario---

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#                 if self.solver():
#                     return True
#                 self.board[row][col] = 0
#         return False


# def solve_sudoku(board):
#     gameboard = Board(board)
#     print(f"Puzzle to solve:\n{gameboard}")
#     if gameboard.solver():
#         print(f"Solved puzzle:\n{gameboard}")
#     else:
#         print("The provided puzzle is unsolvable.")
#     return gameboard


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]


# -------Salida-------

# ===========================================

# Paso 75


# class Board:

#     def __init__(self, board):
#         self.board = board

#     # ---Región editable por el usuario---
#     def __str__(self):
#         board_str = ''
#         for row in self.board:
#             row_str = [str(i) if i != 0 else "*" for i in row]
#             board_str += " ".join(row_str)
#     # ---Región editable por el usuario---

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#                 if self.solver():
#                     return True
#                 self.board[row][col] = 0
#         return False


# def solve_sudoku(board):
#     gameboard = Board(board)
#     print(f"Puzzle to solve:\n{gameboard}")
#     if gameboard.solver():
#         print(f"Solved puzzle:\n{gameboard}")
#     else:
#         print("The provided puzzle is unsolvable.")
#     return gameboard


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]


# -------Salida-------

# ===========================================

# Paso 76


# class Board:

#     def __init__(self, board):
#         self.board = board

#     # ---Región editable por el usuario---
#     def __str__(self):
#         board_str = ''
#         for row in self.board:
#             row_str = [str(i) if i != 0 else "*" for i in row]
#             board_str += " ".join(row_str)
#             board_str += "\n"
#     # ---Región editable por el usuario---

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#                 if self.solver():
#                     return True
#                 self.board[row][col] = 0
#         return False


# def solve_sudoku(board):
#     gameboard = Board(board)
#     print(f"Puzzle to solve:\n{gameboard}")
#     if gameboard.solver():
#         print(f"Solved puzzle:\n{gameboard}")
#     else:
#         print("The provided puzzle is unsolvable.")
#     return gameboard


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]


# -------Salida-------

# ===========================================

# Paso 77


# class Board:

#     def __init__(self, board):
#         self.board = board

#     # ---Región editable por el usuario---
#     def __str__(self):
#         board_str = ''
#         for row in self.board:
#             row_str = [str(i) if i != 0 else "*" for i in row]
#             board_str += " ".join(row_str)
#             board_str += "\n"
#         return board_str
#     # ---Región editable por el usuario---

#     def find_empty_cell(self):
#         for row, contents in enumerate(self.board):
#             try:
#                 col = contents.index(0)
#                 return row, col
#             except ValueError:
#                 pass
#         return None

#     def valid_in_row(self, row, num):
#         return num not in self.board[row]

#     def valid_in_col(self, col, num):
#         return all(self.board[row][col] != num for row in range(9))

#     def valid_in_square(self, row, col, num):
#         row_start = (row // 3) * 3
#         col_start = (col // 3) * 3
#         for row_no in range(row_start, row_start + 3):
#             for col_no in range(col_start, col_start + 3):
#                 if self.board[row_no][col_no] == num:
#                     return False
#         return True

#     def is_valid(self, empty, num):
#         row, col = empty
#         valid_in_row = self.valid_in_row(row, num)
#         valid_in_col = self.valid_in_col(col, num)
#         valid_in_square = self.valid_in_square(row, col, num)
#         return all(
#             [
#                 valid_in_row,
#                 valid_in_col,
#                 valid_in_square,
#             ]
#         )

#     def solver(self):
#         if (next_empty := self.find_empty_cell()) is None:
#             return True
#         for guess in range(1, 10):
#             if self.is_valid(next_empty, guess):
#                 row, col = next_empty
#                 self.board[row][col] = guess
#                 if self.solver():
#                     return True
#                 self.board[row][col] = 0
#         return False


# def solve_sudoku(board):
#     gameboard = Board(board)
#     print(f"Puzzle to solve:\n{gameboard}")
#     if gameboard.solver():
#         print(f"Solved puzzle:\n{gameboard}")
#     else:
#         print("The provided puzzle is unsolvable.")
#     return gameboard


# puzzle = [
#     [0, 0, 2, 0, 0, 8, 0, 0, 0],
#     [0, 0, 0, 0, 0, 3, 7, 6, 2],
#     [4, 3, 0, 0, 0, 0, 8, 0, 0],
#     [0, 5, 0, 0, 3, 0, 0, 9, 0],
#     [0, 4, 0, 0, 0, 0, 0, 2, 6],
#     [0, 0, 0, 4, 6, 7, 0, 0, 0],
#     [0, 8, 6, 7, 0, 4, 0, 0, 0],
#     [0, 0, 0, 5, 1, 9, 0, 0, 8],
#     [1, 7, 0, 0, 0, 6, 0, 0, 5],
# ]


# -------Salida-------

# ===========================================

# Paso 78


class Board:

    def __init__(self, board):
        self.board = board

    def __str__(self):
        board_str = ""
        for row in self.board:
            row_str = [str(i) if i != 0 else "*" for i in row]
            board_str += " ".join(row_str)
            board_str += "\n"
        return board_str

    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return all(self.board[row][col] != num for row in range(9))

    def valid_in_square(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all(
            [
                valid_in_row,
                valid_in_col,
                valid_in_square,
            ]
        )

    def solver(self):
        if (next_empty := self.find_empty_cell()) is None:
            return True
        for guess in range(1, 10):
            if self.is_valid(next_empty, guess):
                row, col = next_empty
                self.board[row][col] = guess
                if self.solver():
                    return True
                self.board[row][col] = 0
        return False


def solve_sudoku(board):
    gameboard = Board(board)
    print(f"Puzzle to solve:\n{gameboard}")
    if gameboard.solver():
        print(f"Solved puzzle:\n{gameboard}")
    else:
        print("The provided puzzle is unsolvable.")
    return gameboard


puzzle = [
    [0, 0, 2, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 7, 6, 2],
    [4, 3, 0, 0, 0, 0, 8, 0, 0],
    [0, 5, 0, 0, 3, 0, 0, 9, 0],
    [0, 4, 0, 0, 0, 0, 0, 2, 6],
    [0, 0, 0, 4, 6, 7, 0, 0, 0],
    [0, 8, 6, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 5, 1, 9, 0, 0, 8],
    [1, 7, 0, 0, 0, 6, 0, 0, 5],
]

# ---Región editable por el usuario---
solve_sudoku(puzzle)
# ---Región editable por el usuario---

# -------Salida-------
# Puzzle to solve:
# * * 2 * * 8 * * *
# * * * * * 3 7 6 2
# 4 3 * * * * 8 * *
# * 5 * * 3 * * 9 *
# * 4 * * * * * 2 6
# * * * 4 6 7 * * *
# * 8 6 7 * 4 * * *
# * * * 5 1 9 * * 8
# 1 7 * * * 6 * * 5

# Solved puzzle:
# 9 6 2 1 7 8 3 5 4
# 8 1 5 9 4 3 7 6 2
# 4 3 7 6 5 2 8 1 9
# 6 5 8 2 3 1 4 9 7
# 7 4 3 8 9 5 1 2 6
# 2 9 1 4 6 7 5 8 3
# 5 8 6 7 2 4 9 3 1
# 3 2 4 5 1 9 6 7 8
# 1 7 9 3 8 6 2 4 5

# ===========================================
