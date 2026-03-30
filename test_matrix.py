import unittest
from matrix import matrix as m

# Import your function here
# from your_file import check_valid

# def check_valid(matrix):
#     # temporary placeholder (remove this when testing your real code)
#     n = len(matrix)
#     expected = set(range(1, n + 1))
    
#     for row in matrix:
#         if set(row) != expected:
#             return False
    
#     for col in zip(*matrix):
#         if set(col) != expected:
#             return False
    
#     return True


class TestMatrixValidity(unittest.TestCase):

    def test_valid_matrix(self):
        matrix = [
            [1, 2, 3],
            [3, 1, 2],
            [2, 3, 1]
        ]
        self.assertTrue(m(matrix))

    def test_duplicate_in_row(self):
        matrix = [
            [1, 1, 3],
            [3, 2, 2],
            [2, 3, 1]
        ]
        self.assertFalse(m(matrix))

    def test_duplicate_in_column(self):
        matrix = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 3, 1]
        ]
        self.assertFalse(m(matrix))
    def test_missing_number(self):
        matrix = [
            [1, 2, 2],
            [3, 1, 2],
            [2, 3, 1]
        ]
        self.assertFalse(m(matrix))

    def test_out_of_range(self):
        matrix = [
            [1, 2, 4],
            [3, 1, 2],
            [2, 3, 1]
        ]
        self.assertFalse(m(matrix))

    def test_single_valid(self):
        matrix = [[1]]
        self.assertTrue(m(matrix))

    def test_single_invalid(self):
        matrix = [[2]]
        self.assertFalse(m(matrix))

    def test_valid_4x4(self):
        matrix = [
            [1, 2, 3, 4],
            [2, 3, 4, 1],
            [3, 4, 1, 2],
            [4, 1, 2, 3]
        ]
        self.assertTrue(m(matrix))

    def test_invalid_column_missing(self):
        matrix = [
            [1, 2, 3],
            [3, 1, 2],
            [3, 3, 1]
        ]
        self.assertFalse(m(matrix))

    def test_not_square_matrix(self):
        matrix = [
            [1, 2, 3],
            [3, 1, 2]
        ]
        self.assertFalse(m(matrix))


if __name__ == "__main__":
    unittest.main()