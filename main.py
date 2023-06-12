import networkx as nx
import random
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

import sys
import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, source):
    distances = {node: sys.maxsize for node in graph}
    distances[source] = 0
    queue = [(0, source)]
    previous = {}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous

# Création du graphe
G = nx.Graph()

# Ajout des sommets au graphe
num_sommets = 10
G.add_nodes_from(range(num_sommets))

# Ajout des arêtes pondérées
for i in range(num_sommets):
    for j in range(i + 1, num_sommets):
        poids = random.randint(1, 100)  # Génération d'un poids aléatoire entre 1 et 100
        G.add_edge(i, j, weight=poids)

# Affichage du graphe
pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')

nx.draw(G, pos, with_labels=True, node_size=100, font_size=8)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Exécution de l'algorithme de Dijkstra
source_node = 0
distances, previous = dijkstra(G, source_node)

# Récupération du plus court chemin vers un nœud cible (ici, le nœud 9)
target_node = 9
shortest_path = [target_node]
while target_node in previous:
    target_node = previous[target_node]
    shortest_path.insert(0, target_node)

# Affichage du plus court chemin en rouge
edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2.0)

plt.show()
