import unittest

from src.solver import solve_quadratic_eq


class TestSolver(unittest.TestCase):
    """
    Testing equation solver for ax^2 + bx + c = 0
    """

    def test_solve_no_roots(self):
        (a, b, c) = (1, 0, 1)
        result = solve_quadratic_eq(a, b, c)
        self.assertEqual(len(result), 0)
