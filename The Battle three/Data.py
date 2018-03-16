import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import random
from sklearn.linear_model import LogisticRegression as LR

def Age_to_notnull(data):
	a= []
	for _ in range(data.Age[data.Age.isnull()].size):
		li = random.choice(range(1,101))
		if li <= 15:
			a.append(8.5)
		elif li >73:
			a.append(55)
		else:
			a.append(27)
	return a
# 读取数据
path_train = 'C:/Users/123/Desktop/train.csv'
path_test = 'C:/Users/123/Desktop/test.csv'
path_test_y = 'C:/Users/123/Desktop/gender_submission.csv'
data = pd.read_csv(path_train)
test_data = pd.read_csv(path_test)
test_y = pd.read_csv(path_test_y).Survived
# 数据复制
train_data = data.copy()
# 数据规约
# 年龄
train_data.Age[train_data.Age.isnull()] = Age_to_notnull(train_data)
test_data.Age[test_data.Age.isnull()] = Age_to_notnull(test_data)
# 票价
train_data.Fare = train_data.Fare / train_data.Fare.max()
test_data.Fare = test_data.Fare / test_data.Fare.max()
test_data.Fare[test_data.Fare.isnull()] = test_data.Fare.mean()
# 性别
train_data.Sex[train_data.Sex == 'female'] = 1
train_data.Sex[train_data.Sex == 'male'] = -1
test_data.Sex[test_data.Sex == 'female'] = 1
test_data.Sex[test_data.Sex == 'male'] = -1
# 数据筛选
x_train = train_data[['Pclass','Sex','Age','SibSp','Parch','Fare']]
y_train = train_data.Survived
x_test = test_data[['Pclass','Sex','Age','SibSp','Parch','Fare']]
# 建模型
lr = LR()
lr.fit(x_train,y_train)
result = lr.predict(x_test)
n = 0
for i,j in zip(test_y,result):
	if i == j:
		n += 1
print('正确率为:',n/test_y.size) 






