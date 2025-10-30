"""Aprenda a diseñar con un algoritmo de ruta corta."""

# Paso 1
# copper = {}
# ----Salida esperada----

# ===========================================

# Paso 2
# copper = {"species": "guinea pig"}
# ----Salida esperada----

# ===========================================

# Paso 3
# copper = {
#     "species": "guinea pig",
#     "age": 2
# }
# ----Salida esperada----

# ===========================================

# Paso 4
# copper = {
#     "species": "guinea pig",
#     "age": 2
# }

# print(copper["species"])
# ----Salida esperada----
# guinea pig

# ===========================================

# Paso 5
# copper = {
#     "species": "guinea pig",
#     "age": 2
# }

# print(copper["age"])
# ----Salida esperada----
# 2

# ===========================================

# Paso 6
# copper = {
#     "species": "guinea pig",
#     "age": 2
# }

# copper["food"] = "hay"
# ----Salida esperada----

# ===========================================

# Paso 7
# copper = {
#     "species": "guinea pig",
#     "age": 2
# }
# copper["food"] = "hay"

# print(copper)
# ----Salida esperada----
# {"species": "guinea pig", "age": 2, "food": "hay"}

# ===========================================

# Paso 8
# copper = {
#     "species": "guinea pig",
#     "age": 2
# }
# copper["food"] = "hay"
# copper["species"] = "Cavia porcellus"

# print(copper)
# ----Salida esperada----
# {'species': 'Cavia porcellus', 'age': 2, 'food': 'hay'}

# ===========================================

# Paso 9
# copper = {
#     "species": "guinea pig",
#     "age": 2
# }
# copper["food"] = "hay"
# copper["species"] = "Cavia porcellus"

# for i in copper:
#     print(i)
# ----Salida esperada----
# species
# age
# food

# ===========================================

# Paso 10

# Región editable por el usuario
# copper = {
#     "species": "guinea pig",
#     "age": 2
# }
# copper["food"] = "hay"
# copper["species"] = "Cavia porcellus"

# for i in copper.values():
#     print(i)
# Región editable por el usuario

# ----Salida esperada----
# Cavia porcellus
# 2
# hay

# ===========================================

# Paso 11

# Región editable por el usuario
# copper = {
#     "species": "guinea pig",
#     "age": 2
# }
# copper["food"] = "hay"
# copper["species"] = "Cavia porcellus"

# for i in copper.items():
#     print(i)
# Región editable por el usuario

# ----Salida esperada----
# ("species", "Cavia porcellus")
# ("age", 2)
# ("food", "hay")

# ===========================================

# Paso 12

# Región editable por el usuario
# copper = {
#     "species": "guinea pig",
#     "age": 2
# }
# copper["food"] = "hay"
# copper["species"] = "Cavia porcellus"

# for i, j in copper.items():
#     print(i, j)
# Región editable por el usuario

# ----Salida esperada----
# species Cavia porcellus
# age 2
# food hay

# ===========================================

# Paso 13

# Región editable por el usuario
# copper = {"species": "guinea pig", "age": 2}
# copper["food"] = "hay"
# copper["species"] = "Cavia porcellus"

# del copper["age"]

# for i, j in copper.items():
#     print(i, j)
# Región editable por el usuario

# ----Salida esperada----
# species Cavia porcellus
# food hay

# ===========================================

# Paso 14

# copper = {"species": "guinea pig", "age": 2}
# Región editable por el usuario

# Región editable por el usuario

# ----Salida esperada----

# ===========================================

# Paso 15

# Región editable por el usuario
# my_graph = {"species": "guinea pig", "age": 2}
# Región editable por el usuario

# ----Salida esperada----

# ===========================================

# Paso 16

# Región editable por el usuario
# my_graph = {
#     "A": "B",
#     "age": 2
# }
# Región editable por el usuario

# ----Salida esperada----

# ===========================================

# Paso 17

# Región editable por el usuario
# my_graph = {
#     "A": "B",
#     "B": "A"
# }
# Región editable por el usuario

# ----Salida esperada----

