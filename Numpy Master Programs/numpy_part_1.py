import numpy as np
# NumPy library ko np naam se import kar rahe hain.

# ===============================
# ⭐ PART 1 : ARRAY CREATION
# ===============================

arr1 = np.array([10, 20, 30, 40, 50])
# Python list ko NumPy array me convert karta hai.

print(arr1)
# Output dekhne ke liye.

arr2 = np.array([[1,2,3],[4,5,6]])
# 2D array create karta hai.

print(arr2)
# Output dekhne ke liye.

arr3 = np.arange(0,11,2)
# Range ke andar values generate karta hai.

print(arr3)
# Output dekhne ke liye.

arr4 = np.linspace(0,1,5)
# Equal interval values banata hai.

print(arr4)
# Output dekhne ke liye.

arr5 = np.zeros((2,3))
# 0 se bhara array banata hai.

print(arr5)
# Output dekhne ke liye.

arr6 = np.ones((3,2))
# 1 se bhara array banata hai.

print(arr6)
# Output dekhne ke liye.

arr7 = np.full((2,2),99)
# Same value se array fill karta hai.

print(arr7)
# Output dekhne ke liye.

arr8 = np.eye(4)
# Identity matrix banata hai.

print(arr8)
# Output dekhne ke liye.

arr9 = np.empty((2,2))
# Uninitialized array banata hai.

print(arr9)
# Output dekhne ke liye.

np.random.seed(42)
# Random output fix karta hai.

arr10 = np.random.rand(3,3)
# Random float values.

print(arr10)
# Output dekhne ke liye.

arr11 = np.random.randint(1,100,size=(3,3))
# Random integer values.

print(arr11)
# Output dekhne ke liye.

arr12 = np.random.randn(2,3)
# Normal distribution values.

print(arr12)
# Output dekhne ke liye.

# ===============================
# ⭐ ARRAY PROPERTIES
# ===============================

print(arr2.ndim)
# Dimensions batata hai.

print(arr2.shape)
# Rows aur columns batata hai.

print(arr2.size)
# Total elements batata hai.

print(arr2.dtype)
# Data type batata hai.

print(arr2.itemsize)
# Ek element ki memory.

print(arr2.nbytes)
# Total memory usage.

# ===============================
# ⭐ INDEXING & SLICING
# ===============================

print(arr1[0])
# First element.

print(arr1[-1])
# Last element.

print(arr2[0,1])
# 2D indexing.

cube = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# 3D array.

print(cube[1,0,1])
# 3D indexing.

print(arr1[1:4])
# Basic slicing.

print(arr1[:3])
# Start se slice.

print(arr1[::2])
# Step slicing.

print(arr2[:,1])
# Second column.

print(arr2[1,:])
# Second row.

print(cube[:,:,0])
# 3D slicing.

# ===============================
# ⭐ BOOLEAN & FANCY INDEXING
# ===============================

print(arr1[arr1 > 25])
# Condition true wale elements.

print(arr11[arr11 % 2 == 0])
# Even numbers.

print(arr1[[0,2,4]])
# Fancy indexing.

print(arr2[[0,1],[2,0]])
# Specific positions.

