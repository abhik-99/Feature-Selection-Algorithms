
"""
 This function discretizes the given features into 3 categories
 Please note that you can increase the number of discretized value that is obtained.

 """
def discretize_feature(feature):
  import numpy as np
  mean=np.mean(feature)
  std=np.std(feature)
  discretized=np.copy(feature)
  
  discretized[np.where(feature<(mean+std/2)) ,]=2#within 1/2 std div
  discretized[np.where(feature>(mean-std/2)),]=2#within 1/2 std div
  
  discretized[np.where(feature>(mean+std/2)),]=0#greater than half
  discretized[np.where(feature<(mean-std/2)),]=1#less than half
  
  return discretized


#Function for finding the Probability distribution of single discrete variable
def pd(x):
  import numpy as np
  rX=np.unique(x)
  pX={}
  for t in rX:
    pX[t]=round(len(np.where(x==t)[0])/len(x),4)
    
  return pX
  
#Function for finding the joint probability distribution of 2 discrete variables
def pD(x,y):
  import numpy as np
  rX=np.unique(x)
  rY=np.unique(y)
  pXY={}
  pX=0
  pY_given_X=0
  
  for t1 in rX:
    i1=np.where(x==t1)[0]
    pX=len(i1)/len(x)
    
    for t2 in rY:
      pY_given_X=len(np.where(y[i1]==t2)[0])/len(y[i1])
      pXY[(t1,t2)]=round(pX*pY_given_X,4)
    
  return pXY


  
#mutual information between two discrete random variables
def mutual_info(x,y):
  import numpy as np
  x=discretize_feature(x)
  c=0
  rX=np.unique(x)
  rY=np.unique(y)
  
  pX=pd(x)
  pY=pd(y)
  pX_Y=pD(x,y)
  
  
  
  Aentropy=0.0
  for t1 in rX:
    if pX[t1]!=0:
      Aentropy-=pX[t1]* np.log2(pX[t1])
  Bentropy=0.0
  for t1 in rY:
    if pY[t1]!=0:
      Bentropy-=pY[t1]*np.log2(pY[t1])
  
  ABentropy=0.0
  for t1 in rX:
    for t2 in rY:
      if pX_Y[(t1,t2)]!=0:
        ABentropy-=pX_Y[(t1,t2)] * np.log2(pX_Y[(t1,t2)])
  #    else:
  #     print(0)
  #print(iX_Y)
  
  return (Aentropy+Bentropy-ABentropy)/(Aentropy+Bentropy) # returns normalized mutual information gain

"""
Call this function if your objective is to pass an attribute matrix or gene set and measure the Mutual Information against a 
discretized feature 'targetClass'

"""
def mutual_info_wrapper(features,targetClass):
  import numpy as np
  mi=np.array([])
  for x in features:
    mi=np.append(mi,mutual_info(features[x],targetClass))
  return np.array(mi)