# ===========================================

# Paso 18

# Región editable por el usuario
# my_graph = {
#     "A": "B",
#     "B": ["A", "C"],
#     "C": "B"
# }
# Región editable por el usuario

# ----Salida esperada----

# ===========================================

# Paso 19

# Región editable por el usuario
# my_graph = {
#     "A": ["B", "D"],
#     "B": ["A", "C"],
#     "C": ["B", "D"],
#     "D": ["A", "C"]
# }
# Región editable por el usuario

# ----Salida esperada----

# ===========================================

# Paso 20

# my_graph = {
# # Región editable por el usuario
#     "A": [("B", 3), ("D", 1)],
# # Región editable por el usuario
#     "B": ["A", "C"],
#     "C": ["B", "D"],
#     "D": ["A", "C"],
# }

# ----Salida esperada----

# ===========================================

# Paso 21

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
# # Región editable por el usuario
#     "B": [("A", 3), ("C", 4)],
# # Región editable por el usuario
#     "C": ["B", "D"],
#     "D": ["A", "C"],
# }

# ----Salida esperada----

# ===========================================

# Paso 22

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     # Región editable por el usuario
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)]
#     # Región editable por el usuario
# }

# ----Salida esperada----

# ===========================================

# Paso 23

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }

# Región editable por el usuario
# def shortest_path():
#     pass
# Región editable por el usuario

# ----Salida esperada----

# ===========================================

# Paso 24

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }

# Región editable por el usuario
# def shortest_path(graph, start):
#     pass
# Región editable por el usuario

# ----Salida esperada----

# ===========================================

# Paso 25

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }

# Región editable por el usuario
# def shortest_path(graph, start):
#     unvisited = []
# Región editable por el usuario

# ----Salida esperada----

# ===========================================

# Paso 26

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }

# Región editable por el usuario
# def shortest_path(graph, start):
#     unvisited = []
#     for node in graph:
#         unvisited.append(node)
# Región editable por el usuario

# ----Salida esperada----

# ===========================================

# Paso 27

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }

# Región editable por el usuario
# def shortest_path(graph, start):
#     distances = {}
#     unvisited = []
#     for node in graph:
#         unvisited.append(node)
# Región editable por el usuario

# ----Salida esperada----

# ===========================================

# Paso 28

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }

# Región editable por el usuario
# def shortest_path(graph, start):
#     distances = {}
#     unvisited = []
#     for node in graph:
#         unvisited.append(node)
#         if node == start:
#             distances[node] = 0
# Región editable por el usuario

# ----Salida esperada----

# ===========================================

# Paso 29

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }

# Región editable por el usuario
# def shortest_path(graph, start):
#     distances = {}
#     unvisited = []
#     for node in graph:
#         unvisited.append(node)
#         if node == start:
#             distances[node] = 0
#         else:
#             distances[node] = float("inf")
# Región editable por el usuario

# ----Salida esperada----

# ===========================================

# Paso 30

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }

# Región editable por el usuario
# def shortest_path(graph, start):
#     distances = {}
#     unvisited = []
#     for node in graph:
#         unvisited.append(node)
#         if node == start:
#             distances[node] = 0
#         else:
#             distances[node] = float("inf")
#     print(f"Unvisited: {unvisited}\nDistances: {distances}")
# Región editable por el usuario

# ----Salida esperada----

# ===========================================

# Paso 31

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }

# Región editable por el usuario
# def shortest_path(graph, start):
#     distances = {}
#     unvisited = []
#     for node in graph:
#         unvisited.append(node)
#         if node == start:
#             distances[node] = 0
#         else:
#             distances[node] = float("inf")
#     print(f"Unvisited: {unvisited}\nDistances: {distances}")

# shortest_path(my_graph, "A")

# Región editable por el usuario

# ----Salida esperada----
# Unvisited: ["A", "B", "C", "D"]
# Distances: {"A": 0, "B": inf, "C": inf, "D": inf}

# ===========================================

# Paso 32

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }

# Región editable por el usuario----
# def shortest_path(graph, start):
#     distances = {}
#     unvisited = []

