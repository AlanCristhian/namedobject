"This module was created for test purpose"


import name


class Class(name.AutoName):
    pass


obj_1 = Class()


a = b = name.AutoName()


c, d = name.AutoName()


class SubClass(name.AutoName):
    def __init__(self) -> None:
        super().__init__()


obj_2 = SubClass()


class Numeric:
    def __init__(self, type: object) -> None:
        self.__type__ = type


class Symbol(Numeric, name.AutoName):
    def __init__(self, type: object) -> None:
        Numeric.__init__(self, type)
        name.AutoName.__init__(self)


obj_3 = Symbol(complex)


class Atom(name.AutoName):
    def __init__(self) -> None:
        super().__init__()

    def __repr__(self) -> str:
        return self.name


e, f, g = Atom()


class Namespace:
    attr = name.AutoName()


for h in [name.AutoName()]:
    pass


for i, j in [name.AutoName()]:
    pass
