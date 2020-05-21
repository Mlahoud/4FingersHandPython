# Forward Kinematic base function
# For Each Finger there is a specific Proximal, Intermediate and Distal length

import numpy as np
from math import cos, sin, pi

def index():
    # lengths
    l_f = 16 * 0
    l_prox = 39.8
    l_intr = 22.4
    l_dist = 15.8
    lengths = [l_prox, l_intr, l_dist, l_f]
    return lengths


def middle():
    # lengths
    l_f = 16 / 10
    l_prox = 44.6
    l_intr = 26.3
    l_dist = 17.4
    lengths = [l_prox, l_intr, l_dist, l_f]
    return lengths


def ring():
    # lengths
    l_f = 16 * 2 / 10
    l_prox = 41.4
    l_intr = 25.7
    l_dist = 17.3
    lengths = [l_prox, l_intr, l_dist, l_f]
    return lengths


def little():
    # lengths
    l_f = 16 * 3 / 10
    l_prox = 32.7
    l_intr = 18.1
    l_dist = 16
    lengths = [l_prox, l_intr, l_dist, l_f]
    return lengths


# Forward Kinematics for the given angles. Unconstrained if constrained = 0 and Constrained if constrained = 1
def fwdkin(th_M, th_P, th_D,finger, constrained = 0):
    # First check if angles are valid and if not throw an exception
    if -pi/3 < th_M > pi/3 or -2*pi/3 < th_P > 0 or -2*pi/3 < th_D > 0:
        print('Angles of ' + finger + ' finger are out of bounds.')
        print('Continuing without ' + finger + ' finger.')
        return []
    else:

        # If the kinematic is constrained then constrain th_D
        if constrained == 1:
            th_D = 2/3*th_P

        # Obtain the Homogeneous Transformations for MCP, PIP, DIP and TIP of each finger
        if finger == 'index':
            lengths = index()
        if finger == 'middle':
            lengths = middle()
        if finger == 'ring':
            lengths = ring()
        if finger == 'little':
            lengths = little()

        # Homogeneous Matrix of the Fixed Frame
        t_fx = np.array([[1,0,0,          0],
                         [0,1,0,          0],
                         [0,0,1, lengths[3]],
                         [0,0,0,          1]])

        # Homogeneous Matrix of the Metacarpophalangeal joint
        t_MCP = np.array([[cos(-th_M),-sin(-th_M),0,         0],
                          [sin(-th_M), cos(-th_M),0,         0],
                          [         0,          0,1,lengths[3]],
                          [         0,          0,0,         1]])

        # Homogeneous Matrix of the Proximal Interphalangeal joint
        t_PIP = np.array([[cos(-th_M-th_P),-sin(-th_M-th_P), 0, lengths[0]*cos(th_M)],
                          [sin(-th_M-th_P), cos(-th_M-th_P), 0, lengths[0]*sin(th_M)],
                          [              0,               0, 1,           lengths[3]],
                          [              0,               0, 0,                    1]])

        # Homogeneous Matrix of the Distal Interphalangeal joint
        t_DIP = np.array([[cos(-th_M-th_P-th_D),-sin(-th_M-th_P-th_D), 0, lengths[1]*cos(th_M+th_P) + lengths[0]*cos(th_M)],
                          [sin(-th_P-th_M-th_D), cos(-th_P-th_M-th_D), 0, lengths[1]*sin(th_M+th_P) + lengths[0]*sin(th_M)],
                          [                   0,                    0, 1,                                       lengths[3]],
                          [                   0,                    0, 0,                                                1]])

        # Homogeneous Matrix of the TIP of the finger
        t_TIP = np.array([[cos(-th_M-th_P-th_D),-sin(-th_P-th_P-th_D), 0, lengths[2]*cos(th_M+th_P+th_D) + lengths[1]*cos(th_M+th_P) + lengths[0]*cos(th_M)],
                          [sin(-th_P-th_M-th_D), cos(-th_P-th_M-th_D), 0, lengths[2]*sin(th_M+th_P+th_D) + lengths[1]*sin(th_M+th_P) + lengths[0]*sin(th_M)],
                          [                   0,                    0, 1,                                                                        lengths[3]],
                          [                   0,                    0, 0,                                                                                 1]])

        H_trans = [t_fx, t_MCP, t_PIP, t_DIP, t_TIP]

        return H_trans
