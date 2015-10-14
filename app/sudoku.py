import networkx as nx


# networkx graph
# g = nx.Graph()
# g is a dict of dicts
# g = {'node1': {'attr1': data1, 'attr2': data2}, 'node2': {}}
# access node: g.node['node1']
# access node attribute: g.node['node1']['attr1']

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
nodes = []
for i in range(len(number)):
    nodes.append([])
    for j in range(len(number)):
        nodes[i].append(number[i]+number[j])


# node is a cell of sudoku
# color: number
# status:
#   true: number correct
#   false: not found

# create nodes function
# arg: graph: networkx graph
#      data: matrix from web form
# desc: create the nodes and add attributes using a matrix from web form.
def createNode(graph, data):
    for i in range(9):
        for j in range(9):
            if int(data[nodes[i][j]]) > 0:
                graph.add_node(nodes[i][j], color=int(data[nodes[i][j]]), status=True)
            else:
                graph.add_node(nodes[i][j], color=[1,2,3,4,5,6,7,8,9], status=False)


def createEdge(graph):
    for i in range(len(number)):
        for j in range(len(number)-1):
            for k in range(j, len(number)-1):
                graph.add_edge(nodes[i][j], nodes[i][k+1])

    for i in range(len(number)-1):
        for j in range(len(number)):
            for k in range(i, len(number)-1):
                graph.add_edge(nodes[i][j], nodes[k+1][j])


# Welsh Powell graph coloring function
# arg: networkx graph
# desc: for all node, if status is false then verify the color of all neighbors
# with status true and remove this color from your color list.
def welshPowell(graph):
    for i in range(len(number)):
        for j in range(len(number)):
            if not graph.node[nodes[i][j]]['status']:
                for e in graph.neighbors(nodes[i][j]):
                    if graph.node[e]['status']:
                        # try remove color
                        try:
                            graph.node[nodes[i][j]]['color'].remove(graph.node[e]['color'])
                        # case color not on the list
                        except ValueError:
                            pass


# Update node value function
# arg: networkx graph
# desc: if status is false and color list length is 1, update status and color.
def updateValue(graph):
    for i in range(len(number)):
        for j in range(len(number)):
            if not graph.node[nodes[i][j]]['status'] and len(graph.node[nodes[i][j]]['color']) == 1:
                graph.node[nodes[i][j]]['status'] = True
                graph.node[nodes[i][j]]['color'] = graph.node[nodes[i][j]]['color'][0]


def makeSolution(graph):
    for i in range(5):
        welshPowell(graph)
        updateValue(graph)