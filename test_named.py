import unittest
import inspect
from itertools import chain
import ast

import named


def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)


class TestAssignChecker(unittest.TestCase):
    def setUp(self):
        self.assign = named._AssignChecker()

    def test_single_assignment(self):
        tree = ast.parse('a = 1')
        self.assertEqual("single", self.assign.check(tree))

    def test_single_assignment(self):
        tree = ast.parse('a, b = 1')
        self.assertEqual("unpacking", self.assign.check(tree))

    def test_single_assignment(self):
        tree = ast.parse('a = b = 1')
        self.assertEqual("multiple", self.assign.check(tree))


class TestNamedObject(unittest.TestCase):

    def test_object_instance(self):
        obj = named.Object()
        self.assertTrue(isinstance(obj, named.Object))

    def test_get_outer_globals_method(self):
        current_frame = inspect.currentframe()
        global_vars = flatten(named._get_outer_globals(current_frame))
        self.assertIn("TestNamedObject", global_vars)

    def test_single_assignment(self):
        obj = named.Object()
        self.assertEqual(obj.__name__, "obj")

    def test_single_attribute_assignment(self):
        obj = named.Object()
        self.assertEqual(obj.__name__, "obj")

    def test_NotImplementedError_in_multiple_assignment(self):
        with self.assertRaises(NotImplementedError):
            a = b = named.Object()

    def test_boke_line(self):
        a = named.Object(
            ) # this line should be broken
        self.assertEqual(a.__name__, "a")

    def test_unpacking(self):
        x, y, z = named.Object(3)
        self.assertEqual(x.__name__, "x")
        self.assertEqual(y.__name__, "y")
        self.assertEqual(z.__name__, "z")

    def test_invalid_object_in_the_product(self):
        message = "'float' object is not 'int'"
        with self.assertRaisesRegex(AssertionError, message):
            x, y, z = named.Object(3.5)

    def test_subclass(self):
        class SubClass(named.Object):
            def __init__(self):
                super().__init__()
        obj = SubClass()
        self.assertEqual(obj.__name__, "obj")

    def test_very_deep_subclass(self):
        class SubClass0(named.Object):
            def __init__(self):
                super().__init__()
        class SubClass1(SubClass0):
            def __init__(self):
                super().__init__()
        class SubClass2(SubClass1):
            def __init__(self):
                super().__init__()
        class SubClass3(SubClass2):
            def __init__(self):
                super().__init__()
        class SubClass4(SubClass3):
            def __init__(self):
                super().__init__()
        class SubClass5(SubClass4):
            def __init__(self):
                super().__init__()
        class SubClass6(SubClass5):
            def __init__(self):
                super().__init__()
        class SubClass7(SubClass6):
            def __init__(self):
                super().__init__()
        class SubClass8(SubClass7):
            def __init__(self):
                super().__init__()
        class SubClass9(SubClass8):
            def __init__(self):
                super().__init__()
        obj = SubClass9()
        self.assertEqual(obj.__name__, "obj")

    def test_multiple_inheritance(self):
        class Numeric:
            def __init__(self, type):
                self.__type__ = type

        class Symbol(Numeric, named.Object):
            def __init__(self, type):
                Numeric.__init__(self, type)
                named.Object.__init__(self)

        x = Symbol(complex)
        self.assertEqual(x.__name__, "x")
        self.assertEqual(x.__type__, complex)


class AtomsSuite(unittest.TestCase):
    def test_single_atom(self):
        a = named.Atom()
        self.assertTrue(a == "a")
        self.assertIsInstance(a, str)

    def test_unpack(self):
        a, b, c = named.Atom(3)
        self.assertTrue(a == "a")
        self.assertTrue(b == "b")
        self.assertTrue(c == "c")
        self.assertIsInstance(a, str)
        self.assertIsInstance(b, str)
        self.assertIsInstance(c, str)


if __name__ == '__main__':
    unittest.main()
