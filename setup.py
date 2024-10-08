from setuptools import find_packages, setup

setup(
    name="oaf_vision_3d",
    version="0.1.0",
    description="OAF 3D Vision Pipeline Workshop",
    packages=find_packages(),
    install_requires=[
        "bokeh",
        "nptyping",
        "numpy",
    ],
    python_requires=">=3.12",
)
