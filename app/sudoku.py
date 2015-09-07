import networkx as nx

#   1   2    3   4
# |   | 1 || 4 |   |
# | 2 |   ||   |   |
# ------------------
# |   | 3 ||   | 4 |
# | 4 |   ||   | 1 |
# create edges and verify the color and eliminate repeats
g = nx.Graph()

# color = number
# status = True : correct, False : not defined

# create nodes
g.add_node(1, color=[1, 2, 3, 4], status=False)
g.add_node(2, color=1, status=True)
g.add_node(3, color=4, status=True)
g.add_node(4, color=[1, 2, 3, 4], status=False)

g.add_node(5, color=2, status=True)
g.add_node(6, color=[1, 2, 3, 4], status=False)
g.add_node(7, color=[1, 2, 3, 4], status=False)
g.add_node(8, color=[1, 2, 3, 4], status=False)

g.add_node(9, color=[1, 2, 3, 4], status=False)
g.add_node(10, color=3, status=True)
g.add_node(11, color=[1, 2, 3, 4], status=False)
g.add_node(12, color=4, status=True)

g.add_node(13, color=4, status=True)
g.add_node(14, color=[1, 2, 3, 4], status=False)
g.add_node(15, color=[1, 2, 3, 4], status=False)
g.add_node(16, color=1, status=True)

# g.node is a dict - key = node name
# to access data - [key = node name][key = data name]
#print g.node[1]['status']
#print g.node[1]['color']

# create edges
# square
s1 = [(1, 2), (1, 5), (1, 6), (2, 5), (2, 6), (5, 6)]
s2 = [(3, 4), (3, 7), (3, 8), (4, 7), (4, 8), (7, 8)]
s3 = [(9, 10), (9, 13), (9, 14), (10, 13), (10, 14), (13, 14)]
s4 = [(11, 12), (11, 15), (11, 16), (12, 15), (12, 16), (15, 16)]

g.add_edges_from(s1)
g.add_edges_from(s2)
g.add_edges_from(s3)
g.add_edges_from(s4)

# lines
l1 = [(1, 3), (1, 4), (2, 3), (2, 4)]
l2 = [(5, 7), (5, 8), (6, 7), (6, 8)]
l3 = [(9, 11), (9, 12), (10, 11), (10, 12)]
l4 = [(13, 15), (13, 16), (14, 15), (14, 16)]

g.add_edges_from(l1)
g.add_edges_from(l2)
g.add_edges_from(l3)
g.add_edges_from(l4)

# column
c1 = [(1, 9), (1, 13), (5, 9), (5, 13)]
c2 = [(2, 10), (2, 14), (6, 10), (6, 14)]
c3 = [(3, 11), (3, 15), (7, 11), (7, 15)]
c4 = [(4, 12), (4, 16), (8, 12), (8, 16)]

g.add_edges_from(c1)
g.add_edges_from(c2)
g.add_edges_from(c3)
g.add_edges_from(c4)


# if node status is false
# for all neighbors status true
# try remove neighbor color
for x in range(1,17):
    if not g.node[x]['status']:
        for e in g.neighbors(x):
            if g.node[e]['status']:
                try:
                    g.node[x]['color'].remove(g.node[e]['color'])
                # if the color is already removed
                except ValueError:
                    pass

# update values
for x in range(1, 17):
    # status = false and one element in color list
    if not g.node[x]['status'] and len(g.node[x]['color']) == 1:
        g.node[x]['status'] = True
        g.node[x]['color'] = g.node[x]['color'][0]


for x in range(1,17):
    if not g.node[x]['status']:
        for e in g.neighbors(x):
            if g.node[e]['status']:
                try:
                    g.node[x]['color'].remove(g.node[e]['color'])
                # if the color is already removed
                except ValueError:
                    pass

# update values
for x in range(1, 17):
    # status = false and one element in color list
    if not g.node[x]['status'] and len(g.node[x]['color']) == 1:
        g.node[x]['status'] = True
        g.node[x]['color'] = g.node[x]['color'][0]

for x in range(1,17):
    if not g.node[x]['status']:
        for e in g.neighbors(x):
            if g.node[e]['status']:
                try:
                    g.node[x]['color'].remove(g.node[e]['color'])
                # if the color is already removed
                except ValueError:
                    pass

# update values
for x in range(1, 17):
    # status = false and one element in color list
    if not g.node[x]['status'] and len(g.node[x]['color']) == 1:
        g.node[x]['status'] = True
        g.node[x]['color'] = g.node[x]['color'][0]

for x in range(1, 5):
    if g.node[x]['status']:
        print g.node[x]['color'],
    else:
        print 'x',
print '\n'

for x in range(5, 9):
    if g.node[x]['status']:
        print g.node[x]['color'],
    else:
        print 'x',
print '\n'

for x in range(9, 13):
    if g.node[x]['status']:
        print g.node[x]['color'],
    else:
        print 'x',
print '\n'

for x in range(13, 17):
    if g.node[x]['status']:
        print g.node[x]['color'],
    else:
        print 'x',
