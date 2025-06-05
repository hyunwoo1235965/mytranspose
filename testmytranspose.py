import os
import sys
import unittest

sys.path.append("C:/Users/Nam Hyunwoo/Downloads/Assignment_GitHub_MyTranspose")
from mytranspose import mytranspose

class TestMyTranspose(unittest.TestCase):
    def test_list_input(self):
        input_matrix = [[1, 2], [3, 4]]
        expected = [[1, 3], [2, 4]]
        result = mytranspose(input_matrix)
        self.assertEqual(result, expected)

    def test_torch_tensor(self):
        import torch
        input_tensor = torch.tensor([[1, 2], [3, 4]])
        expected = torch.tensor([[1, 3], [2, 4]])
        result = mytranspose(input_tensor)
        self.assertTrue(torch.equal(result, expected))

    def test_dataframe(self):
        import pandas as pd
        df = pd.DataFrame({"d": [1, 2], "e": [3, 4], "f": [5, 6]})
        transposed = mytranspose(df)
        expected = df.T
        pd.testing.assert_frame_equal(transposed, expected)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
