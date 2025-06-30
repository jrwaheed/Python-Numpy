import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.cm as cm

# Create an array with start, end and step
points = np.arange(-5, 5, .5)
points_two = np.arange(10, 20, 1)
print(points)

xs, xy = np.meshgrid(points, points)


z = np.sqrt(xs**2 + xy**2)

plt.imshow(z, cmap='gray', extent=[-5, 5, -5, 5])

result = np.where(z > 5, z, 0)
plt.imshow(result, cmap='gray', extent=[-5, 5, -5, 5])

arr_for_sum = np.random.standard_normal((4, 4))
arr_for_bool = arr_for_sum > 0


print(arr_for_sum.mean())
