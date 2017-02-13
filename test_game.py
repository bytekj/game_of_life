#!/usr/bin/python3
"""Test suite for game rules"""
from game import run_game
import sparsematrix
import unittest
import sys


class TestGetNewBorn(unittest.TestCase):
    def test_get_newborn_cell(self):
        pass

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