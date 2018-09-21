import pytest

from sut import multiply


@pytest.mark.parametrize("factor_x,factor_y,expected", [
    (0, 1, 0),
    (1, 1, 1),
    (2, 2, 4),
    (2, 3, 6),
    (3, 4, 12),
    # (6, 6, 666),
])
def test_multiply(factor_x, factor_y, expected):
    assert multiply(factor_x, factor_y) == expected


if __name__ == "__main__":
    pytest.main()
