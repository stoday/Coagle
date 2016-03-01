

import numpy as np
from flask import Flask, render_template, request
import json
import plotly
import plotly.graph_objs as go
import pandas as pd
import re
import sqlite3 as sql3


app = Flask(__name__)


# Go to input Page
@app.route('/')
def goto_input_text():
    return render_template('entry.html')


@app.route('/onmi_input', methods=['POST'])
def process_input():
    text = request.form['onmi_text']

    # Request parser
    date_part = re.search('\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d', text)
    opc_part = re.search('\w\d\d\d\d', text)

    # If-statement after search() tests if it succeeded
    if date_part:
        date_outcome = date_part.group()  #
    else:
        date_outcome = None

    if opc_part:
        opc_outcome = opc_part.group()  #
    else:
        opc_outcome = None

    # Transform data and plot
    if opc_outcome is None and date_outcome is None:
        return render_template('entry.html')
    else:
        conn = sql3.connect('AWDAS2.sqlite')  # Connect DB
        target_date = re.match('(?P<date_str>\d\d\d\d-\d\d-\d\d) (?P<hour_str>\d\d):(?P<minte_second_str>\d\d:\d\d)', date_outcome)

        start_date = target_date.group('date_str') + " %02d" % (int(target_date.group('hour_str'))//8 * 8) + ':00:00'
        end_date = target_date.group('date_str') + " %02d" % ((int(target_date.group('hour_str'))//8 + 1) * 8) + ':00:00'

        sql_cmd = "SELECT datetime_tick, %s " \
                  "FROM AWDAS2_201505_1 WHERE datetime_tick " \
                  "BETWEEN '%s' AND '%s'" % (opc_outcome, start_date, end_date)
        query_out = pd.read_sql_query(sql_cmd, conn)
        ts_raw = pd.Series(data=query_out[opc_outcome].tolist(), index=query_out['datetime_tick'])

        xx = ts_raw.index  # Can use the pandas data structures directly
        yy = ts_raw
        data = [go.Scatter(x=xx, y=yy)]
        layout = {
            'xaxis': {'range': [xx[0], xx[-1]], 'showline': True, 'mirror': True},
            'yaxis': {'showgrid': True, 'showline': True, 'mirror': True},
        }
        graphs = {'data': data, 'layout': layout}

        graphJSON = json.dumps(graphs, cls=plotly.utils.PlotlyJSONEncoder)

        return render_template('show_results.html', ids=['charts'], graphJSON=graphJSON, date_title=start_date, tag_name=opc_outcome )

if __name__ == "__main__":
    app.run(debug=True)
