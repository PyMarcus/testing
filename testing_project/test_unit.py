import unittest
from unit import sum_numbers
from unittest import TestCase


# run with nose2: python -m nose2
class TestSum(TestCase):
    def test_sum_numbers(self) -> None:
        self.assertEqual(sum([1, 2, 3]), sum_numbers([1, 2, 3]), 6)

    def test_is_an_integer(self) -> None:
        self.assertTrue(isinstance(sum_numbers([1, 2, 3]), int))

    def test_is_not_an_integer(self) -> None:
        self.assertFalse(isinstance(sum_numbers([1, 2, 3]), float))

    def test_if_there_is_an_answer(self) -> None:
        self.assertIsNone(None)

    def test_if_is_instance(self) -> None:
        self.assertIsInstance(sum_numbers([1, 2, 3]), int)


if __name__ == '__main__':
    unittest.main()
