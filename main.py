import networkx as nx
import json
import matplotlib.pyplot as plt
from animation import animation

with open('data/sw.json', 'r') as file:
    data = json.load(file)

G = nx.Graph()
names = []

for node in data['nodes']:
    names.append(node['name'])

for link in data['links']:
    G.add_edge(names[link['source']], names[link['target']], weight=link['value'])

d = dict(G.degree)
pos = nx.spring_layout(G, k=1.8, seed=63260)  # seed=63260
leader = max(d, key=d.get)
colormap = ['tab:blue' if node == leader else 'tab:red' for node in G]

nx.draw_networkx(
    G,
    with_labels=True,
    pos=pos,
    node_size=[v * 35 for v in d.values()],
    node_color=colormap,
    edge_color='tab:gray',
    font_color='black',
    font_size=13,
    alpha=0.85
)
plt.tight_layout()

# 1 average length of shortest path - average number of characters connecting two characters
print(f'Average length of shortest path: {nx.average_shortest_path_length(G)}')

# 2 network density - the percentage of relationships between all characters
print(f'Network density: {nx.density(G)}')

# 3 network diameter - the two characters farthest apart
print(f'Network diameter: {nx.diameter(G)}')

# 4 degree information - the most known and the most isolated character
degrees = sorted(G.degree, key=lambda x: x[1], reverse=True)
print(f'The vertex with the highest degree: {degrees[0]}')
print(f'The vertex with the lowest degree: {degrees[-1]}')

# 5 maximal clique - a cluster of tightly related characters
cliques = nx.find_cliques(G)
max_clq = [clq for clq in cliques if len(clq) >= 9]
print(f'Maximal clique: {max_clq}')

# 6 max % of shortest paths for a character
most_shortest_paths = max(nx.load_centrality(G), key=nx.load_centrality(G).get)
print(f'The character that has the highest % of shortest paths: '
      f'{most_shortest_paths} {round(nx.load_centrality(G)[most_shortest_paths], 3) * 100}%')

# 7 max % of shortest paths for an edge (relationship)
most_shortest_paths_e = max(nx.edge_betweenness_centrality(G), key=nx.edge_betweenness_centrality(G).get)
print(f'The relationship between two characters that has the highest % of shortest paths: '
      f'{most_shortest_paths_e} {round(nx.edge_betweenness_centrality(G)[most_shortest_paths_e], 3) * 100}%')

# plt.show()
animation()
