import pandas as pd
import numpy as np
test = pd.read_csv("C:\\Users\\11753\\Desktop\\train1.csv")
arr = test.values
count = 0
# label = 0
print(arr)
for i in range(100):
    for i1 in range(480):
        arr[count][2] = i
        count+=1
np.savetxt('output1.csv',arr,delimiter=',',fmt='%f,%s,%f')
# arr.tofile('output.csv', sep=', ', format='%f')


# print(arr)
