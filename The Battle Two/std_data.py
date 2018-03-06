import pandas as pd 

path = './chapter7/chapter7/demo/data/zscoredata.xls'
data = pd.read_excel(path)


data = (data - data.mean(axis=0))/(data.std(axis=0))
data.columns = ['Z'+i for i in data.columns]
print(data)












