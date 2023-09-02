import unittest
import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir)
from js.core import *


class TestBoolOp(unittest.TestCase):
    def test_and(self):
        and_op = And(True, False)
        self.assertEqual(and_op.render(), "(True && False)")

    def test_or(self):
        or_op = Or(True, False)
        self.assertEqual(or_op.render(), "(True || False)")

    def test_not(self):
        not_op = Not(True)
        self.assertEqual(not_op.render(), "(!True)")

    # Add more test cases for BoolOp with various data types


class TestComparisons(unittest.TestCase):
    def test_lt(self):
        lt_op = LT(5, 10)
        self.assertEqual(lt_op.render(), "(5 < 10)")

    def test_lte(self):
        lte_op = LTE(5, 5)
        self.assertEqual(lte_op.render(), "(5 <= 5)")

    def test_gt(self):
        gt_op = GT(10, 5)
        self.assertEqual(gt_op.render(), "(10 > 5)")

    def test_gte(self):
        gte_op = GTE(5, 5)
        self.assertEqual(gte_op.render(), "(5 >= 5)")

    def test_eq(self):
        eq_op = Eq("hello", "world")
        self.assertEqual(eq_op.render(), '("hello" == "world")')

    def test_noteq(self):
        noteq_op = NotEq("apple", "orange")
        self.assertEqual(noteq_op.render(), '("apple" != "orange")')

    def test_is(self):
        is_op = Is(None, None)
        self.assertEqual(is_op.render(), "(None === None)")

    def test_isnot(self):
        isnot_op = IsNot(True, False)
        self.assertEqual(isnot_op.render(), "(True !== False)")

    # Add more test cases for Comparisons with various data types


class TestType(unittest.TestCase):
    def test_int_type(self):
        int_type = Int(42)
        self.assertEqual(int_type.render(), "42")

    def test_float_type(self):
        float_type = Float(3.14)
        self.assertEqual(float_type.render(), "3.14")

    def test_str_type(self):
        str_type = Str("Hello, World!")
        self.assertEqual(str_type.render(), '"Hello, World!"')

    def test_str_type(self):
        str_type = Str("Hello,\n World!")
        self.assertEqual(str_type.render(), "`Hello,\n World!`")

    def test_complex_type(self):
        complex_type = Complex(1 + 2j)
        self.assertEqual(complex_type.render(), "(1+2j)")

    # Add more test cases for Type with various data types


class TestOp(unittest.TestCase):
    def test_addition(self):
        add_op = Add(3, 4)
        self.assertEqual(add_op.render(), "(3 + 4)")

    def test_subtraction(self):
        sub_op = Sub(10, 5)
        self.assertEqual(sub_op.render(), "(10 - 5)")

    def test_multiplication(self):
        mult_op = Mult(6, 7)
        self.assertEqual(mult_op.render(), "(6 * 7)")

    def test_division(self):
        div_op = Div(20, 4)
        self.assertEqual(div_op.render(), "(20 / 4)")

    # Add more test cases for Op with various data types


class TestBitwiseOp(unittest.TestCase):
    def test_bitand(self):
        bitand_op = BitAnd(5, 3)
        self.assertEqual(bitand_op.render(), "(5 & 3)")

    def test_bitor(self):
        bitor_op = BitOr(5, 3)
        self.assertEqual(bitor_op.render(), "(5 | 3)")

    def test_bitxor(self):
        bitxor_op = BitXor(5, 3)
        self.assertEqual(bitxor_op.render(), "(5 ^ 3)")

    def test_bitinvert(self):
        bitinvert_op = BitInvert(5)
        self.assertEqual(bitinvert_op.render(), "(~5)")


# Import the Scope class from your_module


class TestScope(unittest.TestCase):
    def test_empty_scope(self):
        scope = Scope()
        expected_result = "{\n\n}"
        self.assertEqual(scope.render(), expected_result)

    def test_scope_with_children(self):
        child1 = BuiltIn("Child1")
        child2 = BuiltIn("Child2")
        scope = Scope([child1, child2], indent=2)
        expected_result = "{\n  Child1\n  Child2\n}"
        self.assertEqual(scope.render(), expected_result)

    def test_scope_with_different_indent(self):
        child1 = BuiltIn("Child1")
        child2 = BuiltIn("Child2")
        scope = Scope([child1, child2], indent=4)
        expected_result = "{\n    Child1\n    Child2\n}"
        self.assertEqual(scope.render(), expected_result)

    def test_scope_with_tuple_children(self):
        child1 = BuiltIn("Child1")
        child2 = BuiltIn("Child2")
        scope = Scope((child1, child2))
        expected_result = "{\n  Child1\n  Child2\n}"
        self.assertEqual(scope.render(), expected_result)

    def test_scope_with_set_children(self):
        child1 = BuiltIn("Child1")
        child2 = BuiltIn("Child2")
        scope = Scope({child1, child2})
        expected_result = "{\n  Child1\n  Child2\n}"
        self.assertEqual(scope.render(), expected_result)

    def test_scope_with_mixed_children(self):
        child1 = BuiltIn("Child1")
        child2 = BuiltIn("Child2")
        scope = Scope([child1, child2], indent=2)
        expected_result = "{\n  Child1\n  Child2\n}"
        self.assertEqual(scope.render(), expected_result)

    # Add more test cases as needed


import unittest

# Import the classes from your_module
# from your_module import Assign, Const, Let, Var, BuiltIn


class TestAssign(unittest.TestCase):
    def test_assign_without_value(self):
        assign = Assign("variable")
        expected_result = " variable;"
        self.assertEqual(str(assign), expected_result)

    def test_assign_with_value(self):
        assign = Assign("variable", 42)
        expected_result = " variable = 42;"
        self.assertEqual(str(assign), expected_result)


