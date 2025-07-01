import numpy as np
from numpy.linalg import inv, qr


arr_x_matrix = np.array([[1, 2, 3.], [4, 5, 6]])
arr_y_matrix = np.array([[6, 10], [-1, 7], [8, 9]])


print(np.dot(arr_x_matrix, arr_y_matrix))
print(f"Using the np.dot method\n")


print(arr_x_matrix.dot(arr_y_matrix))  # Same as above, np.dot
print(f"Using the array.dot method\n")


print(arr_x_matrix @ arr_y_matrix)  # And still the same as above
print("Using the @ operator\n")

arr_x = np.array([1, 2, 3])
arr_y = np.array([4, 5, 6])

print("\n")
# Simple multiplication between arrays, not matrix multiplication
print(np.multiply(arr_x, arr_y))


X = np.random.standard_normal((5, 5))

matr = X.T@X

print("\n")
print(X)

print("\n")
print(matr)
