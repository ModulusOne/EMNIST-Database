# resize an image using the PIL image library

import os.path
from PIL import Image
import glob

#root directory in which this file sits - change to your own
root = 'C:/Users/BenHu/Documents/Python/neural network/handwritten character recognition/'

#accessing the master folder of large images first and then the individual folders for each character
for file_name in glob.glob('emnist_dataset/large_images/*'):
    #creates a folder name which we will later save modified images in
    folder_name = file_name.replace('emnist_dataset/large_images\\'  , '')
    i = 0
    for pic in glob.glob(file_name + '/*'):

        # open an image file (.bmp,.jpg,.png,.gif) you have in the working folder
        im1 = Image.open(pic)
        # adjust width and height to your needs
        width = 28
        height = 28
        
        # images are resized in diff ways to give 4 differennt images from the initial onne
        im2 = im1.resize((width, height), Image.NEAREST)      # use nearest neighbour
        im3 = im1.resize((width, height), Image.BILINEAR)     # linear interpolation in a 2x2 environment
        im4 = im1.resize((width, height), Image.BICUBIC)      # cubic spline interpolation in a 4x4 environment
        im5 = im1.resize((width, height), Image.ANTIALIAS)    # best down-sizing filter
        
        #makes a directory if one doesnt already exist
        if not os.path.exists(root + 'emnist_dataset/small_images/' + folder_name):
            os.makedirs(root + 'emnist_dataset/small_images/' + folder_name)
            

        ext = ".png"
        im2.save(root + "emnist_dataset/small_images/" + folder_name + '/' + str(i) + ext)
        i += 1
        im3.save(root + "emnist_dataset/small_images/" + folder_name + '/' +  str(i) + ext)
        i += 1
        im4.save(root + "emnist_dataset/small_images/" + folder_name + '/' +  str(i) + ext)
        i += 1
        im5.save(root + "emnist_dataset/small_images/" + folder_name + '/' +  str(i) +  ext)