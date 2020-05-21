# Basically this loops the inverse kinematics and stores positions in order to make an animation

import numpy as np
from fwdKin import fwdkin as fk
from fwdKin import  index, middle, ring, little
from math import sqrt, pi, radians
import matplotlib.pyplot as plt
from celluloid import Camera
import plotter as pt
import matplotlib.animation as animation

# Part 3: Animation using Inverse Kinematics
finger = 'index'                                           # In case that another finger is wanted just change the name
SamplingDistance = radians(0.10)                           # Sampling distance between positions of the fingertip
learning_rate = 0.0001                                     # Learning rate of the gradient descent part
angles = np.array([0.8, -1.6, -0.9])                       # Initial angles of the finger
if finger == 'index':
    lengths = index()
if finger == 'middle':
    lengths = middle()
if finger == 'ring':
    lengths = ring()
if finger == 'little':
    lengths = little()
x_range = np.arange(30.0, 61.0)                            # Range of x positions of the finger's fingertip
target = np.array([x_range[0], -2.0, lengths[3]])          # Initial target of the finger's fingertip


def dist(tar, ang, finger):
    h_point = fk(ang[0], ang[1], ang[2], finger, 1)  # not constrained by the moment
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

# Start loop for animation here...
print('Computing positions...')
# Init plot
fig = plt.figure()
camera = Camera(fig)
ax = plt.axes(projection="3d")
# Set rotation angle to 30 degrees
ax.view_init(azim=-90, elev=90)
for j in range(len(x_range)):
    err = []
    a_angles = []
    ix = 0
    target = np.array([x_range[j], -2.0, 0.0])
    dis = dist(target, angles, finger)
    while dis > 0.1 and ix < 1000:
        ik = inverse_kinematics(target, angles)
        angles = ik[0]
        dis = dist(target, angles, finger)
        err.append(ik[1])
        ix += 1

    a_angles.append(angles)
    # angles = a_angles[-1]
    h_point = fk(angles[0], angles[1], angles[2], finger, 1)  # not constrained by the moment
    point = np.array([h_point[4][0][3], h_point[4][1][3], h_point[4][2][3]])

    # Starting Animation
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

    #plt.show()

    camera.snap()

print('Producing animation...')
animation = camera.animate()
animation.save('animation.gif', writer = 'user')
print('Done... Check folder where codes are to see the animation file obtained.')