# RANSAC

Python wrapper around Enric Meinhardt's C implementation of RANSAC distributed
in [imscript](https://github.com/mnhrdt/imscript).


## Installation

The `ransac` Python package can be installed from PyPI with

    pip install ransac

Alternatively, it can be installed from sources in editable mode with

    git clone https://github.com/cmla/ransac
    pip install -e ransac


## Usage

    import numpy as np
    import ransac

    matches = np.loadtxt("tests/data/m.txt")
    inliers, F = ransac.find_fundamental_matrix(m)
