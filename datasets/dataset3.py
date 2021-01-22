#                                                                       
#   ┌──────────────────────────────────────────────────────────────────┐
#   │  ######                                             ### ### ###  │
#   │  #     #   ##   #####   ##    ####  ###### #####     #   #   #   │
#   │  #     #  #  #    #    #  #  #      #        #       #   #   #   │
#   │  #     # #    #   #   #    #  ####  #####    #       #   #   #   │
#   │  #     # ######   #   ######      # #        #       #   #   #   │
#   │  #     # #    #   #   #    # #    # #        #       #   #   #   │
#   │  ######  #    #   #   #    #  ####  ######   #      ### ### ###  │
#   └──────────────────────────────────────────────────────────────────┘
#   ┌──────────────────────────────────────────────────────────────────┐
#   │                                                                  │
#   │                                                                  │
#   │           This dataset was taken from our zights-demo.           │
#   │(https://zights-mvp.herokuapp.com/5fdb337266dff00015445c12/dashboa│
#   │                           rd/sessions)                           │
#   │                                                                  │
#   │               The data of this study is available:               │
#   │                 http://dschr.de/api/platformData                 │
#   │        Note: In this file the first session is displayed.        │
#   │                                                                  │
#   │                                                                  │
#   │                                                                  │
#   └──────────────────────────────────────────────────────────────────┘

import sys
import json
import urllib.request
import pandas

# load data from rest api
url = urllib.request.urlopen("http://dschr.de/api/platformData")
data = json.loads(url.read().decode())
ts1 = pandas.DataFrame(data["sessions"][0]["recording"]) # time series 1

# setting timestamp to start by 0
ts1['timestamp'] = ts1['timestamp'].apply(lambda x: x - ts1['timestamp'][0]) 

# filter the data which is out of screen
ts1 = ts1[
        (ts1["x"] > 0) & 
        (ts1["y"] > 0) & 
        (ts1["x"] < data["sessions"][0]["displayDimensions"]["width"]) & 
        (ts1["y"] < data["sessions"][0]["displayDimensions"]["height"])         
        ] 

print(ts1)


# visualize the data

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1st 2D scatter plot
ts1.plot.scatter("x","y", xlabel="x", ylabel="y")

# 2nd 3D scatter plot of all data (all points are blue, because we have no labels)
all3d = plt.figure().gca(projection='3d')
x_saccade = ts1[ts1["label"] == ""]["x"]
y_saccade = ts1[ts1["label"] == ""]["y"]
z_saccade = ts1[ts1["label"] == ""]["timestamp"]
all3d.scatter(x_saccade,y_saccade,z_saccade,c='blue')

x_fixation = ts1[ts1["label"] == ""]["x"]
y_fixation = ts1[ts1["label"] == ""]["y"]
z_fixation = ts1[ts1["label"] == ""]["timestamp"]

all3d.scatter(x_fixation,y_fixation,z_fixation,c='blue')
all3d.set_xlabel('x')
all3d.set_ylabel('y')
all3d.set_zlabel('timestamp')

# 3rd 3D scatter plot of seconds 10 to 15 (all points are blue, because we have no labels)
ts1 = ts1[
        (ts1["timestamp"] > 10000) &
        (ts1["timestamp"] < 15000)
        ]

filter3d = plt.figure().gca(projection='3d')
x_saccade = ts1[ts1["label"] == ""]["x"]
y_saccade = ts1[ts1["label"] == ""]["y"]
z_saccade = ts1[ts1["label"] == ""]["timestamp"]
filter3d.scatter(x_saccade,y_saccade,z_saccade,c='blue')

x_fixation = ts1[ts1["label"] == ""]["x"]
y_fixation = ts1[ts1["label"] == ""]["y"]
z_fixation = ts1[ts1["label"] == ""]["timestamp"]

filter3d.scatter(x_fixation,y_fixation,z_fixation,c='blue')
filter3d.set_xlabel('x')
filter3d.set_ylabel('y')
filter3d.set_zlabel('timestamp')


plt.show()

