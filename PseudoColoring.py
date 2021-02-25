import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np


adj = {
    "a" : ["b","c","d"],
    "b" : ["a","c","e","f"],
    "c" : ["a","b","d","f"],
    "d" : ["a","c","f"],
    "e" : ["b","f"],
    "f" : ["b","c","d","e"],
}
maple = {
    "a" : ["b","c","d"],
    "b" : ["a","c","e"],
    "c" : ["a","b","e"],
    "d" : ["a","e",],
    "e" : ["c","b","d"],
}

complex = {
    "a" : ["b","g"],
    "b" : ["a","c","d","f"],
    "c" : ["b","d"],
    "d" : ["c","b","e"],
    "e" : ["d","f"],
    "f" : ["b","g","e"],
    "g" : ["f","a"]
}

colors = {1: {"a"}}
cicle = 0;
added_nodes = []
nodes_from = []
nodes_to = []

for node in complex:
    assigned = False

    for c in colors:
        # print('current color ' + str(c))
        valid = True

        for v in colors[c]:
            # print('node = ' + str(node) + " in  map[" + str(v) + "]" + str(complex[v]))
            if node in complex[v]:
                # print(f'{node} + {v} ')
                nodes_from.append(str(node).upper())
                nodes_to.append(str(v).upper())
                # print("not valid")
                valid = False
                break

        if valid:
            if node not in added_nodes:
                colors[c].add(node)
                added_nodes.append(node)
                # print('CURRENT COLORS =' + str(colors))
                assigned = True

    if not assigned:
        colors[len(colors)+1] = {node}
        # print('new color in node ' + str(colors) + ' xd ' + str({node}))

    cicle +=1

# print(len(colors))
# print(node_conections)

# HARDCODED NODES ARRAY [('A', 'B'), ('A', 'G'), ('B', 'G'), ('D', 'C'), ('E', 'D'),
#      ('F', 'E'), ('F', 'E'), ('F', 'F'),('B','D')]
# df = pd.DataFrame({ 'from':['A','A','B','D','E','F','F','F','B',], 'to':['B','G','G','C','D','E','G','B','D']})

# Create df with node connections
df = pd.DataFrame({ 'from':nodes_from, 'to':nodes_to})
print(df)

# G = nx.DiGraph()
# Build your graph
# Plot df nodes to Graph
G= nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.Graph())

# G.add_edges_from(node_conections)

# And a data frame with characteristics for your nodes
# carac = pd.DataFrame({ 'ID':[i for i in complex.keys()], 'myvalue':['group1','group1','group2','group3','group3'] })
newlist = [i for i in complex]
# print(newlist)
group_values = []
bloqueado = []

dataframelist = []
for i in colors.keys():
    for item in newlist:
        if item in colors[i]:
            dataframelist.append(item.upper())
            group_values.append(i)

# print(group_values)

carac = pd.DataFrame({ 'ID':dataframelist, 'myvalue': group_values })

G.nodes()
carac= carac.set_index('ID')
carac=carac.reindex(G.nodes())


print(carac)

pos = nx.spring_layout(G,k=4.0)
nx.draw_networkx(G, pos, cmap=plt.get_cmap('cool'),
                       node_color = carac['myvalue'], node_size = 400,  arrows= False, with_labels=2,font_color='k')

# nx.draw(G, pos,font_color='w')
# nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
# nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
plt.show()





















# G = nx.DiGraph()
# G.add_edges_from(
#     [('A', 'B'), ('A', 'C'), ('D', 'B'), ('E', 'C'), ('E', 'F'),
#      ('B', 'H'), ('B', 'G'), ('B', 'F'), ('C', 'G')])
#
# val_map = {'A': 1.0,
#            'D': 0.5,
#            'H': 0.0}
#
# values = [val_map.get(node, 0.25) for node in G.nodes()]
#
# # Specify the edges you want here
# red_edges = [('A', 'C'), ('E', 'C')]
# edge_colours = ['black' if not edge in red_edges else 'red'
#                 for edge in G.edges()]
# black_edges = [edge for edge in G.edges() if edge not in red_edges]
#
# # Need to create a layout when doing
# # separate calls to draw nodes and edges
# pos = nx.spring_layout(G,k=4.0)
# print(pos)
# nx.draw_networkx(G, pos, cmap=plt.get_cmap('jet'),
#                        node_color = values, node_size = 400,  arrows= True, with_labels=2)
# nx.draw_networkx_labels(G, pos)
# nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
# nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=False)
# plt.show()