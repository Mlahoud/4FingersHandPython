# Gradient descent of the translational part of the homogeneous matrix
# Gradient descent part was adapted to python from:
# https://www.alanzucconi.com/2017/04/10/robotic-arms/

import numpy as np
from fwdKin import fwdkin, index, middle, ring, little
from math import sqrt, pi, radians
import matplotlib.pyplot as plt
import plotter as pt

# Part 2: Inverse Kinematics

finger = 'index'                              # In case that another finger is wanted just change the name
SamplingDistance = radians(0.10)              # Sampling distance between positions of the fingertip
learning_rate = 0.0001                        # Learning rate of the gradient descent part
angles = np.array([0.8, -1.6, -0.9])          # Initial angles of the finger
if finger == 'index':
    lengths = index()
if finger == 'middle':
    lengths = middle()
if finger == 'ring':
    lengths = ring()
if finger == 'little':
    lengths = little()
target = np.array([35.0, -2.0, lengths[3]])   # Target position of the fingertip. Z value depends on the selected finger


def dist(tar, ang, finger):
    h_point = fwdkin(ang[0], ang[1], ang[2], finger, 1)  # not constrained by the moment
    point = np.array([h_point[4][0][3], h_point[4][1][3], h_point[4][2][3]])
    res = sqrt((point[0] - tar[0])**2 + (point[1] - tar[1])**2)
    return res


def partial_gradient(tar, ang, idx):
    angle = ang[idx]
    f_x = dist(tar, ang, finger)
    ang[idx] += np.array([SamplingDistance])

    f_x_plus_d = dist(tar, ang, finger)
    grad = (f_x_plus_d - f_x) / SamplingDistance

    ang[idx] = angle

    return grad


def inverse_kinematics(tar, ang):
    for m in range(3):
        gradient = partial_gradient(tar, ang, m)
        ang[m] -= learning_rate * gradient
    ang[0] = np.clip(angles[0], -pi/3, pi/3)
    ang[1] = np.clip(angles[1], -2*pi/3, 0.0)
    ang[2] = np.clip(angles[2], -2*pi/3, 0.0)
    error = dist(tar, ang, finger)
    return [ang, error]


dis = dist(target, angles, finger)

print('initial distance: ' + str(dis))
ix = 0
err = []
while dis > 0.1 and ix < 1000:
    ik = inverse_kinematics(target, angles)
    angles = ik[0]
    dis = dist(target, angles, finger)
    err.append(ik[1])
    ix += 1


# Init plot
fig = plt.figure()
ax = plt.axes(projection="3d")
# Set rotation angle to 30 degrees
ax.view_init(azim=-90, elev=90)


h_point = fwdkin(angles[0], angles[1], angles[2], finger, 1)  # not constrained by the moment
point = np.array([h_point[4][0][3], h_point[4][1][3], h_point[4][2][3]])

print('Number of iterations: ' + str(ix))
print('Desired position: ' + str(target))
print('Final Position: ' + str(point))
print('Final Angles: ' + str(angles))
print('error in distance: ' + str(dist(target, angles, finger)))

pt.plot(h_point, ax, finger)

# Set Title and labels of plot
plt.xlabel('x [mm]')
plt.ylabel('y [mm]')
ax.set_zlabel('z [cm]')
plt.title('Hand Inverse Kinematics')

# Plot the obstacle plane y = -2
xx, zz = np.meshgrid(range(90), range(10))
yy = xx * 0 - 2
ax.plot_surface(xx , yy, zz - 2, alpha=0.6)

# Adjust dimensions of the plot
ax.set_xlim(-4, 90)
ax.set_ylim(-4, 90)
ax.set_zlim(-2, 8)

fig2 = plt.figure()
plt.plot(err)
plt.xlabel('Iterations')
plt.ylabel('Error')
plt.title('Error vs Iterations')
plt.show()

# Show plot
plt.show()
