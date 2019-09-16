# image-classification-and-manipulation-in-python-machine-learning

<b>image-classifiaction on the fashion-mnist inbuilt dataset in keras library all image classifiaction operations operations perform on Fashio-MNIST dataset  </b>
### Prerequisites

What things you need to install the packages and how to install them

```
install anaconda and jupyter notebook
tensorflow ,pandas,numpy,python(pip)Preferred Installer Program (Python),amtplotlib,keras etc.
if you don't install this then you get error after
that you to install that ok
conda create -n myenv pip python=3.7
then 
activate myenv 
then you can run this project in your jupyter notebook
```

# image classifiaction program workflow
<hr>
<b>Steps for image classification in python on fashion MNIST dataset</b>
<br>
<b> Step 1</b>
 First we need to import all libraries that are listed in below images then we have to access that dataset in keras library
and then we have to give class labels to images then after that we have to train and test load the images 
     <b> how to that is given in below image </b>
<img src="https://github.com/krishnakakade1999/image-classification-and-manipulation-in-python-machine-learning/blob/master/documentation-images/Annotation%202019-09-12%20190847.png" alt="one">

<b> Step 2</b>
here we need to get images from the data for we are taking images samples in test_images or in train_images and we are taking samples of that images and we need to preprocess the data
sample Preview image is below

<img src="https://github.com/krishnakakade1999/image-classification-and-manipulation-in-python-machine-learning/blob/master/documentation-images/Annotation%202019-09-12%20190955.png" alt="two">

<b>Step 3</b>
Here we need to acess test_images and train_images and from that we are printing some of the images from the inbuilt dataset 

<img src="https://github.com/krishnakakade1999/image-classification-and-manipulation-in-python-machine-learning/blob/master/documentation-images/Annotation%202019-09-12%20191022.png" alt="three">

<b>Step 4</b>
Here we need to setup the layers for images 
<img src="https://github.com/krishnakakade1999/image-classification-and-manipulation-in-python-machine-learning/blob/master/documentation-images/Annotation%202019-09-12%20191149.png" alt="four">
*The number of epochs is a hyperparameter that defines the number times that the learning algorithm will work through the entire training dataset. One epoch means that each sample in the training dataset has had an opportunity to update the internal model parameters. An epoch is comprised of one or more batches*
<br>
<b>Step 5</b>
Here in this code we have to check accuracy of the model and making predictions on them 

<img src="https://github.com/krishnakakade1999/image-classification-and-manipulation-in-python-machine-learning/blob/master/documentation-images/Annotation%202019-09-12%20191230.png" alt="five">
<img src="https://github.com/krishnakakade1999/image-classification-and-manipulation-in-python-machine-learning/blob/master/documentation-images/Annotation%202019-09-12%20191315.png" alt="six">


<b> Step 6</b>

Now we are going to plot with prediction several image from our prediction and in which prediction we got our result with images and this model is 80% correct and predictions result prediction_result = np.argmax(predictions_single[0]) output=9
<img src="https://github.com/krishnakakade1999/image-classification-and-manipulation-in-python-machine-learning/blob/master/documentation-images/Annotation%202019-09-12%20191357.png" alt="six">
<img src="https://github.com/krishnakakade1999/image-classification-and-manipulation-in-python-machine-learning/blob/master/documentation-images/Annotation%202019-09-12%20191451.png" alt="six">

<b>for getting code you can grow through the .ipynb main code file</b>

# image manipulation in python 
<b>this section is in working state </b>

## Contributing

Please read [CONTRIBUTING.md](https://github.com/krishnakakade1999/image-classification-and-manipulation-in-python-machine-learning/blob/master/CONTRIBUTING.md) for contributing click this link.


## Author

* **Krishna kakade**  - [krishnakakade1999](https://github.com/krishnakakade1999)



