### Author:
Abhik Banerjee
### Implemented in:
*_Python 3.6_*

## Information Gain Implementation
It is one of the most common forms of feature usefullness evaluation methods used in Decision Trees. It provides us with a measure of how much a certain feature contributes towards the classification of the target feature. Another Popular method used is GINI Index.

## Mutual Information Gain Implementation.
There is not much difference between Information Gain and Mutual Information Gain Algorithms in terms of how they are implemented. The difference lies in the fact that while Information Gain is used to get a measure against target class, mutual information gain gives the measure of how much teo different features in a dataset provide information about one another. 
This can be usefull in elimination of duplicate features or features which are very similar.


## ReliefF Implementation
ReliefF is an Algorithm usde for getting the scores of Features in a Dataset on basis of which the relevance of the feature towards the Classification of an Observation can be measured. Relief is the first variant of the Algorithm developed by Kira and Rendell way back in 1992. Since then, 6 variants of Relief Algorithm (from ReliefA to ReliefF) have been developed.
### Advantage of ReliefF over Relief:
1. Relief Algorithm takes into account only the *first* "hit" and first "miss". ReliefF, however, takes into account *first "n"* "hits" and "misses" which improves reliability.
2. Original Relief Algorithm was used for Feature Selection for only _Two-Class Classification Dataset_. ReliefF can be used for _Multi-Class Classification Dataset_.


### How to Use the Code:
#### Arguments to Pass: 
*df* :- Dataset. Pass the dataset as a _DataFrame_ to the method. Make sure the Column names are Numeric.
*n_neighbours* :- The number of _nearest_ "hits" and "misses" to take into Account.
*instances_to_select* :- Instead of running the process exhaustively like Relief, ReliefF randomly selects a specified number of instances.

#### Please note:
This Python Implementations of ReliefF, Mutual Information and Information Gain were written by me. However, the Algorithms and concepts have been taken from a certain Papers and Wikipedia which has been mentioned as a Documentation within the code itself. My code is far from perfect. As such, if you can improve upon it, I encourage you to do so.
- Abhik Banerjee
