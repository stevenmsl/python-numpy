#%%
import numpy as np
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x.shape)
#%% Positive Indexes
# j - i = 7 -1 = 6, where i is the starting index, and j is the stopping index
# m = (j -i) / k = 6 /2 = 3, where k is the step, and m is the number of elements selected You should have 3 elements selected 
print(x[1:7:2]) # [1 3 5]
# m = (j -i) / k + remainder =  (8-1)/2 + 1 = 4  
print(x[1:8:2]) # [1 3 5 7]
print(x[1:9:2]) # [1 3 5 7]
#%% Negative indexes
# this is the same as print(x[8:10:1])
# Total number of elements is 10. 10 -2 = 8. So the starting index is 8.
#m = (j – i) / 1 = (10 – 8) /1 =2. The result should have 2 elements.    
print(x[-2:10]) #[8,9]
#same as print(x[7:3:-1])
# m = |3-7|/|-1|= 4 
print(x[-3:3:-1]) #[7 6 5 4]
#%% Ellipsis
# j = n = 10, k = 1
# same as print(x[5:10:1])
print(x[5:]) #[5,6,7,8,9]
#%%
x = np.array( 
    [
      #C1 #C2 #C3
     [[1],[2],[3]], #Row 1 
     [[4],[5],[6]]  #Row 2
    ])
print(x.shape) #(2,3,1)
print(x.ndim) 
print(x[1:2]) #pull the first row
print(x[1:2].shape) #(1,3,1)
#%%
x = np.array( 
    [
      #C1 #C2 #C3
     [[1,10],[2,20],[3,30]], #Row 1 
     [[4,40],[5,50],[6,60]]  #Row 2
    ])
print(x.shape) #should be (2,3,2)
# Keep the rows and columns structure-wise
# and then select the first element in the third dimension
print(x[...,0])
print(x[...,0].shape) # The third dimension is gone – the array changes to a scalar. For example [1,10] -> 1

#%% new axis
x = np.array(
    [
     [[1,10],[2,20],[3,30]], 
     [[4,40],[5,50],[6,60]]
    ]
    )
print(x[:,np.newaxis,:,:].shape)
# expand by one unit-length dimension between first dimension and the second -  
# so everything after the first dimension got pushed down the hierarch 
# [
#  #Col 1    
#  [[[ 1 10] [ 2 20] [ 3 30]]] #Row 1 
#  [[[ 4 40] [ 5 50] [ 6 60]]] #Row 2 
# ]

print(x[:,np.newaxis,:,:])
#%% Advanced indexing 
x = np.array(
    [
     [1, 2], 
     [3, 4], 
     [5, 6]
    ])
print(x.shape) #should be (3,2)
#The row index is [0,1,2] -
#so what this is saying is that we want to select row 1, row 2, and row 3.
#The column index is [0,1,0]
#so for row 1, I will pick col 1, for row 2 col 2, and for row 3 col 1.
print(x[[0,1,2],[0,1,0]]) 
#%% non broadcasting
x = np.array(
             [
              [ 0,  1,  2],
              [ 3,  4,  5],
              [ 6,  7,  8],
              [ 9, 10, 11]])
rows = np.array(
    [
     [ 0, 0], #This will constitute the first row of the resulting away. 
              #Pick something from row 1 as col 1. Pick from row 1 again from the col 2. 
     [ 3, 3]  #Pick from row 4 this time
    ])
cols = np.array(
    [
     [0, 2], #Pick col 1 and col 3 from the corresponding row being specified in the row index.   
     [0, 2]
    ]
    )

print(x[rows,cols])
#%% broadcasting
x = np.array(
             [
              [ 0,  1,  2],
              [ 3,  4,  5],
              [ 6,  7,  8],
              [ 9, 10, 11]
             ])
rows = np.array([0,3])
cols = np.array([0,2])

# The resulting array will have just one row [0, 11]
# with 0 comes from the first col of the firs row, and 11 from the third col of the 4th row 
print(x[rows,cols]) 
# rows[:, np.newaxis] becomes a 2 dimensional array
# shape: (2,1)
# [
#  [0] # row 1 - Elements will come from the first row of x. Which columns though? [0,2]  – the first and the third column  
#  [3] # row 2 - Elements will come from the fourth row of x.
# ]
print(x[rows[:, np.newaxis],cols])
print(x[np.ix_(rows,cols)])

