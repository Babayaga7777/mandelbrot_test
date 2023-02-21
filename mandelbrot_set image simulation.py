import numpy as np
import matplotlib.pyplot as plt

# Define the function for computing the Mandelbrot set
def mandelbrot(c, max_iterations):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iterations:
        z = z**2 + c
        n += 1
    if n == max_iterations:
        return 0
    else:
        return n

# Set the limits of the plot
xmin, xmax = -0.75, -0.745
ymin, ymax = 0.1, 0.105

# Set the resolution of the plot
resolution = 10000

# Create the x and y coordinates
x = np.linspace(xmin, xmax, resolution)
y = np.linspace(ymin, ymax, resolution)

# Create a grid of the x and y coordinates
X, Y = np.meshgrid(x, y)

# Compute the Mandelbrot set
M = np.zeros((resolution, resolution))
for i in range(resolution):
    for j in range(resolution):
        c = X[i, j] + Y[i, j]*1j
        M[i, j] = mandelbrot(c, 1000)

# Plot the Mandelbrot set
plt.figure(figsize=(20,20))
plt.imshow(M.T, extent=[xmin, xmax, ymin, ymax], cmap='jet', origin='lower')
plt.axis('off')
plt.show()
plt.savefig('mandelbrot_high_res.png', dpi=300)
