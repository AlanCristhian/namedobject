import unittest
import inspect
from itertools import chain
import ast

import namedobject


def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)


class TestAssignChecker(unittest.TestCase):
    def setUp(self):
        self.assign = namedobject._AssignChecker()

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
    def setUp(self):
        self.obj = namedobject.NamedObject()

    def test_object_instance(self):
        self.obj = namedobject.NamedObject()
        self.assertTrue(isinstance(self.obj, namedobject.NamedObject))

    def test_get_outer_globals_method(self):
        current_frame = inspect.currentframe()
        global_vars = flatten(self.obj._get_outer_globals(current_frame))
        self.assertIn("TestNamedObject", global_vars)

    def test_single_assignment(self):
        obj = namedobject.NamedObject()
        self.assertEqual(obj.__name__, "obj")

    def test_single_attribute_assignment(self):
        self.obj = namedobject.NamedObject()
        self.assertEqual(self.obj.__name__, "obj")

    def test_NotImplementedError_in_multiple_assignment(self):
        with self.assertRaises(NotImplementedError):
            a = b = namedobject.NamedObject()


if __name__ == '__main__':
    unittest.main()
