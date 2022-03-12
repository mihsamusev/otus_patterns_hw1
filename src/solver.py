import math
from numbers import Real


def _is_usable_real(v: Real):
    """
    Checks if number is real, non nan, and non inf
    """
    return isinstance(v, Real) and math.isfinite(v)


def solve_quadratic_eq(a: Real, b: Real, c: Real) -> tuple:
    """
    Solves quadratic equation ax^2 + bx + c = 0
    Returns a tuple of roots (x1, x2) if solution exists, otherwise ()
    """
    if not all(map(_is_usable_real, (a, b, c))):
        raise TypeError("Values a, b and c should be non NaN, non Inf, reals")

    if math.isclose(a, 0):
        raise ZeroDivisionError("Coefficient 'a' cant be 0")

    disc = b * b - 4 * a * c
    if disc < 0:
        return ()

    disc_sqrt = 0 if math.isclose(disc, 0, abs_tol=10e-9) else math.sqrt(disc)
    x1 = (-b + disc_sqrt) / (2 * a)
    x2 = (-b - disc_sqrt) / (2 * a)
    result = (x1, x2)
    return result
