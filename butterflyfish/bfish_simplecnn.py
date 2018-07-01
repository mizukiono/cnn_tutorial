
# coding: utf-8

# In[1]:


from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import EarlyStopping
from keras.preprocessing.image import load_img, img_to_array


# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# In[3]:


epochs = 30


# In[4]:


# データをつくる
train_datagen = ImageDataGenerator(rescale=1.0/255, rotation_range=90, width_shift_range=0.2, height_shift_range=0.2,
                                  horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1.0/255)


# In[5]:


train_generator = train_datagen.flow_from_directory('../data/butterflyfish/train', target_size=(200,200),
                                                    batch_size=32, class_mode='binary')


# In[6]:


validation_generator = test_datagen.flow_from_directory('../data/butterflyfish/validation', target_size=(200,200),
                                                        batch_size=32, class_mode='binary')


# In[7]:


# モデルをつくる
model = Sequential()
model.add(Convolution2D(32, (3, 3), activation='relu', input_shape=(200, 200, 3)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Convolution2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Convolution2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))


# In[8]:


print(train_generator.class_indices)


# In[9]:


model.summary()


# In[10]:


model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# In[11]:


history = model.fit_generator(train_generator, epochs=epochs, verbose=1, validation_data=validation_generator)


# In[12]:


plt.plot(range(1, epochs+1), history.history['acc'], label="training")
plt.plot(range(1, epochs+1), history.history['val_acc'], label="validation")
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()


# In[15]:


img = load_img("../data/originaldata/test.jpg", target_size=(200, 200))
plt.imshow(img)


# In[16]:


array = img_to_array(img)
array /= 255
x = np.expand_dims(array, axis=0)
pred = model.predict(x)
print(pred[0])
if pred[0] >= 0.5:
    print('トゲチョウチョウウオです')
else:
    print('チョウチョウウオです')


# In[17]:


img = load_img("../data/originaldata/test2.jpg", target_size=(200, 200))
plt.imshow(img)


# In[18]:


array = img_to_array(img)
array /= 255
x = np.expand_dims(array, axis=0)
pred = model.predict(x)
print(pred[0])
if pred[0] >= 0.5:
    print('トゲチョウチョウウオです')
else:
    print('チョウチョウウオです')


# In[19]:


img = load_img("../data/originaldata/test3.jpg", target_size=(200, 200))
plt.imshow(img)


# In[20]:


array = img_to_array(img)
array /= 255
x = np.expand_dims(array, axis=0)
pred = model.predict(x)
print(pred[0])
if pred[0] >= 0.5:
    print('トゲチョウチョウウオです')
else:
    print('チョウチョウウオです')

