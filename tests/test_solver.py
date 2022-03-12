import math
import unittest
from cmath import nan

import pytest
from src.solver import solve_quadratic_eq


class TestSolver(unittest.TestCase):
    """
    Testing equation solver for ax^2 + bx + c = 0
    """

    def test_solve_zero_roots(self):
        (a, b, c) = (1, 0, 1)
        result = solve_quadratic_eq(a, b, c)
        self.assertEqual(len(result), 0)

    def test_solve_two_different_roots(self):
        (a, b, c) = (1, 0, -1)
        result = solve_quadratic_eq(a, b, c)
        self.assertEqual(len(result), 2)
        self.assertTrue(math.isclose(result[0], 1))
        self.assertTrue(math.isclose(result[1], -1))

    def test_solve_two_identical_roots_zero_disc(self):
        (a, b, c) = (1.0, 2.0, 1.0)
        result = solve_quadratic_eq(a, b, c)
        self.assertEqual(len(result), 2)
        self.assertTrue(math.isclose(result[0], -1))
        self.assertTrue(math.isclose(result[1], -1))

    def test_solve_two_identical_roots_sub_epsilon_disc(self):
        sub_eps = 10e-10  # additional sub epsilon value
        (a, b, c) = (1.0, 2.0 + sub_eps, 1.0)
        result = solve_quadratic_eq(a, b, c)
        self.assertEqual(len(result), 2)
        self.assertTrue(math.isclose(result[0], -1))
        self.assertTrue(math.isclose(result[1], -1))

    def test_solve_zero_a_raises_division_error(self):
        (a, b, c) = (0, 2, 1)
        self.assertRaises(ZeroDivisionError, solve_quadratic_eq, a, b, c)

    def test_solve_non_real_type_raises(self):
        (a, b, c) = (1, 2, 1)

        # non real types
        self.assertRaises(TypeError, solve_quadratic_eq, "1", b, c)
        self.assertRaises(TypeError, solve_quadratic_eq, a, "2", c)
        self.assertRaises(TypeError, solve_quadratic_eq, a, b, "1")

        # types that can be interpreted as real
        self.assertRaises(TypeError, solve_quadratic_eq, math.nan, b, c)
        self.assertRaises(TypeError, solve_quadratic_eq, math.inf, b, c)
