import pandas as pd 
import random
from Keras.models import Sequential
from Keras.layers.core import Dense,Activation

path = './chapter6/chapter6/demo/data/model.xls'
data = pd.read_excel(path)
data = data.as_matrix()
random.shuffle(data)
train_data = data[:int(len(data)*0.8),:]
test_data = data[int(len(data)*0.8):,:]

net = Sequential()
net.add(Dense(3,10))
net.add(Activation('relu'))
net.add(Dense(10,1))
net.add(Activation('sigmoid'))
net.compile(loss='binary_crossentropy',optimizer='adam',class_mode='binary')

net.fit(train_data[:,:3],train_data[:,3],nb_epoch=1000,batch_size=1)

predict_result = net.predict_classes(train_data[:,:3].reshape(len(train_data)))












