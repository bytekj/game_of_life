#!/usr/bin/python3
"""Test suite for game rules"""
from game import run_game, get_newborn, apply_game_rules
from sparsematrix import SparseMatrix
import unittest
import sys


class TestGetNewBorn(unittest.TestCase):
    def test_get_newborn_cell(self):
        """
        test for cell with three live neighbours
        """
        matrix = SparseMatrix()
        matrix.add_element((4, 5), 1)
        matrix.add_element((5, 5), 1)
        matrix.add_element((6, 5), 1)
        matrix.add_element((6, 4), 1)
        matrix.add_element((4, 4), 1)
        matrix.add_element((5, 6), 1)
        result = get_newborn(matrix, (5, 5))

        self.assertEqual(set(result), set([(4, 6), (6, 6)]))

    def test_get_newborn_three_neighbours(self):
        matrix = SparseMatrix()
        matrix.add_element((4, 5), 1)
        matrix.add_element((5, 5), 1)
        matrix.add_element((6, 5), 1)
        result = get_newborn(matrix, (5, 5))
        self.assertEqual(set(result), set([(5, 6), (5, 4)]))

class TestApplyGameRules(unittest.TestCase):
    def test_two_neighbours(self):
        """
        test for only two live cells which are neighbours of each other
        """
        matrix = SparseMatrix()
        matrix.add_element((4, 5), 1)
        matrix.add_element((5, 5), 1)
        resulting_matrix = apply_game_rules(matrix)
        self.assertEqual(resulting_matrix.get_iterable(), {})

    def test_alone_cell(self):
        """
        test for only one live cell
        """
        matrix = SparseMatrix()
        matrix.add_element((4, 5), 1)
        resulting_matrix = apply_game_rules(matrix)
        self.assertEqual(resulting_matrix.get_iterable(), {})

    def test_three_neighbours(self):
        matrix = SparseMatrix()
        matrix.add_element((4, 5), 1)
        matrix.add_element((5, 5), 1)
        matrix.add_element((6, 5), 1)
        resulting_matrix = apply_game_rules(matrix)
        expected_result = dict()
        expected_result.update({(5, 6):1, (5, 5):1, (5, 4): 1})
        self.assertEqual(resulting_matrix.get_iterable(), expected_result)

    def test_four_neighbours(self):
        matrix = SparseMatrix()
        matrix.add_element((4, 5), 1)
        matrix.add_element((5, 5), 1)
        matrix.add_element((6, 5), 1)
        matrix.add_element((6, 4), 1)
        
        resulting_matrix = apply_game_rules(matrix)

        expected_result = dict()
        expected_result.update({(5, 6):1, (5, 5):1, (6, 5):1, (6, 4):1})
        self.assertEqual(resulting_matrix.get_iterable(), expected_result)

    def test_six_neighbours(self):
        matrix = SparseMatrix()
        matrix.add_element((4, 5), 1)
        matrix.add_element((5, 5), 1)
        matrix.add_element((6, 5), 1)
        matrix.add_element((6, 4), 1)
        matrix.add_element((4, 4), 1)
        matrix.add_element((5, 6), 1)

        resulting_matrix = apply_game_rules(matrix)

        expected_result = dict()
        expected_result.update({(5, 6):1, (6, 5):1, (6, 4):1, (4, 6):1,
                                (4, 5):1, (4, 4):1, (6, 6):1})
        self.assertEqual(resulting_matrix.get_iterable(), expected_result)

if __name__ == '__main__':
    unittest.main()