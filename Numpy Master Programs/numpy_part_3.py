import numpy as np
# NumPy library import.

# =========================================
# ⭐ PART 3 : SORTING + BROADCASTING + LINALG
# =========================================

# ---------- SORTING ----------

arr = np.array([40,10,70,20,50])
# Sorting example array.

print(np.sort(arr))
# Ascending sort return karta hai.

print(np.argsort(arr))
# Sorted order ke indexes return karta hai.

# ---------- SEARCHING ----------

nums = np.array([5,10,15,20,25,30])
# Searching example array.

print(np.where(nums>15))
# Condition true ke indexes return karta hai.

print(np.where(nums==20))
# Specific value ka index return karta hai.

print(np.nonzero(nums))
# Non-zero values ke indexes return karta hai.

# ---------- BOOLEAN MASKING ----------

mask = nums > 15
# Boolean mask create karta hai.

print(mask)
# True/False values print karta hai.

print(nums[mask])
# Mask ke basis par values filter karta hai.

# ---------- COPY vs VIEW ----------

a = np.array([1,2,3,4])
# Original array.

b = a.view()
# View original data share karta hai.

c = a.copy()
# Copy alag memory banata hai.

a[0] = 100
# Original array change.

print(a)
# Original print.

print(b)
# View bhi change dikhayega.

print(c)
# Copy same rahegi.

# ---------- BROADCASTING ----------

x = np.array([[1,2,3],[4,5,6]])
# 2D array.

print(x + 10)
# Har element me 10 add hota hai.

row = np.array([10,20,30])
# 1D row array.

print(x + row)
# Broadcasting row wise apply hota hai.

col = np.array([[100],[200]])
# Column vector.

print(x + col)
# Broadcasting column wise apply hota hai.

# ---------- MATRIX OPERATIONS ----------

m1 = np.array([[1,2],[3,4]])
# First matrix.

m2 = np.array([[5,6],[7,8]])
# Second matrix.

print(np.dot(m1,m2))
# Dot product.

print(np.matmul(m1,m2))
# Matrix multiplication.

print(m1 @ m2)
# @ operator se matrix multiplication.

print(m1.T)
# Transpose.

# ---------- LINEAR ALGEBRA ----------

print(np.linalg.det(m1))
# Determinant nikalta hai.

print(np.linalg.inv(m1))
# Inverse matrix return karta hai.

values, vectors = np.linalg.eig(m1)
# Eigen values aur vectors return karta hai.

print(values)
# Eigen values print.

print(vectors)
# Eigen vectors print.

A = np.array([[2,1],[1,3]])
# Linear equation matrix.

B = np.array([8,13])
# Result vector.

print(np.linalg.solve(A,B))
# Linear equations solve karta hai.

# ---------- RANDOM UTILITIES ----------

colors = np.array(['Red','Blue','Green','Black'])
# Choice example.

print(np.random.choice(colors))
# Random element choose karta hai.

print(np.random.choice(colors,2))
# Multiple random values.

np.random.shuffle(colors)
# Original array shuffle karta hai.

print(colors)
# Shuffled array.

print(np.random.permutation(colors))
# New shuffled copy return karta hai.
