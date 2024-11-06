# %% [markdown]
# # Transformation Matrix
#
# This class holds a 4x4 transformation matrix, which is a combination of a 3x3
# rotation matrix and a 3x1 translation vector. It uses the
# `scipy.spatial.transform.Rotation` class to represent the rotation, as this class
# provides a convenient way work with different rotation representations (e.g. rotation
# matrix, quaternion, Euler angles, etc.), and numpy for the translation vector.
#
# The class provides methods to:
# - Convert to and from a 4x4 transformation matrix
# - Create a transformation from a rotation vector and translation vector
# - Invert the transformation
# - Rotate, translate, and transform points
# - Use the `@` operator to apply the transformation to points or combine two
#   transformations

# %%
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, overload

import numpy as np
from nptyping import Float32, NDArray, Shape
from scipy.spatial.transform import Rotation

T = TypeVar("T", NDArray[Shape["H, W, 3"], Float32], "TransformationMatrix")


@dataclass
class TransformationMatrix:
    rotation: Rotation = Rotation.from_matrix(np.identity(3))
    translation: NDArray[Shape["3"], Float32] = field(
        default_factory=lambda: np.array([0, 0, 0], np.float32)
    )

    def as_matrix(self) -> NDArray[Shape["4, 4"], Float32]:
        matrix = np.identity(4, np.float32)
        matrix[:3, :3] = self.rotation.as_matrix()
        matrix[:3, 3] = self.translation
        return matrix

    @staticmethod
    def from_matrix(matrix: NDArray[Shape["4, 4"], Float32]) -> TransformationMatrix:
        return TransformationMatrix(
            rotation=Rotation.from_matrix(matrix[:3, :3]), translation=matrix[:3, 3]
        )

    @staticmethod
    def from_rvec_and_tvec(
        rvec: NDArray[Shape["3"], Float32], tvec: NDArray[Shape["3"], Float32]
    ) -> TransformationMatrix:
        return TransformationMatrix(
            rotation=Rotation.from_rotvec(np.array(rvec)), translation=np.array(tvec)
        )

    def inverse(self) -> TransformationMatrix:
        return TransformationMatrix.from_matrix(np.linalg.inv(self.as_matrix()))

    def rotate(
        self, points: NDArray[Shape["H, W, 3"], Float32]
    ) -> NDArray[Shape["H, W, 3"], Float32]:
        return np.einsum("ij,...j->...i", self.rotation.as_matrix(), points)

    def translate(
        self, points: NDArray[Shape["H, W, 3"], Float32]
    ) -> NDArray[Shape["H, W, 3"], Float32]:
        return points + self.translation[None, None, :]

    def transform(
        self, points: NDArray[Shape["H, W, 3"], Float32]
    ) -> NDArray[Shape["H, W, 3"], Float32]:
        return self.translate(points=self.rotate(points=points))

    @overload
    def __matmul__(
        self, other: NDArray[Shape["H, W, 3"], Float32]
    ) -> NDArray[Shape["H, W, 3"], Float32]: ...

    @overload
    def __matmul__(self, other: TransformationMatrix) -> TransformationMatrix: ...

    def __matmul__(self, other: T) -> T:
        if isinstance(other, NDArray):
            return self.transform(points=other)  # type: ignore
        if isinstance(other, TransformationMatrix):
            return TransformationMatrix.from_matrix(
                self.as_matrix() @ other.as_matrix()
            )
        raise NotImplementedError(other)
