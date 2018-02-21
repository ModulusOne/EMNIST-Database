# EMNIST-Database
An EMNIST database i created in CSV format (converted from a 28x28 pixel image)
Theres not too many examples for each number/character (165 for each) so would probably be best used as test input into your neural net.

I struggled to find alphabetical characters dataset in csv format ready for input into a neural network so i thought id make my own using a few images of handwritten characters i found online (forgive me as i cant find the source at the moment)

I will also add the code in which i used to convert the images into 28x28 from their original size (alot bigger)
and i will also add the code to turn the images into a csv file

Each line in the file is a seperate image, and the first number in each line is the mark of the character of the image e.g. a-,A,b-,B,c-,C,1,2,3...
Numbers are marked by their respective numbers (1=1,2=2,3=3, etc), each letter of the alphabet in capital letters is marked in capital (A,B,C,D,E,F etc) and lowercase letters are marked with a dash at the end (a-,b-,c-,d-, etc)
