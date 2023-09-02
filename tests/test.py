import unittest
import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir)
from js.core import *

class TestJs(unittest.TestCase):
    
    def test_builtin(self):
        obj = BuiltIn()
        self.assertEqual(
            repr(obj),
            "BuiltIn({'args': (), 'kwargs': {}})",
            "Should be: BuiltIn({'args': (), 'kwargs': {}})",
        )

    def test_And_constant(self):
        self.assertEqual(
            And("me", "you").__str__(), '"me" && "you"', 'Should be: "me" && "you"'
        )

    def test_And_variable(self):
        me = "me"
        you = "you"
        self.assertEqual(
            And(me, you).__str__(), '("me" && "you")', 'Should be: ("me" && "you")'
        )
    def test_Or_constant(self):
        self.assertEqual(
            And("me", "you").__str__(), '("me" || "you")', 'Should be: ("me" || "you")'
        )

    def test_Or_variable(self):
        me = 1
        you = 2
        self.assertEqual(
            And(me, you).__str__(), '(1 || 2)', 'Should be: (1 || 2)'
        )
    def test_Not_variable(self):
        self.assertEqual(
            Not(Or(1,2)).__str__(), '!((1 || 2))', 'Should be: !((1 || 2))'
        )


if __name__ == "__main__":
    tect = unittest.main(exit=False)
    with open("./issues/README.md", "w") as f:
        f.write("# JSinUI test results\n\n")
        f.write(
            "Thid file contains results of last \
            last test of JSINUI module, we are trying to\
            fix them as soon as possible.\n\n------\n\n"
        )

        f.write("### Failures: \n\n")
        for i in tect.result.failures.copy():
            f.write("``` python\n")
            for j in i:
                f.write(str(j) + "\n")
            f.write("```\n------------\n")
        f.write("### Errors:\n\n")
        for i in tect.result.errors.copy():
            f.write("``` python\n")
            for j in i:
                f.write(str(j) + "\n")
            f.write("```\n------------\n")

        f.write("### ExpectedFailures: \n\n")
        for i in tect.result.expectedFailures.copy():
            f.write("``` python\n")
            for j in i:
                f.write(str(j) + "\n")
            f.write("```\n------------\n")
