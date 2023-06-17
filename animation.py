import networkx as nx
import matplotlib.pyplot as plt
from data import main, character_die


def animation():
    plt.ion()
    plt.tight_layout()
    G = nx.Graph()
    names, edges = main()
    for i in range(len(names)):
        character_die(G)
        G.add_node(names[i])
        for edge in edges:
            if G.has_node(edge[0]) is True and G.has_node(edge[1]) is True:
                G.add_edge(edge[0], edge[1], weight=edge[2])
        d = dict(G.degree)
        leader = max(d, key=d.get)
        colormap = ['tab:blue' if node == leader else 'tab:red' for node in G]
        try:
            last = nx.diameter(G)
            plt.title(f'Diameter: {nx.diameter(G)}')
        except nx.NetworkXError:
            plt.title(f'Diameter: {last}')
        nx.draw_networkx(
            G,
            with_labels=True,
            pos=nx.spring_layout(G, k=1.8, seed=63260),  # seed=63260,
            node_size=[v * 35 for v in d.values()],
            node_color=colormap,
            edge_color='tab:gray',
            font_color='black',
            font_size=13,
            alpha=0.85
        )
        if i == 110:
            plt.savefig(f'{"frames"}/frame_{str(i).zfill(5)}.png')
            plt.show(block=True)
        else:
            plt.savefig(f'{"frames"}/frame_{str(i).zfill(5)}.png')
            plt.show(block=False)
            plt.pause(0.3)
            plt.clf()
