
# coding: utf-8

# In[1]:


from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential, Model
from keras.layers import Input, Activation, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import SGD
from keras.callbacks import CSVLogger
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


# In[2]:


# "failed to create cublas handle"
# と出る場合はGPUメモリの不足っぽいので制限してやればよい

# TensorFlowのGPUメモリ使用量の制限
from keras.backend.tensorflow_backend import set_session
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.5
set_session(tf.Session(config=config))


# In[3]:


img_width = 150
img_height = 150
train_data_dir = "../data/butterflyfish/train"
val_data_dir = "../data/butterflyfish/validation/"

train_samples = 200
val_samples = 60
epochs = 100


# In[4]:


input_tensor = Input(shape=(150, 150, 3))
vgg16_model = VGG16(include_top=False, weights='imagenet', input_tensor=input_tensor)


# In[5]:


# vgg16_model.summary()


# In[6]:


# VGGの下につなぐFC層を構築
top_model = Sequential()
top_model.add(Flatten(input_shape=vgg16_model.output_shape[1:]))
# Flattenへの入力指定はbatch数を除いておく
top_model.add(Dense(256, activation='relu'))
top_model.add(Dropout(0.5))
top_model.add(Dense(1, activation='sigmoid'))


# In[7]:


top_model.summary()


# In[8]:


model = Model(inputs=vgg16_model.input, outputs=top_model(vgg16_model.output))


# In[9]:


model.summary()


# In[10]:


for layer in model.layers[:15]:
    layer.trainable = False


# In[11]:


model.summary()


# In[12]:


model.compile(loss='binary_crossentropy', optimizer=SGD(lr=0.0001, momentum=0.9), metrics=['accuracy'])


# In[13]:


# データをつくる
train_datagen = ImageDataGenerator(rescale=1.0/255, rotation_range=90, width_shift_range=0.2, height_shift_range=0.2,
                                  horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1.0/255)


# In[14]:


train_generator = train_datagen.flow_from_directory(train_data_dir, target_size=(150,150),
                                                    batch_size=32, class_mode='binary')
validation_generator = test_datagen.flow_from_directory(val_data_dir, target_size=(150,150),
                                                    batch_size=32, class_mode='binary')


# In[15]:


print(train_generator.class_indices)


# In[ ]:


history = model.fit_generator(train_generator, epochs=epochs, verbose=1, validation_data=validation_generator)


# In[ ]:


plt.plot(range(1, epochs+1), history.history['acc'], label="training")
plt.plot(range(1, epochs+1), history.history['val_acc'], label="validation")
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

