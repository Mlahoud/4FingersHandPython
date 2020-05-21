# Function to plot the homogeneous matrices
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


def plot(h_matrix,ax,finger):

    # Points of the hand
    O = [h_matrix[0][0][3], h_matrix[0][1][3], h_matrix[0][2][3]]
    A = [h_matrix[1][0][3], h_matrix[1][1][3], h_matrix[1][2][3]]
    B = [h_matrix[2][0][3], h_matrix[2][1][3], h_matrix[2][2][3]]
    C = [h_matrix[3][0][3], h_matrix[3][1][3], h_matrix[3][2][3]]
    D = [h_matrix[4][0][3], h_matrix[4][1][3], h_matrix[4][2][3]]

    # Plot of lines
    ax.plot([O[0], A[0]], [O[1], A[1]],'k', zs=[O[2], A[2]])
    ax.plot([A[0], B[0]], [A[1], B[1]],'k', zs=[A[2], B[2]])
    ax.plot([B[0], C[0]], [B[1], C[1]],'k', zs=[B[2], C[2]])
    ax.plot([C[0], D[0]], [C[1], D[1]],'k', zs=[C[2], D[2]])

    # Plot of points
    ax.scatter3D(O[0], O[1], O[2],c='black')
    metha = ax.scatter3D(A[0], A[1], A[2],c='r', cmap='hsv')
    prox = ax.scatter3D(B[0], B[1], B[2],c='g', cmap='hsv')
    distal = ax.scatter3D(C[0], C[1], C[2],c='b', cmap='hsv')
    tip = ax.scatter3D(D[0], D[1], D[2],c='c', cmap='hsv')
    label = finger + ' finger'
    ax.text(O[0], O[1], O[2], label)

    ax.legend([metha, prox, distal, tip],["Metacarpophalangeal joint", "Proximal interphalangeal joint", "Distal interphalangeal joint", "Fingertip"])

    #label2 = 'Metacarpophalangeal joint'
    #ax.text(O[0], O[1], O[2], label2)
    # Plot frames
    # Fixed frame
    vect_len = 10
    ax.plot([O[0], O[0]+vect_len*h_matrix[0][0][0]],
            [O[1], O[1]+vect_len*h_matrix[0][0][1]], 'r', label = 'x-axis', zs=[O[2], O[2]+vect_len*h_matrix[0][0][2]])
    ax.plot([O[0], O[0]+vect_len*h_matrix[0][1][0]],
            [O[1], O[1]+vect_len*h_matrix[0][1][1]], 'g', label = 'y-axis', zs=[O[2], O[2]+vect_len*h_matrix[0][1][2]])
    ax.plot([O[0], O[0]+vect_len*h_matrix[0][2][0]],
            [O[1], O[1]+vect_len*h_matrix[0][2][1]], 'b', label = 'z-axis', zs=[O[2], O[2]+vect_len/10*h_matrix[0][2][2]])

    # MCP frame
    ax.plot([A[0], O[0]+vect_len*h_matrix[1][0][0]],
            [A[1], O[1]+vect_len*h_matrix[1][0][1]], 'r', zs=[A[2], A[2]+vect_len*h_matrix[1][0][2]])
    ax.plot([A[0], O[0]+vect_len*h_matrix[1][1][0]],
            [A[1], O[1]+vect_len*h_matrix[1][1][1]], 'g', zs=[A[2], A[2]+vect_len*h_matrix[1][1][2]])
    ax.plot([A[0], O[0]+vect_len*h_matrix[1][2][0]],
            [A[1], O[1]+vect_len*h_matrix[1][2][1]], 'b', zs=[A[2], A[2]+vect_len/10*h_matrix[1][2][2]])

    # PIP frame
    ax.plot([B[0], B[0]+vect_len*h_matrix[2][0][0]],
            [B[1], B[1]+vect_len*h_matrix[2][0][1]], 'r', zs=[B[2], B[2]+vect_len*h_matrix[2][0][2]])
    ax.plot([B[0], B[0]+vect_len*h_matrix[2][1][0]],
            [B[1], B[1]+vect_len*h_matrix[2][1][1]], 'g', zs=[B[2], B[2]+vect_len*h_matrix[2][1][2]])
    ax.plot([B[0], B[0]+vect_len*h_matrix[2][2][0]],
            [B[1], B[1]+vect_len*h_matrix[2][2][1]], 'b', zs=[B[2], B[2]+vect_len/10*h_matrix[2][2][2]])

    # DIP frame
    ax.plot([C[0], C[0]+vect_len*h_matrix[3][0][0]],
            [C[1], C[1]+vect_len*h_matrix[3][0][1]], 'r', zs=[C[2], C[2]+vect_len*h_matrix[3][0][2]])
    ax.plot([C[0], C[0]+vect_len*h_matrix[3][1][0]],
            [C[1], C[1]+vect_len*h_matrix[3][1][1]], 'g', zs=[C[2], C[2]+vect_len*h_matrix[3][1][2]])
    ax.plot([C[0], C[0]+vect_len*h_matrix[3][2][0]],
            [C[1], C[1]+vect_len*h_matrix[3][2][1]], 'b', zs=[C[2], C[2]+vect_len/10*h_matrix[3][2][2]])

    # TIP frame
    ax.plot([D[0], D[0]+vect_len*h_matrix[3][0][0]],
            [D[1], D[1]+vect_len*h_matrix[3][0][1]], 'r', zs=[D[2], D[2]+vect_len*h_matrix[3][0][2]])
    ax.plot([D[0], D[0]+vect_len*h_matrix[3][1][0]],
            [D[1], D[1]+vect_len*h_matrix[3][1][1]], 'g', zs=[D[2], D[2]+vect_len*h_matrix[3][1][2]])
    ax.plot([D[0], D[0]+vect_len*h_matrix[3][2][0]],
            [D[1], D[1]+vect_len*h_matrix[3][2][1]], 'b', zs=[D[2], D[2]+vect_len/10*h_matrix[3][2][2]])





