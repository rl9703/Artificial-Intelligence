'''
    Author: Rishab Lalwani
    Title: LSTM classification using Keras and Tensorflow
'''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Model
from keras.layers import LSTM, Activation, Dense, Dropout, Input, Embedding
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt

#Import json files using pandas
df1 = pd.read_json('subreddit1.json', orient='split')
df2 = pd.read_json('subreddit2.json', orient='split')
df3 = pd.read_json('subreddit3.json', orient='split')


#frames=[df2,df1]
frames = [df1,df2,df3]
result = pd.concat(frames)
titles=result.loc[:,'title']
dat=[]
X = result.title
Y = result.dataset
# Transform output Y
le = LabelEncoder()
Y = le.fit_transform(Y)
Y = Y.reshape(-1,1)

#Training LSTM using Keras ( 50% train + 25% test )
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25)

max_words = 1000
max_len = 150
tok = Tokenizer(num_words=max_words)
tok.fit_on_texts(X_train)
sequences = tok.texts_to_sequences(X_train)
sequences_matrix = sequence.pad_sequences(sequences,maxlen=max_len)

# Create RNN model
def RNN():
    '''
    :return: RNN model for training
    '''
    # We have used two dropout layers
    inputs = Input(name='inputs',shape=[max_len])
    layer = Embedding(max_words,50,input_length=max_len)(inputs)
    layer = LSTM(64)(layer)
    layer = Dense(256,name='FC1')(layer)
    layer = Activation('relu')(layer)
    layer = Dropout(0.5)(layer)
    layer = Dense(3,name='out_layer')(layer)
    layer = Activation('softmax')(layer)
    model = Model(inputs=inputs,outputs=layer)
    return model

model = RNN()
model.summary()

# Training using Keras
model.compile(loss='sparse_categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
history=model.fit(sequences_matrix,Y_train,batch_size=128,epochs=10,
          validation_split=0.2,callbacks=[EarlyStopping(monitor='val_loss',min_delta=0.0001)])

#testing
test_sequences = tok.texts_to_sequences(X_test)
test_sequences_matrix = sequence.pad_sequences(test_sequences,maxlen=max_len)


#Evaluation
accr = model.evaluate(test_sequences_matrix,Y_test)
print('Accuracy:',accr[1]*100,'%')


# Plot accuracy and loss curves using matplotlib
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# Summarize history for loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