#     print(f"Unvisited: {unvisited}\nDistances: {distances}")

# shortest_path(my_graph, "A")

# Región editable por el usuario----

# ----Salida esperada----
# Unvisited: ["A", "B", "C", "D"]
# Distances: {"A": 0, "B": inf, "C": inf, "D": inf}

# ===========================================

# Paso 33

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }

# Región editable por el usuario----
# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {}

#     print(f"Unvisited: {unvisited}\nDistances: {distances}")

# shortest_path(my_graph, "A")

# Región editable por el usuario----

# ----Salida esperada----
# Unvisited: ["A", "B", "C", "D"]
# Distances: {}

# ===========================================

# Paso 34

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }

# Región editable por el usuario----
# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {}
#     paths = {key: [] for key in graph}

#     print(f"Unvisited: {unvisited}\nDistances: {distances}")

# shortest_path(my_graph, "A")
# Región editable por el usuario----

# ----Salida esperada----
# Unvisited: ["A", "B", "C", "D"]
# Distances: {}

# ===========================================

# Paso 35

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }

# Región editable por el usuario----
# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {
#         node: 0 if node == start else float('inf')
#         for node in graph
#     }
#     paths = {key: [] for key in graph}

#     print(f"Unvisited: {unvisited}\nDistances: {distances}")

# shortest_path(my_graph, "A")
# Región editable por el usuario----

# ----Salida esperada----
# Unvisited: ["A", "B", "C", "D"]
# Distances: {"A": 0, "B": inf, "C": inf, "D": inf}

# ===========================================

# Paso 36

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }

# Región editable por el usuario----
# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {
#         node: 0 if node == start else float('inf')
#         for node in graph
#     }
#     paths = {key: [] for key in graph}
#     paths[start].append(start)

#     print(f"Unvisited: {unvisited}\nDistances: {distances}")

# shortest_path(my_graph, "A")
# Región editable por el usuario----

# ----Salida esperada----
# Unvisited: ["A", "B", "C", "D"]
# Distances: {"A": 0, "B": inf, "C": inf, "D": inf}

# ===========================================

# Paso 37

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }

# Región editable por el usuario----
# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {
#         node: 0 if node == start else float('inf')
#         for node in graph
#     }
#     paths = {key: [] for key in graph}
#     paths[start].append(start)

#     print(f"Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}")

# shortest_path(my_graph, "A")
# Región editable por el usuario----

# # ----Salida esperada----
# Unvisited: ["A", "B", "C", "D"]
# Distances: {"A": 0, "B": inf, "C": inf, "D": inf}
# Paths: {"A": ["A"], "B": [], "C": [], "D": []}

# ===========================================

# Paso 38

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }


# Región editable por el usuario----
# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {
#         node: 0 if node == start else float('inf')
#         for node in graph
#     }
#     paths = {key: [] for key in graph}
#     paths[start].append(start)

#     print(f"Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}")

# # shortest_path(my_graph, "A")
# Región editable por el usuario----

# # ----Salida esperada----

# ===========================================

# Paso 39

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }

# Región editable por el usuario----
# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {
#         node: 0 if node == start else float('inf')
#         for node in graph
#     }
#     paths = {key: [] for key in graph}
#     paths[start].append(start)
#     while unvisited:
#         pass

#     print(f"Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}")
# Región editable por el usuario----
# shortest_path(my_graph, "A")

# # ----Salida esperada----

# ===========================================

# Paso 40

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }


# Región editable por el usuario----
# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {
#         node: 0 if node == start else float('inf')
#         for node in graph
#     }
#     paths = {key: [] for key in graph}
#     paths[start].append(start)
#     while unvisited:
#         current = min(unvisited)

#     print(f"Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}")
# Región editable por el usuario----

# shortest_path(my_graph, "A")

# # ----Salida esperada----

# ===========================================

# Paso 41

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }

# Región editable por el usuario----
# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {node: 0 if node == start else float("inf") for node in graph}
#     paths = {key: [] for key in graph}
#     paths[start].append(start)
#     while unvisited:
#         current = min(unvisited, key=distances.get)

