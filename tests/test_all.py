"""
Module: test_all.py

Test suite for the entire project.

Reference: https://docs.pytest.org/en/stable/getting-started.html#get-started
"""

from py_template.core import foo


def test_foo() -> None:
    assert foo.bar() == 0


def test_baz() -> None:
    result: list[int] = foo.baz()
    assert len(result) == 10
    assert all(0 <= x <= 100 for x in result)
