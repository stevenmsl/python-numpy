#%%
import numpy as np
from numpy import array
#%% Addition of arrays 
x1 = array([1,2,3,4,5])
x1_new = x1[:, np.newaxis]
# x1_new is a two-dimensional array. 
# Each element in the original one-dimensional array changed from a scalar to a vector. 
# x1_new now has 5 rows instead of just one in x1.
print (x1_new)
# should be (5,1)
print (x1_new.shape) 
# The number of elements in this one-dimensional array x2 will determine how many columns the resulting 2- dimensional array is going to have. 
x2 = array([5,4,3,2,1,7])
print (x1_new + x2)
#should be (5broadcasting,6)
print ((x1_new + x2).shape)
x2 = array([5,4,3])
print (x1_new + x2)
#should be (5,3)
print ((x1_new + x2).shape)


