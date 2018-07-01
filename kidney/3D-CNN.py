
# coding: utf-8

# In[25]:


from keras.models import Sequential
from keras.layers import Conv3D, MaxPooling3D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.preprocessing import image


# In[31]:


import matplotlib.pyplot as plt
import numpy as np


# In[22]:


model = Sequential()
model.add(Conv3D(32, (3, 3, 3), activation='relu', input_shape=(200, 200, 26, 1)))
model.add(MaxPooling3D(pool_size=(2, 2, 1)))
model.add(Conv3D(32, (3, 3, 3), activation='relu'))
model.add(MaxPooling3D(pool_size=(2, 2, 1)))
model.add(Conv3D(64, (3, 3, 3), activation='relu'))
model.add(MaxPooling3D(pool_size=(2, 2, 1)))
model.add(Conv3D(64, (3, 3, 3), activation='relu'))
model.add(MaxPooling3D(pool_size = (2, 2, 2)))

model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))


# In[23]:


model.summary()


# In[24]:


model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# In[49]:


img00 = image.load_img('../data/kidney/R-0-000.jpg', grayscale=True, target_size=(100, 100))
x00 = image.img_to_array(img00)
img10 = image.load_img('../data/kidney/R-1-000.jpg', grayscale=True, target_size=(100, 100))
x10 = image.img_to_array(img10)
img20 = image.load_img('../data/kidney/R-2-000.jpg', grayscale=True, target_size=(100, 100))
x20 = image.img_to_array(img20)
img30 = image.load_img('../data/kidney/R-3-000.jpg', grayscale=True, target_size=(100, 100))
x30 = image.img_to_array(img30)


# In[65]:





# In[52]:


x00x10 = np.concatenate((x00, x10))
x20x30 = np.concatenate((x20, x30))
x = np.concatenate((x00x10, x20x30), axis=1)


# In[67]:


image.array_to_img(x)

