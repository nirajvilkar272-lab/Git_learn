# 3D plot in matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D



# Sample practice question
x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)
z = np.sin(np.sqrt(x**2 + y**2))

fig,ax = plt.subplots(1,1,1,figsize = (8,6),'projection':'3d')

plt.show()
### END ###


### Sample Dataset ###

# Line & Scatter data
z_line = np.linspace(0, 20, 200)
x_line = np.sin(z_line)
y_line = np.cos(z_line)

x_scatter = np.random.rand(200) * 10
y_scatter = np.random.rand(200) * 10
z_scatter = np.random.rand(200) * 10

# Surface, Wireframe, Contour data
X = np.linspace(-5, 5, 100)
Y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(X, Y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Bar3D data
x_bar = [1, 2, 3, 4, 5]
y_bar = [1, 2, 3, 4, 5]
z_bar = np.zeros_like(x_bar)
dx = np.ones_like(x_bar) * 0.5
dy = np.ones_like(y_bar) * 0.5
dz = [2, 5, 3, 7, 4]

# Quiver (vector field) data
x_quiver, y_quiver, z_quiver = np.meshgrid(np.arange(-2, 3, 1),
                                           np.arange(-2, 3, 1),
                                           np.arange(-2, 3, 1))
u = -y_quiver
v = x_quiver
w = np.zeros_like(z_quiver)

# Subplot must be defined before
fig,ax = plt.subplots(subplot_kw={'projection':'3d'})

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
# or
fig,ax = plt.subplots(subplot_kw={'projection':'3d'})

# required to be declared ⬆︎

#Inbuilt functions with Attributes
# 3d plots in matplotlib

# here  (x[i], y[j], z[k]) is one point in space.
# and   (X[i,j], Y[i,j], Z[i,j]) is a grid point on a surface.

# line plot
ax.plot3D(x, y, z)

# scatter plot
ax.scatter3D(x, y, z)

# surface plot
ax.plot_surface(X, Y, Z)

# wireframe plot
ax.plot_wireframe(X, Y, Z)

# contour plot
ax.contour3D(X, Y, Z)

# bar3d plot
ax.bar3d(x, y, z, dx, dy, dz)

# stem plot (works in 3d too)
ax.stem(x, y, z)

# quiver plot
ax.quiver(x, y, z, u, v, w)

# trisurf plot
ax.plot_trisurf(x, y, z)

# tricontour plot
ax.tricontour(x, y, z)

# voxels plot
ax.voxels(data)

plt.show()






















