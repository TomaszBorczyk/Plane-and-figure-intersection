from plotting import plot
from geometry import get_working_area, cut_off_voxels, plane_eq


def main():
    voxels = get_working_area(8)
    voxels = cut_off_voxels(voxels, plane_eq(0, 0, 1, 3))
    voxels = cut_off_voxels(voxels, plane_eq(0, 1, 0, 1))
    plot(voxels)


if __name__ == '__main__':
    main()
