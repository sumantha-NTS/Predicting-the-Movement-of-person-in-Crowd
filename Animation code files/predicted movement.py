### importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tensorflow as tf
import numpy as np

### importing LSTM model
model = tf.keras.models.load_model('my_model.h5')

### input location
lat = float(input('Enter the latitude :'))
lon = float(input('Enter the latitude :'))

### creating the array of input
inp = np.array([lat,lon])

### predicting for input data
predict = model.predict(inp.reshape(1,1,2))

# create empty lists for the x and y data
x = []
y = []

# create the figure and axes objects
fig, ax = plt.subplots(figsize=(17,10))
image = plt.imread('map1.png')

### Defining Animate function
def animate(i,predict,inp):
     y.append(predict[0][i][0])
     x.append(predict[0][i][1])
    
     ax.clear()
     ax.imshow(image,extent=[-37.107572,-37.049679,-10.924259,-10.900281])
     ax.scatter(inp[1],inp[0],color='blue',marker='*',s=150,label='location')
     ax.scatter(x, y,color='red',label='prediction')
     ax.legend()
     ax.set_ylim(-10.924259,-10.900281)
     ax.set_xlim(-37.107572,-37.049679)     

### calling the animate function
ani = FuncAnimation(fig, animate, frames=len(predict[0]), interval=10, repeat=False,fargs=[predict,inp])

### Heading and axis names
fig.suptitle('Prediction')
fig.supxlabel('Longitude')
fig.supylabel('Latitude')

### saving the gif file
ani.save('Prediction movement.gif',writer='pillow',fps=30)
plt.show()