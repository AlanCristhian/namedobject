from __future__ import annotations

import unittest

import name
import _module


class LocalVariableSuite(unittest.TestCase):
    def test_object_instance(self) -> None:
        obj = name.AutoName()
        self.assertTrue(isinstance(obj, name.AutoName))

    def test_single_assignment(self) -> None:
        obj = name.AutoName()
        self.assertEqual(obj.__name__, "obj")

    def test_multiple_assignment(self) -> None:
        a = b = c = name.AutoName()
        self.assertEqual(a.__name__, "c")
        self.assertEqual(b.__name__, "c")
        self.assertEqual(c.__name__, "c")

    def test_unpacking(self) -> None:
        x, y = name.AutoName()
        self.assertEqual(x.__name__, "x")
        self.assertEqual(y.__name__, "y")

    def test_subclass(self) -> None:
        class SubClass(name.AutoName):
            def __init__(self) -> None:
                super().__init__()
        obj = SubClass()
        self.assertEqual(obj.__name__, "obj")

    def test_multiple_inheritance(self) -> None:
        class Numeric:
            def __init__(self, type: object) -> None:
                self.__type__ = type

        class Symbol(Numeric, name.AutoName):
            def __init__(self, type: object) -> None:
                Numeric.__init__(self, type)
                name.AutoName.__init__(self)

        x = Symbol(complex)
        self.assertEqual(x.__name__, "x")
        self.assertEqual(x.__type__, complex)

    def test_assignment_in_a_child_class_method(self) -> None:
        """ Test the stored name in a method of a class that inherit from
        `name.AutoName`.
        """
        class Atom(name.AutoName):
            def __init__(self) -> None:
                super().__init__()

            def __repr__(self) -> str:
                return self.__name__

        a, b, c = Atom()
        self.assertEqual(repr((a, b, c)), "(a, b, c)")

    def test_assigned_name_in_a_namespace(self) -> None:
        class Namespace:
            attr = name.AutoName()
        self.assertEqual(Namespace.attr.__name__, "attr")

    def test_assigned_name_in_a_property_method(self) -> None:
        class Number(name.AutoName):
            @property
            def name(self) -> str:
                return self.__name__
        n = Number()
        self.assertEqual(n.name, "n")

    def test_multiple_assignment_in_namespace(self) -> None:
        class Multiple:
            attr_1 = attr_2 = name.AutoName()
        self.assertEqual(Multiple.attr_1.__name__, "attr_2")
        self.assertEqual(Multiple.attr_2.__name__, "attr_2")

    def test_single_assignment_in_context_manager(self) -> None:
        with name.AutoName() as context_obj:
            self.assertEqual(context_obj.__name__, "context_obj")

    def test_multiple_assignment_in_context_manager(self) -> None:
        with name.AutoName() as (context_ob_1, context_ob_2):
            self.assertEqual(context_ob_1.__name__, "context_ob_1")
            self.assertEqual(context_ob_2.__name__, "context_ob_2")

    def test_single_var_in_for_loop(self) -> None:
        for x in [name.AutoName()]:
            pass
        self.assertEqual(x.__name__, "x")

    def test_two_vars_in_for_loop(self) -> None:
        for x, y in [name.AutoName()]:
            pass
        self.assertEqual(x.__name__, "x")
        self.assertEqual(y.__name__, "y")

    def test_default_name(self) -> None:
        self.assertEqual(name.AutoName().__name__, "<nameless>")

    def test_inside_function(self) -> None:
        def function():
            inner = name.AutoName()
            return inner
        self.assertEqual(function().__name__, "inner")

    def test_extended_arg_opcode(self) -> None:
        _000 = name.AutoName()
        _001 = name.AutoName()
        _002 = name.AutoName()
        _003 = name.AutoName()
        _004 = name.AutoName()
        _005 = name.AutoName()
        _006 = name.AutoName()
        _007 = name.AutoName()
        _008 = name.AutoName()
        _009 = name.AutoName()
        _010 = name.AutoName()
        _011 = name.AutoName()
        _012 = name.AutoName()
        _013 = name.AutoName()
        _014 = name.AutoName()
        _015 = name.AutoName()
        _016 = name.AutoName()
        _017 = name.AutoName()
        _018 = name.AutoName()
        _019 = name.AutoName()
        _020 = name.AutoName()
        _021 = name.AutoName()
        _022 = name.AutoName()
        _023 = name.AutoName()
        _024 = name.AutoName()
        _025 = name.AutoName()
        _026 = name.AutoName()
        _027 = name.AutoName()
        _028 = name.AutoName()
        _029 = name.AutoName()
        _030 = name.AutoName()
        _031 = name.AutoName()
        _032 = name.AutoName()
        _033 = name.AutoName()
        _034 = name.AutoName()
        _035 = name.AutoName()
        _036 = name.AutoName()
        _037 = name.AutoName()
        _038 = name.AutoName()
        _039 = name.AutoName()
        _040 = name.AutoName()
        _041 = name.AutoName()
        _042 = name.AutoName()
        _043 = name.AutoName()
        _044 = name.AutoName()
        _045 = name.AutoName()
        _046 = name.AutoName()
        _047 = name.AutoName()
        _048 = name.AutoName()
        _049 = name.AutoName()
        _050 = name.AutoName()
        _051 = name.AutoName()
        _052 = name.AutoName()
        _053 = name.AutoName()
        _054 = name.AutoName()
        _055 = name.AutoName()
        _056 = name.AutoName()
        _057 = name.AutoName()
        _058 = name.AutoName()
        _059 = name.AutoName()
        _060 = name.AutoName()
        _061 = name.AutoName()
        _062 = name.AutoName()
        _063 = name.AutoName()
        _064 = name.AutoName()
        _065 = name.AutoName()
        _066 = name.AutoName()
        _067 = name.AutoName()
        _068 = name.AutoName()
        _069 = name.AutoName()
        _070 = name.AutoName()
        _071 = name.AutoName()
        _072 = name.AutoName()
        _073 = name.AutoName()
        _074 = name.AutoName()
        _075 = name.AutoName()
        _076 = name.AutoName()
        _077 = name.AutoName()
        _078 = name.AutoName()
        _079 = name.AutoName()
        _080 = name.AutoName()
        _081 = name.AutoName()
        _082 = name.AutoName()
        _083 = name.AutoName()
        _084 = name.AutoName()
        _085 = name.AutoName()
        _086 = name.AutoName()
        _087 = name.AutoName()
        _088 = name.AutoName()
        _089 = name.AutoName()
        _090 = name.AutoName()
        _091 = name.AutoName()
        _092 = name.AutoName()
        _093 = name.AutoName()
        _094 = name.AutoName()
        _095 = name.AutoName()
        _096 = name.AutoName()
        _097 = name.AutoName()
        _098 = name.AutoName()
        _099 = name.AutoName()
        _100 = name.AutoName()
        _101 = name.AutoName()
        _102 = name.AutoName()
        _103 = name.AutoName()
        _104 = name.AutoName()
        _105 = name.AutoName()
        _106 = name.AutoName()
        _107 = name.AutoName()
        _108 = name.AutoName()
        _109 = name.AutoName()
        _110 = name.AutoName()
        _111 = name.AutoName()
        _112 = name.AutoName()
        _113 = name.AutoName()
        _114 = name.AutoName()
        _115 = name.AutoName()
        _116 = name.AutoName()
        _117 = name.AutoName()
        _118 = name.AutoName()
        _119 = name.AutoName()
        _120 = name.AutoName()
        _121 = name.AutoName()
        _122 = name.AutoName()
        _123 = name.AutoName()
        _124 = name.AutoName()
        _125 = name.AutoName()
        _126 = name.AutoName()
        _127 = name.AutoName()
        _128 = name.AutoName()
        _129 = name.AutoName()
        _130 = name.AutoName()
        _131 = name.AutoName()
        _132 = name.AutoName()
        _133 = name.AutoName()
        _134 = name.AutoName()
        _135 = name.AutoName()
        _136 = name.AutoName()
        _137 = name.AutoName()
        _138 = name.AutoName()
        _139 = name.AutoName()
        _140 = name.AutoName()
        _141 = name.AutoName()
        _142 = name.AutoName()
        _143 = name.AutoName()
        _144 = name.AutoName()
        _145 = name.AutoName()
        _146 = name.AutoName()
        _147 = name.AutoName()
        _148 = name.AutoName()
        _149 = name.AutoName()
        _150 = name.AutoName()
        _151 = name.AutoName()
        _152 = name.AutoName()
        _153 = name.AutoName()
        _154 = name.AutoName()
        _155 = name.AutoName()
        _156 = name.AutoName()
        _157 = name.AutoName()
        _158 = name.AutoName()
        _159 = name.AutoName()
        _160 = name.AutoName()
        _161 = name.AutoName()
        _162 = name.AutoName()
        _163 = name.AutoName()
        _164 = name.AutoName()
        _165 = name.AutoName()
        _166 = name.AutoName()
        _167 = name.AutoName()
        _168 = name.AutoName()
        _169 = name.AutoName()
        _170 = name.AutoName()
        _171 = name.AutoName()
        _172 = name.AutoName()
        _173 = name.AutoName()
        _174 = name.AutoName()
        _175 = name.AutoName()
        _176 = name.AutoName()
        _177 = name.AutoName()
        _178 = name.AutoName()
        _179 = name.AutoName()
        _180 = name.AutoName()
        _181 = name.AutoName()
        _182 = name.AutoName()
        _183 = name.AutoName()
        _184 = name.AutoName()
        _185 = name.AutoName()
        _186 = name.AutoName()
        _187 = name.AutoName()
        _188 = name.AutoName()
        _189 = name.AutoName()
        _190 = name.AutoName()
        _191 = name.AutoName()
        _192 = name.AutoName()
        _193 = name.AutoName()
        _194 = name.AutoName()
        _195 = name.AutoName()
        _196 = name.AutoName()
        _197 = name.AutoName()
        _198 = name.AutoName()
        _199 = name.AutoName()
        _200 = name.AutoName()
        _201 = name.AutoName()
        _202 = name.AutoName()
        _203 = name.AutoName()
        _204 = name.AutoName()
        _205 = name.AutoName()
        _206 = name.AutoName()
        _207 = name.AutoName()
        _208 = name.AutoName()
        _209 = name.AutoName()
        _210 = name.AutoName()
        _211 = name.AutoName()
        _212 = name.AutoName()
        _213 = name.AutoName()
        _214 = name.AutoName()
        _215 = name.AutoName()
        _216 = name.AutoName()
        _217 = name.AutoName()
        _218 = name.AutoName()
        _219 = name.AutoName()
        _220 = name.AutoName()
        _221 = name.AutoName()
        _222 = name.AutoName()
        _223 = name.AutoName()
        _224 = name.AutoName()
        _225 = name.AutoName()
        _226 = name.AutoName()
        _227 = name.AutoName()
        _228 = name.AutoName()
        _229 = name.AutoName()
        _230 = name.AutoName()
        _231 = name.AutoName()
        _232 = name.AutoName()
        _233 = name.AutoName()
        _234 = name.AutoName()
        _235 = name.AutoName()
        _236 = name.AutoName()
        _237 = name.AutoName()
        _238 = name.AutoName()
        _239 = name.AutoName()
        _240 = name.AutoName()
        _241 = name.AutoName()
        _242 = name.AutoName()
        _243 = name.AutoName()
        _244 = name.AutoName()
        _245 = name.AutoName()
        _246 = name.AutoName()
        _247 = name.AutoName()
        _248 = name.AutoName()
        _249 = name.AutoName()
        _250 = name.AutoName()
        _251 = name.AutoName()
        _252 = name.AutoName()
        _253 = name.AutoName()
        _254 = name.AutoName()
        _255 = name.AutoName()
        _256 = name.AutoName()
        self.assertEqual(_256.__name__, "_256")

    def test_warlust(self) -> None:
        (x := name.AutoName())
        self.assertEqual(x.__name__, "x")

    def test_custom_attribute(self) -> None:
        class Number(name.AutoName):
            def __init__(self) -> None:
                super().__init__()
                self.name = self.__name__
        n = Number()
        self.assertEqual(n.name, "n")

    def test_name_collision(self):
        "Test that the name is searched in the correct namespace"
        class Subclass(name.AutoName):
            def __init__(self):
                interior = name.AutoName()
                super().__init__()
                self.interior = interior.__name__

        def namespace():
            exterior = Subclass()
            self.assertEqual(exterior.__name__, "exterior")
            self.assertEqual(exterior.interior, "interior")
        namespace()

    def test_subclass_arguments(self):
        class Numeric:
            def __init__(self, type: object) -> None:
                self.__type__ = type

        class Variable(name.AutoName, Numeric):
            def __init__(self, type: object) -> None:
                name.AutoName.__init__(self)
                Numeric.__init__(self, type)

        foo, var = Variable(int)
        self.assertEqual(foo.__name__, "foo")
        self.assertEqual(var.__name__, "var")


