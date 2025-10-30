# Paso 1
# rods = {}
# ----Salida esperada----

# ===========================================

# Paso 2
# rods = {
#     "A": [],
#     "B": [],
#     "C": []
# }
# ----Salida esperada----

# ===========================================

# Paso 3
# rods = {
#     "A": range(3, 0, -1),
#     "B": [],
#     "C": []
# }

# ----Salida esperada----

# ===========================================

# Paso 4
# rods = {
#     "A": range(3, 0, -1),
#     "B": [],
#     "C": []
# }
# print(type(rods["A"]))

# ----Salida esperada----
# <class 'range'>

# ===========================================

# Paso 5
# rods = {
#     "A": list(range(3, 0, -1)),
#     "B": [],
#     "C": []
# }
# print(type(rods["A"]))

# ----Salida esperada----
# <class 'list'>

# ===========================================

# Paso 6
# rods = {
#     "A": list(range(3, 0, -1)),
#     "B": [],
#     "C": []
# }

# ----Salida esperada----

# ===========================================

# Paso 7
# rods = {
#     "A": list(range(3, 0, -1)),
#     "B": [],
#     "C": []
# }
# def move():
#     pass

# ----Salida esperada----

# ===========================================

# Paso 8
# NUMBER_OF_DISKS = 3
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# def move():
#     pass

# ----Salida esperada----

# ===========================================

# Paso 9
# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# def move():
#     pass

# ----Salida esperada----

# ===========================================

# Paso 10
# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# print(number_of_moves)
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# def move():
#     pass

# ----Salida esperada----
# 7

# ===========================================

# Paso 11
# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# def move():
#     print(rods)

# ----Salida esperada----

# ===========================================

# Paso 12
# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# def move():
#     print(rods)

# move()

# ----Salida esperada----
# {"A": [3, 2, 1], "B": [], "C": []}

# ===========================================


# Paso 13
# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# def move(n, source, auxiliary, target):
#     print(rods)


# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}

# ===========================================

# Paso 14
# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# def move(n, source, auxiliary, target):
#     print(rods)

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}

# ===========================================

# Paso 15
# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods)

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}

# ===========================================

# Paso 16
# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods)
#     for i in range(number_of_moves):
#         print(i)

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# 0
# 1
# 2
# 3
# 4
# 5
# 6

# ===========================================

# Paso 17

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods)
#     for i in range(number_of_moves):
#         if (i + 1) % 3 == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 1 allowed between A and C
# Move 4 allowed between A and C
# Move 7 allowed between A and C

# ===========================================

# Paso 18

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# # Región editable por el usuario
# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods)
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3
#         if (i + 1) % 3 == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
# # Región editable por el usuario

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 1 allowed between A and C
# Move 4 allowed between A and C
# Move 7 allowed between A and C

# ===========================================

# Paso 19

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# # Región editable por el usuario
# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods)
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3
#         if remainder == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
# # Región editable por el usuario

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 1 allowed between A and C
# Move 4 allowed between A and C
# Move 7 allowed between A and C

# ===========================================

# Paso 20

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# # Región editable por el usuario
# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods)
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3
#         if remainder == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
# # Región editable por el usuario

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 1 allowed between A and C
# Move 2 allowed between A and B
# Move 4 allowed between A and C
# Move 5 allowed between A and B
# Move 7 allowed between A and C

# ===========================================

# Paso 21

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# # Región editable por el usuario
# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods)
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3
#         if remainder == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")
# # Región editable por el usuario

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 1 allowed between A and C
# Move 2 allowed between A and B
# Move 3 allowed between B and C
# Move 4 allowed between A and C
# Move 5 allowed between A and B
# Move 6 allowed between B and C
# Move 7 allowed between A and C

# ===========================================

# Paso 22

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods)
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3

#         # Región editable por el usuario
#         if remainder == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
#             forward = False
#         # Región editable por el usuario

#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 1 allowed between A and C
# Move 2 allowed between A and B
# Move 3 allowed between B and C
# Move 4 allowed between A and C
# Move 5 allowed between A and B
# Move 6 allowed between B and C
# Move 7 allowed between A and C

# ===========================================

# Paso 23

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods)
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3
#         if remainder == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
#             forward = False

#         # Región editable por el usuario
#             if not rods[target]:
#                 forward = True
#         # Región editable por el usuario

#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 1 allowed between A and C
# Move 2 allowed between A and B
# Move 3 allowed between B and C
# Move 4 allowed between A and C
# Move 5 allowed between A and B
# Move 6 allowed between B and C
# Move 7 allowed between A and C

# ===========================================

# Paso 24

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods)
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3
#         if remainder == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
#             forward = False

#             # Región editable por el usuario
#             if not rods[target]:
#                 forward = True
#             elif rods[source] and rods[source][-1] < rods[target][-1]:
#                 forward = True
#         # Región editable por el usuario

#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 1 allowed between A and C
# Move 2 allowed between A and B
# Move 3 allowed between B and C
# Move 4 allowed between A and C
# Move 5 allowed between A and B
# Move 6 allowed between B and C
# Move 7 allowed between A and C

# ===========================================

# Paso 25

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods)
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3

#         # Región editable por el usuario
#         if remainder == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
#             forward = False
#             if not rods[target]:
#                 forward = True
#             elif rods[source] and rods[source][-1] < rods[target][-1]:
#                 forward = True
#             if forward:
#                 print(f"Moving disk {rods[source][-1]} from {source} to {target}")
#         # Región editable por el usuario

#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 1 allowed between A and C
# Moving disk 1 from A to C
# Move 2 allowed between A and B
# Move 3 allowed between B and C
# Move 4 allowed between A and C
# Moving disk 1 from A to C
# Move 5 allowed between A and B
# Move 6 allowed between B and C
# Move 7 allowed between A and C
# Moving disk 1 from A to C

# ===========================================

# Paso 26

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods)
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3

#         # Región editable por el usuario
#         if remainder == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
#             forward = False
#             if not rods[target]:
#                 forward = True
#             elif rods[source] and rods[source][-1] < rods[target][-1]:
#                 forward = True
#             if forward:
#                 print(f"Moving disk {rods[source][-1]} from {source} to {target}")
#                 rods[target].append(rods[source].pop())
#         # Región editable por el usuario

