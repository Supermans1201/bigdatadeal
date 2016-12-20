import numpy as np
from kmodes import kmodes

import pandas as pd

rawexcel = "F:/bigdata/dealed/dealed.xlsx"
data = pd.read_excel(rawexcel)
# # random categorical data
# data = np.random.choice(20, (100, 10))
# print data

km = kmodes.KModes(n_clusters=4, init='Huang', n_init=5, verbose=1)
clusters = km.fit_predict(data)
print clusters

import  numpy
numpy.savetxt('dealed_modes.csv',clusters , delimiter = ',')