#     print(f"Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}")
# Región editable por el usuario----

# shortest_path(my_graph, "A")

# # ----Salida esperada----

# ===========================================

# Paso 42

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }

# Región editable por el usuario----
# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {node: 0 if node == start else float("inf") for node in graph}
#     paths = {key: [] for key in graph}
#     paths[start].append(start)
#     while unvisited:
#         current = min(unvisited, key=distances.get)
#         for node, distance in graph[current]:
#             pass

#     print(f"Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}")
# Región editable por el usuario----

# shortest_path(my_graph, "A")

# # ----Salida esperada----

# ===========================================

# Paso 43

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }


# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {node: 0 if node == start else float("inf") for node in graph}
#     paths = {node: [] for node in graph}
#     paths[start].append(start)
#     while unvisited:
#         current = min(unvisited, key=distances.get)
# # Región editable por el usuario----
#         for node, distance in graph[current]:
#             if distance + distances[current] < distances[node]:
#                 pass
# Región editable por el usuario----

# print(f"Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}")

# shortest_path(my_graph, "A")

# # ----Salida esperada----

# ===========================================---

# Paso 44

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }


# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {node: 0 if node == start else float("inf") for node in graph}
#     paths = {node: [] for node in graph}
#     paths[start].append(start)
#     while unvisited:
#         current = min(unvisited, key=distances.get)
#         # Región editable por el usuario----
#         for node, distance in graph[current]:
#             if distance + distances[current] < distances[node]:
#                 distances[node] = distance + distances[current]
#     # Región editable por el usuario----

#     print(f"Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}")

# shortest_path(my_graph, "A")

# # ----Salida esperada----

# ===========================================

# Paso 45

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }


# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {node: 0 if node == start else float("inf") for node in graph}
#     paths = {node: [] for node in graph}
#     paths[start].append(start)
#     while unvisited:
#         current = min(unvisited, key=distances.get)
#         # Región editable por el usuario----
#         for node, distance in graph[current]:
#             if distance + distances[current] < distances[node]:
#                 distances[node] = distance + distances[current]
#                 if paths[node][-1] == node:
#                     pass
#     # Región editable por el usuario----

#     print(f"Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}")

# shortest_path(my_graph, "A")

# # ----Salida esperada----

# ===========================================

# Paso 46

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }

# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {node: 0 if node == start else float("inf") for node in graph}
#     paths = {node: [] for node in graph}
#     paths[start].append(start)

#     while unvisited:
#         current = min(unvisited, key=distances.get)
#         # Región editable por el usuario----
#         for node, distance in graph[current]:
#             if distance + distances[current] < distances[node]:
#                 distances[node] = distance + distances[current]
#                 if paths[node][-1] == node:
#                     paths[node] = paths[current]
#     # Región editable por el usuario----

#     print(f"Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}")


# shortest_path(my_graph, "A")

# # ----Salida esperada----

# ===========================================

# Paso 47

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }


# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {node: 0 if node == start else float("inf") for node in graph}
#     paths = {node: [] for node in graph}
#     paths[start].append(start)

#     while unvisited:
#         current = min(unvisited, key=distances.get)
#         for node, distance in graph[current]:
#             if distance + distances[current] < distances[node]:
#                 distances[node] = distance + distances[current]
#                 # Región editable por el usuario----
#                 if paths[node][-1] == node:
#                     paths[node] = paths[current]
#                 else:
#                     paths[node].extend(paths[current])
#     # Región editable por el usuario----

#     print(f"Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}")


# shortest_path(my_graph, "A")

# # ----Salida esperada----

# ===========================================

# Paso 48

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }


# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {node: 0 if node == start else float("inf") for node in graph}
#     paths = {node: [] for node in graph}
#     paths[start].append(start)

#     # Región editable por el usuario----
#     while unvisited:
#         current = min(unvisited, key=distances.get)
#         for node, distance in graph[current]:
#             if distance + distances[current] < distances[node]:
#                 distances[node] = distance + distances[current]
#                 if paths[node][-1] == node:
#                     paths[node] = paths[current]
#                 else:
#                     paths[node].extend(paths[current])
#                 paths[node].append(node)
#     # Región editable por el usuario----

