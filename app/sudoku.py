import networkx as nx

#   1   2   3
# | 9 | 4 |   |
# | 6 |   |   |
# |   |   | 2 |
# create edges and verify the color and eliminate repeats
g = nx.Graph()

n = [x for x in range(1, 10)]
nodes = [x for x in range(1, 10)]
# color = number
# status = True : correct, False : not defined
g.add_node(1, color=9, status=True)
g.add_node(2, color=4, status=True)
g.add_node(3, color=n, status=False)
g.add_node(4, color=6, status=True)
g.add_node(5, color=n, status=False)
g.add_node(6, color=n, status=False)
g.add_node(7, color=n, status=False)
g.add_node(8, color=n, status=False)
g.add_node(9, color=2, status=True)

e = []
for x in range(0, 9):
    for y in range(x+1, 9):
        e.append((nodes[x], nodes[y]))
g.add_edges_from(e)

# g.node is a dict - key = node name
# to access data - [key = node name][key = data name]
print g.node[1]['status']
print g.node[1]['color']

# if node status is false
# for all neighbors status true
# try remove neighbor color
for x in range(1,10):
    if not g.node[x]['status']:
        for e in g.neighbors(x):
            if g.node[e]['status']:
                try:
                    g.node[x]['color'].remove(g.node[e]['color'])
                # if the color is already removed
                except ValueError:
                    pass

print g.node