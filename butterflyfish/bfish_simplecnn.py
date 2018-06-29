
# coding: utf-8

# In[1]:


from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt


# In[2]:


epochs = 100


# In[3]:


# データをつくる
train_datagen = ImageDataGenerator(rescale=1.0/255, rotation_range=90, width_shift_range=0.2, height_shift_range=0.2)
test_datagen = ImageDataGenerator(rescale=1.0/255)


# In[4]:


train_generator = train_datagen.flow_from_directory('../data/butterflyfish/train', target_size=(150,150), 
                                                    batch_size=32, class_mode='binary')


# In[5]:


validation_generator = test_datagen.flow_from_directory('../data/butterflyfish/validation', target_size=(150,150), 
                                                        batch_size=32, class_mode='binary')


# In[6]:


# モデルをつくる
model = Sequential()
model.add(Convolution2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Convolution2D(32, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Convolution2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))


# In[7]:


model.summary()


# In[8]:


model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# In[9]:


history = model.fit_generator(train_generator, epochs=epochs, verbose=1, validation_data=validation_generator)


# In[10]:


plt.plot(range(1, epochs+1), history.history['acc'], label="training")
plt.plot(range(1, epochs+1), history.history['val_acc'], label="validation")
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

