import unittest
import numpy as np
from mytranspose import mytranspose

class TestMyTranspose(unittest.TestCase):

    def test_matrix(self):
        a = np.array([[1, 2], [3, 4]])
        expected = np.array([[1, 3], [2, 4]])
        np.testing.assert_array_equal(mytranspose(a), expected)

    def test_empty_matrix(self):
        a = np.empty((0, 0))
        expected = a
        np.testing.assert_array_equal(mytranspose(a), expected)

    def test_vector(self):
        a = np.array([1, 2, 3])
        expected = a.reshape(-1, 1)
        np.testing.assert_array_equal(mytranspose(a), expected)

    def test_nan_vector(self):
        a = np.array([1, 2, np.nan])
        expected = a.reshape(-1, 1)
        np.testing.assert_array_equal(mytranspose(a), expected)

if __name__ == "__main__":
    unittest.main()
