from grafo import Graph

# Crear el grafo no dirigido con personajes de Star Wars
grafo = Graph(dirigido=False)

# a) Insertar vertices con nombres de personajes
personajes = [
    "Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO", "Leia",
    "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"
]

# Insertar vertices para cada personaje
for personaje in personajes:
    grafo.insert_vertice(personaje)

# Añadir aristas con el número de episodios compartidos entre personajes
# Representan las relaciones entre personajes y la cantidad de episodios en los que aparecieron juntos
grafo.insert_arista("Luke Skywalker", "Darth Vader", 3)
grafo.insert_arista("Luke Skywalker", "Leia", 5)
grafo.insert_arista("Luke Skywalker", "Yoda", 2)
grafo.insert_arista("Darth Vader", "Yoda", 1)
grafo.insert_arista("Leia", "Han Solo", 4)
grafo.insert_arista("Leia", "Chewbacca", 4)
grafo.insert_arista("Leia", "C-3PO", 4)
grafo.insert_arista("Chewbacca", "Han Solo", 6)
grafo.insert_arista("Rey", "Kylo Ren", 3)
grafo.insert_arista("R2-D2", "C-3PO", 7)
grafo.insert_arista("Luke Skywalker", "Han Solo", 2)
grafo.insert_arista("BB-8", "Rey", 2)

# a) Mostrar el grafo completo para verificar su estructura
print("Punto a) Grafo inicial con personajes de Star Wars:")
grafo.show_graph()

# b) Hallar el arbol de expansion minimo y determinar si contiene a Yoda
arbol_minimo = grafo.kruskal("Luke Skywalker")

# Verificar si el arbol de expansion minimo contiene a "Yoda"
contiene_yoda = any("Yoda" in arbol for arbol in arbol_minimo)
print()
if contiene_yoda:
    print("b) El arbol de expansion minimo SI contiene a Yoda")
else:
    print("b) El arbol de expansion minimo NO contiene a Yoda")
print("Arbol de expansion minimo:", arbol_minimo)

# c) Determinar el numero maximo de episodios que comparten dos personajes
max_episodios = 0
personajes_max_episodios = ("", "")

for nodo in grafo.elements:
    for arista in nodo['aristas']:
        if arista['peso'] > max_episodios:
            max_episodios = arista['peso']
            personajes_max_episodios = (nodo['value'], arista['value'])

print()
print(f"c) Los personajes que comparten el maximo de episodios son {personajes_max_episodios[0]} y {personajes_max_episodios[1]} con {max_episodios} episodios.")