#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 1 allowed between A and C
# Moving disk 1 from A to C
# Move 2 allowed between A and B
# Move 3 allowed between B and C
# Move 4 allowed between A and C
# Move 5 allowed between A and B
# Move 6 allowed between B and C
# Move 7 allowed between A and C

# ===========================================

# Paso 27

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods)
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3
#         if remainder == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
#             forward = False
#             if not rods[target]:
#                 forward = True
#             elif rods[source] and rods[source][-1] < rods[target][-1]:
#                 forward = True

#             # Región editable por el usuario
#             if forward:
#                 print(f"Moving disk {rods[source][-1]} from {source} to {target}")
#                 rods[target].append(rods[source].pop())
#             else:
#                 print(f"Moving disk {rods[target][-1]} from {target} to {source}")
#                 rods[source].append(rods[target].pop())
#             # Región editable por el usuario

#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 1 allowed between A and C
# Moving disk 1 from A to C
# Move 2 allowed between A and B
# Move 3 allowed between B and C
# Move 4 allowed between A and C
# Moving disk 1 from C to A
# Move 5 allowed between A and B
# Move 6 allowed between B and C
# Move 7 allowed between A and C
# Moving disk 1 from A to C

# ===========================================

# Paso 28

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }
# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods)
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3
#         if remainder == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
#             forward = False
#             if not rods[target]:
#                 forward = True
#             elif rods[source] and rods[source][-1] < rods[target][-1]:
#                 forward = True

#             # Región editable por el usuario
#             if forward:
#                 print(f"Moving disk {rods[source][-1]} from {source} to {target}")
#                 rods[target].append(rods[source].pop())
#             else:
#                 print(f"Moving disk {rods[target][-1]} from {target} to {source}")
#                 rods[source].append(rods[target].pop())
#             # display our progress
#             print(rods)
#             # Región editable por el usuario

#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 1 allowed between A and C
# Moving disk 1 from A to C
# {'A': [3, 2], 'B': [], 'C': [1]}
# Move 2 allowed between A and B
# Move 3 allowed between B and C
# Move 4 allowed between A and C
# Moving disk 1 from C to A
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 5 allowed between A and B
# Move 6 allowed between B and C
# Move 7 allowed between A and C
# Moving disk 1 from A to C
# {'A': [3, 2], 'B': [], 'C': [1]}

# ===========================================

# Paso 29

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }

# # Región editable por el usuario
# def make_allowed_move():
#     pass
# # Región editable por el usuario

# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods)
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3
#         if remainder == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
#             forward = False
#             if not rods[target]:
#                 forward = True
#             elif rods[source] and rods[source][-1] < rods[target][-1]:
#                 forward = True
#             if forward:
#                 print(f"Moving disk {rods[source][-1]} from {source} to {target}")
#                 rods[target].append(rods[source].pop())
#             else:
#                 print(f"Moving disk {rods[target][-1]} from {target} to {source}")
#                 rods[source].append(rods[target].pop())
#             # display our progress
#             print(rods)
#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 1 allowed between A and C
# Moving disk 1 from A to C
# {'A': [3, 2], 'B': [], 'C': [1]}
# Move 2 allowed between A and B
# Move 3 allowed between B and C
# Move 4 allowed between A and C
# Moving disk 1 from C to A
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 5 allowed between A and B
# Move 6 allowed between B and C
# Move 7 allowed between A and C
# Moving disk 1 from A to C
# {'A': [3, 2], 'B': [], 'C': [1]}

# ===========================================

# Paso 30

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
# }


# # Región editable por el usuario
# def make_allowed_move(rod1, rod2):
#     pass
# # Región editable por el usuario

# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods)
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3
#         if remainder == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
#             forward = False
#             if not rods[target]:
#                 forward = True
#             elif rods[source] and rods[source][-1] < rods[target][-1]:
#                 forward = True
#             if forward:
#                 print(f"Moving disk {rods[source][-1]} from {source} to {target}")
#                 rods[target].append(rods[source].pop())
#             else:
#                 print(f"Moving disk {rods[target][-1]} from {target} to {source}")
#                 rods[source].append(rods[target].pop())
#             # display our progress
#             print(rods)
#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 1 allowed between A and C
# Moving disk 1 from A to C
# {'A': [3, 2], 'B': [], 'C': [1]}
# Move 2 allowed between A and B
# Move 3 allowed between B and C
# Move 4 allowed between A and C
# Moving disk 1 from C to A
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 5 allowed between A and B
# Move 6 allowed between B and C
# Move 7 allowed between A and C
# Moving disk 1 from A to C
# {'A': [3, 2], 'B': [], 'C': [1]}

# ===========================================

# Paso 31

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {"A": list(range(NUMBER_OF_DISKS, 0, -1)), "B": [], "C": []}


# # Región editable por el usuario
# def make_allowed_move(rod1, rod2):
#     forward = False
#     if not rods[target]:
#         forward = True
#     elif rods[source] and rods[source][-1] < rods[target][-1]:
#         forward = True
#     if forward:
#         print(f"Moving disk {rods[source][-1]} from {source} to {target}")
#         rods[target].append(rods[source].pop())
#     else:
#         print(f"Moving disk {rods[target][-1]} from {target} to {source}")
#         rods[source].append(rods[target].pop())
#     # display our progress
#     print(rods)


# def move(n, source, auxiliary, target):
#     print(rods)
#     # display starting configuration
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3
#         if remainder == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
#         # Región editable por el usuario

#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")


# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 1 allowed between A and C
# Move 2 allowed between A and B
# Move 3 allowed between B and C
# Move 4 allowed between A and C
# Move 5 allowed between A and B
# Move 6 allowed between B and C
# Move 7 allowed between A and C

# ===========================================

# Paso 32

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {"A": list(range(NUMBER_OF_DISKS, 0, -1)), "B": [], "C": []}


