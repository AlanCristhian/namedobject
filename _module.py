"This module was created for test purpose"


import name


class Class(name.AutoName):
    pass


obj_1 = Class()


a = b = name.AutoName()


c, d = name.AutoName(2)


class SubClass(name.AutoName):
    def __init__(self, count: int = 1) -> None:
        super().__init__(count)


obj_2 = SubClass()


class Numeric:
    def __init__(self, type: object) -> None:
        self.__type__ = type


class Symbol(Numeric, name.AutoName):
    def __init__(self, type: object, count: int = 1) -> None:
        Numeric.__init__(self, type)
        name.AutoName.__init__(self, count)


obj_3 = Symbol(complex)


class Atom(name.AutoName):
    def __init__(self, count: int = 1) -> None:
        super().__init__(count)

    def __repr__(self) -> str:
        return self.__name__


e, f, g = Atom(3)


class Namespace:
    attr = name.AutoName()


with name.AutoName() as context_0:
    pass


with name.AutoName(2) as (context_1, context_2):
    pass


for h in [name.AutoName()]:
    pass


for i, j in [name.AutoName(2)]:
    pass