class CellVariableSuite(unittest.TestCase):
    def test_single_assignment(self) -> None:
        a = name.AutoName()
        b = name.AutoName()
        c = name.AutoName()

        def inner():
            return a, b, c

        x, y, z = inner()
        self.assertEqual(x.__name__, "a")
        self.assertEqual(y.__name__, "b")
        self.assertEqual(z.__name__, "c")

    def test_multiple_assignment(self) -> None:
        a = b = c = name.AutoName()

        def inner():
            return a, b, c

        x, y, z = inner()
        self.assertEqual(x.__name__, "c")
        self.assertEqual(y.__name__, "c")
        self.assertEqual(z.__name__, "c")

    def test_unpacking(self) -> None:
        a, b, c = name.AutoName()

        def inner():
            return a, b, c

        x, y, z = inner()
        self.assertEqual(x.__name__, "a")
        self.assertEqual(y.__name__, "b")
        self.assertEqual(z.__name__, "c")

    def test_subclass(self) -> None:
        class SubClass(name.AutoName):
            def __init__(self) -> None:
                super().__init__()

        a = SubClass()

        def inner():
            return a

        x = inner()
        self.assertEqual(x.__name__, "a")

    def test_multiple_inheritance(self) -> None:
        class Numeric:
            def __init__(self, type: object) -> None:
                self.__type__ = type

        class Symbol(Numeric, name.AutoName):
            def __init__(self, type: object) -> None:
                Numeric.__init__(self, type)
                name.AutoName.__init__(self)

        x = Symbol(complex)

        def inner():
            return x

        a = inner()
        self.assertEqual(a.__name__, "x")
        self.assertEqual(a.__type__, complex)

    def test_assignment_in_a_child_class_method(self) -> None:
        class Atom(name.AutoName):
            def __init__(self) -> None:
                super().__init__()

            def __repr__(self) -> str:
                return self.__name__

        a, b, c = Atom()

        def inner():
            return a, b, c

        x, y, z = inner()
        self.assertEqual(repr((x, y, z)), "(a, b, c)")

    def test_assigned_name_in_a_property_method(self) -> None:
        class Number(name.AutoName):
            @property
            def name(self) -> str:
                return self.__name__

        n = Number()

        def inner():
            return n

        m = inner()
        self.assertEqual(m.name, "n")

    def test_single_assignment_in_context_manager(self) -> None:
        with name.AutoName() as context_obj:
            def inner():
                return context_obj
        obj = inner()
        self.assertEqual(obj.__name__, "context_obj")

    def test_multiple_assignment_in_context_manager(self) -> None:
        with name.AutoName() as (a, b, c):
            def inner():
                return a, b, c
        x, y, z = inner()
        self.assertEqual(x.__name__, "a")
        self.assertEqual(y.__name__, "b")
        self.assertEqual(z.__name__, "c")

    def test_single_var_in_for_loop(self) -> None:
        for x in [name.AutoName()]:
            def inner():
                return x
        a = inner()
        self.assertEqual(a.__name__, "x")

    def test_two_vars_in_for_loop(self) -> None:
        for x, y in [name.AutoName()]:
            def inner():
                return x, y
        a, b = inner()
        self.assertEqual(x.__name__, "x")
        self.assertEqual(y.__name__, "y")


