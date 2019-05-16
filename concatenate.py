#%%
import numpy as np 
#%%
a = np.concatenate(([1,2,3], [4,5,6]))
print (a)
# Expand dimension – the new axis is placed as 1 axis
# (6,) -> (6, 1)
b = a[:, None]
print (b)
# Expand dimension – the new axis is placed as 0 axis
# (6,) -> (1, 6)
c = a[None, :]
print (c)
print (c.shape)
#%% 
alist = ([1, 2, 3], [4, 5, 6])
[np.expand_dims(a,1) for a in alist]