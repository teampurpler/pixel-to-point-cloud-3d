import os

from setuptools import find_packages, setup


def _requirements() -> list[str]:
    requirements = [
        "ipywidgets",
        "matplotlib",
        "nptyping",
        "numpy",
        "opencv-python",
        "scipy",
    ]
    if os.environ.get("CI") is None:
        requirements.append("open3d")
    return requirements


setup(
    name="oaf_vision_3d",
    version="0.1.0",
    description="OAF 3D Vision Pipeline Workshop",
    packages=find_packages(),
    install_requires=_requirements(),
    python_requires=">=3.10",
)
