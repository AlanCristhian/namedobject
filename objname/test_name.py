import sys
import unittest

import name
from . import _module


class LocalVariableSuite(unittest.TestCase):
    def test_object_instance(self) -> None:
        obj = name.AutoName()
        self.assertTrue(isinstance(obj, name.AutoName))

    def test_single_assignment(self) -> None:
        obj = name.AutoName()
        self.assertEqual(obj.name, "obj")

    def test_multiple_assignment(self) -> None:
        a = b = c = name.AutoName()
        self.assertEqual(a.name, "c")
        self.assertEqual(b.name, "c")
        self.assertEqual(c.name, "c")

    def test_unpacking(self) -> None:
        x, y = name.AutoName()
        self.assertEqual(x.name, "x")
        self.assertEqual(y.name, "y")

    def test_subclass(self) -> None:
        class SubClass(name.AutoName):
            def __init__(self) -> None:
                super().__init__()
        obj = SubClass()
        self.assertEqual(obj.name, "obj")

    def test_multiple_inheritance(self) -> None:
        class Numeric:
            def __init__(self, type: object) -> None:
                self.__type__ = type

        class Symbol(Numeric, name.AutoName):
            def __init__(self, type: object) -> None:
                Numeric.__init__(self, type)
                name.AutoName.__init__(self)

        x = Symbol(complex)
        self.assertEqual(x.name, "x")
        self.assertEqual(x.__type__, complex)

    def test_assignment_in_a_child_class_method(self) -> None:
        """ Test the stored name in a method of a class that inherit from
        `name.AutoName`.
        """
        class Atom(name.AutoName):
            def __init__(self) -> None:
                super().__init__()

            def __repr__(self) -> str:
                return self.name

        a, b, c = Atom()
        self.assertEqual(repr((a, b, c)), "(a, b, c)")

    def test_assigned_name_in_a_namespace(self) -> None:
        class Namespace:
            attr = name.AutoName()
        self.assertEqual(Namespace.attr.name, "attr")

    def test_assigned_name_in_a_property_method(self) -> None:
        class Number(name.AutoName):
            @property
            def custom_attribute_name(self) -> str:
                return self.name
        n = Number()
        self.assertEqual(n.custom_attribute_name, "n")

    def test_multiple_assignment_in_namespace(self) -> None:
        class Multiple:
            attr_1 = attr_2 = name.AutoName()
        self.assertEqual(Multiple.attr_1.name, "attr_2")
        self.assertEqual(Multiple.attr_2.name, "attr_2")

    def test_single_var_in_for_loop(self) -> None:
        for x in [name.AutoName()]:
            pass
        self.assertEqual(x.name, "x")

    def test_two_vars_in_for_loop(self) -> None:
        for x, y in [name.AutoName()]:
            pass
        self.assertEqual(x.name, "x")
        self.assertEqual(y.name, "y")

    def test_default_name(self) -> None:
        self.assertEqual(name.AutoName().name, "<nameless>")

    def test_inside_function(self) -> None:
        def function():
            inner = name.AutoName()
            return inner
        self.assertEqual(function().name, "inner")

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
        self.assertEqual(_256.name, "_256")

    @unittest.skipIf(sys.version_info < (3, 8), "No warlust operator.")
    def test_warlust(self) -> None:
        expression = "\n".join((
            '(x := name.AutoName())',
            'self.assertEqual(x.name, "x")',
        ))
        exec(expression)

    def test_custom_attribute(self) -> None:
        class Number(name.AutoName):
            def __init__(self) -> None:
                super().__init__()
                self.name = self.name
        n = Number()
        self.assertEqual(n.name, "n")

    def test_name_collision(self):
        "Test that the name is searched in the correct namespace"
        class Subclass(name.AutoName):
            def __init__(self):
                interior = name.AutoName()
                super().__init__()
                self.interior = interior.name

        def namespace():
            exterior = Subclass()
            self.assertEqual(exterior.name, "exterior")
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
        self.assertEqual(foo.name, "foo")
        self.assertEqual(var.name, "var")

    def test_autoname_instance_as_object_attribute(self) -> None:
        class Object:
            def __init__(self):
                self.attribute = name.AutoName()
        obtained = Object().attribute.name
        self.assertEqual(obtained, "attribute")


