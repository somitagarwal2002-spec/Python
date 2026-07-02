import numpy as np
# NumPy library ko import kar rahe hain.

# ========================================
# ⭐ PART 2 : RESHAPE + JOIN + MATH + STATS
# ========================================

arr = np.arange(1,13)
# 1 se 12 tak ka 1D array banata hai.

print(arr)
# Original array print karta hai.

# ---------- RESHAPE ----------

arr2 = arr.reshape(3,4)
# 1D array ko 3x4 me convert karta hai.

print(arr2)
# Reshaped array print karta hai.

print(arr2.T)
# Transpose return karta hai.

flat = arr2.flatten()
# Copy bana kar 1D array deta hai.

print(flat)
# Flatten array print karta hai.

rav = arr2.ravel()
# View ke form me 1D array return karta hai.

print(rav)
# Ravel array print karta hai.

temp = np.arange(6)
# Resize example ke liye array.

temp.resize((2,3))
# Original array ka size permanently change karta hai.

print(temp)
# Resize ke baad array.

# ---------- JOIN ----------

a = np.array([1,2,3])
# First array.

b = np.array([4,5,6])
# Second array.

print(np.concatenate((a,b)))
# Arrays ko end-to-end join karta hai.

print(np.hstack((a,b)))
# Horizontally join karta hai.

print(np.vstack((a,b)))
# Vertically join karta hai.

print(np.column_stack((a,b)))
# Column wise join karta hai.

print(np.row_stack((a,b)))
# Row wise join karta hai.

# ---------- SPLIT ----------

arr3 = np.arange(1,13)
# Split example array.

print(np.split(arr3,3))
# Equal parts me split karta hai.

mat = arr3.reshape(3,4)
# 2D array.

print(np.hsplit(mat,2))
# Columns split karta hai.

print(np.vsplit(mat,3))
# Rows split karta hai.

# ---------- MATHEMATICAL OPERATIONS ----------

x = np.array([10,20,30])
# Math example array.

y = np.array([1,2,3])
# Second array.

print(x+y)
# Addition.

print(x-y)
# Subtraction.

print(x*y)
# Multiplication.

print(x/y)
# Division.

print(x//y)
# Floor Division.

print(x%y)
# Modulus.

print(x**2)
# Power operation.

# ---------- UNIVERSAL FUNCTIONS ----------

print(np.sqrt(x))
# Square root.

print(np.square(y))
# Square.

print(np.abs([-5,4,-3]))
# Absolute values.

print(np.exp([1,2]))
# Exponential value.

print(np.log([1,2,3]))
# Natural logarithm.

print(np.sin([0,np.pi/2]))
# Sine values.

print(np.cos([0,np.pi]))
# Cosine values.

print(np.tan([0,np.pi/4]))
# Tangent values.

print(np.round([1.2356],2))
# Round values.

print(np.ceil([2.3,4.1]))
# Upper integer.

print(np.floor([2.9,4.8]))
# Lower integer.

# ---------- STATISTICS ----------

nums = np.array([10,20,30,40,50])
# Statistics array.

print(np.sum(nums))
# Total sum.

print(np.mean(nums))
# Average value.

print(np.median(nums))
# Median value.

print(np.std(nums))
# Standard deviation.

print(np.var(nums))
# Variance.

print(np.min(nums))
# Minimum value.

print(np.max(nums))
# Maximum value.

print(np.argmin(nums))
# Minimum index.

print(np.argmax(nums))
# Maximum index.

print(np.percentile(nums,25))
# 25th percentile.

print(np.percentile(nums,50))
# 50th percentile.

print(np.percentile(nums,75))
# 75th percentile.