class ModuleVariableSuite(unittest.TestCase):
    def test_single_assignment(self) -> None:
        self.assertEqual(_module.obj_1.__name__, "obj_1")

    def test_multiple_assignment(self) -> None:
        self.assertEqual(_module.a.__name__, "b")
        self.assertEqual(_module.b.__name__, "b")

    def test_unpacking(self) -> None:
        self.assertEqual(_module.c.__name__, "c")
        self.assertEqual(_module.d.__name__, "d")

    def test_subclass(self) -> None:
        self.assertEqual(_module.obj_2.__name__, "obj_2")

    def test_multiple_inheritance(self) -> None:
        self.assertEqual(_module.obj_3.__name__, "obj_3")
        self.assertEqual(_module.obj_3.__type__, complex)

    def test_assignment_in_a_child_class_method(self) -> None:
        """ Test the stored name in a method of a class that inherit from
        `name.AutoName`.
        """
        expected = repr((_module.e, _module.f, _module.g))
        self.assertEqual(expected, "(e, f, g)")

    def test_assigned_name_in_a_namespace(self) -> None:
        self.assertEqual(_module.Namespace.attr.__name__, "attr")

    def test_single_assignment_in_context_manager(self) -> None:
        self.assertEqual(_module.context_0.__name__, "context_0")

    def test_multiple_assignment_in_context_manager(self) -> None:
        self.assertEqual(_module.context_1.__name__, "context_1")
        self.assertEqual(_module.context_2.__name__, "context_2")

    def test_single_var_in_for_loop(self) -> None:
        self.assertEqual(_module.h.__name__, "h")

    def test_two_vars_in_for_loop(self) -> None:
        self.assertEqual(_module.i.__name__, "i")
        self.assertEqual(_module.j.__name__, "j")


