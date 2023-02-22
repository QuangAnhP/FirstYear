
# %% Create an array with specified data type and dimension; Change data type:

import numpy as np
x = np.array([1, 2, 3, 4, 5], dtype='f4', ndmin=1)           # 4 bytes float, 1 dimension
print(x)
print(x.dtype)
y = x.astype('i')
print(y)
print(y.dtype)

# %% Accesing indexs:

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print()
print(arr[0, 1, 2])

# %% Slicing:
    # 1D:
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print()
print(arr[1:5:2]) # start:end:steps

    # 2D:
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[0:2, 1:4])  # return from both elements the index 2nd -> 4th

# %% Copy vs View:
'''
Copy: make a new, independent array
View: use the same array with different name (changes will happen to both)
To check if arrays own their data:
    name".base": "None" if it owns the data, otherwise original data will be refered
'''

# %% Shape and Reshape:
print()
arr = np.array([[1, 2 , 3 , 4], [5, 6 , 7 , 8]])
print(arr.shape)                                    # (elements in 1st dimension, elements in 2nd dimenstion, ...)

newarr = arr.reshape(2, 2, -1)                      # pass in "-1" as a "unknown" dimesion(the computer will do it for u)
print(f"newarr looks like this: {newarr}")          # "reshape" returns a view, not a copy

print(f"Flattened newarr: {newarr.reshape(-1)}")

# %% Iteration:
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)                                      # Have to do 'n'th loop
  
print()      
for x in np.nditer(arr):
    print(x)                                        # Much better way!

    # Iterating with different data types:
print()
arr = np.array([1, 2, 3])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):           # op-dtypes to change the datatype of elements, flags=['buffered'] to create extra space to work with
  print(x)

    #Iterating with different steps (DIDN'T GET IT):
print()
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x in np.nditer(arr[:, ::2]):
  print(x)

    #Enumerated Iteration:
print()
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
  print(idx, x)                         # (Posion in dimesion 1, position in dimesion 2,...) value

# %% Joining arrays:
print()
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])

new_arr1 = np.concatenate((arr1, arr2))         #axis = 0 | <=> hstack()
print(new_arr1)

new_arr2 = np.concatenate((arr3, arr4), axis = 0)
print(new_arr2)

new_arr3 = np.concatenate((arr3, arr4), axis = 1)     
print(new_arr3)

new_arr4 = np.stack((arr1, arr2))               # <=> vstack()
print(new_arr4)

new_arr5 = np.stack((arr1, arr2), axis = 1)     # <=> dstack()
print(new_arr5)

# %% Spliting arrays:
print()

new_arr1 = np.array_split(arr1, 2)                    # splite(name of spliting array, number of splits)
print(new_arr1)

new_arr2 = np.array_split(arr1, 3)
print(new_arr2)
print(new_arr2[0])
print(new_arr2[1])
print(new_arr2[2])

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)             # <=> hsplit(arr, 3)
print(newarr)

# %% Search:
print()
arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)                        # return positions us tuple
y = np.where(arr % 2 == 0)                    # return positions of even number
print(x)
print(y)

    # Search sorted: return the value to insert a value so the list is still in sorted order
print()
arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7, side='right')     # default side is left (start counting index from left)
y = np.searchsorted(arr, [1, 3, 7, 8])        # return tuple of position
print(x)
print(y)

# %% Sort:
print()
arr1 = np.array([[4, 2, 1], [5, 9, 3]])         # Also works with str and boo(False -> True) | All arrays are sorted
print(np.sort(arr1))

# %% Filter:
    # The manual way: 
print()
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]  # manually giving T/F values.

newarr = arr[x]
print(newarr)

    # The normal way:
arr = np.array([41, 42, 43, 44])
filter_arr = []

for element in arr:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

    # The better way:
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
