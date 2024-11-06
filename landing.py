# %% [markdown]
# # Introduction
#
# Welcome to the "Pixel to Point Cloud" workshop repository! This project is designed
# to guide you through building a comprehensive 3D vision pipeline, transforming 2D
# images into 3D point clouds using Python and computer vision techniques.
#
# ## Overview
#
# This [repository](https://github.com/martvald/oaf-3d-vision-pipeline-workshop)
# contains materials for an 8-week workshop series that will introduce you to the
# fascinating world of 3D computer vision. Whether you're a beginner or have some
# programming experience, this course will help you understand and implement key
# concepts in 3D vision.
#
# ## Repository Structure
#
# - `workshops/`: Contains the jupyter notebooks for each workshop
# - `oaf_vision_3d/`: Python package we will build throughout the workshops
# - `test_data/`: Test images and data for the workshops
# - `ci/`: Continuous integration scripts
#
# ## Getting Started
#
# 1. Clone this repository:
#
#     ````{margin}
#     ```{warning}
#     I recommend to make a seperate folders for cloning repositories to, make sure
#     this folders is not within a synced folder like `OneDrive` or `iCloud`. These
#     are the locations I use personally:
#     - Unix: `/Users/{user_name}/Code`
#     - Windows: `C:/Code`
#     ```
#     ````
#
#     I recommend to install [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
#     and make a [github](https://github.com/). Git is a version control system that
#     allows you to track changes to your code, collaborate with others, and easily
#     revert to previous versions if needed. GitHub is a platform that provides hosting
#     for Git repositories, making it easy to share your code and collaborate with
#     others.
#
#     `````{tab-set}
#     ````{tab-item} GIT
#     Clone the repo to the desired
#     ```shell
#     git clone https://github.com/martvald/pixel-to-point-cloud.git
#     ```
#     ````
#
#     ````{tab-item} Manual
#     1. Go to the [repos github page](https://github.com/martvald/oaf-3d-vision-pipeline-workshop).
#     2. Click on the green `Code` button.
#     3. Click `Download ZIP`.
#     4. Extract the zip file in the desired location
#     ````
#     `````
#
# 2. Set up your Python environment:
#
#     I recommend running code from a virtual environment. This assures that changes,
#     installations and more does not affect the whole pc, only the current environment.
#
#     `````{tab-set}
#     ````{tab-item} Windows
#     Open a terminal at the repo root and make a new environment:
#     ```shell
#     python -m venv ENV
#     ```
#     Activate the environment:
#
#     ```shell
#     ENV/Scripts/activate
#     ```
#
#     Install dependencies:
#     ```shell
#     pip install -e . -e ci/ci_tools
#     ```
#     ````
#
#     ````{tab-item} Unix
#     Open a terminal at the repo root and make a new environment:
#     ```shell
#     python -m venv ENV
#     ```
#     Activate the environment:
#
#     ```shell
#     source ENV/bin/activate
#     ```
#
#     Install dependencies:
#     ```shell
#     pip install -e . -e ci/ci_tools
#     ```
#     ````
#     `````
#
# 3. Open editor at repo root in the virtual environment:
#
#     For these workshops, I will use the free Visual Studio Code (VS Code), a popular
#     code editor from Microsoft that offers a wide range of plugins and features. I
#     find VS Code to be an excellent choice for Python programming, but you are free
#     to use your preferred editor if you already have a favorite. It will be up to you
#     to ensure that you know how to set up and use your chosen editor effectively.
#
#     To open the repository in VS Code:
#
#     `````{tab-set}
#     ````{tab-item} Windows
#     Open a terminal at the repo root and enter your vitual environment:
#     ```shell
#     ENV/Scripts/activate
#     ```
#
#     Open VS Code at repo root:
#     ```shell
#     code .
#     ```
#     ````
#
#     ````{tab-item} Unix
#     Open a terminal at the repo root and enter your vitual environment:
#     ```shell
#     source ENV/bin/activate
#     ```
#
#     Open VS Code at repo root:
#     ```shell
#     code .
#     ```
#     ````
#     `````
#
# ## Workshop Schedule
#
# 1. [Introduction to 3D Vision](workshops/01_introduction_to_3d_vision.ipynb)
# 2. [Understanding Camera Models](workshops/02_understanding_camera_models.ipynb)
# 3. [Image Distortion and Undistortion](workshops/03_image_distortion_and_undistortion.ipynb)
# 4. [3D-2D Projections and PnP](workshops/04_3d_2d_projections_and_pnp.ipynb)
# 5. [Dual Camera Setups](workshops/05_dual_camera_setups.ipynb)
# 6. From Disparity to Depth
# 7. Stereo Matching Fundamentals
# 8. Building Your 3D Vision Pipeline
#
# ## Contributing
#
# We welcome contributions and suggestions! Please open an issue or submit a pull
# request if you have any improvements or find any bugs.
#
# ## License
#
# This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for
# details.
#
# Happy learning, and enjoy your journey into the world of 3D vision!
#
# ## Change history
#
# We don't keep history in this repository but the current version of these pages was
# made and published with:


# %% tags=["remove_input"]
import sys
from datetime import datetime

print("- Last run:", datetime.now())
print("- Python version:", sys.version)
print("- OS:", sys.platform)
