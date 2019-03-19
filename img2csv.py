# helper to load data from PNG image files
import scipy.misc
# glob helps select multiple files using patterns
import glob
import numpy
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


root = 'C:/Users/BenHu/Documents/Python/neural network/handwritten character recognition/'
#accessing the master folder firstly and then the individual folders for each character
for file_name in glob.glob('handwritten_characters/small_images/*'):
    #gets individual file name of each image
    for pic in glob.glob(file_name + '/*'):     
        image_file_name = pic
        label = file_name.replace('handwritten_characters/small_images\\', '')
        
        # load image data from png files into an array
        img_array = scipy.misc.imread(image_file_name, flatten=True)
        # reshape from 28x28 to list of 784 values, invert values
        img_array  = 255.0 - img_array.reshape(784)

        # append label and image data  to test data set
        #first value of list will be the correct label
        record = numpy.append(label,img_array)
        
        #opening the csv file ready to write to
        csv = open('emnist_dataset/EMNIST_dataset.csv', "a")
        
        #viewinng each seperate img seperately ready to append to csv file
        for single in record:
            #each pixel value is written seperated by comma, first value is label
            csv.write(single + ',')
        
        #when individual img is donne a new line is written ready for next img data
        csv.write('\n')
        csv.close()