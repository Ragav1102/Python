import numpy as np

array_1d = np.array([10, 20, 30, 40, 50])

array_2d = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

array_3d = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])

print("1D Array:")
print(array_1d) # Print the 1D array
print("Dimensions:", array_1d.ndim) #print the number of dimensions of the 1D array

print("2D Array:")
print(array_2d)  # Print the 2D array
print("Dimensions:", array_2d.ndim)   #print the number of dimensions of the 2D array

print("3D Array:")
print(array_3d)   #Print the 3D array
print("Dimensions:", array_3d.ndim)  #print the number of dimensions of the 3D array
print()


print( np.eye(5))  #print a 5x5 identity matrix
print(np.arange(1,13)) #print(np.arange(1,13).reshape(3,4)) #reshape the array to 3 rows and 4 columns
print(np.zeros(10)) #print zeros array of size 10
print(np.zeros((3,4))) #print a 3x4 array of zeros
print(np.ones(15)) #print a 1D array of ones with size 15
print(np.ones(10)) #print a 1D array of ones with size 10
print(np.linspace(0,1,5)) #print a linearly spaced array from 0 to 1 with 5 points
print(np.linspace(1,10,6))  #print a linearly spaced array from 1 to 10 with 6 points
print(np.random.randint(1,100,(2,3)))  #print a 2x3 array of random integers between 1 and 100
print()

arr=np.array([[1,2],[3,4],[5,6]])
print( arr.ndim) #print the number of dimensions of the array
print(arr.shape) #Print the shape of the array (number of rows and columns)
print(arr.size)  #Print the total number of elements in the array
print(arr.dtype)  #Print the data type of the elements in the array (in bytes)
print(arr.itemsize)  #Print the size of each element in the array (in bytes)
print()

#numpy array data type
arr=np.arange(1,13) #create a 1D array with elements from 1 to 12
a=arr.reshape(3,4)  #reshape the 1D array to a 2D array with 3 rows and 4 columns
print(a)
print()


arr=np.array([10,20,30,40,50,60])
print(arr[1:4])  #Print the elements of the array from index 1 to 4 (not including index 4)
print(arr[::2])  #print the elements of the array with a step of 2 (every second element)
print(arr[::-1])  #print the elements of the array in reverse order
print()

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
print()

print(arr[0:2])  #Print the first two rows of the array
print(arr[2,0])  #Print the element at row index 2 and column index 0 (which is 7)
print(arr[0])  #Print the first row of the array
print()
print(arr[0,:]) #Print the first row of the array (all columns)
print()
print(arr[:,1])  #Print the second column of the array (all rows)
print()
print(arr[1:3])  #Print the elements of the array from row index 1 to 3 (not including index 3)
print()
print(arr[0:2,1:2])  #Print the elements of the array from row index 0 to 2 (not including index 2) and column index 1 to 2 (not including index 2)
print()
print(arr[0:2,1:3])  #Print the elements of the array from row index 0 to 2 (not including index 2) and column index 1 to 3 (not including index 3) 
print()

arr=np.array([10,20,30,40,50])
a=arr>25
print (arr[a])