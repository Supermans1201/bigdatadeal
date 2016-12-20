from __future__ import division
from numpy.random import random
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
np.random.seed(12345)
plt.rc('figure', figsize=(10, 6))
from pandas import Series, DataFrame
import pandas as pd
np.set_printoptions(precision=4)

names=['a','b',"c","d","flower"]
df=pd.read_csv('iris.csv',header=None,names=names,index_col=names[4])
print df


