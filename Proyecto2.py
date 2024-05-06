import json
import networkx as nx
import geopandas as gpd

# Read GeoJSON file
print('Empezo a leer el archivo')
gdf = gpd.read_file('MallaBogota.geojson')
print('Termino de leer el archivo')
# Display the GeoDataFrame


# Initialize a networkx graph
G = nx.Graph()

for index, row in gdf.iterrows():
    # Extract node attributes from GeoDataFrame columns
    node_attributes = {key: row[key] for key in row.keys() if key != 'geometry'}
    
    # Extract geometry from the row
    geometry = row['geometry']
    
    # Check the geometry type
    if geometry.geom_type == 'Point':
        # For point geometries, add a node to the graph
        G.add_node(index, **node_attributes)
    elif geometry.geom_type == 'LineString':
        # For LineString geometries, add edges to the graph
        nodes = list(geometry.coords)
        for i in range(len(nodes) - 1):
            G.add_edge(nodes[i], nodes[i+1], **node_attributes)
    elif geometry.geom_type == 'MultiLineString':
        # For MultiLineString geometries, iterate over each LineString
        for line in geometry:
            nodes = list(line.coords)
            for i in range(len(nodes) - 1):
                G.add_edge(nodes[i], nodes[i+1], **node_attributes)

# Now you have a networkx graph `G` representing the spatial data from the GeoDataFrame