import pandas as pd 

path = './chapter7/chapter7/demo/data/air_data.csv'
data = pd.read_csv(path,encoding='utf-8')

data = data[data['SUM_YR_1'].notnull() & data['SUM_YR_2'].notnull()]

index_1 = data['SUM_YR_1'] != 0 
index_2 = data['SUM_YR_2'] != 0
index_3 = (data['SEG_KM_SUM'] == 0) & (data['avg_discount'] == 0)
data = data[index_1|index_2|index_3]
print(data)













