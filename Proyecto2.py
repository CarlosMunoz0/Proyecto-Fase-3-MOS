import json
import networkx as nx

# Cargar datos GeoJSON
with open('MallaBogota.geojson') as f:
    datos_geojson = json.load(f)

# Crear un grafo geográfico
G = nx.Graph()

# Iterar sobre cada característica (Feature) en los datos GeoJSON
for feature in datos_geojson['features']:
    # Obtener los atributos de la característica
    props = feature['properties']
    
    # Obtener la geometría (LineString)
    coords = feature['geometry']['coordinates']
    
    # Agregar los nodos (puntos de inicio y fin de la línea)
    inicio = tuple(coords[0])
    fin = tuple(coords[-1])
    G.add_node(inicio, **props)
    G.add_node(fin, **props)
    
    # Agregar la arista (línea) entre los nodos
    G.add_edge(inicio, fin, object=feature)