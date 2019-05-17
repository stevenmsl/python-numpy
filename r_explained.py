#%%
import numpy as np 
#%% 
# goal: np.r_['0,2,0', [1,2,3], [4,5,6]]
a = np.array([1,2,3])
b = np.array([4,5,6])
# start with the third argument in '0,2,0', which is 0
# A third argument of ‘0’ would place the 1’s at the end of the array shape.
# So what this mean is that you would expand the shape from (3,) to (3,1)
# - this is literally what it means to place 1’s at the end of array shape
a = a[:, None]
b = b[:, None]
print (a)
print (b)
print (a.shape, b.shape)
# Next look at the second argument, which is the minimum number of dimensions to force the entries to. 
# In this case it's (3, 1)  – you already have two dimensions. Nothing further needs to be done here.
# Now onto the first argument, stack along the 0 axis.
c = np.concatenate((a,b),axis=0)
print (c)
# goal: np.r_['1,2,0', [1,2,3], [4,5,6]]
# same as above other than you stack along the 1 axis 
c = np.concatenate((a,b),axis=1)
print (c)



