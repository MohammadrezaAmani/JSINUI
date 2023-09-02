from js.core import *

import unittest


class TestSum(unittest.TestCase):

    def test_builtin(self):
        obj = BuiltIn()
        self.assertEqual(repr, "BuiltIn({'args': (), 'kwargs': {}})", "BuiltIn({'args': (), 'kwargs': {}})")

    # def test_sum_tuple(self):
    #     self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()