class TestConst(unittest.TestCase):
    def test_const_without_value(self):
        const = Const("constVariable")
        expected_result = "const constVariable;"
        self.assertEqual(str(const), expected_result)

    def test_const_with_value(self):
        const = Const("constVariable", "hello")
        expected_result = 'const constVariable = "hello";'
        self.assertEqual(str(const), expected_result)


class TestLet(unittest.TestCase):
    def test_let_without_value(self):
        let = Let("letVariable")
        expected_result = "let letVariable;"
        self.assertEqual(str(let), expected_result)

    def test_let_with_value(self):
        let = Let("letVariable", 3.14)
        expected_result = "let letVariable = 3.14;"
        self.assertEqual(str(let), expected_result)


class TestVar(unittest.TestCase):
    def test_var_without_value(self):
        var = Var("varVariable")
        expected_result = "var varVariable;"
        self.assertEqual(str(var), expected_result)

    def test_var_with_value(self):
        var = Var("varVariable", True)
        expected_result = "var varVariable = True;"
        self.assertEqual(str(var), expected_result)


# Import the classes you want to test
class TestPythonToJavaScriptConversion(unittest.TestCase):
    def test_iterator(self):
        # Test Iterator class
        iterable = [1, 2, 3]
        js_code = Iterator(iterable).renderClass()
        expected_js = "[1, 2, 3][Symbol.iterator]()"
        self.assertEqual(js_code, expected_js)

    def test_generator(self):
        # Test Generator class
        generator_func = "yield 1; yield 2;"
        js_code = Generator(generator_func).renderClass()
        expected_js = "function* () {\nyield 1; yield 2;\n}"
        self.assertEqual(js_code, expected_js)

    def test_list(self):
        # Test List class
        elements = [1, 2, 3]
        js_code = List(elements).renderClass()
        expected_js = "[1, 2, 3]"
        self.assertEqual(js_code, expected_js)

    def test_tuple(self):
        # Test Tuple class
        elements = (1, 2, 3)
        js_code = Tuple(elements).renderClass()
        expected_js = "[1, 2, 3]"
        self.assertEqual(js_code, expected_js)

    def test_range(self):
        # Test Range class
        start = 1
        stop = 6
        step = 2
        js_code = Range(start, stop, step).renderClass()
        expected_js = "Array.from(1, 6, 2)"
        self.assertEqual(js_code, expected_js)

    def test_immutable_sequence(self):
        # Test ImmutableSequence class
        elements = [1, 2, 3]
        js_code = ImmutableSequence(elements).renderClass()
        expected_js = "Object.freeze([1, 2, 3])"
        self.assertEqual(js_code, expected_js)

    def test_binary_sequence(self):
        # Test BinarySequence class
        binary_str = "1010"
        js_code = BinarySequence(binary_str).renderClass()
        expected_js = 'parseInt("1010", 2)'
        self.assertEqual(js_code, expected_js)

    def test_bytes(self):
        # Test Bytes class
        bytes_value = b"Hello, World!"
        js_code = Bytes(bytes_value).renderClass()
        expected_js = "new Uint8Array([72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33])"
        self.assertEqual(js_code, expected_js)

    def test_bytes_array(self):
        # Test BytesArray class
        elements = [65, 66, 67]
        js_code = BytesArray(elements).renderClass()
        expected_js = "new Uint8Array([65, 66, 67])"
        self.assertEqual(js_code, expected_js)

    def test_memory_view(self):
        # Test MemoryView class
        buffer_obj = "new ArrayBuffer(8)"
        js_code = MemoryView(buffer_obj).renderClass()
        expected_js = "new DataView(new ArrayBuffer(8))"
        self.assertEqual(js_code, expected_js)

    def test_string_format(self):
        # Test StringFormat class
        format_str = "Hello, {}!"
        args = ("world",)
        js_code = StringFormat(format_str, args).renderClass()
        expected_js = '`Hello, ${"world"}!`.format(world)'
        self.assertEqual(js_code, expected_js)

    def test_set(self):
        # Test Set class
        elements = [1, 2, 3]
        js_code = Set(elements).renderClass()
        expected_js = "new Set([1, 2, 3])"
        self.assertEqual(js_code, expected_js)

    def test_frozen_set(self):
        # Test FrozenSet class
        elements = [1, 2, 3]
        js_code = FrozenSet(elements).renderClass()
        expected_js = "new Set([1, 2, 3])"
        self.assertEqual(js_code, expected_js)

    def test_dict(self):
        # Test Dict class
        key_value_pairs = {"a": 1, "b": 2, "c": 3}
        js_code = Dict(key_value_pairs).renderClass()
        expected_js = '{"a": 1, "b": 2, "c": 3}'
        self.assertEqual(js_code, expected_js)

    def test_union_type(self):
        # Test UnionType class
        types = ["number", "string"]
        js_code = UnionType(types).renderClass()
        expected_js = "number | string"
        self.assertEqual(js_code, expected_js)


class TestZip(unittest.TestCase):
    def test_zip_render(self):
        # Create some example iterable objects
        list1 = [1, 2, 3]
        list2 = ["a", "b", "c"]
        tuple1 = (10, 20, 30)

        # Create a Zip object
        zip_obj = Zip(list1, list2, tuple1)

        # Render the Zip object
        rendered_code = zip_obj.render()

        # Define the expected JavaScript code
        expected_code = 'Array.from([1, 2, 3, "a", "b", "c", [10, 20, 30]]).map((_,i)=>[_[i], _[i+3], _[i+6]])'

        # Assert that the rendered code matches the expected code
        self.assertEqual(rendered_code, expected_code)


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
