# -*- coding:utf-8 -*-
import pandas as pd 
import random
from sklearn.tree import DecisionTreeClassifier
from cm_plot import *

path = './chapter6/chapter6/demo/data/model.xls'
data = pd.read_excel(path)
data = data.as_matrix()
random.shuffle(data)
train_data = data[:int(len(data)*0.8),:]
test_data = data[int(len(data)*0.8):,:]

tree = DecisionTreeClassifier()
tree.fit(train_data[:,:3],train_data[:,3])
cm_plot(train_data[:,3],tree.predict(train_data[:,:3])).show()