# # Región editable por el usuario
# def make_allowed_move(rod1, rod2):
#     forward = False
#     if not rods[target]:
#         forward = True
#     elif rods[rod1] and rods[rod1][-1] < rods[target][-1]:
#         forward = True
#     if forward:
#         print(f"Moving disk {rods[rod1][-1]} from {rod1} to {target}")
#         rods[target].append(rods[rod1].pop())
#     else:
#         print(f"Moving disk {rods[target][-1]} from {target} to {rod1}")
#         rods[rod1].append(rods[target].pop())
#     # display our progress
#     print(rods)


# def move(n, source, auxiliary, target):
#     print(rods)
#     # display starting configuration
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3
#         if remainder == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
#         # Región editable por el usuario

#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")


# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 1 allowed between A and C
# Move 2 allowed between A and B
# Move 3 allowed between B and C
# Move 4 allowed between A and C
# Move 5 allowed between A and B
# Move 6 allowed between B and C
# Move 7 allowed between A and C

# ===========================================

# Paso 33

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {"A": list(range(NUMBER_OF_DISKS, 0, -1)), "B": [], "C": []}


# # Región editable por el usuario
# def make_allowed_move(rod1, rod2):
#     forward = False
#     if not rods[rod2]:
#         forward = True
#     elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
#         forward = True
#     if forward:
#         print(f"Moving disk {rods[rod1][-1]} from {rod1} to {rod2}")
#         rods[rod2].append(rods[rod1].pop())
#     else:
#         print(f"Moving disk {rods[rod2][-1]} from {rod2} to {rod1}")
#         rods[rod1].append(rods[rod2].pop())
#     # display our progress
#     print(rods)


# def move(n, source, auxiliary, target):
#     print(rods)
#     # display starting configuration
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3
#         if remainder == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
#         # Región editable por el usuario

#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")


# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 1 allowed between A and C
# Move 2 allowed between A and B
# Move 3 allowed between B and C
# Move 4 allowed between A and C
# Move 5 allowed between A and B
# Move 6 allowed between B and C
# Move 7 allowed between A and C

# ===========================================

# Paso 34

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {"A": list(range(NUMBER_OF_DISKS, 0, -1)), "B": [], "C": []}


# def make_allowed_move(rod1, rod2):
#     forward = False
#     if not rods[rod2]:
#         forward = True
#     elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
#         forward = True
#     if forward:
#         print(f"Moving disk {rods[rod1][-1]} from {rod1} to {rod2}")
#         rods[rod2].append(rods[rod1].pop())
#     else:
#         print(f"Moving disk {rods[rod2][-1]} from {rod2} to {rod1}")
#         rods[rod1].append(rods[rod2].pop())
#     # display our progress
#     print(rods)


# def move(n, source, auxiliary, target):
#     print(rods)
#     # display starting configuration
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3

#         # Región editable por el usuario
#         if remainder == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
#             make_allowed_move(source, target)
#         # Región editable por el usuario

#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")


# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 1 allowed between A and C
# Move 2 allowed between A and B
# Move 3 allowed between B and C
# Move 4 allowed between A and C
# Move 5 allowed between A and B
# Move 6 allowed between B and C
# Move 7 allowed between A and C

# ===========================================

# Paso 35

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {"A": list(range(NUMBER_OF_DISKS, 0, -1)), "B": [], "C": []}


# def make_allowed_move(rod1, rod2):
#     forward = False
#     if not rods[rod2]:
#         forward = True
#     elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
#         forward = True
#     if forward:
#         print(f"Moving disk {rods[rod1][-1]} from {rod1} to {rod2}")
#         rods[rod2].append(rods[rod1].pop())
#     else:
#         print(f"Moving disk {rods[rod2][-1]} from {rod2} to {rod1}")
#         rods[rod1].append(rods[rod2].pop())
#     # display our progress
#     print(rods)


# def move(n, source, auxiliary, target):
#     print(rods)
#     # display starting configuration
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3

#         # Región editable por el usuario
#         if remainder == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
#             make_allowed_move(source, target)
#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#             make_allowed_move(source, auxiliary)
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")
#             make_allowed_move(auxiliary, target)
#         # Región editable por el usuario


# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}
# Move 1 allowed between A and C
# Moving disk 1 from A to C
# {'A': [3, 2], 'B': [], 'C': [1]}
# Move 2 allowed between A and B
# Moving disk 2 from A to B
# {'A': [3], 'B': [2], 'C': [1]}
# Move 3 allowed between B and C
# Moving disk 1 from C to B
# {'A': [3], 'B': [2, 1], 'C': []}
# Move 4 allowed between A and C
# Moving disk 3 from A to C
# {'A': [], 'B': [2, 1], 'C': [3]}
# Move 5 allowed between A and B
# Moving disk 1 from B to A
# {'A': [1], 'B': [2], 'C': [3]}
# Move 6 allowed between B and C
# Moving disk 2 from B to C
# {'A': [1], 'B': [], 'C': [3, 2]}
# Move 7 allowed between A and C
# Moving disk 1 from A to C
# {'A': [], 'B': [], 'C': [3, 2, 1]}

# ===========================================

# Paso 36

# NUMBER_OF_DISKS = 3
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {"A": list(range(NUMBER_OF_DISKS, 0, -1)), "B": [], "C": []}


# def make_allowed_move(rod1, rod2):
#     forward = False
#     if not rods[rod2]:
#         forward = True
#     elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
#         forward = True
#     if forward:
#         print(f"Moving disk {rods[rod1][-1]} from {rod1} to {rod2}")
#         rods[rod2].append(rods[rod1].pop())
#     else:
#         print(f"Moving disk {rods[rod2][-1]} from {rod2} to {rod1}")
#         rods[rod1].append(rods[rod2].pop())

#     # Región editable por el usuario
#     # display our progress
#     print(rods, "\n")


# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods, "\n")
#     # Región editable por el usuario

#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3

#         if remainder == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
#             make_allowed_move(source, target)
#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#             make_allowed_move(source, auxiliary)
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")
#             make_allowed_move(auxiliary, target)


# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [3, 2, 1], 'B': [], 'C': []}

# Move 1 allowed between A and C
# Moving disk 1 from A to C
# {'A': [3, 2], 'B': [], 'C': [1]}

# Move 2 allowed between A and B
# Moving disk 2 from A to B
# {'A': [3], 'B': [2], 'C': [1]}

