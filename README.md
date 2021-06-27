# Predicting-the-Movement-of-person-in-Crowd
Predicting the movement of a person in the crowd based on the movement of the crowd in particular timestamp.

## Objective:

## Dataset:
Dataset is prepared by considering the latitude and longitude of the 5000 people locations which is represented in *Map.html*. Also the scatter points of the locations are visualized in the **Analysis.ipnb** file.

## Methodology:
**First Step:** K-Means clustering is performed on the dataset to understand the data. After performing for **k** cluster, i got the best clustering for **16 clusters** same has been explained in **.ipnb**attached file.

**Second Step:** Timestamp data of 960 people from the crowd is considered to understand the movement of the crowd. Three level timestamp data is considered for the study which is presented in **.ipnb** file.

**Third Step:** 

## Prediction:
Location of the person need to be matched with the cluster depending upon the distance and density of the cluster which represents that the there is high probability that person will move to place which is nearer and has high density.
Next location of the person is predicted with the help of **Long Short Term Memory (LSTM)** model which take the input from timestamp data of the crowd.

# Reference:
1. https://www.researchgate.net/publication/330484606_Forecasting_Pedestrian_Movements_Using_Recurrent_Neural_Networks_An_Application_of_Crowd_Monitoring_Data
2. https://medium.com/decathlondevelopers/building-a-rnn-recommendation-engine-with-tensorflow-505644aa9ff3
