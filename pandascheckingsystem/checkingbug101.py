import sys
import pandas as pd
import numpy as np
from numpy import dtype

print('python version: ', sys.version)
print('pandas version: ', pd.__version__)

data_dtype = [('name', dtype(object)), ('value', 'f8'), ('value2', dtype(object)),]
table = pd.DataFrame(np.zeros(0, dtype=data_dtype), index=pd.Index([], dtype=np.int64))
dtypes = table.dtypes
index = np.arange(10, dtype=np.int32)

data_dict = {'value2': np.ones(10, dtype=float), 'value': np.zeros(10, dtype=float),
             'name': np.array([np.arange(13) + x for x in range(10)], dtype=float)}

dd = pd.DataFrame(index=index, columns=table.columns)
dd = dd.assign(**data_dict)
print('**** Original ****', type(dd))
print(dd.head())
print('**** Bad Copy ****')
cc = dd.copy().head()
print(cc)

print('**** 1D ndarray ****')
data_dict['name'] = data_dict['name'][:, 0]
dd = pd.DataFrame(index=index, columns=table.columns)
dd = dd.assign(**data_dict)
print(dd.copy().head())

'''
Program output:
python version:  3.8.16 | packaged by conda-forge | (default, Feb  1 2023, 15:53:35) [MSC v.1929 64 bit (AMD64)]
pandas version:  0+untagged.1.g6169cba
**** Original ****
   name  value  value2
0   0.0    0.0     1.0
1   1.0    0.0     1.0
2   2.0    0.0     1.0
3   3.0    0.0     1.0
4   4.0    0.0     1.0
**** Bad Copy ****
   name  value  value2
0   0.0    2.0     1.0
1   1.0    3.0     2.0
2   2.0    4.0     3.0
3   3.0    5.0     4.0
4   4.0    6.0     5.0
**** 1D ndarray ****
   name  value  value2
0   0.0    0.0     1.0
1   1.0    0.0     1.0
2   2.0    0.0     1.0
3   3.0    0.0     1.0
4   4.0    0.0     1.0
'''