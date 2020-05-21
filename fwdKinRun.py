
# Main of the Hand simulator
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import fwdKin as fk
import plotter as pt
from math import pi

# Part 1: Forward Kinematics with ot without constrains
# Constrains will exists for example if h_index = fk.fwdkin(0.0, 0.0, 0.0, 'index', 1)
# Constrains will not exists for example if h_index = fk.fwdkin(0.0, 0.0, 0.0, 'index')

# Init plot
fig = plt.figure()
ax = plt.axes(projection="3d")
# Set rotation angle to 30 degrees
ax.view_init(azim=-90, elev=130)

# Homogeneous Matrices
h_index = fk.fwdkin(pi/3, -2*pi/6, -2*pi/6, 'index')          # Obtains the Homogeneous Matrices of index finger
if len(h_index) != 0:                                         # If there is no problem with angles then plot
    pt.plot(h_index, ax, 'index')
h_middle = fk.fwdkin(pi/3, -2*pi/6, -2*pi/6, 'middle')        # Obtains the Homogeneous Matrices of middle finger
if len(h_middle) != 0:                                        # If there is no problem with angles then plot
    pt.plot(h_middle, ax, 'middle')
h_ring = fk.fwdkin(pi/3, -2*pi/6, -2*pi/6, 'ring')            # Obtains the Homogeneous Matrices of ring finger
if len(h_ring) != 0:                                          # If there is no problem with angles then plot
    pt.plot(h_ring, ax, 'ring')
h_little = fk.fwdkin(pi/ 3, -2*pi/6, -2*pi/6, 'little')       # Obtains the Homogeneous Matrices of little finger
if len(h_little) != 0:                                        # If there is no problem with angles then plot
    pt.plot(h_little, ax, 'little')
plt.colors = 'grayscale'

# Set Title and labels of plot
plt.xlabel('x [mm]')
plt.ylabel('y [mm]')
ax.set_zlabel('z [cm]')
plt.title('Hand Simulation')

# Plot the obstacle plane y = -2
xx, zz = np.meshgrid(range(90), range(10))
yy = xx * 0 - 2
ax.plot_surface(xx, yy, zz - 2, alpha = 0.6)

# Adjust dimensions of the plot
ax.set_xlim(-4, 90)
ax.set_ylim(-4, 90)
ax.set_zlim(-2, 8)

# Show plot
plt.show()
