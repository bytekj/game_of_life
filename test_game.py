#!/usr/bin/python3
"""Test suite for game rules"""
from game import run_game, get_newborn
from sparsematrix import SparseMatrix
import unittest
import sys


class TestGetNewBorn(unittest.TestCase):
    def test_get_newborn_cell(self):
        """
        test for cell with two live neighbours
        """
        matrix = SparseMatrix()
        matrix.add_element((4, 5), 1)
        matrix.add_element((5, 5), 1)
        matrix.add_element((4, 4), 1)
        result = get_newborn(matrix, (4, 5))
        self.assertEqual(result, [(5, 4)])

class TestApplyGameRules(unittest.TestCase):
    def test_two_neighbours(self):
        pass
    def test_alone_cell(self):
        pass
    def test_three_neighbours(self):
        pass
    def test_four_neighbours(self):
        pass

if __name__ == '__main__':
    unittest.main()