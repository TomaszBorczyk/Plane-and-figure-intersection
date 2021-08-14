import matplotlib.pyplot as plt
import numpy as np


def plot(voxels):
    # set the colors of each object
    colors = np.empty(voxels.shape, dtype=object)
    colors.fill('red')

    # and plot everything
    ax = plt.figure().add_subplot(projection='3d')
    ax.voxels(voxels, facecolors=colors, edgecolor='k')

    plt.show()
