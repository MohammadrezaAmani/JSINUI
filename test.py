from js.core import *

import unittest


class TestJs(unittest.TestCase):
    def test_builtin(self):
        obj = BuiltIn()
        self.assertEqual(
            repr(obj),
            "BuiltIn({'args': (), 'kwargs': {}})",
            "Should be: BuiltIn({'args': (), 'kwargs': {}})",
        )

    def test_and_constant(self):
        self.assertEqual(
            And("me", "you").__str__(), '"me" && "you"', 'Should be: "me" && "you"'
        )

    def test_and_variable(self):
        me = "me"
        you = "you"
        self.assertEqual(
            And(me, you).__str__(), '"me" && "you"', 'Should be: "me" && "you"'
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
