import pandas as pd 
from scipy.interpolate import lagrange

data_path = './chapter6/chapter6/demo/data/missing_data.xls'
data = pd.read_excel(data_path,header=None)
def ployinterp_column(s,n,k=5):
	y = s[list(range(n-k,n))+list(range(n+1,n+1+k))]
	y = y[y.notnull()]
	return lagrange(y.index,list(y))(n)

for i in data.columns:
	for j in range(len(data)):
		if (data[i].isnull())[j]:
			data[i][j] = ployinterp_column(data[i],j)















