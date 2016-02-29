
#-*-codin: utf-8-*-

import sqlite3 as sql3
import pandas as pd

import calendar
import numpy as np

conn = sql3.connect('AWDAS2.sqlite')

# impor CSV into SQLite3 file
# df = pd.DataFrame.from_csv('./dataset/AWDAS2_201505_1_align.csv', infer_datetime_format=True)
# df.to_sql('AWDAS2_201505_1', conn, if_exists='replace', index=True)
# print 'Import data is done!'

# Read table information from SQLite3 file
# print 'Querying...'
# outcome = pd.read_sql_query('PRAGMA table_info(AWDAS2_201505_1);', conn)
# print outcome

# Query data
start_date = '2015-05-01 00:00:00'
end_date = '2015-05-01 10:00:00'
sql_cmd = "SELECT datetime_tick, F2218  FROM AWDAS2_201505_1 WHERE datetime_tick BETWEEN '" \
          + start_date + "' AND '" + end_date + "' LIMIT 5"
outcome = pd.read_sql_query(sql_cmd, conn)
series_outcome = pd.Series(data=outcome.F2218.tolist(), index=outcome.datetime_tick)
print series_outcome

print 'Done'


def get_week_of_month(year, month, day):
    x = np.array(calendar.monthcalendar(year, month))
    week_of_month = np.where(x == day)[0][0] + 1
    return week_of_month

print get_week_of_month(2015, 5, 3)



