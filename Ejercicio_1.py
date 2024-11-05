from arbol_avl import BinaryTree

# Cargar datos de Pokemon (ejemplo).
pokemons = [
    {"nombre": "Bulbasaur", "numero": 1, "tipos": ["Planta", "Veneno"]},
    {"nombre": "Ivysaur", "numero": 2, "tipos": ["Planta", "Veneno"]},
    {"nombre": "Charmander", "numero": 4, "tipos": ["Fuego"]},
    {"nombre": "Squirtle", "numero": 7, "tipos": ["Agua"]},
    {"nombre": "Pikachu", "numero": 25, "tipos": ["Electrico"]},
    {"nombre": "Jolteon", "numero": 135, "tipos": ["Electrico"]},
    {"nombre": "Lycanroc", "numero": 745, "tipos": ["Roca"]},
    {"nombre": "Tyrantrum", "numero": 697, "tipos": ["Roca", "Dragón"]},
    {"nombre": "Steelix", "numero": 208, "tipos": ["Acero", "Tierra"]},
    {"nombre": "Scizor", "numero": 212, "tipos": ["Acero", "Bicho"]},
    # Agrega mas datos segun sea necesario.
]

# A)
# Crear los arboles AVL.
arbol_por_nombre = BinaryTree()
arbol_por_numero = BinaryTree()
arbol_por_tipo = {}

# Insertar datos en los arboles.
for pokemon in pokemons:
    # Insertar por nombre.
    arbol_por_nombre.insert_node(pokemon["nombre"].lower(), pokemon)
    
    # Insertar por numero.
    arbol_por_numero.insert_node(pokemon["numero"], pokemon)
    
    # Insertar por tipo.
    for tipo in pokemon["tipos"]:
        tipo = tipo.lower()
        if tipo not in arbol_por_tipo:
            arbol_por_tipo[tipo] = BinaryTree()
            arbol_por_tipo[tipo].other_value = {"pokemons": []}  # Inicializar contenedor para los Pokemon de este tipo
        arbol_por_tipo[tipo].insert_node(pokemon["nombre"].lower(), pokemon)
        arbol_por_tipo[tipo].other_value["pokemons"].append(pokemon)  # Guardar Pokemon en el arbol por tipo

# B)
print("PUNTO B")
# Busqueda exacta por numero
def buscar_por_numero(arbol, numero):
    resultado = arbol.search(numero)
    if resultado:
        return resultado.other_value
    else:
        return "Pokemon no encontrado"

# Busqueda por proximidad de nombre
def buscar_por_nombre_proximidad(arbol, nombre_parcial):
    print(f"\nResultados de busqueda por proximidad para '{nombre_parcial}':")
    arbol.proximity_search(nombre_parcial.lower())

# Ejemplo de uso en el punto B
numero_a_buscar = 25
print(f"\nBusqueda de Pokemon con numero {numero_a_buscar}:")
print(buscar_por_numero(arbol_por_numero, numero_a_buscar))

nombre_parcial = "bul"
buscar_por_nombre_proximidad(arbol_por_nombre, nombre_parcial)

# C)
print()
print("PUNTO C")
# Funcion para obtener y mostrar los nombres de Pokemon de un tipo especifico.
def mostrar_nom_tipo(arbol_tipo, tipo):
    if tipo in arbol_tipo:
        print(f"\nPokemon de tipo {tipo.capitalize()}:")
        arbol_tipo[tipo].inorden()  # Utiliza el metodo inorden para mostrar en orden los nombres.
    else:
        print(f"\nNo hay Pokemon de tipo {tipo.capitalize()}.")

# Ejemplo de uso en el punto C
mostrar_nom_tipo(arbol_por_tipo, "agua")
mostrar_nom_tipo(arbol_por_tipo, "fuego")
mostrar_nom_tipo(arbol_por_tipo, "planta")
mostrar_nom_tipo(arbol_por_tipo, "electrico")

# D)
print()
print("PUNTO D")
# Listado en orden ascendente por numero.
def listar_orden_numero(arbol):
    print("\nListado en orden ascendente por numero:")
    arbol.inorden()  # `inorden` muestra todos los Pokemon ordenados por numero

# Listado en orden ascendente por nombre.
def listar_orden_nombre(arbol):
    print("\nListado en orden ascendente por nombre:")
    arbol.inorden()  # `inorden` muestra todos los Pokemon ordenados por nombre

# Listado por nivel, agrupado por nombre.
def listar_nivel(arbol):
    print("\nListado de Pokemon por nivel:")
    arbol.by_level()  # `by_level` muestra los Pokemon agrupados por niveles

# ejecutar las funciones para el punto D
listar_orden_numero(arbol_por_numero)
listar_orden_nombre(arbol_por_nombre)
listar_nivel(arbol_por_nombre)

# E)
# Mostrar datos de algunos Pokemon
print()
print("PUNTO E")
print("\nDatos de los Pokemon Jolteon, Lycanroc y Tyrantrum:")
for nombre in ["Jolteon", "Lycanroc", "Tyrantrum"]:
    resultado = arbol_por_nombre.search(nombre.lower())
    if resultado:
        print(resultado.other_value)
    else:
        print(f"{nombre} no encontrado")

# F)
# Determinar cuantos Pokemon hay de tipo electrico y acero
print()
print("PUNTO F")
def count_pokemon_by_types(types):
    print()
    print(" Determinar la cantidad de Pokemon de tipo electrico y acero")
    for pokemon_type in types:
        type_node = arbol_por_tipo.get(pokemon_type)  # Busca el arbol correspondiente al tipo
        count = len(type_node.other_value["pokemons"]) if type_node else 0  # Cuenta los Pokemon en el tipo
        print(f"Cantidad de Pokemons de tipo {pokemon_type}: {count}")

# Ejemplo de uso para f)
count_pokemon_by_types(["electrico", "acero"])
