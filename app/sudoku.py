import networkx as nx


number = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
nodes = []
for i in range(len(number)):
    nodes.append([])
    for j in range(len(number)):
        nodes[i].append(number[i]+number[j])

square = [['00','01','02','10','11','12','20','21','22'],
          ['03','04','05','13','14','15','23','24','25'],
          ['06','07','08','16','17','18','26','27','28'],
          ['30','31','32','40','41','42','50','51','52'],
          ['33','34','35','43','44','45','53','54','55'],
          ['36','37','38','46','47','48','56','57','58'],
          ['60','61','62','70','71','72','80','81','82'],
          ['63','64','65','73','74','75','83','84','85'],
          ['66','67','68','76','77','78','86','87','88']]


# Configuration:
# each node is a cell of a sudoku sheet
# color means the number of cell
# status says if the cell already with the correct number(color)


# Desc: create nodes and for each node attribute color and status from data.
# @graph: networkx graph
# @data: data from web form(array)
def createNode(graph, data):
    for i in range(9):
        for j in range(9):
            if int(data[nodes[i][j]]) > 0:
                graph.add_node(nodes[i][j], color=int(data[nodes[i][j]]), status=True)
            else:
                graph.add_node(nodes[i][j], color=[1,2,3,4,5,6,7,8,9], status=False)


# Desc: create all edges of sudoku: rows, columns and squares
# @graph: networkx graph
def createEdge(graph):
    # rows edges
    for i in range(len(number)):
        for j in range(len(number)-1):
            for k in range(j, len(number)-1):
                graph.add_edge(nodes[i][j], nodes[i][k+1])

    # columns edges
    for i in range(len(number)-1):
        for j in range(len(number)):
            for k in range(i, len(number)-1):
                graph.add_edge(nodes[i][j], nodes[k+1][j])

    # square edges(using another matrix)
    for i in range(len(number)):
        for j in range(len(number)-1):
            for k in range(j, len( number)-1):
                graph.add_edge(square[i][j], square[i][k+1])


# Desc: checks if the sudoku is valid.
# @graph: networkx graph
def verification(graph):
    for i in range(len(number)):
        for j in range(len(number)):
            if graph.node[nodes[i][j]]['status']:
                for e in graph.neighbors(nodes[i][j]):
                    if graph.node[e]['status'] and graph.node[e]['color'] == graph.node[nodes[i][j]]['color']:
                        return False
    return True


# Desc: using Welsh Powell coloring graph function, for all nodes with status=false verifies the color
# of your neighbors with status=true, eliminating colors of your color list.
# @graph: networkx graph
def welshPowell(graph):
    for i in range(len(number)):
        for j in range(len(number)):
            if not graph.node[nodes[i][j]]['status']:
                for e in graph.neighbors(nodes[i][j]):  # neighbors
                    if graph.node[e]['status']: # if neighbors['status] == True
                        # try remove color
                        try:
                            graph.node[nodes[i][j]]['color'].remove(graph.node[e]['color'])
                        # case color not on the list
                        except ValueError:
                            pass


# Desc: if status is false and color list length is 1, update status and color.
# @graph: networkx graph
def updateValue(graph):
    for i in range(len(number)):
        for j in range(len(number)):
            if not graph.node[nodes[i][j]]['status'] and len(graph.node[nodes[i][j]]['color']) == 1:
                graph.node[nodes[i][j]]['status'] = True
                graph.node[nodes[i][j]]['color'] = graph.node[nodes[i][j]]['color'][0]


# Desc: hardcode yet, execute welsh powell and update 5 times
# @graph: networkx graph
def makeSolution(graph):
    for i in range(5):
        welshPowell(graph)
        updateValue(graph)
# For somes medium and hard sudokus level, don't find a single solution!