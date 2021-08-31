[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/thisistaimur/TUB_WS_FinalProject/HEAD)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/thisistaimur/TUB_WU_FinalProject/blob/main/index.ipynb)


# Density-based clustering of webcam-based eyetracking data into fixations  using Machine Learning


### Authored by: Taimur Khan, Benjamin Nava Höer
**Final Project for TU Berlin WU'20 course: Machine Learning using Python - Theory and Application**

**Source-code: [Github](https://github.com/thisistaimur/TUB_WU_FinalProject)**

___**Licensed under:**___ [Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/)
## Summary

Machine Learning(ML) methods have shown promissing results in the classification of eyetracking data into fixations and saccades. However, present ML models for such classsification are trained with data from eyetracking hardware, and hence do not perform well on webcam-based eyetrackng. Additonally, no labeled (fixations and saccades) dataset exists for webcam-based eyetracking data.

Here, an unlabeled dataset of an eyetracking timeseries was clustered using the spatial clustering algorithms DBSCAN and OPTICS, as well as the spatio-temporal clustering algorithms ST-DBSCAN and ST-OPTICS. The silhouette score was not found to be the appropriate evaluation metric for the obtained clusterings. A second, heuristically hand-labelled dataset was used to evaluate the accuracy of the most promising algorithms ST-DBSCAN and ST-OPTICS. 75.38% of the predicted labels in ST-OPTICS and 85.02% with ST-DBSCAN matched the provided labels, making these a valuable tool for the labeling of webcam-based eyetracking data.

Although ST-DBSCAN shows higher accuracy value, it must be noted that the hand-labeled dataset used to measure model accuracy contains equally spread out gaze points, as compared to "wild" eyetracking datasets where the data is not as equally spaced. The resulting variance in cluster densities might cause an accuracy loss for ST-DBSCAN in "wild" data. A further analysis of hand labaled datasets is suggested to create a better understanding of the performance difference between ST-OPTICS and ST-DBSCAN.

___Fig 1:___ Data comparison between Webgazer and Tobii-Pro X3-120 showing the different in data quality and noise.


<img src="resources\problem.png" alt="Drawing" style="width: 700px;"/>

## Folder Structure
```
+-- ipynb_checpoints --> Checkpoints of the Jupyter notebook
+-- datasets
|   +-- adsata-golden.json
|   +-- dataset1.py
|   +-- dataset2.py
|   +-- dataset3.py
+-- research
|   +-- PDFs for all project related research
+-- index.ipynb --> main Jupyter notebook
+-- requirements.txt --> dependencies for Binder containers
```

## Project Members
* Taimur Khan
* Benjamin Nava Höer