# Move 3 allowed between B and C
# Moving disk 1 from C to B
# {'A': [3], 'B': [2, 1], 'C': []}

# Move 4 allowed between A and C
# Moving disk 3 from A to C
# {'A': [], 'B': [2, 1], 'C': [3]}

# Move 5 allowed between A and B
# Moving disk 1 from B to A
# {'A': [1], 'B': [2], 'C': [3]}

# Move 6 allowed between B and C
# Moving disk 2 from B to C
# {'A': [1], 'B': [], 'C': [3, 2]}

# Move 7 allowed between A and C
# Moving disk 1 from A to C
# {'A': [], 'B': [], 'C': [3, 2, 1]}

# ===========================================

# Paso 37

# # Región editable por el usuario
# NUMBER_OF_DISKS = 4
# # Región editable por el usuario

# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {"A": list(range(NUMBER_OF_DISKS, 0, -1)), "B": [], "C": []}


# def make_allowed_move(rod1, rod2):
#     forward = False
#     if not rods[rod2]:
#         forward = True
#     elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
#         forward = True
#     if forward:
#         print(f"Moving disk {rods[rod1][-1]} from {rod1} to {rod2}")
#         rods[rod2].append(rods[rod1].pop())
#     else:
#         print(f"Moving disk {rods[rod2][-1]} from {rod2} to {rod1}")
#         rods[rod1].append(rods[rod2].pop())

#     # display our progress
#     print(rods, "\n")


# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods, "\n")
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3
#         if remainder == 1:
#             print(f"Move {i + 1} allowed between {source} and {target}")
#             make_allowed_move(source, target)
#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#             make_allowed_move(source, auxiliary)
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")
#             make_allowed_move(auxiliary, target)


# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [4, 3, 2, 1], 'B': [], 'C': []}

# Move 1 allowed between A and C
# Moving disk 1 from A to C
# {'A': [4, 3, 2], 'B': [], 'C': [1]}

# Move 2 allowed between A and B
# Moving disk 2 from A to B
# {'A': [4, 3], 'B': [2], 'C': [1]}

# Move 3 allowed between B and C
# Moving disk 1 from C to B
# {'A': [4, 3], 'B': [2, 1], 'C': []}

# Move 4 allowed between A and C
# Moving disk 3 from A to C
# {'A': [4], 'B': [2, 1], 'C': [3]}

# Move 5 allowed between A and B
# Moving disk 1 from B to A
# {'A': [4, 1], 'B': [2], 'C': [3]}

# Move 6 allowed between B and C
# Moving disk 2 from B to C
# {'A': [4, 1], 'B': [], 'C': [3, 2]}

# Move 7 allowed between A and C
# Moving disk 1 from A to C
# {'A': [4], 'B': [], 'C': [3, 2, 1]}

# Move 8 allowed between A and B
# Moving disk 4 from A to B
# {'A': [], 'B': [4], 'C': [3, 2, 1]}

# Move 9 allowed between B and C
# Moving disk 1 from C to B
# {'A': [], 'B': [4, 1], 'C': [3, 2]}

# Move 10 allowed between A and C
# Moving disk 2 from C to A
# {'A': [2], 'B': [4, 1], 'C': [3]}

# Move 11 allowed between A and B
# Moving disk 1 from B to A
# {'A': [2, 1], 'B': [4], 'C': [3]}

# Move 12 allowed between B and C
# Moving disk 3 from C to B
# {'A': [2, 1], 'B': [4, 3], 'C': []}

# Move 13 allowed between A and C
# Moving disk 1 from A to C
# {'A': [2], 'B': [4, 3], 'C': [1]}

# Move 14 allowed between A and B
# Moving disk 2 from A to B
# {'A': [], 'B': [4, 3, 2], 'C': [1]}

# Move 15 allowed between B and C
# Moving disk 1 from C to B
# {'A': [], 'B': [4, 3, 2, 1], 'C': []}

# ===========================================

# Paso 38

# NUMBER_OF_DISKS = 4
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {"A": list(range(NUMBER_OF_DISKS, 0, -1)), "B": [], "C": []}


# def make_allowed_move(rod1, rod2):
#     forward = False
#     if not rods[rod2]:
#         forward = True
#     elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
#         forward = True
#     if forward:
#         print(f"Moving disk {rods[rod1][-1]} from {rod1} to {rod2}")
#         rods[rod2].append(rods[rod1].pop())
#     else:
#         print(f"Moving disk {rods[rod2][-1]} from {rod2} to {rod1}")
#         rods[rod1].append(rods[rod2].pop())

#     # display our progress
#     print(rods, "\n")


# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods, "\n")
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3

#         # Región editable por el usuario
#         if remainder == 1:
#             if n % 2 != 0:
#                 print(f"Move {i + 1} allowed between {source} and {target}")
#                 make_allowed_move(source, target)
#         # Región editable por el usuario

#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#             make_allowed_move(source, auxiliary)
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")
#             make_allowed_move(auxiliary, target)


# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [4, 3, 2, 1], 'B': [], 'C': []}

# Move 2 allowed between A and B
# Moving disk 1 from A to B
# {'A': [4, 3, 2], 'B': [1], 'C': []}

# Move 3 allowed between B and C
# Moving disk 1 from B to C
# {'A': [4, 3, 2], 'B': [], 'C': [1]}

# Move 5 allowed between A and B
# Moving disk 2 from A to B
# {'A': [4, 3], 'B': [2], 'C': [1]}

# Move 6 allowed between B and C
# Moving disk 1 from C to B
# {'A': [4, 3], 'B': [2, 1], 'C': []}

# Move 8 allowed between A and B
# Moving disk 1 from B to A
# {'A': [4, 3, 1], 'B': [2], 'C': []}

# Move 9 allowed between B and C
# Moving disk 2 from B to C
# {'A': [4, 3, 1], 'B': [], 'C': [2]}

# Move 11 allowed between A and B
# Moving disk 1 from A to B
# {'A': [4, 3], 'B': [1], 'C': [2]}

# Move 12 allowed between B and C
# Moving disk 1 from B to C
# {'A': [4, 3], 'B': [], 'C': [2, 1]}

