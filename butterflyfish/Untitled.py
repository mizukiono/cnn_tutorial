
# coding: utf-8

# In[3]:


from keras.preprocessing.image import ImageDataGenerator


# In[5]:


# データをつくる
train_datagen = ImageDataGenerator(rescale=1.0/255)
test_datagen = ImageDataGenerator(rescale=1.0/255)

