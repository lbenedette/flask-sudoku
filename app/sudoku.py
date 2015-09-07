import networkx as nx

# networkx graph
# g = nx.Graph()
# g is a dict of dicts
# g = {'node1': {'attr1': data1, 'attr2': data2}, 'node2': {}}
# access node: g.node['node1']
# access node attribute: g.node['node1']['attr1']

#TODO: create edge function

# node is a cell of sudoku
# color: number
# status:
#   true: number correct
#   false: not found

# create nodes function
# arg: graph: networkx graph
#      data: matrix from web form
# desc: create the nodes and add attributes using a matrix from web form.
def CreateNode(graph, data):
    i = 1
    for j in range(9):
        for k in range(9):
            if data[j][k] > 0:
                graph.add_node(i, color=data[j][k], status=True)
            else:
                graph.add_node(i, color=[1,2,3,4,5,6,7,8,9], status=False)


# Welsh Powell graph coloring function
# arg: networkx graph
# desc: for all node, if status is false then verify the color of all neighbors
# with status true and remove this color from your color list.
def WelshPowell(graph):
    for i in range(1,17):
        if not graph.node[i]['status']:
            for e in graph.neighbors(i):
                if graph.node[e]['status']:
                    # try remove color
                    try:
                        graph.node[i]['color'].remove(graph.node[e]['color'])
                    # case color not on the list
                    except ValueError:
                        pass


# Update node value function
# arg: networkx graph
# desc: if status is false and color list lenght is 1, update status and color.
def UpdateValue(graph):
    for i in range(1, 17):
        if not graph.node[i]['status'] and len(graph.node[i]['color']) == 1:
            graph.node[i]['status'] = True
            graph.node[i]['color'] = graph.node[i]['color'][0]


#TODO: doing!!!
def SudokuSolution(data):
    # create graph using networkx lib
    sudoku = nx.Graph()
    CreateNode(sudoku, data)
