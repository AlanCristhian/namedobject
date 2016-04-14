import inspect
import traceback
import ast
import itertools
import sys
import re


class _AssignChecker(ast.NodeVisitor):
    def __init__(self):
        self._assign_type = None

    def check(self, node):
        self.visit(node)
        return self._assign_type

    def visit_Assign(self, node):
        if isinstance(node.targets[0], ast.Tuple):
            self._assign_type = "unpacking"
        elif len(node.targets) > 1:
            self._assign_type = "multiple"
        else:
            self._assign_type = "single"
        self.generic_visit(node)


def _get_outer_globals(frame):
    # Yield all global variables in the higher (calling) frames
    while frame:
        yield frame.f_globals
        frame = frame.f_back


class Object:
    """Make an object with the __name__ property."""
    def __init__(self, amount=0):
        # !!!: the _get_name_from_traceback() method should be executed
        # in the __init__() method to work. May be this have some relation
        # with the traceback.extract_stack() method.
        self._from_traceback_name = self._get_name_from_traceback()
        self._index = None
        assert isinstance(amount, int), \
               "'%s' object is not 'int'" % amount.__class__.__name__
        self._amount = amount
        self._name = None

    def __iter__(self):
        return (Object()._set_index(i) for i in range(self._amount))

    def _set_index(self, index):
        self._index = index
        return self

    def _get_source_code(self):
        # Return the source code that create the object.
        try:
            for _stack_position in itertools.count(-3, -1):
                filename, *_ = traceback.extract_stack()[_stack_position]
                if sys.base_exec_prefix in filename:
                    break
            *_, text = traceback.extract_stack()[_stack_position + 1]
            return text
        except IndexError:
            return

    def _get_name_from_traceback(self):
        # Find the name looking the text of the traceback
        text = self._get_source_code()
        assign_type = None
        if text:
            try:
                tree = ast.parse(text)
                assign = _AssignChecker()
                assign_type = assign.check(tree)
                if assign_type == "multiple":
                    raise NotImplementedError(
                        "Can not assing a unique name to multiple variables.")
            except SyntaxError:
                left, *_ = text.split('=')
                if "," in left:
                    assign_type = "unpacking"
                else:
                    assign_type = "single"
            if assign_type == "single":
                full_name, *_ = text.split('=')
                *_, name = full_name.split('.')
                return name.strip()
            elif assign_type == "unpacking":
                full_name, *_ = text.split('=')
                *_, name_list = full_name.split('.')
                names = re.sub(" |\(|\)", "", name_list).split(",")
                return names
            else:
                return None
        else:
            return None

    def _get_name_from_globals(self):
        # Find the name looking each superior global namespace
        global_variables = _get_outer_globals(inspect.currentframe())
        for variables in global_variables:
            # CAVEAT: the same object could have many names. So I store all
            # in the names var.
            names = []
            for name, value in variables.items():
                if value is self:
                    names.append(name)
            if len(names) > 1:
                raise NotImplementedError(
                    "Can not assing a unique name to multiple variables.")
        if len(names) == 0:
            raise RuntimeError("Can not found the name of this variable.")
        else:
            return names[0]

    @property
    def __name__(self):
        # Find the name of the instance of the current class
        if self._name is None:
            if self._from_traceback_name is None:
                self._name = self._get_name_from_globals()
            else:
                if isinstance(self._from_traceback_name, list):
                    self._name = self._from_traceback_name[self._index]
                else:
                    self._name = self._from_traceback_name
        return self._name

    # NOTE: I Can not override the __qualname__ property. That's an cpython
    # resctriction. See http://bugs.python.org/issue19073
    # @_cached_property
    # def __qualname__(self):
    #     return "%s.%s" % (self.__class__.__name__, self.__name__)

    def __repr__(self):
        return self.__name__


