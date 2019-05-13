#%% 
import numpy as np
#%%
# -1:1:6j start with -1 and end with 1. 
# start with -1 and end with 1. You have 6 data points in total all evenly spaced.
# (1-(-1))/5 = 0.4  
# [-1. , -0.6, -0.2,  0.2,  0.6,  1.]
# and you can then concatenate with other arrays or scalars to form a bigger array 
np.r_[-1:1:6j, [0]*3, 5, 6]

#%%
a = np.array([[0, 1, 2], [3, 4, 5]])
print(np.r_['-1',a,a,a])
# Array a has 3 columns. So, in the end after the concatenation along the y axis 
# you are going to have 9 columns. 
# (2,9) 
print(np.r_['-1',a,a,a].shape)

#%% minimum number of dimensions
a = np.r_['0', [1,2,3], [4,5,6]]
print(a)
#(6,)
print(a.shape)
a = np.r_['0,2', [1,2,3], [4,5,6]]
# Should be a 2-dimensional array
print(a)
#(2,3)
print(a.shape)
# Should be a 3-dimensional array
a = np.r_['0,3', [1,2,3], [4,5,6]]
print(a)
#(2, 1 , 3)
print(a.shape)
#%% axis contains the start of the arrays
a = np.r_['0,2,-1', [1,2,3], [4,5,6]]
# Should be a 2-dimensional array
print(a)
#(2,3)
print(a.shape)

a = np.r_['0,2,0', [1,2,3], [4,5,6]]
# Should be a 2-dimensional array
print(a)
#(6,1)
print(a.shape)

