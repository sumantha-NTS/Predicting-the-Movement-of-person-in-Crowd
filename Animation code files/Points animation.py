### importing the libraries
from random import randint
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation

### reading the dataset
data = pd.read_csv('../map_data.csv',index_col='id',usecols=['id','Latitude','Longitude'])

# create empty lists for the x and y data
x = []
y = []

# create the figure and axes objects
fig, ax = plt.subplots(figsize=(17,10))

### reading the image
image = plt.imread('map.png')

### Defining Animate function
def animate(i):
    pt = randint(1,4500) # grab a random integer to be the next y-value in the animation
    y.append(data.Latitude[pt:pt+100])
    x.append(data.Longitude[pt:pt+100])
    ax.clear()
    ax.imshow(image,extent=[-99.7116,-99.704908,32.4676,32.4709])
    ax.scatter(x, y,color='red')
    ax.set_xlim([-99.7116, -99.704908])
    ax.set_ylim([32.4676, 32.4709])

### calling the animate function
ani = FuncAnimation(fig, animate, frames=200, interval=10, repeat=False)

### printing the heading and axis names
fig.suptitle('Animation', fontsize=14)
fig.supxlabel('Longitude')
fig.supylabel('Latitude')

### saving the file
#ani.save('../Animation/video.gif',writer='pillow',fps=30)
plt.show()