class Atom(str):
    def __init__(self, amount=0):
        self._from_traceback_name = self._get_name_from_traceback()
        self._index = None
        assert isinstance(amount, int), \
               "'%s' object is not 'int'" % amount.__class__.__name__
        self._amount = amount
        self._name = None

    def __iter__(self):
        return (Atom()._set_index(i) for i in range(self._amount))

    def _set_index(self, index):
        self._index = index
        return self

    def _get_source_code(self):
        # Return the source code that create the object.
        try:
            for _stack_position in itertools.count(-3, -1):
                filename, *_ = traceback.extract_stack()[_stack_position]
                if sys.base_exec_prefix in filename:
                    break
            *_, text = traceback.extract_stack()[_stack_position + 1]
            return text
        except IndexError:
            return

    def _get_name_from_traceback(self):
        # Find the name looking the text of the traceback
        text = self._get_source_code()
        assign_type = None
        if text:
            try:
                tree = ast.parse(text)
                assign = _AssignChecker()
                assign_type = assign.check(tree)
                if assign_type == "multiple":
                    raise NotImplementedError(
                        "Can not assing a unique name to multiple variables.")
            except SyntaxError:
                left, *_ = text.split('=')
                if "," in left:
                    assign_type = "unpacking"
                else:
                    assign_type = "single"
            if assign_type == "single":
                full_name, *_ = text.split('=')
                *_, name = full_name.split('.')
                return name.strip()
            elif assign_type == "unpacking":
                full_name, *_ = text.split('=')
                *_, name_list = full_name.split('.')
                names = re.sub(" |\(|\)", "", name_list).split(",")
                return names
            else:
                return None
        else:
            return None

    def _get_name_from_globals(self):
        # Find the name looking each superior global namespace
        global_variables = _get_outer_globals(inspect.currentframe())
        for variables in global_variables:
            # CAVEAT: the same object could have many names. So I store all
            # in the names var.
            names = []
            for name, value in variables.items():
                if value is self:
                    names.append(name)
            if len(names) > 1:
                raise NotImplementedError(
                    "Can not assing a unique name to multiple variables.")
        if len(names) == 0:
            raise RuntimeError("Can not found the name of this variable.")
        else:
            return names[0]

    def _set_value(self):
        # Find the name of the instance of the current class
        if self._name is None:
            if self._from_traceback_name is None:
                self._name = self._get_name_from_globals()
            else:
                if isinstance(self._from_traceback_name, list):
                    self._name = self._from_traceback_name[self._index]
                else:
                    self._name = self._from_traceback_name

    def __add__(self, *args, **kwargs):
        self._set_value()
        return self._name.__add__(*args, **kwargs)

    def __contains__(self, *args, **kwargs):
        self._set_value()
        return self._name.__contains__(*args, **kwargs)

    def __eq__(self, *args, **kwargs):
        self._set_value()
        return self._name.__eq__(*args, **kwargs)

    def __format__(self, *args, **kwargs):
        self._set_value()
        return self._name.__format__(*args, **kwargs)

    def __ge__(self, *args, **kwargs):
        self._set_value()
        return self._name.__ge__(*args, **kwargs)

    def __getitem__(self, *args, **kwargs):
        self._set_value()
        return self._name.__getitem__(*args, **kwargs)

    def __getnewargs__(self, *args, **kwargs):
        self._set_value()
        return self._name.__getnewargs__(*args, **kwargs)

    def __gt__(self, *args, **kwargs):
        self._set_value()
        return self._name.__gt__(*args, **kwargs)

    def __hash__(self, *args, **kwargs):
        self._set_value()
        return self._name.__hash__(*args, **kwargs)

    def __le__(self, *args, **kwargs):
        self._set_value()
        return self._name.__le__(*args, **kwargs)

    def __len__(self, *args, **kwargs):
        self._set_value()
        return self._name.__len__(*args, **kwargs)

    def __lt__(self, *args, **kwargs):
        self._set_value()
        return self._name.__lt__(*args, **kwargs)

    def __mod__(self, *args, **kwargs):
        self._set_value()
        return self._name.__mod__(*args, **kwargs)

    def __mul__(self, *args, **kwargs):
        self._set_value()
        return self._name.__mul__(*args, **kwargs)

    def __ne__(self, *args, **kwargs):
        self._set_value()
        return self._name.__ne__(*args, **kwargs)

    def __reduce__(self, *args, **kwargs):
        self._set_value()
        return self._name.__reduce__(*args, **kwargs)

    def __reduce_ex__(self, *args, **kwargs):
        self._set_value()
        return self._name.__reduce_ex__(*args, **kwargs)

    def __repr__(self, *args, **kwargs):
        self._set_value()
        return self._name.__repr__(*args, **kwargs)

    def __rmod__(self, *args, **kwargs):
        self._set_value()
        return self._name.__rmod__(*args, **kwargs)

    def __rmul__(self, *args, **kwargs):
        self._set_value()
        return self._name.__rmul__(*args, **kwargs)

    def __str__(self, *args, **kwargs):
        self._set_value()
        return self._name.__str__(*args, **kwargs)

    def capitalize(self, *args, **kwargs):
        self._set_value()
        return self._name.capitalize(*args, **kwargs)

    def casefold(self, *args, **kwargs):
        self._set_value()
        return self._name.casefold(*args, **kwargs)

    def center(self, *args, **kwargs):
        self._set_value()
        return self._name.center(*args, **kwargs)

    def count(self, *args, **kwargs):
        self._set_value()
        return self._name.count(*args, **kwargs)

    def encode(self, *args, **kwargs):
        self._set_value()
        return self._name.encode(*args, **kwargs)

    def endswith(self, *args, **kwargs):
        self._set_value()
        return self._name.endswith(*args, **kwargs)

    def expandtabs(self, *args, **kwargs):
        self._set_value()
        return self._name.expandtabs(*args, **kwargs)

    def find(self, *args, **kwargs):
        self._set_value()
        return self._name.find(*args, **kwargs)

    def format(self, *args, **kwargs):
        self._set_value()
        return self._name.format(*args, **kwargs)

    def format_map(self, *args, **kwargs):
        self._set_value()
        return self._name.format_map(*args, **kwargs)

    def index(self, *args, **kwargs):
        self._set_value()
        return self._name.index(*args, **kwargs)

    def isalnum(self, *args, **kwargs):
        self._set_value()
        return self._name.isalnum(*args, **kwargs)

    def isalpha(self, *args, **kwargs):
        self._set_value()
        return self._name.isalpha(*args, **kwargs)

    def isdecimal(self, *args, **kwargs):
        self._set_value()
        return self._name.isdecimal(*args, **kwargs)

    def isdigit(self, *args, **kwargs):
        self._set_value()
        return self._name.isdigit(*args, **kwargs)

    def isidentifier(self, *args, **kwargs):
        self._set_value()
        return self._name.isidentifier(*args, **kwargs)

    def islower(self, *args, **kwargs):
        self._set_value()
        return self._name.islower(*args, **kwargs)

    def isnumeric(self, *args, **kwargs):
        self._set_value()
        return self._name.isnumeric(*args, **kwargs)

    def isprintable(self, *args, **kwargs):
        self._set_value()
        return self._name.isprintable(*args, **kwargs)

    def isspace(self, *args, **kwargs):
        self._set_value()
        return self._name.isspace(*args, **kwargs)

    def istitle(self, *args, **kwargs):
        self._set_value()
        return self._name.istitle(*args, **kwargs)

    def isupper(self, *args, **kwargs):
        self._set_value()
        return self._name.isupper(*args, **kwargs)

    def join(self, *args, **kwargs):
        self._set_value()
        return self._name.join(*args, **kwargs)

    def ljust(self, *args, **kwargs):
        self._set_value()
        return self._name.ljust(*args, **kwargs)

    def lower(self, *args, **kwargs):
        self._set_value()
        return self._name.lower(*args, **kwargs)

    def lstrip(self, *args, **kwargs):
        self._set_value()
        return self._name.lstrip(*args, **kwargs)

    def maketrans(self, *args, **kwargs):
        self._set_value()
        return self._name.maketrans(*args, **kwargs)

    def partition(self, *args, **kwargs):
        self._set_value()
        return self._name.partition(*args, **kwargs)

    def replace(self, *args, **kwargs):
        self._set_value()
        return self._name.replace(*args, **kwargs)

    def rfind(self, *args, **kwargs):
        self._set_value()
        return self._name.rfind(*args, **kwargs)

    def rindex(self, *args, **kwargs):
        self._set_value()
        return self._name.rindex(*args, **kwargs)

    def rjust(self, *args, **kwargs):
        self._set_value()
        return self._name.rjust(*args, **kwargs)

    def rpartition(self, *args, **kwargs):
        self._set_value()
        return self._name.rpartition(*args, **kwargs)

    def rsplit(self, *args, **kwargs):
        self._set_value()
        return self._name.rsplit(*args, **kwargs)

    def rstrip(self, *args, **kwargs):
        self._set_value()
        return self._name.rstrip(*args, **kwargs)

    def split(self, *args, **kwargs):
        self._set_value()
        return self._name.split(*args, **kwargs)

    def splitlines(self, *args, **kwargs):
        self._set_value()
        return self._name.splitlines(*args, **kwargs)

    def startswith(self, *args, **kwargs):
        self._set_value()
        return self._name.startswith(*args, **kwargs)

    def strip(self, *args, **kwargs):
        self._set_value()
        return self._name.strip(*args, **kwargs)

    def swapcase(self, *args, **kwargs):
        self._set_value()
        return self._name.swapcase(*args, **kwargs)

    def title(self, *args, **kwargs):
        self._set_value()
        return self._name.title(*args, **kwargs)

    def translate(self, *args, **kwargs):
        self._set_value()
        return self._name.translate(*args, **kwargs)

    def upper(self, *args, **kwargs):
        self._set_value()
        return self._name.upper(*args, **kwargs)

    def zfill(self, *args, **kwargs):
        self._set_value()
        return self._name.zfill(*args, **kwargs)
