#!/usr/bin/env python
# coding: utf-8
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)

fashion_mnist=keras.datasets.fashion_mnist
import os
print(os.getcwd())

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names=['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Ankle boot','Bag']


train_images.shape

len(train_labels)

test_images.shape

len(train_labels)

train_labels

#### now we have to preprocess this data so now we are try to load an image krishna's writes
plt.figure()
plt.imshow(train_images[0])
plt.colorbar()
plt.grid(False)
plt.show()

train_images=train_images/255.0
test_images=test_images/255.0

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)#for unshowing the grid lines in the images 
    plt.imshow(train_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()
# where are displaying classes name below

# now we have to set layers the basic represention of neural network is layer
# relu is rectfied linear network
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])