class CellVariableSuite(unittest.TestCase):
    def test_single_assignment(self) -> None:
        a = name.AutoName()
        b = name.AutoName()
        c = name.AutoName()

        def inner():
            return a, b, c

        x, y, z = inner()
        self.assertEqual(x.name, "a")
        self.assertEqual(y.name, "b")
        self.assertEqual(z.name, "c")

    def test_multiple_assignment(self) -> None:
        a = b = c = name.AutoName()

        def inner():
            return a, b, c

        x, y, z = inner()
        self.assertEqual(x.name, "c")
        self.assertEqual(y.name, "c")
        self.assertEqual(z.name, "c")

    def test_unpacking(self) -> None:
        a, b, c = name.AutoName()

        def inner():
            return a, b, c

        x, y, z = inner()
        self.assertEqual(x.name, "a")
        self.assertEqual(y.name, "b")
        self.assertEqual(z.name, "c")

    def test_subclass(self) -> None:
        class SubClass(name.AutoName):
            def __init__(self) -> None:
                super().__init__()

        a = SubClass()

        def inner():
            return a

        x = inner()
        self.assertEqual(x.name, "a")

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
        self.assertEqual(a.name, "x")
        self.assertEqual(a.__type__, complex)

    def test_assignment_in_a_child_class_method(self) -> None:
        class Atom(name.AutoName):
            def __init__(self) -> None:
                super().__init__()

            def __repr__(self) -> str:
                return self.name

        a, b, c = Atom()

        def inner():
            return a, b, c

        x, y, z = inner()
        self.assertEqual(repr((x, y, z)), "(a, b, c)")

    def test_assigned_name_in_a_property_method(self) -> None:
        class Number(name.AutoName):
            @property
            def custom_attribute_name(self) -> str:
                return self.name

        n = Number()

        def inner():
            return n

        m = inner()
        self.assertEqual(m.custom_attribute_name, "n")

    def test_single_var_in_for_loop(self) -> None:
        for x in [name.AutoName()]:
            def inner():
                return x
        a = inner()
        self.assertEqual(a.name, "x")

    def test_two_vars_in_for_loop(self) -> None:
        for x, y in [name.AutoName()]:
            def inner():
                return x, y
        a, b = inner()
        self.assertEqual(x.name, "x")
        self.assertEqual(y.name, "y")


class ModuleVariableSuite(unittest.TestCase):
    def test_single_assignment(self) -> None:
        self.assertEqual(_module.obj_1.name, "obj_1")

    def test_multiple_assignment(self) -> None:
        self.assertEqual(_module.a.name, "b")
        self.assertEqual(_module.b.name, "b")

    def test_unpacking(self) -> None:
        self.assertEqual(_module.c.name, "c")
        self.assertEqual(_module.d.name, "d")

    def test_subclass(self) -> None:
        self.assertEqual(_module.obj_2.name, "obj_2")

    def test_multiple_inheritance(self) -> None:
        self.assertEqual(_module.obj_3.name, "obj_3")
        self.assertEqual(_module.obj_3.__type__, complex)

    def test_assignment_in_a_child_class_method(self) -> None:
        """ Test the stored name in a method of a class that inherit from
        `name.AutoName`.
        """
        expected = repr((_module.e, _module.f, _module.g))
        self.assertEqual(expected, "(e, f, g)")

    def test_assigned_name_in_a_namespace(self) -> None:
        self.assertEqual(_module.Namespace.attr.name, "attr")

    def test_single_var_in_for_loop(self) -> None:
        self.assertEqual(_module.h.name, "h")

    def test_two_vars_in_for_loop(self) -> None:
        self.assertEqual(_module.i.name, "i")
        self.assertEqual(_module.j.name, "j")


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
        return self.name


gi, gj, gk = GAtom()


class GNumber(name.AutoName):
    @property
    def custom_attribute_name(self) -> str:
        return self.name


gl = GNumber()


for gp in [name.AutoName()]:
    pass


for gq, gr in [name.AutoName()]:
    pass


class GlobalVariableSuite(unittest.TestCase):
    def test_single_assignment(self) -> None:
        global ga
        self.assertEqual(ga.name, "ga")

    def test_multiple_assignment(self) -> None:
        global gb, gc, gd
        self.assertEqual(gb.name, "gd")
        self.assertEqual(gc.name, "gd")
        self.assertEqual(gd.name, "gd")

    def test_unpacking(self) -> None:
        global ge, gf
        self.assertEqual(ge.name, "ge")
        self.assertEqual(gf.name, "gf")

    def test_subclass(self) -> None:
        global gg
        self.assertEqual(gg.name, "gg")

    def test_multiple_inheritance(self) -> None:
        global gh
        self.assertEqual(gh.name, "gh")
        self.assertEqual(gh.__type__, complex)

    def test_assignment_in_a_child_class_method(self) -> None:
        global gi, gj, gk
        self.assertEqual(repr((gi, gj, gk)), "(gi, gj, gk)")

    def test_assigned_name_in_a_property_method(self) -> None:
        global gl
        self.assertEqual(gl.custom_attribute_name, "gl")

    def test_single_var_in_for_loop(self) -> None:
        global gp
        self.assertEqual(gp.name, "gp")

    def test_two_vars_in_for_loop(self) -> None:
        global gq, gr
        self.assertEqual(gq.name, "gq")
        self.assertEqual(gr.name, "gr")