# Global variables for GlobalVariableSuite
# ========================================


ga = name.AutoName()
gb = gc = gd = name.AutoName()
ge, gf = name.AutoName()


class GSubclass(name.AutoName):
    def __init__(self) -> None:
        super().__init__()


gg = GSubclass()


class GNumeric:
    def __init__(self, type: object) -> None:
        self.__type__ = type


class GSymbol(GNumeric, name.AutoName):
    def __init__(self, type: object) -> None:
        GNumeric.__init__(self, type)
        name.AutoName.__init__(self)


gh = GSymbol(complex)


class GAtom(name.AutoName):
    def __init__(self) -> None:
        super().__init__()

    def __repr__(self) -> str:
        return self.__name__


gi, gj, gk = GAtom()


class GNumber(name.AutoName):
    @property
    def name(self) -> str:
        return self.__name__


gl = GNumber()


with name.AutoName() as gm:
    pass


with name.AutoName() as (gn, go):
    pass


for gp in [name.AutoName()]:
    pass


for gq, gr in [name.AutoName()]:
    pass


class GlobalVariableSuite(unittest.TestCase):
    def test_single_assignment(self) -> None:
        global ga
        self.assertEqual(ga.__name__, "ga")

    def test_multiple_assignment(self) -> None:
        global gb, gc, gd
        self.assertEqual(gb.__name__, "gd")
        self.assertEqual(gc.__name__, "gd")
        self.assertEqual(gd.__name__, "gd")

    def test_unpacking(self) -> None:
        global ge, gf
        self.assertEqual(ge.__name__, "ge")
        self.assertEqual(gf.__name__, "gf")

    def test_subclass(self) -> None:
        global gg
        self.assertEqual(gg.__name__, "gg")

    def test_multiple_inheritance(self) -> None:
        global gh
        self.assertEqual(gh.__name__, "gh")
        self.assertEqual(gh.__type__, complex)

    def test_assignment_in_a_child_class_method(self) -> None:
        global gi, gj, gk
        self.assertEqual(repr((gi, gj, gk)), "(gi, gj, gk)")

    def test_assigned_name_in_a_property_method(self) -> None:
        global gl
        self.assertEqual(gl.name, "gl")

    def test_single_assignment_in_context_manager(self) -> None:
        global gm
        self.assertEqual(gm.__name__, "gm")

    def test_multiple_assignment_in_context_manager(self) -> None:
        global gn, go
        self.assertEqual(gn.__name__, "gn")
        self.assertEqual(go.__name__, "go")

    def test_single_var_in_for_loop(self) -> None:
        global gp
        self.assertEqual(gp.__name__, "gp")

    def test_two_vars_in_for_loop(self) -> None:
        global gq, gr
        self.assertEqual(gq.__name__, "gq")
        self.assertEqual(gr.__name__, "gr")


if __name__ == '__main__':

    # A weird bug with global variables can only be tested here
    class TypedObj:
        def __init__(self, type: object) -> None:
            self.__type__ = type

    class NamedObj(TypedObj, name.AutoName):
        def __init__(self, type: object) -> None:
            TypedObj.__init__(self, type)
            name.AutoName.__init__(self)

    class ReprObj(name.AutoName):
        def __repr__(self) -> str:
            return self.__name__

    class Variable(ReprObj, NamedObj):
        def __init__(self, type: object) -> None:
            ReprObj.__init__(self)
            NamedObj.__init__(self, type)

    foo, var = Variable(int)

    assert foo.__name__ == "foo"
    assert var.__name__ == "var"
    assert foo.__type__ == int
    assert var.__type__ == int

    unittest.main()