# Move 14 allowed between A and B
# Moving disk 3 from A to B
# {'A': [4], 'B': [3], 'C': [2, 1]}

# Move 15 allowed between B and C
# Moving disk 1 from C to B
# {'A': [4], 'B': [3, 1], 'C': [2]}

# ===========================================

# Paso 39

# NUMBER_OF_DISKS = 4
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {"A": list(range(NUMBER_OF_DISKS, 0, -1)), "B": [], "C": []}


# def make_allowed_move(rod1, rod2):
#     forward = False
#     if not rods[rod2]:
#         forward = True
#     elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
#         forward = True
#     if forward:
#         print(f"Moving disk {rods[rod1][-1]} from {rod1} to {rod2}")
#         rods[rod2].append(rods[rod1].pop())
#     else:
#         print(f"Moving disk {rods[rod2][-1]} from {rod2} to {rod1}")
#         rods[rod1].append(rods[rod2].pop())

#     # display our progress
#     print(rods, "\n")


# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods, "\n")
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3

#         # Región editable por el usuario
#         if remainder == 1:
#             if n % 2 != 0:
#                 print(f"Move {i + 1} allowed between {source} and {target}")
#                 # make_allowed_move(source, target)
#             else:
#                 print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#                 # make_allowed_move(source, auxiliary)
#         # Región editable por el usuario

#         elif remainder == 2:
#             print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#             make_allowed_move(source, auxiliary)
#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")
#             make_allowed_move(auxiliary, target)


# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [4, 3, 2, 1], 'B': [], 'C': []}

# Move 2 allowed between A and B
# Moving disk 1 from A to B
# {'A': [4, 3, 2], 'B': [1], 'C': []}

# Move 3 allowed between B and C
# Moving disk 1 from B to C
# {'A': [4, 3, 2], 'B': [], 'C': [1]}

# Move 5 allowed between A and B
# Moving disk 2 from A to B
# {'A': [4, 3], 'B': [2], 'C': [1]}

# Move 6 allowed between B and C
# Moving disk 1 from C to B
# {'A': [4, 3], 'B': [2, 1], 'C': []}

# Move 8 allowed between A and B
# Moving disk 1 from B to A
# {'A': [4, 3, 1], 'B': [2], 'C': []}

# Move 9 allowed between B and C
# Moving disk 2 from B to C
# {'A': [4, 3, 1], 'B': [], 'C': [2]}

# Move 11 allowed between A and B
# Moving disk 1 from A to B
# {'A': [4, 3], 'B': [1], 'C': [2]}

# Move 12 allowed between B and C
# Moving disk 1 from B to C
# {'A': [4, 3], 'B': [], 'C': [2, 1]}

# Move 14 allowed between A and B
# Moving disk 3 from A to B
# {'A': [4], 'B': [3], 'C': [2, 1]}

# Move 15 allowed between B and C
# Moving disk 1 from C to B
# {'A': [4], 'B': [3, 1], 'C': [2]}

# ===========================================

# Paso 40

# NUMBER_OF_DISKS = 4
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {"A": list(range(NUMBER_OF_DISKS, 0, -1)), "B": [], "C": []}


# def make_allowed_move(rod1, rod2):
#     forward = False
#     if not rods[rod2]:
#         forward = True
#     elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
#         forward = True
#     if forward:
#         print(f"Moving disk {rods[rod1][-1]} from {rod1} to {rod2}")
#         rods[rod2].append(rods[rod1].pop())
#     else:
#         print(f"Moving disk {rods[rod2][-1]} from {rod2} to {rod1}")
#         rods[rod1].append(rods[rod2].pop())

#     # display our progress
#     print(rods, "\n")


# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods, "\n")
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3
#         if remainder == 1:
#             if n % 2 != 0:
#                 print(f"Move {i + 1} allowed between {source} and {target}")
#                 make_allowed_move(source, target)

#             # Región editable por el usuario
#             else:
#                 print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#                 make_allowed_move(source, auxiliary)

#         elif remainder == 2:
#             if n % 2 != 0:
#                 print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#                 make_allowed_move(source, auxiliary)
#             # Región editable por el usuario

#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")
#             make_allowed_move(auxiliary, target)


# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [4, 3, 2, 1], 'B': [], 'C': []}

# Move 1 allowed between A and B
# Moving disk 1 from A to B
# {'A': [4, 3, 2], 'B': [1], 'C': []}

# Move 3 allowed between B and C
# Moving disk 1 from B to C
# {'A': [4, 3, 2], 'B': [], 'C': [1]}

# Move 4 allowed between A and B
# Moving disk 2 from A to B
# {'A': [4, 3], 'B': [2], 'C': [1]}

# Move 6 allowed between B and C
# Moving disk 1 from C to B
# {'A': [4, 3], 'B': [2, 1], 'C': []}

# Move 7 allowed between A and B
# Moving disk 1 from B to A
# {'A': [4, 3, 1], 'B': [2], 'C': []}

# Move 9 allowed between B and C
# Moving disk 2 from B to C
# {'A': [4, 3, 1], 'B': [], 'C': [2]}

# Move 10 allowed between A and B
# Moving disk 1 from A to B
# {'A': [4, 3], 'B': [1], 'C': [2]}

# Move 12 allowed between B and C
# Moving disk 1 from B to C
# {'A': [4, 3], 'B': [], 'C': [2, 1]}

# Move 13 allowed between A and B
# Moving disk 3 from A to B
# {'A': [4], 'B': [3], 'C': [2, 1]}

# Move 15 allowed between B and C
# Moving disk 1 from C to B
# {'A': [4], 'B': [3, 1], 'C': [2]}

# ===========================================

# Paso 41

# NUMBER_OF_DISKS = 4
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {"A": list(range(NUMBER_OF_DISKS, 0, -1)), "B": [], "C": []}


# def make_allowed_move(rod1, rod2):
#     forward = False
#     if not rods[rod2]:
#         forward = True
#     elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
#         forward = True
#     if forward:
#         print(f"Moving disk {rods[rod1][-1]} from {rod1} to {rod2}")
#         rods[rod2].append(rods[rod1].pop())
#     else:
#         print(f"Moving disk {rods[rod2][-1]} from {rod2} to {rod1}")
#         rods[rod1].append(rods[rod2].pop())

