import numpy as np
arr = np.arange(9).reshape((3,3))
print(arr)
arr1 = np.concatenate([arr,arr],axis = 1)
print(arr1)
arr1 = np.concatenate([arr,arr],axis = 0)
print(arr1)