#     print(f"Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}")


# shortest_path(my_graph, "A")

# # ----Salida esperada----

# ===========================================

# Paso 49

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }


# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {node: 0 if node == start else float("inf") for node in graph}
#     paths = {node: [] for node in graph}
#     paths[start].append(start)

#     # Región editable por el usuario----
#     while unvisited:
#         current = min(unvisited, key=distances.get)
#         for node, distance in graph[current]:
#             if distance + distances[current] < distances[node]:
#                 distances[node] = distance + distances[current]
#                 if paths[node][-1] == node:
#                     paths[node] = paths[current]
#                 else:
#                     paths[node].extend(paths[current])
#                 paths[node].append(node)
#         unvisited.remove(current)
#     # Región editable por el usuario----

#     print(f"Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}")


# shortest_path(my_graph, "A")

# # ----Salida esperada----

# ===========================================

# Paso 50

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }


# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {node: 0 if node == start else float("inf") for node in graph}
#     paths = {node: [] for node in graph}
#     paths[start].append(start)

#     while unvisited:
#         current = min(unvisited, key=distances.get)
#         for node, distance in graph[current]:
#             if distance + distances[current] < distances[node]:
#                 distances[node] = distance + distances[current]
#                 # Región editable por el usuario----
#                 if paths[node] and paths[node][-1] == node:
#                     paths[node] = paths[current]
#                 # Región editable por el usuario----
#                 else:
#                     paths[node].extend(paths[current])
#                 paths[node].append(node)
#         unvisited.remove(current)

#     print(f"Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}")


# shortest_path(my_graph, "A")

# # ----Salida esperada----

# ===========================================

# Paso 51

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }


# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {node: 0 if node == start else float("inf") for node in graph}
#     paths = {node: [] for node in graph}
#     paths[start].append(start)

#     while unvisited:
#         current = min(unvisited, key=distances.get)
#         for node, distance in graph[current]:
#             if distance + distances[current] < distances[node]:
#                 distances[node] = distance + distances[current]
#                 # Región editable por el usuario----
#                 if paths[node] and paths[node][-1] == node:
#                     paths[node] = paths[current]
#                 # Región editable por el usuario----
#                 else:
#                     paths[node].extend(paths[current])
#                 paths[node].append(node)
#         unvisited.remove(current)

#     print(f"Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}")


# shortest_path(my_graph, "A")

# # ----Salida esperada----
# Unvisited: []
# Distances: {"A": 0, "B": 3, "C": 7, "D": 1}
# Paths: {"A": ["A"], "B": ["A", "B", "C"], "C": ["A", "B", "C"], "D": ["A", "D"]}

# ===========================================

# Paso 52

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }


# def shortest_path(graph, start):
#     unvisited = list(graph)
#     distances = {node: 0 if node == start else float("inf") for node in graph}
#     paths = {node: [] for node in graph}
#     paths[start].append(start)

#     while unvisited:
#         current = min(unvisited, key=distances.get)
#         for node, distance in graph[current]:
#             if distance + distances[current] < distances[node]:
#                 distances[node] = distance + distances[current]
#                 # Región editable por el usuario----
#                 if paths[node] and paths[node][-1] == node:
#                     paths[node] = paths[current][:]
#                 # Región editable por el usuario----
#                 else:
#                     paths[node].extend(paths[current])
#                 paths[node].append(node)
#         unvisited.remove(current)

#     print(f"Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}")


# shortest_path(my_graph, "A")

# # ----Salida esperada----
# Unvisited: []
# Distances: {"A": 0, "B": 3, "C": 7, "D": 1}
# Paths: {"A": ["A"], "B": ["A", "B", "C"], "C": ["A", "B", "C"], "D": ["A", "D"]}

# ===========================================

# Paso 53

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }


# def shortest_path(graph, start, target=""):
#     unvisited = list(graph)
#     distances = {node: 0 if node == start else float("inf") for node in graph}
#     paths = {node: [] for node in graph}
#     paths[start].append(start)

#     while unvisited:
#         current = min(unvisited, key=distances.get)
#         for node, distance in graph[current]:
#             if distance + distances[current] < distances[node]:
#                 distances[node] = distance + distances[current]
#                 # Región editable por el usuario----
#                 if paths[node] and paths[node][-1] == node:
#                     paths[node] = paths[current][:]
#                 # Región editable por el usuario----
#                 else:
#                     paths[node].extend(paths[current])
#                 paths[node].append(node)
#         unvisited.remove(current)

#     print(f"Unvisited: {unvisited}\nDistances: {distances}\nPaths: {paths}")


# shortest_path(my_graph, "A")

# # ----Salida esperada----
# Unvisited: []
# Distances: {"A": 0, "B": 3, "C": 7, "D": 1}
# Paths: {"A": ["A"], "B": ["A", "B", "C"], "C": ["A", "B", "C"], "D": ["A", "D"]}

# ===========================================

# Paso 54

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }


# def shortest_path(graph, start, target=""):
#     unvisited = list(graph)
#     distances = {node: 0 if node == start else float("inf") for node in graph}
#     paths = {node: [] for node in graph}
#     paths[start].append(start)

#     while unvisited:
#         current = min(unvisited, key=distances.get)
#         for node, distance in graph[current]:
#             if distance + distances[current] < distances[node]:
#                 distances[node] = distance + distances[current]
#                 if paths[node] and paths[node][-1] == node:
#                     paths[node] = paths[current][:]
#                 else:
#                     paths[node].extend(paths[current])
#                 paths[node].append(node)
#         unvisited.remove(current)

#     # Región editable por el usuario----
#     targets_to_print = [target] if target else graph


# shortest_path(my_graph, "A")
# Región editable por el usuario---

# # ----Salida esperada----

# ===========================================

# Paso 55

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }


# def shortest_path(graph, start, target=""):
#     unvisited = list(graph)
#     distances = {node: 0 if node == start else float("inf") for node in graph}
#     paths = {node: [] for node in graph}
#     paths[start].append(start)

#     while unvisited:
#         current = min(unvisited, key=distances.get)
#         for node, distance in graph[current]:
#             if distance + distances[current] < distances[node]:
#                 distances[node] = distance + distances[current]
#                 if paths[node] and paths[node][-1] == node:
#                     paths[node] = paths[current][:]
#                 else:
#                     paths[node].extend(paths[current])
#                 paths[node].append(node)
#         unvisited.remove(current)

#     # Región editable por el usuario----
#     targets_to_print = [target] if target else graph
#     for node in targets_to_print:
#         print(
#             f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}'
#         )


# shortest_path(my_graph, "A")
# Región editable por el usuario---

# # ----Salida esperada----
# A-A distance: 0
# Path: A

# A-B distance: 3
# Path: A -> B

# A-C distance: 7
# Path: A -> B -> C

# A-D distance: 1
# Path: A -> D

# ===========================================

# Paso 56

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }


# def shortest_path(graph, start, target=""):
#     unvisited = list(graph)
#     distances = {node: 0 if node == start else float("inf") for node in graph}
#     paths = {node: [] for node in graph}
#     paths[start].append(start)

#     while unvisited:
#         current = min(unvisited, key=distances.get)
#         for node, distance in graph[current]:
#             if distance + distances[current] < distances[node]:
#                 distances[node] = distance + distances[current]
#                 if paths[node] and paths[node][-1] == node:
#                     paths[node] = paths[current][:]
#                 else:
#                     paths[node].extend(paths[current])
#                 paths[node].append(node)
#         unvisited.remove(current)

#     # Región editable por el usuario----
#     targets_to_print = [target] if target else graph
#     for node in targets_to_print:
#         if node==start:
#             continue
#         print(
#             f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}'
#         )


# shortest_path(my_graph, "A")
# Región editable por el usuario---

# # ----Salida esperada----
# A-B distance: 3
# Path: A -> B

