# %% [markdown]
# # Triangulation
#
# This function triangulates 3D points from two sets of two undistorted normalized
# pixels and a [`TransformationMatrix`](transformation_matrix.py) object. The process
# for this was discussed in more detail in the workshop
# [5: Dual Camera Setups](../workshops/05_dual_camera_setups.ipynb).


# %%
import numpy as np
from nptyping import Float32, NDArray, Shape

from oaf_vision_3d.transformation_matrix import TransformationMatrix


def triangulate_points(
    undistorted_normalized_pixels_0: NDArray[Shape["H, W, 2"], Float32],
    undistorted_normalized_pixels_1: NDArray[Shape["H, W, 2"], Float32],
    transformation_matrix: TransformationMatrix,
) -> NDArray[Shape["H, W, 3"], Float32]:
    v_0 = np.pad(
        undistorted_normalized_pixels_0, ((0, 0), (0, 0), (0, 1)), constant_values=1
    )
    v_1 = transformation_matrix.rotate(
        np.pad(
            undistorted_normalized_pixels_1, ((0, 0), (0, 0), (0, 1)), constant_values=1
        )
    )
    p_1_p_0 = -transformation_matrix.translation[None, None, :]

    a = (v_0 * v_0).sum(axis=-1)
    b = (v_0 * v_1).sum(axis=-1)
    c = (v_1 * v_1).sum(axis=-1)
    d = (v_0 * p_1_p_0).sum(axis=-1)
    e = (v_1 * p_1_p_0).sum(axis=-1)

    t = (b * e - c * d) / (a * c - b * b)

    return v_0 * t[..., None]
