import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorecal_crossentropy

# importing data from text file .
f = open("New Text Document.txt",'r')
k = f.readlines()
f.close()

# data is in format [x1,x2,y] where [x1,x2] being one training example and y being label
# x1 represents atomic number and x2 represents atomic mass of element
# label y =1 corresponds to existance of that element . y=0 means that element can not exist naturally


# creating temporary lists to fetch data
X = []
Y = []

for i in k:
    i = i.strip().split()
    X.append([float(i[0]),float(i[1])])
    Y.append(int(i[2]))

# converting above created lists into numpy array
X = np.array(X)
Y = np.array(Y).T
# print(X)
# print(Y)
# X has shape 256x2 and Y 256x1

# creating a neural network . here i am using sigmoid activation function cause it gives better results that tanh/relu
model = Sequential()
model.add(Dense(units=4,activation='sigmoid',input_dim=2))
model.add(Dense(units=3,activation='sigmoid'))
model.add(Dense(units=2,activation='sigmoid'))
model.add(Dense(units=1,activation='sigmoid'))
# print the neural network details built above
model.summary()

# compile model
model.compile(optimizer=Adam(0.001),loss='binary_crossentropy',metrics=['accuracy'])
model.fit(X,Y,epochs=750,batch_size=64)

# running the model for 750 epochs gives accuracy about 0.9831
# further increase in iterations doesnt increase accuracy .


# making predicting
Y_ = model.predict(X)




# with the help of this model you can predict the existance of an element : Based on its atoomic number and atomic
# mass number