#     # display our progress
#     print(rods, "\n")


# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods, "\n")
#     for i in range(number_of_moves):
#         remainder = (i + 1) % 3
#         if remainder == 1:
#             if n % 2 != 0:
#                 print(f"Move {i + 1} allowed between {source} and {target}")
#                 make_allowed_move(source, target)
#             else:
#                 print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#                 make_allowed_move(source, auxiliary)

#         # Región editable por el usuario
#         elif remainder == 2:
#             if n % 2 != 0:
#                 print(f"Move {i + 1} allowed between {source} and {auxiliary}")
#                 make_allowed_move(source, auxiliary)
#             else:
#                 print(f"Move {i + 1} allowed between {source} and {target}")
#                 make_allowed_move(source, target)
#         # Región editable por el usuario

#         elif remainder == 0:
#             print(f"Move {i + 1} allowed between {auxiliary} and {target}")
#             make_allowed_move(auxiliary, target)


# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [4, 3, 2, 1], 'B': [], 'C': []}

# Move 1 allowed between A and B
# Moving disk 1 from A to B
# {'A': [4, 3, 2], 'B': [1], 'C': []}

# Move 2 allowed between A and C
# Moving disk 2 from A to C
# {'A': [4, 3], 'B': [1], 'C': [2]}

# Move 3 allowed between B and C
# Moving disk 1 from B to C
# {'A': [4, 3], 'B': [], 'C': [2, 1]}

# Move 4 allowed between A and B
# Moving disk 3 from A to B
# {'A': [4], 'B': [3], 'C': [2, 1]}

# Move 5 allowed between A and C
# Moving disk 1 from C to A
# {'A': [4, 1], 'B': [3], 'C': [2]}

# Move 6 allowed between B and C
# Moving disk 2 from C to B
# {'A': [4, 1], 'B': [3, 2], 'C': []}

# Move 7 allowed between A and B
# Moving disk 1 from A to B
# {'A': [4], 'B': [3, 2, 1], 'C': []}

# Move 8 allowed between A and C
# Moving disk 4 from A to C
# {'A': [], 'B': [3, 2, 1], 'C': [4]}

# Move 9 allowed between B and C
# Moving disk 1 from B to C
# {'A': [], 'B': [3, 2], 'C': [4, 1]}

# Move 10 allowed between A and B
# Moving disk 2 from B to A
# {'A': [2], 'B': [3], 'C': [4, 1]}

# Move 11 allowed between A and C
# Moving disk 1 from C to A
# {'A': [2, 1], 'B': [3], 'C': [4]}

# Move 12 allowed between B and C
# Moving disk 3 from B to C
# {'A': [2, 1], 'B': [], 'C': [4, 3]}

# Move 13 allowed between A and B
# Moving disk 1 from A to B
# {'A': [2], 'B': [1], 'C': [4, 3]}

# Move 14 allowed between A and C
# Moving disk 2 from A to C
# {'A': [], 'B': [1], 'C': [4, 3, 2]}

# Move 15 allowed between B and C
# Moving disk 1 from B to C
# {'A': [], 'B': [], 'C': [4, 3, 2, 1]}

# ===========================================

# Paso 42

# NUMBER_OF_DISKS = 4
# number_of_moves = 2**NUMBER_OF_DISKS - 1
# rods = {"A": list(range(NUMBER_OF_DISKS, 0, -1)), "B": [], "C": []}


# def make_allowed_move(rod1, rod2):
#     forward = False
#     if not rods[rod2]:
#         forward = True
#     elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
#         forward = True
#     if forward:
#         print(f"Moving disk {rods[rod1][-1]} from {rod1} to {rod2}")
#         rods[rod2].append(rods[rod1].pop())
#     else:
#         print(f"Moving disk {rods[rod2][-1]} from {rod2} to {rod1}")
#         rods[rod1].append(rods[rod2].pop())
#     # display our progress
#     print(rods, "\n")


# # Región editable por el usuario
# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods, "\n")
# # Región editable por el usuario


# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [4, 3, 2, 1], 'B': [], 'C': []}

# ===========================================

# Paso 43

# NUMBER_OF_DISKS = 4
# rods = {"A": list(range(NUMBER_OF_DISKS, 0, -1)), "B": [], "C": []}


# def move(n, source, auxiliary, target):
#     # display starting configuration
#     print(rods, "\n")

# # Región editable por el usuario

# # Región editable por el usuario

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [4, 3, 2, 1], 'B': [], 'C': []}

# ===========================================

# Paso 44

# NUMBER_OF_DISKS = 4
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
#     }

# def move(n, source, auxiliary, target):

# # Región editable por el usuario
#     if n > 0:
#         move(n - 1, source, auxiliary, target)
# # Región editable por el usuario

#         # display starting configuration
#         print(rods, "\n")

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {"A": [4, 3, 2, 1], "B": [], "C": []}

# {"A": [4, 3, 2, 1], "B": [], "C": []}

# {"A": [4, 3, 2, 1], "B": [], "C": []}

# {"A": [4, 3, 2, 1], "B": [], "C": []}

# ===========================================

# Paso 45

# NUMBER_OF_DISKS = 4
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
#     }

# def move(n, source, auxiliary, target):

#     # Región editable por el usuario
#     if n > 0:
#         # move n - 1 disks from source to auxiliary, so they are out of the way
#         move(n - 1, source, auxiliary, target)
#         # Región editable por el usuario

#         # display starting configuration
#         print(rods, "\n")

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {"A": [4, 3, 2, 1], "B": [], "C": []}

# {"A": [4, 3, 2, 1], "B": [], "C": []}

# {"A": [4, 3, 2, 1], "B": [], "C": []}

# {"A": [4, 3, 2, 1], "B": [], "C": []}

# ===========================================

# Paso 46

# NUMBER_OF_DISKS = 4
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
#     }

# def move(n, source, auxiliary, target):

#     # Región editable por el usuario
#     if n > 0:
#         # move n - 1 disks from source to auxiliary, so they are out of the way
#         move(n - 1, source, auxiliary, target)
#         rods[target].append(rods[source].pop())
#         # Región editable por el usuario

