# Predicting-the-Movement-of-person-in-Crowd
Predicting the movement of a person in the crowd based on the movement of the crowd in particular timestamp.

## Objective:
Crowd analysis is the practice of interpreting data on the natural movement of groups or objects. Masses of bodies, particularly humans, are the subjects of these crowd tracking analyses that include how a particular crowd moves and when a movement pattern changes. Researchers use the data to predict future crowd movement, crowd density, and plan responses to potential events such as those that require evacuation routes. Applications of crowd analysis can range from video game crowd simulation to security and surveillance.

## Dataset:
Dataset is prepared by considering the latitude and longitude of the 5000 people locations which is represented in *Map.html*. Also the scatter points of the locations are visualized in the **Analysis.ipnb** file.

## Methodology:
Methodology is the methods/approachs followed to achieve the objective of the project \
**First Step:** K-Means clustering is performed on the dataset to understand the distribution of data. After performing for **k** cluster, i got the best clustering for **16 clusters** same has been explained in **.ipnb**attached file.

**Second Step:** Timestamp data of 960 people from the crowd is considered to understand the movement of the crowd. **Three level timestamp** data is considered for the study which is presented in **.ipnb** file. The timestamp is matched with the cluster points.
1. 1st level timestamp : This is the initial location of the person at timestamp-0.
2. 2nd level timestamp : New location to which person moved at timestamp-1.
3. 3rd level timestamp : New location to which person moved from previous location (2nd level timestamp location) at timestamp-2.

**Third Step:** For better understanding of the movement and cluster dependencies, **Long Short Term Memory (LSTM)** model is created as LSTM's are better in understanding the sequence data and fitted with the timestamp data of 960 people which represents the location of person, when the person is moved from one point to other during timestamp-0 to timestamp-2.


## Prediction:
Location of the person need to be matched with the cluster depending upon the distance and density of the cluster which represents that the there is high probability that person will move to place which is nearer and has high density.\
Next location of the person is predicted with the help of **Long Short Term Memory (LSTM)** model which take the input from timestamp data of the crowd.

# Reference:
1. https://www.researchgate.net/publication/330484606_Forecasting_Pedestrian_Movements_Using_Recurrent_Neural_Networks_An_Application_of_Crowd_Monitoring_Data
2. https://medium.com/decathlondevelopers/building-a-rnn-recommendation-engine-with-tensorflow-505644aa9ff3
3. https://en.wikipedia.org/wiki/Crowd_analysis
4. https://towardsdatascience.com/markov-models-and-markov-chains-explained-in-real-life-probabilistic-workout-routine-65e47b5c9a73
