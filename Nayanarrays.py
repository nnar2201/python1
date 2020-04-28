'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # “as” lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
fig.show()

# Read the data into an array
img = plt.imread(filename)




###
# Make a rectangle of pixels yellow
###

height = len(img)
width = len(img[0])
for row in range(420, 470):
    for column in range(135, 162):
        img[row][column] = [0, 255, 0] # red + green = yellow
        
        
        
        

img = plt.imread(filename)

###
# Change a region if condition is True
###

height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta


for r in range(420,470):
    for c in range(width):
        if sum(img[r][c])>300: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
            
            
        
if __name__ == ¨__main__¨:
  image = make_mask(100,70,10)
  fig, ax = plt.subplots(1, 1)
  ax.imshow(image)
  fig.show()