# A-C distance: 7
# Path: A -> B -> C

# A-D distance: 1
# Path: A -> D

# ===========================================

# Paso 57

# my_graph = {
#     "A": [("B", 3), ("D", 1)],
#     "B": [("A", 3), ("C", 4)],
#     "C": [("B", 4), ("D", 7)],
#     "D": [("A", 1), ("C", 7)],
# }


# def shortest_path(graph, start, target=""):
#     unvisited = list(graph)
#     distances = {node: 0 if node == start else float("inf") for node in graph}
#     paths = {node: [] for node in graph}
#     paths[start].append(start)

#     while unvisited:
#         current = min(unvisited, key=distances.get)
#         for node, distance in graph[current]:
#             if distance + distances[current] < distances[node]:
#                 distances[node] = distance + distances[current]
#                 if paths[node] and paths[node][-1] == node:
#                     paths[node] = paths[current][:]
#                 else:
#                     paths[node].extend(paths[current])
#                 paths[node].append(node)
#         unvisited.remove(current)

#     # Región editable por el usuario----
#     targets_to_print = [target] if target else graph
#     for node in targets_to_print:
#         if node==start:
#             continue
#         print(
#             f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}'
#         )
#     return distances, paths


# shortest_path(my_graph, "A")
# Región editable por el usuario---

# # ----Salida esperada----
# A-B distance: 3
# Path: A -> B

# A-C distance: 7
# Path: A -> B -> C

# A-D distance: 1
# Path: A -> D

# ===========================================

# Paso 58

# my_graph = {
#     "A": [("B", 5), ("C", 3), ("E", 11)],
#     "B": [("A", 5), ("C", 1), ("F", 2)],
#     "C": [("A", 3), ("B", 1), ("D", 1), ("E", 5)],
#     "D": [("C", 1), ("E", 9), ("F", 3)],
#     "E": [("A", 11), ("C", 5), ("D", 9)],
#     "F": [("B", 2), ("D", 3)],
# }


# def shortest_path(graph, start, target=""):
#     unvisited = list(graph)
#     distances = {node: 0 if node == start else float("inf") for node in graph}
#     paths = {node: [] for node in graph}
#     paths[start].append(start)

#     while unvisited:
#         current = min(unvisited, key=distances.get)
#         for node, distance in graph[current]:
#             if distance + distances[current] < distances[node]:
#                 distances[node] = distance + distances[current]
#                 if paths[node] and paths[node][-1] == node:
#                     paths[node] = paths[current][:]
#                 else:
#                     paths[node].extend(paths[current])
#                 paths[node].append(node)
#         unvisited.remove(current)

#     # Región editable por el usuario----
#     targets_to_print = [target] if target else graph
#     for node in targets_to_print:
#         if node == start:
#             continue
#         print(
#             f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}'
#         )
#     return distances, paths


# shortest_path(my_graph, "A")
# Región editable por el usuario---

# # ----Salida esperada----
# A-B distance: 4
# Path: A -> C -> B

# A-C distance: 3
# Path: A -> C

# A-D distance: 4
# Path: A -> C -> D

# A-E distance: 8
# Path: A -> C -> E

# A-F distance: 6
# Path: A -> C -> B -> F

# ===========================================

# Paso 59

my_graph = {
    "A": [("B", 5), ("C", 3), ("E", 11)],
    "B": [("A", 5), ("C", 1), ("F", 2)],
    "C": [("A", 3), ("B", 1), ("D", 1), ("E", 5)],
    "D": [("C", 1), ("E", 9), ("F", 3)],
    "E": [("A", 11), ("C", 5), ("D", 9)],
    "F": [("B", 2), ("D", 3)],
}


def shortest_path(graph, start, target=""):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float("inf") for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)

    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)

    # Región editable por el usuario----
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(
            f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}'
        )
    return distances, paths


shortest_path(my_graph, "A", "F")
# Región editable por el usuario---

# # ----Salida esperada----
# A-F distance: 6
# Path: A -> C -> B -> F

# ===========================================