#         # display starting configuration
#         print(rods, "\n")

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {"A": [4, 3, 2, 1], "B": [], "C": []}

# {"A": [4, 3, 2, 1], "B": [], "C": []}

# {"A": [4, 3, 2, 1], "B": [], "C": []}

# {"A": [4, 3, 2, 1], "B": [], "C": []}

# ===========================================

# Paso 47

# NUMBER_OF_DISKS = 4
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
#     }

# def move(n, source, auxiliary, target):

#     # Región editable por el usuario
#     if n > 0:
#         # move n - 1 disks from source to auxiliary, so they are out of the way
#         move(n - 1, source, auxiliary, target)
#         # move the nth disk from source to target
#         rods[target].append(rods[source].pop())
#         # Región editable por el usuario

#         # display starting configuration
#         print(rods, "\n")

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {"A": [4, 3, 2, 1], "B": [], "C": []}

# {"A": [4, 3, 2, 1], "B": [], "C": []}

# {"A": [4, 3, 2, 1], "B": [], "C": []}

# {"A": [4, 3, 2, 1], "B": [], "C": []}

# ===========================================

# Paso 48

# NUMBER_OF_DISKS = 4
# rods = {
#     "A": list(range(NUMBER_OF_DISKS, 0, -1)),
#     "B": [],
#     "C": []
#     }

# def move(n, source, auxiliary, target):

#     # Región editable por el usuario
#     if n > 0:
#         # move n - 1 disks from source to auxiliary, so they are out of the way
#         move(n - 1, source, auxiliary, target)
#         # move the nth disk from source to target
#         rods[target].append(rods[source].pop())
#         # Región editable por el usuario

#         # display our progress
#         print(rods, "\n")

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [4, 3, 2], 'B': [], 'C': [1]}

# {'A': [4, 3], 'B': [], 'C': [1, 2]}

# {'A': [4], 'B': [], 'C': [1, 2, 3]}

# {'A': [], 'B': [], 'C': [1, 2, 3, 4]}

# ===========================================

# Paso 49

# NUMBER_OF_DISKS = 4
# rods = {"A": list(range(NUMBER_OF_DISKS, 0, -1)), "B": [], "C": []}


# # Región editable por el usuario
# def move(n, source, auxiliary, target):
#     if n > 0:
#         # move n - 1 disks from source to auxiliary, so they are out of the way
#         move(n - 1, source, target, auxiliary)

#         # move the nth disk from source to target
#         rods[target].append(rods[source].pop())

#         # display our progress
#         print(rods, "\n")


# # Región editable por el usuario

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [4, 3, 2], 'B': [1], 'C': []}

# {'A': [4, 3], 'B': [1], 'C': [2]}

# {'A': [4], 'B': [1, 3], 'C': [2]}

# {'A': [], 'B': [1, 3], 'C': [2, 4]}

# ===========================================

# Paso 50

# NUMBER_OF_DISKS = 4
# rods = {"A": list(range(NUMBER_OF_DISKS, 0, -1)), "B": [], "C": []}


# # Región editable por el usuario
# def move(n, source, auxiliary, target):
#     if n > 0:
#         # move n - 1 disks from source to auxiliary, so they are out of the way
#         move(n - 1, source, target, auxiliary)

#         # move the nth disk from source to target
#         rods[target].append(rods[source].pop())

#         # display our progress
#         print(rods, "\n")

#         move(n - 1, auxiliary, source, target)


# # Región editable por el usuario

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [4, 3, 2], 'B': [1], 'C': []}

# {'A': [4, 3], 'B': [1], 'C': [2]}

# {'A': [4, 3], 'B': [], 'C': [2, 1]}

# {'A': [4], 'B': [3], 'C': [2, 1]}

# {'A': [4, 1], 'B': [3], 'C': [2]}

# {'A': [4, 1], 'B': [3, 2], 'C': []}

# {'A': [4], 'B': [3, 2, 1], 'C': []}

# {'A': [], 'B': [3, 2, 1], 'C': [4]}

# {'A': [], 'B': [3, 2], 'C': [4, 1]}

# {'A': [2], 'B': [3], 'C': [4, 1]}

# {'A': [2, 1], 'B': [3], 'C': [4]}

# {'A': [2, 1], 'B': [], 'C': [4, 3]}

# {'A': [2], 'B': [1], 'C': [4, 3]}

# {'A': [], 'B': [1], 'C': [4, 3, 2]}

# {'A': [], 'B': [], 'C': [4, 3, 2, 1]}

# ===========================================

# Paso 51

# NUMBER_OF_DISKS = 4
# rods = {"A": list(range(NUMBER_OF_DISKS, 0, -1)), "B": [], "C": []}


# # Región editable por el usuario
# def move(n, source, auxiliary, target):
#     if n > 0:
#         # move n - 1 disks from source to auxiliary, so they are out of the way
#         move(n - 1, source, target, auxiliary)

#         # move the nth disk from source to target
#         rods[target].append(rods[source].pop())

#         # display our progress
#         print(rods, "\n")

#         # move the n - 1 disks that we left on auxiliary onto target
#         move(n - 1, auxiliary, source, target)


# # Región editable por el usuario

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, "A", "B", "C")

# ----Salida esperada----
# {'A': [4, 3, 2], 'B': [1], 'C': []}

# {'A': [4, 3], 'B': [1], 'C': [2]}

# {'A': [4, 3], 'B': [], 'C': [2, 1]}

# {'A': [4], 'B': [3], 'C': [2, 1]}

# {'A': [4, 1], 'B': [3], 'C': [2]}

# {'A': [4, 1], 'B': [3, 2], 'C': []}

# {'A': [4], 'B': [3, 2, 1], 'C': []}

# {'A': [], 'B': [3, 2, 1], 'C': [4]}

# {'A': [], 'B': [3, 2], 'C': [4, 1]}

# {'A': [2], 'B': [3], 'C': [4, 1]}

# {'A': [2, 1], 'B': [3], 'C': [4]}

# {'A': [2, 1], 'B': [], 'C': [4, 3]}

# {'A': [2], 'B': [1], 'C': [4, 3]}