class IterableUnpackingAndMultipleAssignmentCase(unittest.TestCase):
    def test_0(self) -> None:
        #  6 DUP_TOP
        #  8 STORE_FAST               1 (a)
        # 10 STORE_FAST               2 (b)
        a = b = name.AutoName()
        self.assertEqual(a.name, "b")
        self.assertEqual(b.name, "b")

    def test_1(self) -> None:
        #  6 UNPACK_SEQUENCE          2
        #  8 STORE_FAST               1 (a)
        # 10 STORE_FAST               2 (b)
        a, b = name.AutoName()
        self.assertEqual(a.name, "a")
        self.assertEqual(b.name, "b")

    def test_2(self) -> None:
        #  6 DUP_TOP
        #  8 STORE_FAST               1 (a)
        # 10 UNPACK_SEQUENCE          2
        # 12 STORE_FAST               2 (b)
        # 14 STORE_FAST               3 (c)
        a = b, c = name.AutoName()
        self.assertEqual(a.name, "a")
        self.assertEqual(b.name, "b")
        self.assertEqual(c.name, "c")

    def test_3(self) -> None:
        #  6 DUP_TOP
        #  8 UNPACK_SEQUENCE          2
        # 10 STORE_FAST               1 (a)
        # 12 STORE_FAST               2 (b)
        # 14 STORE_FAST               3 (c)
        a, b = c = name.AutoName()
        self.assertEqual(a.name, "a")
        self.assertEqual(b.name, "b")
        self.assertEqual(c.name, "c")

    def test_4(self) -> None:
        #  6 DUP_TOP
        #  8 STORE_FAST               1 (a)
        # 10 DUP_TOP
        # 12 STORE_FAST               2 (b)
        # 14 UNPACK_SEQUENCE          2
        # 16 STORE_FAST               3 (c)
        # 18 STORE_FAST               4 (d)
        a = b = c, d = name.AutoName()
        self.assertEqual(a.name, "b")
        self.assertEqual(b.name, "b")
        self.assertEqual(c.name, "c")
        self.assertEqual(d.name, "d")

    def test_5(self) -> None:
        """ multiple and unpacking
              6 DUP_TOP
              8 UNPACK_SEQUENCE          2
             10 STORE_FAST               1 (a)
             12 STORE_FAST               2 (b)
             14 DUP_TOP
             16 STORE_FAST               3 (c)
             18 STORE_FAST               4 (d)
        """
        a, b = c = d = name.AutoName()
        self.assertEqual(a.name, "a")
        self.assertEqual(b.name, "b")
        self.assertEqual(c.name, "d")
        self.assertEqual(d.name, "d")

    def test_6(self) -> None:
        #  6 DUP_TOP
        #  8 STORE_FAST               1 (a)
        # 10 DUP_TOP
        # 12 STORE_FAST               2 (b)
        # 14 DUP_TOP
        # 16 UNPACK_SEQUENCE          2
        # 18 STORE_FAST               3 (c)
        # 20 STORE_FAST               4 (d)
        # 22 DUP_TOP
        # 24 STORE_FAST               5 (e)
        # 26 STORE_FAST               6 (f)
        a = b = c, d = e = f = name.AutoName()
        self.assertEqual(a.name, "f")
        self.assertEqual(b.name, "f")
        self.assertEqual(c.name, "c")
        self.assertEqual(d.name, "d")
        self.assertEqual(e.name, "f")
        self.assertEqual(f.name, "f")

    def test_7(self):
        #  6 DUP_TOP
        #  8 UNPACK_SEQUENCE          2
        # 10 STORE_FAST               1 (a)
        # 12 STORE_FAST               2 (b)
        # 14 DUP_TOP
        # 16 STORE_FAST               3 (c)
        # 18 DUP_TOP
        # 20 STORE_FAST               4 (d)
        # 22 UNPACK_SEQUENCE          2
        # 24 STORE_FAST               5 (e)
        # 26 STORE_FAST               6 (f)
        a, b = c = d = e, f = name.AutoName()
        self.assertEqual(a.name, "a")
        self.assertEqual(b.name, "b")
        self.assertEqual(c.name, "d")
        self.assertEqual(d.name, "d")
        self.assertEqual(e.name, "e")
        self.assertEqual(f.name, "f")


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
            return self.name

    class Variable(ReprObj, NamedObj):
        def __init__(self, type: object) -> None:
            ReprObj.__init__(self)
            NamedObj.__init__(self, type)

    foo, var = Variable(int)

    assert foo.name == "foo"
    assert var.name == "var"
    assert foo.__type__ == int
    assert var.__type__ == int

    unittest.main()
