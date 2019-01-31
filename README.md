# ReliefF Implementation
ReliefF is an Algorithm usde for getting the scores of Features in a Dataset on basis of which the relevance of the feature towards the Classification of an Observation can be measured. Relief is the first variant of the Algorithm developed by Kira and Rendell way back in 1992. Since then, 6 variants of Relief Algorithm (from ReliefA to ReliefF) have been developed.
### Implemented in:
*_Python 3.6_*
## Advantage of ReliefF over Relief:
1. Relief Algorithm takes into account only the *first* "hit" and first "miss". ReliefF, however, takes into account *first "n"* "hits" and "misses" which improves reliability.
2. Original Relief Algorithm was used for Feature Selection for only _Two-Class Classification Dataset_. ReliefF can be used for _Multi-Class Classification Dataset_.


## How to Use the Code:
### Arguments to Pass: 
*df* :- Dataset. Pass the dataset as a _DataFrame_ to the method. Make sure the Column names are Numeric.
*n_neighbours* :- The number of _nearest_ "hits" and "misses" to take into Account.
*instances_to_select* :- Instead of running the process exhaustively like Relief, ReliefF randomly selects a specified number of instances.

#### Please note:
This Python Implementation of ReliefF was written by me. However, the Algorithm and concepts have been taken from a certain Paper which has been mentioned as a Documentation within the code itself. My code is far from perfect. As such, if you can improve upon it, I encourage you to do so.
