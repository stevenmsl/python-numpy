import numpy as np
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x.shape)
# j - i = 7 -1 = 6, where i is the starting index, and j is the stopping index
# m = (j -i) / k = 6 /2 = 3, where k is the step, and m is the number of elements selected You should have 3 elements selected 
print(x[1:7:2]) # [1 3 5]
# m = (j -i) / k + remainder =  (8-1)/2 + 1 = 4  
print(x[1:8:2]) # [1 3 5 7]
print(x[1:9:2]) # [1 3 5 7]
#negative indexes
# this is the same as print(x[8:10:1])
# Total number of elements is 10. 10 -2 = 8. So the starting index is 8.
#m = (j – i) / 1 = (10 – 8) /1 =2. The result should have 2 elements.    
print(x[-2:10]) #[8,9]
#same as print(x[7:3:-1])
# m = |3-7|/|-1|= 4 
print(x[-3:3:-1]) #[7 6 5 4]
# j = n = 10, k = 1
# same as print(x[5:10:1])
print(x[5:]) #[5,6,7,8,9]
x = np.array( [[[1],[2],[3]], [[4],[5],[6]]])
print (x)
print(x.shape)