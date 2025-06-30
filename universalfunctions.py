import numpy as np

simple_arr = np.array([1, 2, 3, 4, 5, 6])
simple_arr_two = np.array([[10, 10, 10], [20, 20, 20], [30, 30, 30], [
                          # Random numbers. (Actually pseudo-random numbers)
                          40, 40, 40], [50, 50, 50], [60, 60, 60]])

print(np.random.standard_normal(size=(2, 2)))

# Universal function examples (sqrt and exp). Also called ufunc's
print(f"{np.sqrt(simple_arr)} \n")
print(np.exp(simple_arr))

# binary ufuncs
binary_one = np.random.standard_normal(size=(1, 6))
binary_two = np.random.standard_normal(size=(1, 6))

binary_result = np.maximum(binary_one, binary_two)
print(binary_result)
