import numpy as np

# 1. Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# 2. Array of zeros and ones
zeros = np.zeros((2, 3))
ones = np.ones((3, 2))
print("\nZeros:\n", zeros)
print("\nOnes:\n", ones)

# 3. Create array with range
range_arr = np.arange(0, 10, 2)  # Start=0, Stop=10, Step=2
print("\nRange array:", range_arr)

# 4. Reshape array
reshaped = np.arange(12).reshape(3, 4)
print("\nReshaped array (3x4):\n", reshaped)

# 5. Basic operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("\nAddition:", a + b)
print("Multiplication:", a * b)
print("Dot product:", np.dot(a, b))

# 6. Statistics
print("\nMean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Max value:", np.max(arr))

# 7. Random numbers
random_array = np.random.rand(2, 3)  # 2x3 array with random floats
print("\nRandom array:\n", random_array)

# 8. Indexing and slicing
print("\nElement at index 2:", arr[2])
print("Slice from index 1 to 4:", arr[1:5])



/*  Array creation

Reshaping

Basic math

Stats (mean, std, max)

Random values

Indexing and slicing
*/

