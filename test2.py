import numpy as np
arr1 =np.array([[1., -3., 15., -466.],[1.,2.,3.,4.]])

print(arr1*arr1)
print(np.square(arr1))
print(np.inner(arr1,arr1))
print(np.dot(arr1,np.transpose(arr1)))
print(np.sum(arr1*arr1,axis=0))
print(np.diag(np.sum(arr1*arr1,axis=0)))
