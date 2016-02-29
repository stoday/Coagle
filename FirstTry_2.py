
import numpy as np
from flask import Flask, render_template
import json
import plotly
import plotly.graph_objs as go
import pandas as pd

import sqlite3 as sql

app = Flask(__name__)


@app.route("/")
def home():
    aa = np.random.randint(1, 10, 5)
    bb = np.array([[1, 2], [3, 4]])
    return str(bb) + ' Still Work !!'


@app.route('/z7')
def index7():
    ts_raw = pd.DataFrame.from_csv('.\dataset\AWDAS2_201505_1_align.csv', infer_datetime_format=True)
    xx = ts_raw.index  # Can use the pandas data structures directly
    yy = pd.Series(ts_raw['F2218'], index=ts_raw.index)
    data = [go.Scatter(x=xx[0:10], y=yy[0:10])]
    layout = {
        'xaxis': {'range': [xx[0], xx[10]], 'showgrid': True},
        'yaxis': {'range': [48, 60], 'showgrid': True},
        # 'width': 600, 'height': 600,
        'shapes': [
            # unfilled Rectangle
            {
                'type': 'rect',
                'x0': '2015-05-01 00:01:00',
                'y0': 48,
                'x1': '2015-05-01 00:02:00',
                'y1': 60,
                'line': {'color': 'rgba(128, 0, 128, 1)'},
            },
            # filled Rectangle
            {
                'type': 'rect',
                'x0': '2015-05-01 00:03:00',
                'y0': 48,
                'x1': '2015-05-01 00:04:00',
                'y1': 60,
                'line': {'color': 'rgba(128, 0, 128, 1)', 'width': 2},
                'fillcolor': 'rgba(128, 0, 128, 0.7)',
            },
        ]
    }
    graphs = {'data': data, 'layout': layout}

    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index3.html', ids=['aaa'], graphJSON=graphJSON, xxx='xxx')


@app.route('/z8')
def index8():
    ts_raw = pd.DataFrame.from_csv('.\dataset\AWDAS2_201505_1_align.csv', infer_datetime_format=True)
    xx = ts_raw.index  # Can use the pandas data structures directly
    yy = pd.Series(ts_raw['F2218'], index=ts_raw.index)
    data = [go.Scatter(x=xx, y=yy)]
    layout = {
        'xaxis': {'range': [xx[0], xx[-1]], 'showline': True, 'mirror': True},
        'yaxis': {'showgrid': True, 'showline': True, 'mirror': True},
    }
    graphs = {'data': data, 'layout': layout}

    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index3.html', ids=['aaa'], graphJSON=graphJSON, xxx='xxx')


@app.route('/table')
def table8():
    ts_raw = pd.DataFrame.from_csv('.\dataset\AWDAS2_201505_1_align.csv', infer_datetime_format=True)
    xx = ts_raw.index  # Can use the pandas data structures directly
    yy = pd.Series(ts_raw['F2218'], index=ts_raw.index)
    data = [go.Scatter(x=xx, y=yy)]
    layout = {
        'xaxis': {'range': [xx[0], xx[-1]], 'showline': True, 'mirror': True},
        'yaxis': {'showgrid': True, 'showline': True, 'mirror': True},
    }
    graphs = {'data': data, 'layout': layout}

    graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index3.html', ids=['aaa'], graphJSON=graphJSON, xxx='xxx')


if __name__ == "__main__":
    app.run(debug=True)
