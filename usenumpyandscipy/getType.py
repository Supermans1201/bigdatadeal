import pandas as pd
data = pd.read_csv('new.csv',sep=',')
datalist= data.values.tolist()
def type(tup):
    for dl in datalist:
        # print dl[0],dl[1],dl[2],'::'
        # print tup[0],tup[2],tup[3]

        if abs(dl[0]-tup[0])<=0.001:
            if abs(dl[1]-tup[2])<=0.001:
                if abs(dl[2]-tup[3])<=0.001:
                    return dl[3]

