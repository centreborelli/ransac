# RANSAC

[![Build Status](https://travis-ci.com/cmla/ransac.svg?branch=master)](https://travis-ci.com/cmla/ransac)
[![PyPI version](https://img.shields.io/pypi/v/ransac)](https://pypi.org/project/ransac)

Python wrapper around Enric Meinhardt's C implementation of RANSAC distributed
in [imscript](https://github.com/mnhrdt/imscript).


## Installation

The `ransac` Python package can be installed from PyPI with

    pip install ransac

Alternatively, it can be installed from sources in editable mode with

    git clone https://github.com/cmla/ransac
    cd ransac
    pip install -e .


## Usage

    import numpy as np
    import ransac

    matches = np.loadtxt("tests/data/matches.txt")
    inliers, F = ransac.find_fundamental_matrix(matches)
