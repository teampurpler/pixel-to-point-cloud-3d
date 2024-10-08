# %% [markdown]
# # Lens Model

# %%
from dataclasses import dataclass

from nptyping import Float32, NDArray, Shape


def _normalize_pixels(
    pixels: NDArray[Shape["H, W, 2"], Float32],
    camera_matrix: NDArray[Shape["3, 3"], Float32],
) -> NDArray[Shape["H, W, 2"], Float32]:
    principal_point = camera_matrix[:2, 2]
    focal_length = camera_matrix[[0, 1], [0, 1]]
    return (pixels - principal_point[None, None, :]) / focal_length[None, None, :]


@dataclass
class LensModel:
    camera_matrix: NDArray[Shape["3, 3"], Float32]
    distortion_coefficients: NDArray[Shape["*"], Float32]

    def normalize_pixels(
        self, pixels: NDArray[Shape["H, W, 2"], Float32]
    ) -> NDArray[Shape["H, W, 2"], Float32]:
        return _normalize_pixels(pixels, self.camera_matrix)
