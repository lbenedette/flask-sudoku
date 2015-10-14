from flask import render_template, request
from sudoku import nx, nodes, createNode, createEdge, makeSolution
from app import app

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', nodes=nodes)


@app.route("/solution", methods=['POST'])
def sudoku():
    sdk = nx.Graph()
    data = request.form
    createNode(sdk, data)
    createEdge(sdk)
    makeSolution(sdk)
    return render_template('solution.html', nodes=nodes, graph=sdk)
