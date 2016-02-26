import numpy as np
import pandas as pd

aa = np.random.randint(1, 10, 5)
print aa.astype(str)
print np.size(aa, axis=0)

print "aa %s bb" % (str(aa[0]))
print '--------------------------'

ts = pd.DataFrame.from_csv('.\dataset\datetime_data.csv', header=None, infer_datetime_format=True)
ts_s = pd.Series(ts[1], index=ts.index)
# print ts_series.head()
print '--------------------------'

ts_raw = pd.DataFrame.from_csv('.\dataset\AWDAS2_201505_1_align.csv', infer_datetime_format=True)
ts_raw.F2218
ts_raw_series = pd.Series(ts_raw.F2218, index=ts_raw.index)
