import numpy as np
from scipy import misc
from imp import reload
from labfuns import *
import random


X=np.array([[23 ,43, 21,1],[33, 44, 2,1],[15 ,12, 23,2],[41, 23, 33,5],[1, 2 ,3,2],[3 ,2 ,1,33]])
labels=[1,2,3,2,1,3]
classes=np.unique(labels)
Nclasses=np.size(classes)
mu=np.zeros((Nclasses,4))
W = np.ones((6,1))/float(6)
sig = np.zeros((Nclasses,4,4))
prior= np.zeros((Nclasses,1))

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
    var=np.dot(var,np.transpose(var))
    sig[jdx]=np.diag(np.diag(var))/float(np.size(idx))

for jdx, c in enumerate(classes):
    idx = np.where(labels == c)[0]
    prior[jdx] = np.sum(W[idx])/np.sum(W[:])
print(prior.shape)    
print(sig.shape)
print(sig)
print(mu.shape)
