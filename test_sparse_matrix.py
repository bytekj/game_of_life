#!/usr/bin/python3
"""
Test suite for SparseMatrix Class
"""

import unittest
from sparsematrix import SparseMatrix

class TestSparseMatrix(unittest.TestCase):
    """
    Test cases for SparseMatrix functions
    """

    def test_add_element_live(self):
        """
        Test for setting a live cell
        """
        matrix = SparseMatrix()
        matrix.add_element((2, 3), 1)
        resulting_dict = {(2, 3): 1}
        self.assertEqual(matrix.get_iterable(), resulting_dict)

    def test_add_element_dead(self):
        """
        Test for setting a dead cell
        """
        matrix = SparseMatrix()
        matrix.add_element((2, 3), 0)
        resulting_dict = {(2, 3): 0}
        self.assertEqual(matrix.get_iterable(), resulting_dict)

    """
    Test cases for live/dead cells with one or more live neighbour cells
    """
    def test_check_surrounding_two(self):
        """
        test for cell with two live neighbours
        """
        matrix = SparseMatrix()
        matrix.add_element((4, 6), 1)
        matrix.add_element((5, 6), 1)
        matrix.add_element((6, 6), 1)
        self.assertEqual(matrix.check_surrounding((5, 6)), 2)

    def test_check_surrounding_one(self):
        """
        Test for cell with one live neighbour
        """
        matrix = SparseMatrix()
        matrix.add_element((4, 6), 1)
        matrix.add_element((5, 6), 1)
        matrix.add_element((6, 6), 1)
        self.assertEqual(matrix.check_surrounding((4, 6)), 1)

    def test_check_two_surrounding_dead_cell(self):
        """
        Test for dead cell surrounded by two live cells
        """
        matrix = SparseMatrix()
        matrix.add_element((4, 6), 1)
        matrix.add_element((5, 6), 1)
        self.assertEqual(matrix.check_surrounding((4, 5)), 2)

    def test_check_one_surrounding_dead_cell(self):
        """
        Test for dead cell surrounded by one live cell
        """
        matrix = SparseMatrix()
        matrix.add_element((4, 6), 1)

        self.assertEqual(matrix.check_surrounding((4, 5)), 1)

if __name__ == '__main__':
    unittest.main()
