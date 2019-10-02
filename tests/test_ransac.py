import numpy as np
import ransac

def test_ransac():
    matches = np.loadtxt("tests/data/matches.txt")
    inliers, F = ransac.find_fundamental_matrix(matches)

    np.testing.assert_allclose(F, np.loadtxt("tests/data/F.txt"), atol=1e-5)
