
import numpy as np
import pandas as pd

aa = np.random.randint(1, 10, 5)
print aa.astype(str)
print np.size(aa, axis=0)

print "aa %s bb" % (str(aa[0]))

xxx = pd.read_csv('.\dataset\AWDAS2_201505_1_align.csv')
ccc = list(xxx.columns.values)
print ccc[2]
print str(xxx.loc[0][0]) + ' : ' + str(xxx.loc[0][1])
print '--------------------------'

tsd = pd.DataFrame.from_csv('.\dataset\datetime_data.csv', infer_datetime_format=True)
print tsd.index[0:10]
print tsd[0:10]
print tsd.head()
print '--------------------------'

rng = pd.date_range('1/1/2011', periods=1440/3, freq='H')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
# print ts[1:]
# print ts.index[1:]