# {'A': [], 'B': [1], 'C': [4, 3, 2]}

# {'A': [], 'B': [], 'C': [4, 3, 2, 1]}

# ===========================================

# Paso 52

# NUMBER_OF_DISKS = 4
# A = list(range(NUMBER_OF_DISKS, 0, -1))
# B = []
# C = []


# # Región editable por el usuario
# def move(n, source, auxiliary, target):
#     if n > 0:
#         # move n - 1 disks from source to auxiliary, so they are out of the way
#         move(n - 1, source, target, auxiliary)

#         # move the nth disk from source to target
#         target.append(source.pop())

#         # display our progress
#         print(A, B, C, "\n")

#         # move the n - 1 disks that we left on auxiliary onto target
#         move(n - 1, auxiliary, source, target)


# # Región editable por el usuario

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, A, B, C)

# ----Salida esperada----
# [4, 3, 2] [1] []

# [4, 3] [1] [2]

# [4, 3] [] [2, 1]

# [4] [3] [2, 1]

# [4, 1] [3] [2]

# [4, 1] [3, 2] []

# [4] [3, 2, 1] []

# [] [3, 2, 1] [4]

# [] [3, 2] [4, 1]

# [2] [3] [4, 1]

# [2, 1] [3] [4]

# [2, 1] [] [4, 3]

# [2] [1] [4, 3]

# [] [1] [4, 3, 2]

# [] [] [4, 3, 2, 1]

# ===========================================

# Paso 53

# NUMBER_OF_DISKS = 5
# A = list(range(NUMBER_OF_DISKS, 0, -1))
# B = []
# C = []


# # Región editable por el usuario
# def move(n, source, auxiliary, target):
#     if n > 0:
#         # move n - 1 disks from source to auxiliary, so they are out of the way
#         move(n - 1, source, target, auxiliary)

#         # move the nth disk from source to target
#         target.append(source.pop())

#         # display our progress
#         print(A, B, C, "\n")

#         # move the n - 1 disks that we left on auxiliary onto target
#         move(n - 1, auxiliary, source, target)


# # Región editable por el usuario

# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, A, B, C)

# ----Salida esperada----
# [5, 4, 3, 2] [] [1]

# [5, 4, 3] [2] [1]

# [5, 4, 3] [2, 1] []

# [5, 4] [2, 1] [3]

# [5, 4, 1] [2] [3]

# [5, 4, 1] [] [3, 2]

# [5, 4] [] [3, 2, 1]

# [5] [4] [3, 2, 1]

# [5] [4, 1] [3, 2]

# [5, 2] [4, 1] [3]

# [5, 2, 1] [4] [3]

# [5, 2, 1] [4, 3] []

# [5, 2] [4, 3] [1]

# [5] [4, 3, 2] [1]

# [5] [4, 3, 2, 1] []

# [] [4, 3, 2, 1] [5]

# [1] [4, 3, 2] [5]

# [1] [4, 3] [5, 2]

# [] [4, 3] [5, 2, 1]

# [3] [4] [5, 2, 1]

# [3] [4, 1] [5, 2]

# [3, 2] [4, 1] [5]

# [3, 2, 1] [4] [5]

# [3, 2, 1] [] [5, 4]

# [3, 2] [] [5, 4, 1]

# [3] [2] [5, 4, 1]

# [3] [2, 1] [5, 4]

# [] [2, 1] [5, 4, 3]

# [1] [2] [5, 4, 3]

# [1] [] [5, 4, 3, 2]

# [] [] [5, 4, 3, 2, 1]

# ===========================================

# Paso 54

# NUMBER_OF_DISKS = 5
# A = list(range(NUMBER_OF_DISKS, 0, -1))
# B = []
# C = []


# # Región editable por el usuario
# def move(n, source, auxiliary, target):
#     if n <= 0:
#         return
# # Región editable por el usuario

#         # move n - 1 disks from source to auxiliary, so they are out of the way
#         move(n - 1, source, target, auxiliary)

#         # move the nth disk from source to target
#         target.append(source.pop())

#         # display our progress
#         print(A, B, C, "\n")

#         # move the n - 1 disks that we left on auxiliary onto target
#         move(n - 1, auxiliary, source, target)


# # initiate call from source A to target C with auxiliary B
# move(NUMBER_OF_DISKS, A, B, C)

# ----Salida esperada----
# []


# ===========================================

# Paso 55

# Región editable por el usuario
NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []


def move(n, source, auxiliary, target):
    if n <= 0:
        return
    # move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)

    # move the nth disk from source to target
    target.append(source.pop())

    # display our progress
    print(A, B, C, "\n")

    # move the n - 1 disks that we left on auxiliary onto target
    move(n - 1, auxiliary, source, target)


# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)
# Región editable por el usuario

# ----Salida esperada----
# [5, 4, 3, 2] [] [1]

# [5, 4, 3] [2] [1]

# [5, 4, 3] [2, 1] []

# [5, 4] [2, 1] [3]

# [5, 4, 1] [2] [3]

# [5, 4, 1] [] [3, 2]

# [5, 4] [] [3, 2, 1]

# [5] [4] [3, 2, 1]

# [5] [4, 1] [3, 2]

# [5, 2] [4, 1] [3]

# [5, 2, 1] [4] [3]

# [5, 2, 1] [4, 3] []

# [5, 2] [4, 3] [1]

# [5] [4, 3, 2] [1]

# [5] [4, 3, 2, 1] []

# [] [4, 3, 2, 1] [5]

# [1] [4, 3, 2] [5]

# [1] [4, 3] [5, 2]

# [] [4, 3] [5, 2, 1]

# [3] [4] [5, 2, 1]

# [3] [4, 1] [5, 2]

# [3, 2] [4, 1] [5]

# [3, 2, 1] [4] [5]

# [3, 2, 1] [] [5, 4]

# [3, 2] [] [5, 4, 1]

# [3] [2] [5, 4, 1]

# [3] [2, 1] [5, 4]

# [] [2, 1] [5, 4, 3]

# [1] [2] [5, 4, 3]

# [1] [] [5, 4, 3, 2]

# [] [] [5, 4, 3, 2, 1]


# ===========================================
