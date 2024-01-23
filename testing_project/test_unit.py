import unittest
from unit import sum_numbers
from unittest import TestCase
from fractions import Fraction


# run with pytest: pytest filename.py -v
# run with unittest: python -m unittest discover -v
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

    def test_list_of_fractions(self) -> None:
        self.assertEqual(sum_numbers([Fraction(1, 2), Fraction(1, 2)]), 1)

    def test_bad_type(self) -> None:
        data = "Some text to list of integer expected"
        with self.assertRaises(TypeError):
            result = sum_numbers(data)


if __name__ == '__main__':
    unittest.main()
