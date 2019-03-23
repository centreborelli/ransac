import os
import ctypes
import numpy as np


lib = ctypes.CDLL(os.path.join('lib', 'libransac.so'))


def find_fundamental_matrix(matches, ntrials=1000, max_err=0.3):
    """
    Estimate a fundamental matrix from a list of point matches, with RANSAC.

    Args:
        matches (array_like): list of point matches, each match being
            represented by a list or tuple (x1, y1, x2, y2) containing the x, y
            coordinates of two matching points
        ntrials (int): number of trials for the random sample selection
        max_err (float): maximum error, in pixels, for a match to be considered
            as an inlier

    Return:
        inliers_mask (array_like): list of booleans, True for inliers, False
            for outliers
        fundamental_matrix (numpy array): array of shape (3, 3) representing
            the fundamental matrix
    """
    n = len(matches)
    lib.find_fundamental_matrix_by_ransac.argtypes = (
        np.ctypeslib.ndpointer(dtype=ctypes.c_bool, shape=(n,)),     # inliers
        np.ctypeslib.ndpointer(dtype=ctypes.c_float, shape=(9,)),    # F
        np.ctypeslib.ndpointer(dtype=ctypes.c_float, shape=(n, 4)),  # matches
        ctypes.c_int, ctypes.c_int, ctypes.c_float
    )
    lib.find_fundamental_matrix_by_ransac.restype = ctypes.c_int

    inliers_mask = np.zeros(n, dtype=np.bool)
    fundamental_matrix = np.zeros(9, dtype=np.float32)
    lib.find_fundamental_matrix_by_ransac(inliers_mask, fundamental_matrix,
                                          np.asarray(matches).astype(np.float32),
                                          n, ntrials, max_err)
    return inliers_mask, fundamental_matrix.reshape((3, 3))
