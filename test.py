from js.core import *

import unittest


class TestSum(unittest.TestCase):
    def test_builtin(self):
        obj = BuiltIn()
        self.assertEqual(
            repr(obj),
            "BuiltIn({'args': (), 'kwargs': {}})",
            "BuiltIn({'args': (), 'kwargs': {}})",
        )


if __name__ == "__main__":
    unittest.main()
