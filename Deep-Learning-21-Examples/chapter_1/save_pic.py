from tensorflow.examples.tutorials.mnist import  input_data

import scipy.misc
import os

minst = input_data.read_data_sets("MNIST_data/", one_hot=True)

save_dir = 'MNIST_data/raw/'
if os.path.exists(save_dir) is False:
    os.makedirs(save_dir)

# keep first 20 images
for i in range(20):
    image_array = minst.train.images[i,:].reshape(28,28)
    filename = save_dir+'minst_train_'+str(i)+'.jpg'
    # scipy.misc.toimage(image_array,cmin=0.0,cmax=1.0).save(filename)
    scipy.misc.imsave(filename,image_array)
