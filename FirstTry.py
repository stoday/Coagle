
import numpy as np
from flask import Flask, render_template
import json
import plotly

import plotly.graph_objs as go

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

    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index2.html',
                           ids=['aaa'],
                           graphJSON=graphJSON)


@app.route('/z3')
def index3():
    ts_raw = pd.DataFrame.from_csv('.\dataset\AWDAS2_201505_1_align.csv', infer_datetime_format=True)
    graphs = dict(
        data=[
            dict(
                x=ts_raw.index,  # Can use the pandas data structures directly
                y=pd.Series(ts_raw['F2218'], index=ts_raw.index)
            )
        ]
    )

    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index3.html',
                           ids=['aaa'],
                           graphJSON=graphJSON,
                           xxx='xxx')


@app.route('/z4')
def index4():
    graphs = dict(
        data=[
            dict(
                x=[1, 2, 3],  # Can use the pandas data structures directly
                y=[4, 5, 6],
                type='bar'
            ),
        ],
        layout=dict(
            title='first graph'
        )
    )

    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index3.html',
                           ids=['aaa'],
                           graphJSON=graphJSON,
                           xxx='xxx')


@app.route('/z5')
def index5():
    trace0 = go.Scatter(x=[1.5, 4.5], y=[0.75, 0.75], text=['Unfilled Rectangle', 'Filled Rectangle'], mode='text')
    data = [trace0]
    layout = {'xaxis': {'range': [0, 7], 'showgrid': False }, 'yaxis': {'range':[0, 3.5]}, 'width': 600, 'height': 600,
        'shapes': [
            # unfilled Rectangle
            {
                'type': 'rect',
                'x0': 1,
                'y0': 1.5,
                'x1': 5,
                'y1': 3,
                'line': {'color': 'rgba(128, 0, 128, 1)'},
            },
            # filled Rectangle
            {
                'type': 'rect',
                'x0': 4,
                'y0': 1,
                'x1': 6,
                'y1': 2,
                'line': {'color': 'rgba(128, 0, 128, 1)', 'width': 2},
                'fillcolor': 'rgba(128, 0, 128, 0.7)',
            },
        ]
    }
    graphs = {'data': data, 'layout': layout}

    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index3.html', ids=['aaa'], graphJSON=graphJSON, xxx='xxx')


@app.route('/z6')
def index6():
    ts_raw = pd.DataFrame.from_csv('.\dataset\AWDAS2_201505_1_align.csv', infer_datetime_format=True)
    xx = ts_raw.index  # Can use the pandas data structures directly
    yy = pd.Series(ts_raw['F2218'], index=ts_raw.index)
    data = [go.Scatter(x=['2013-10-04 22:23:00', '2013-11-04 22:23:00', '2013-12-04 22:23:00'], y=[1, 3, 6])]
    layout = {'width': 600, 'height': 600,
        'shapes': [
            # unfilled Rectangle
            {
                'type': 'rect',
                'x0': '2013-10-04 22:23:00',
                'y0': 1.5,
                'x1': '2013-10-14 22:23:00',
                'y1': 3,
                'line': {'color': 'rgba(128, 0, 128, 1)'},
            },
            # filled Rectangle
            {
                'type': 'rect',
                'x0': '2013-10-24 22:23:00',
                'y0': 1,
                'x1': '2013-11-04 22:23:00',
                'y1': 10,
                'line': {'color': 'rgba(128, 0, 128, 1)', 'width': 2},
                'fillcolor': 'rgba(128, 0, 128, 0.7)',
            },
        ]
    }
    graphs = {'data': data, 'layout': layout}

    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index3.html', ids=['aaa'], graphJSON=graphJSON, xxx='xxx')


if __name__ == "__main__":
    app.run(debug=True)
