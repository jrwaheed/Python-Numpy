import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.cm as cm

# Create an array with start, end and step
points = np.arange(-5, 5, .5)
points_two = np.arange(10, 20, 1)
# print(points)

xs, xy = np.meshgrid(points, points)


z = np.sqrt(xs**2 + xy**2)

plt.imshow(z, cmap='gray', extent=[-5, 5, -5, 5])

result = np.where(z > 5, z, 0)
plt.imshow(result, cmap='gray', extent=[-5, 5, -5, 5])

arr_for_sum = np.random.standard_normal((4, 4))
arr_for_bool = arr_for_sum > 0


# Method for boolean arrays

boolean_arr = np.random.standard_normal(100)
print((boolean_arr > 0).sum())

# Sorting by row and by column
sorted_arr = np.random.standard_normal((5, 3))
sorted_arr.sort(axis=0)
print(sorted_arr)

# Save an array
saved_arr = np.zeros((5, 3))
np.save('saved_arr.npy', saved_arr)


# Read the binary file and close with 'with' keyword
with open('saved_arr.npy', 'rb') as data:  # 'rb' for read binary
    loaded_arr = np.load(data)

print(loaded_arr)
