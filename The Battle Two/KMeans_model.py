import pandas as pd 
from sklearn.cluster import KMeans


path = './chapter7/chapter7/demo/tmp/zscoreddata.xls'
data = pd.read_excel(path)

k = 5 
kmodel = KMeans(n_clusters = k,n_jobs = 1)
kmodel.fit(data)

center_point = kmodel.cluster_centers_ 
label = kmodel.labels_
print(label)













