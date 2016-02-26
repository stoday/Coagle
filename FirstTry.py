
import numpy as np
from flask import Flask, render_template
import json
import plotly
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    aa = np.random.randint(1, 10, 5)
    bb = np.array([[1, 2], [3, 4]])
    return str(bb) + ' Still Work !!'


@app.route("/a")
def home2():
    aa = np.random.randint(1, 10, 5)
    bb = np.array([[1, 2], [3, 4]])
    return str(aa) + str(bb) + ' Still Work !!'


@app.route('/z1')
def index1():
    rng = pd.date_range('1/1/2011', periods=1440/3, freq='H')
    ts = pd.Series(np.random.randn(len(rng)), index=rng)

    graphs = [
        dict(
            data=[
                dict(
                    x=[1, 2, 3],
                    y=[10, 20, 30],
                    type='scatter'
                ),
            ],
            layout=dict(
                title='first graph'
            )
        ),

        dict(
            data=[
                dict(
                    x=[1, 3, 5],
                    y=[10, 50, 30],
                    type='bar'
                ),
            ],
            layout=dict(
                title='second graph'
            )
        ),

        dict(
            data=[
                dict(
                    x=ts.index,  # Can use the pandas data structures directly
                    y=ts
                )
            ]
        )
    ]

    # Add "ids" to each of the graphs to pass up to the client
    # for templating
    ids = ['graph-{}'.format(i) for i, _ in enumerate(graphs)]

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html',
                           ids=ids,
                           graphJSON=graphJSON)


@app.route('/z2')
def index2():
    rng = pd.date_range('1/1/2011', periods=1440/3, freq='H')
    ts = pd.Series(np.random.randn(len(rng)), index=rng)

    graphs = dict(
            data=[
                dict(
                    x=ts.index,  # Can use the pandas data structures directly
                    y=ts
                )
            ]
        )

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index2.html',
                           ids=['aaa'],
                           graphJSON=graphJSON)


@app.route('/z3')
def index3():
    # xxx = pd.read_csv('.\dataset\AWDAS2_201505_1_align.csv')
    rng = pd.date_range('1/1/2011', periods=1440/3, freq='H')
    ts = pd.Series(np.random.randn(len(rng)), index=rng)
    # ts = pd.DataFrame.from_csv('.\dataset\datetime_data.csv', header=None, infer_datetime_format=True)
    graphs = dict(
            data=[
                dict(
                    x=ts.index[1:],  # Can use the pandas data structures directly
                    y=ts[1:]
                )
            ]
        )

    # Convert the figures to JSON
    # PlotlyJSONEncoder appropriately converts pandas, datetime, etc
    # objects to their JSON equivalents
    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index3.html',
                           ids=['aaa'],
                           graphJSON=graphJSON,
                           xxx='xxx')


if __name__ == "__main__":
    app.run(debug=True)
