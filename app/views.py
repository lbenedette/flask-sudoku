from flask import render_template, request, redirect, url_for, flash
from sudoku import nx, nodes, createNode, createEdge, makeSolution, verification
from app import app


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title='H O M E', nodes=nodes)


@app.route("/solution", methods=['POST'])
def sudoku():
    sdk = nx.Graph()
    data = request.form
    createNode(sdk, data)
    createEdge(sdk)
    if not verification(sdk):
        flash('Warning! There can not be equal numbers in the same row, column or square.')
        return redirect(url_for('index'))
    makeSolution(sdk)
    return render_template('solution.html', title='S O L U T I O N', nodes=nodes, graph=sdk)
