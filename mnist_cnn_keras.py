
# coding: utf-8

# In[1]:


from __future__ import print_function

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
from keras.utils import plot_model


# In[2]:


batch_size = 128
num_classes = 10
epochs = 12

#input image dimensions
img_rows, img_cols = 28, 28

#the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()


# In[3]:


if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)
display(input_shape)


# In[4]:


x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')


# In[5]:


# convert class vectors to binary class metrices
y_train = keras.utils.to_categorical(y_train ,num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)


# In[6]:


model = Sequential()


# In[7]:


model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=input_shape))
model.add(Conv2D(64, (3,3),activation='relu'))
# model.add(Conv2D(64, (3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))


# In[8]:


model.summary()


# In[8]:


model.compile(loss=keras.losses.categorical_crossentropy, 
             optimizer=keras.optimizers.Adadelta(),
             metrics=['accuracy'])


# In[9]:


model.fit(x_train, y_train,
         batch_size=batch_size, epochs=epochs,
         verbose=1, validation_data=(x_test, y_test))


# In[10]:


score = model.evaluate(x_test, y_test, verbose=1)


# In[11]:


print(score)

0.9913:もともとのやつのaccuracy
0.9905:Dropoutを抜く
0.9931:Convを一層増やした
# In[8]:


# plot_model(model, to_file='model.png')

