#                                                                       
#   ┌──────────────────────────────────────────────────────────────────┐
#   │      ######                                             ###      │
#   │      #     #   ##   #####   ##    ####  ###### #####     #       │
#   │      #     #  #  #    #    #  #  #      #        #       #       │
#   │      #     # #    #   #   #    #  ####  #####    #       #       │
#   │      #     # ######   #   ######      # #        #       #       │
#   │      #     # #    #   #   #    # #    # #        #       #       │
#   │      ######  #    #   #   #    #  ####  ######   #      ###      │
#   └──────────────────────────────────────────────────────────────────┘
#   ┌──────────────────────────────────────────────────────────────────┐
#   │                                                                  │
#   │                                                                  │
#   │  This dataset was taken from the first method of my BA thesis.   │
#   │                                                                  │
#   │  The data is available: http://dschr.de/api/collectWebgazerData  │
#   │                                                                  │
#   │Note: For the first session I did labeling by hand, which I stored│
#   │               in a new database. It is available:                │
#   │                 http://dschr.de/api/handLabeled                  │
#   │       This handlabeled session is displayed in this file.        │
#   │                                                                  │
#   │                                                                  │
#   └──────────────────────────────────────────────────────────────────┘

import sys
import json
import urllib.request
import pandas

#url = urllib.request.urlopen("http://dschr.de/api/collectWebgazerData")
url = urllib.request.urlopen("http://dschr.de/api/handLabeled")
data = json.loads(url.read().decode())
ts1 = pandas.DataFrame(data[0]["data"]) # time series 1

# setting timestamp to start by 0
ts1['timestamp'] = ts1['timestamp'].apply(lambda x: x - ts1['timestamp'][0]) 

# filter the data which is out of screen
ts1 = ts1[
        (ts1["x"] > 0) & 
        (ts1["y"] > 0) & 
        (ts1["x"] < data[0]["windowInnerWidth"]) & 
        (ts1["y"] < data[0]["windowInnerHeight"])  
        ] 

print(ts1)


# visualize the data

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1st 2D scatter plot
ts1.plot.scatter("x","y", xlabel="x", ylabel="y")

# 2nd 3D scatter plot of all data where saccades are green and fixations are orange
all3d = plt.figure().gca(projection='3d')
x_saccade = ts1[ts1["label"] == "saccade"]["x"]
y_saccade = ts1[ts1["label"] == "saccade"]["y"]
z_saccade = ts1[ts1["label"] == "saccade"]["timestamp"]
all3d.scatter(x_saccade,y_saccade,z_saccade,c='green')

x_fixation = ts1[ts1["label"] == "fixation"]["x"]
y_fixation = ts1[ts1["label"] == "fixation"]["y"]
z_fixation = ts1[ts1["label"] == "fixation"]["timestamp"]

all3d.scatter(x_fixation,y_fixation,z_fixation,c='orange')
all3d.set_xlabel('x')
all3d.set_ylabel('y')
all3d.set_zlabel('timestamp')

# 3rd 3D scatter plot of seconds 10 to 15 where saccades are green and fixations are orange
ts1 = ts1[
        (ts1["timestamp"] > 10000) &
        (ts1["timestamp"] < 15000)
        ]

filter3d = plt.figure().gca(projection='3d')
x_saccade = ts1[ts1["label"] == "saccade"]["x"]
y_saccade = ts1[ts1["label"] == "saccade"]["y"]
z_saccade = ts1[ts1["label"] == "saccade"]["timestamp"]
filter3d.scatter(x_saccade,y_saccade,z_saccade,c='green')

x_fixation = ts1[ts1["label"] == "fixation"]["x"]
y_fixation = ts1[ts1["label"] == "fixation"]["y"]
z_fixation = ts1[ts1["label"] == "fixation"]["timestamp"]

filter3d.scatter(x_fixation,y_fixation,z_fixation,c='orange')
filter3d.set_xlabel('x')
filter3d.set_ylabel('y')
filter3d.set_zlabel('timestamp')


plt.show()

