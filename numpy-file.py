#Lab 6 - Numpy Arrays, Attribute Functions

import numpy as np


#create an array with 2 lists of 2x3 arrays

t = np.array([
    [
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [3, 4, 5],
        [2, 5, 1]
    ]
    
])

#print the array
print(t)

#to determine the shape of an array
#use the attribute <array>.shape

#determine the shape of the array 't'
#print the value
print(f"The array 't' has shape of {t.shape}.")

#to determine the number of elements inside an array
#use the attribute <array>.size

#determine the size of the 't' array
print(f"The 't' array has {t.size} elements inside it.")

#create a 3x3 array with 2 elements in the list

tt = np.array([
    [
        [5, 6, 7],
        [3, 4, 6],
        [17, 3, 0]
    ],
    [
        [3, 6, 7],
        [6, 1, 67],
        [9, 1, -65]
    ]
])
print(f"The array 'tt' is this...\n{tt}.")
#determine the shape of the array
#use the attribute <array>.shape
print(f"The array 'tt' has a shape {tt.shape}.")

#determine the size of the array 'tt'
#use the attribute <array>.size
print(f"The array 'tt' has size of {tt.size}.")

#determine the depth or dimensions of the array 'tt'
#use the attribute <array>.ndim

print(f"The array 'tt' has dimensions of {tt.ndim}.")

#determine the data type of the elements in the array 'tt'
#use the attribute <array>.dtype
print(f"The array 'tt' has a data type of {tt.dtype}.")

#assign the dtype of the array 'tt' as a floating integer
tt = np.array([
    [
        [5, 6, 7],
        [3, 4, 6],
        [17, 3, 0]
    ],
    [
        [3, 6, 7],
        [6, 1, 67],
        [9, 1, -65]
    ]
], dtype=float)

#now use attribute dtype to determine data type for 'tt'
print(f"The array 'tt' has a data type of {tt.dtype}.")
