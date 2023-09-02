class Constatant:
    FalseCons = "False"
    TrueCons = "True"
    NoneCons = "None"
    NotImplementedCons = "NotImplemented"
    EllipsisCons = "..."
    CopyrightCons = "copyright"
    LicenseCons = "license"
    And = "&&"
    Or = "||"
    Not = "!"


class BuiltIn(object):
    def __init__(self, *args, **kwargs) -> None:
        self.args = args
        self.kwargs = kwargs

    def render(self):
        return self.renderClass()

    def renderClass(self):
        return str(self.__dict__)

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return f"{str(self.__class__.__name__)}({self.__str__()})"


def convertType(obj):
    #! complete this function, add more types and use it every where
    convert = {str: Str, int: Int, float: Float, complex: Complex}

    if type(obj) in convert:
        objtype = convert[type(obj)]
        return objtype(obj)
    return obj


class BoolOp(BuiltIn):
    def __init__(self, obj1=None, obj2=None, op=None) -> None:
        self.obj1 = obj1
        self.obj2 = obj2
        self.op = op

    @property
    def obj1(self):
        return self.__obj1

    @obj1.setter
    def obj1(self, obj):
        self.__obj1 = convertType(obj)

    @property
    def op(self):
        return self.__op

    @op.setter
    def op(self, val: str):
        self.__op = val

    @property
    def obj2(self):
        return self.__obj2

    @obj2.setter
    def obj2(self, obj):
        self.__obj2 = convertType(obj)

    def renderClass(self):
        if not self.obj2:
            return f"{self.op}({self.obj1})"
        return f"({str(self.obj1)} {(self.op)} {(self.obj2)})"


class And(BoolOp):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2, Constatant.And)


class Or(BoolOp):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2, Constatant.Or)


class Not(BoolOp):
    def __init__(self, obj1=None) -> None:
        super().__init__(obj1, op=Constatant.Not)


class Comparisons(BuiltIn):
    def __init__(self, obj1=None, obj2=None, op=None) -> None:
        self.obj1 = obj1
        self.obj2 = obj2
        self.op = op

    @property
    def obj1(self):
        return self.__obj1

    @obj1.setter
    def obj1(self, obj):
        self.__obj1 = convertType(obj)

    @property
    def op(self):
        return self.__op

    @op.setter
    def op(self, val: str):
        self.__op = val

    @property
    def obj2(self):
        return self.__obj2

    @obj2.setter
    def obj2(self, obj):
        self.__obj2 = convertType(obj)

    def renderClass(self):
        return f"({str(self.obj1)} {(self.op)} {(self.obj2)})"


class LT(Comparisons):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2, "<")


class LTE(Comparisons):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2, "<=")


class GT(Comparisons):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2, ">")


class GTE(Comparisons):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2, ">=")


class Eq(Comparisons):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2, "==")


class NotEq(Comparisons):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2, "!=")


class Is(Comparisons):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2, "===")


class IsNot(Comparisons):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2, "!==")


class Type(BuiltIn):
    def __init__(self, obj=None) -> None:
        self.obj = obj

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = self.cast(obj)

    def cast(self, obj):
        return obj

    def renderClass(self):
        return f"{str(self.obj)}"


class Int(Type, int):
    def __init__(self, obj=None) -> None:
        super().__init__(obj)

    def cast(self, obj):
        return int(obj)


class Float(Type, float):
    def __init__(self, obj=None) -> None:
        super().__init__(obj)

    def cast(self, obj):
        return float(obj)


class Str(Type, str):
    def __init__(self, obj=None) -> None:
        super().__init__(obj)

    def renderClass(self):
        if "\n" in self.obj:
            return f"`{self.obj}`"
        return f'"{self.obj}"'

    def cast(self, obj):
        return str(obj)


class Complex(Type):
    def __init__(self, obj=None) -> None:
        super().__init__(obj)


if __name__ == "__main__":
    print(Not(And(4, 2)))
