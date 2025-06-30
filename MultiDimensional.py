import numpy as np

# Multidimensional indexing syntax for Numpy arrays will not work with regular
# Python lists

simple_arr = np.array([1, 2, 3, 4, 5, 6])
simple_arr_two = np.array([[10, 10, 10], [20, 20, 20], [30, 30, 30], [
                          40, 40, 40], [50, 50, 50], [60, 60, 60]])

# arr_one = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
# print(arr_one[1][2])


# arr_two = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr_two[0][1][0])

# print(arr_one[:2, 1:])

names = np.array(["Bob", "Alex", "Will", "Randy", "Will", "Joe", "Tim"])

print(names == "Will")

# Boolean inversion
print(~(names == "Will"))

# Fancy indexing
fancy_arr = np.zeros((8, 4))

for ele in range(8):
    fancy_arr[ele] = ele

print(fancy_arr)

print(fancy_arr[[1, 3, 5, 7]])

# Reshape method
new_arr = np.arange(32)
print(new_arr)
print(new_arr.reshape(8, 4))


# Transpose method. Note the use of "T" and not "transpose"
new_arr = np.arange(32).reshape(8, 4)
print(new_arr)


# Dot method. Which is equivalent to matrix multiplication
print(simple_arr_two)
print(np.dot(simple_arr, simple_arr_two))
