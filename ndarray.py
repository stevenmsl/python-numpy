import numpy as np
x = np.array(
    [
     #Col 1      #Col 2
     [[ 1, 2, 3],[ 4, 5, 6]], #Row 1
     [[ 7, 8, 9],[10,11,12]], #Row 2
     [[13,14,15],[16,17,18]]  #Row 3
    ]   
    , np.int32)
# My take on this: arrange the array in a way that’s easy to read. 
# Starting by identifying the rows, then the columns, and then down
# to a single element. In this case, there are 3 rows and 2 columns. 
# And a single element itself is an array; for example [1,2,3] 
# – the number of elements in this array is the number of layers. 
# So, the shape hence is (3,2,3).       
print (x.shape) 
#Rows are gone. So the shape changes from (3,2,3) to (2,3)
#Add up Col 1 of row 1,2, and 3 to produce the first row. 
#Add up Col 2 of row 1,2, and 3 to produce the second row.
print(x.sum(0), x.sum(0).shape)
#Columns are gone. So the shape changes from (3,2,3) to (3,3)
#Add up Col 1 and Col 2 of row 1 to produce the first row. 
#Add up Col 1 and Col 2 of row 2 to produce the second row.
#Add up Col 1 and Col 2 of row 3 to produce the third row. 
print(x.sum(1), x.sum(1).shape)
#Layers are gone. So the shape changes from (3,2,3) to (3,2)
#Reduce a single element from an array to a scalar value by adding up all items in the array.
#For example, [1,2,3] in row 1, col 1 will change to 1+2+3 = 6
print(x.sum(2), x.sum(2).shape)
