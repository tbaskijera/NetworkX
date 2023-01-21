import networkx as nx
import random
import string
import numpy as np
from matplotlib import pyplot as plt
from docx import Document


nodes = []


def average_degree():
    values = []
    for node in G.degree:
        values.append(node[1])
    return sum(values) / len(G.degree)


def hub():
    values = []
    hubs = []
    for node in G.degree:
        values.append(node[1])
    for node in G.degree:
        if node[1] == max(values):
            hubs.append(node)
    return hubs


def draw():
    pos = nx.spring_layout(G)
    nx.draw(G, pos, font_size=16, with_labels=False)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    nx.draw_networkx_labels(G, pos)
    plt.show()


def remove_smaller_edges():
    small = [(a, b) for a, b, attrs in G.edges(
        data=True) if attrs["weight"] <= 50]
    G.remove_edges_from(small)


def write2txt():

    with open("NetworkX_Toni_Baskijera.txt", "w") as f:

        f.write('Broj čvorova, N: ' + str(len(G.nodes)) + '\n')
        f.write('Broj veza, K, N: ' + str(len(G.edges())) + '\n')
        f.write('Prosječni stupanj, <k>: ' + str(average_degree()) + '\n')
        f.write('Gustoća mreže, d: ' + str(nx.density(G)) + '\n')
        f.write(
            'Prosječna duljina najkraćeg puta, L: ' + str(nx.average_shortest_path_length(G)) + '\n')
        f.write('Dijametar mreže, D: ' + str(nx.diameter(G)) + '\n')
        f.write(
            'Koeficijent grupiranja, c: ' + str(nx.average_clustering(G)) + '\n')
        f.write(
            'Koeficijent asortativnosti, a: ' + str(nx.degree_assortativity_coefficient(G)) + '\n')
        f.write(
            'Broj komponenti: ' + str(nx.number_connected_components(G)) + '\n')
        f.write('Hub(s): ' + str(hub()))


def create_graph():
    for i in range(0, 50):
        nodes.append(''.join(random.choice(
            string.ascii_lowercase) for i in range(3)))

    for node in nodes:
        G.add_node(node)

    for i in range(0, 200):
        G.add_edge(np.random.choice(nodes), np.random.choice(
            nodes), weight=random.randint(1, 100))


def write_graph():
    with open("graph.graphml", "wb") as ofile:
        nx.write_graphml(G, ofile)


G = nx.Graph()
create_graph()
write_graph()
write2txt()
draw()
remove_smaller_edges()
draw()

x = G.degree()
plt.hist(x)
plt.show()
