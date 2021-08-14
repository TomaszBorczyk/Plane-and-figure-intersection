import numpy as np


# params a, b, c, d
# coords x, y, z
def plane_eq(a, b, c, d):
    return lambda x, y, z: a * x + b * y + c * z - d


# # TODO: include direction/normal to plane
def cut_off_voxels(voxels, plane):
    x, y, z = voxels.shape

    for x_curr in range(x):
        for y_curr in range(y):
            for z_curr in range(z):
                voxel_value = voxels[x_curr][y_curr][z_curr]

                # this does not work lol, different bool types
                # if voxel_value is True
                if np.equal(voxel_value, True):
                    voxels[x_curr][y_curr][z_curr] = plane(x_curr, y_curr, z_curr) > 0

    return voxels


# cubic area
def get_working_area(dimension):
    # voxels = np.zeros((dimension, dimension, dimension))
    voxels = np.full((dimension, dimension, dimension), True, dtype=bool)
    # voxels.fill(True)

    return voxels



def get_voxels():
    # prepare some coordinates
    x, y, z = np.indices((8, 8, 8))

    # draw cuboids in the top left and bottom right corners, and a link between
    # them
    cube1 = (x < 3) & (y < 3) & (z < 3)
    cube2 = (x >= 5) & (y >= 5) & (z >= 5)
    link = abs(x - y) + abs(y - z) + abs(z - x) <= 2

    # combine the objects into a single boolean array
    voxels = cube1 | cube2 | link

    return voxels
