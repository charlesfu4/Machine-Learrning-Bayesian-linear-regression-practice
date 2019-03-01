import numpy as np
from scipy import misc
from imp import reload
from labfuns import *
import random


X=np.array([[23 ,43, 21],[33, 44, 2],[15 ,12, 23],[41, 23, 33],[1, 2 ,3],[3 ,2 ,1]])
labels=[1,2,3,2,1,3]
classes=np.unique(labels)
Nclasses=np.size(classes)
mu=np.zeros((Nclasses,3))
W = np.ones((6,1))/float(6)
sig = np.zeros((Nclasses,3,3))
print(classes)

for jdx,c in enumerate(classes):
    idx = np.where(labels==c)[0]
    print(idx)
    xlc=X[idx,:]
    print(xlc)
    mu[jdx]=np.sum(xlc,axis=0)/np.size(idx)
    print(mu)

for jdx,c in enumerate(classes):
    idx = np.where(labels==c)[0]
    xlc=X[idx,:]
    mu[jdx]=np.sum(xlc,axis=0)/np.size(idx)
    var=np.subtract(xlc,mu[jdx])
    sig[jdx]=np.diag(np.diag(np.dot(np.transpose(var),var)/float(np.size(idx))))
   
print(sig)   
