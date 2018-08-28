from __future__ import annotations

from typing import no_type_check
import unittest

import name


class AutoNameSuite(unittest.TestCase):
    def test_object_instance(self) -> None:
        obj = name.AutoName()
        self.assertTrue(isinstance(obj, name.AutoName))

    def test_single_assignment(self) -> None:
        obj = name.AutoName()
        self.assertEqual(obj.__assigned_name__, "obj")

    def test_NameError_in_multiple_assignment(self) -> None:
        description = "Can not assign a unique name to multiple variables\."
        with self.assertRaisesRegex(NameError, description):
            a = b = name.AutoName()
            a.__assigned_name__
        with self.assertRaisesRegex(NameError, description):
            a = b = name.AutoName()
            b.__assigned_name__

    def test_unpacking(self) -> None:
        x, y = name.AutoName(2)
        self.assertEqual(x.__assigned_name__, "x")
        self.assertEqual(y.__assigned_name__, "y")

    @no_type_check
    def test_count_argument_type(self) -> None:
        description = "Expected 'int' object, got 'float'"
        with self.assertRaisesRegex(AssertionError, description):
            x, y = name.AutoName(3.5)

    def test_count_sign(self) -> None:
        description = "Expected positive 'int' number, got '-2'"
        with self.assertRaisesRegex(AssertionError, description):
            x, y = name.AutoName(-2)

    def test_subclass(self) -> None:
        class SubClass(name.AutoName):
            def __init__(self, count: int = 0) -> None:
                super().__init__(count)
        obj = SubClass()
        self.assertEqual(obj.__assigned_name__, "obj")

    def test_multiple_inheritance(self) -> None:
        class Numeric:
            def __init__(self, type: object) -> None:
                self.__type__ = type

        class Symbol(Numeric, name.AutoName):
            def __init__(self, type: object, count: int = 0) -> None:
                Numeric.__init__(self, type)
                name.AutoName.__init__(self, count)

        x = Symbol(complex)
        self.assertEqual(x.__assigned_name__, "x")
        self.assertEqual(x.__type__, complex)

    def test_assigned_name_in_a_method_of_the_child_class(self) -> None:
        """ Test the stored name in a method of a class that inherit from
        `name.AutoName`.
        """
        class Atom(name.AutoName):
            def __init__(self, count: int = 0) -> None:
                super().__init__(count)

            def __repr__(self) -> str:
                return self.__assigned_name__

        a, b, c = Atom(3)
        self.assertEqual(repr((a, b, c)), "(a, b, c)")


if __name__ == '__main__':
    unittest.main()
