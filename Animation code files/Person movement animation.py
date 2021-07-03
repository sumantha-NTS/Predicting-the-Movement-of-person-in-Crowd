### importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

### reading the dataset
data = pd.read_csv('go_track_trackspoints.csv')

# create empty lists for the x and y data
x = []
y = []


# create the figure and axes objects
fig, ax = plt.subplots(figsize=(20,10))

### Defining Animate function
def animate(i,z):
    data1 = data[data.track_id == z].reset_index(drop=True)
    y.append(data1.latitude[i])
    x.append(data1.longitude[i])
    
    ax.clear()
    ax.scatter(x, y,color='red',label='location')
    ax.legend()

### Entering the person id
z = int(input('Enter Person ID: '))

### calling animate function
ani = FuncAnimation(fig, animate, frames=len(data[data.track_id==z]), interval=10, repeat=False,fargs=[z])

### printing heading and axis names
fig.suptitle('id = {} - Person Movement'.format(z))
fig.supxlabel('Longitude')
fig.supylabel('Latitude')

### saving the gif file
ani.save('person movement.gif',writer='pillow',fps=30)
plt.show()