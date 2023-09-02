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
    Add = '+'
    Sub = '-'
    Mult = '*'
    Div = '/'
    FloorDiv = 'Math.floor'
    Pow = 'Math.pow'
    Mod = '%'
    BitAnd = '&'
    BitOr = '|'
    BitXor = '^'
    LShift = '<<'
    RShift = '>>'
    Negative = '-'
    Posetive = '+'
    BitInvert = '~'
    
    


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
        if self.obj2 == None:
            return f"({self.op}{self.obj1})"
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


class Op(BuiltIn):
    def __init__(self, obj1=None, obj2=None, op=None, method=None, aug=None) -> None:
        self.obj1 = obj1
        self.obj2 = obj2
        self.method = method
        self.aug = aug
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
    def op(self, val:str):
        self.__op = val
        
    @property 
    def obj2(self):
        return self.__obj2
    @obj2.setter
    def obj2(self, obj):
        self.__obj2 = convertType(obj)
        
    @property 
    def method(self):
        return self.__method
    @method.setter
    def method(self, val:str):
        self.__method = val
        
    @property 
    def aug(self):
        return self.__aug
    @aug.setter
    def aug(self, val:bool):
        self.__aug = val
        
    def renderClass(self):
        render_text = ''
        if self.obj2 == None:
            render_text = f'({self.op}{self.obj1})'
        elif self.aug:
            if self.method:
                render_text = f'{self.obj1} = {self.op}({self.obj1},{self.obj2})'
            else:
                render_text = f'{self.obj1} {self.op}= {self.obj2}'
        else:
            if self.method:
                render_text = f'{self.op}({self.obj1},{self.obj2})'
            else:
                render_text = f'({self.obj1} {self.op} {self.obj2})'

        return render_text

class Add(Op):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2,Constatant.Add,)


class Sub(Op):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2,Constatant.Sub,)


class Mult(Op):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2,Constatant.Mult,)


class Div(Op):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2,Constatant.Div,)


class FloorDiv(Op):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2,Constatant.FloorDiv,)


class Mod(Op):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2,Constatant.Mod,)


class Pow(Op):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2,Constatant.Pow,)


class Negative(Op):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2,Constatant.Negative,)


class Posetive(Op):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2,Constatant.Posetive,)


class BitwiseOp(Op):
    def __init__(self, obj1=None, obj2=None, op=None, method=None, aug=None) -> None:
        super().__init__(obj1, obj2, op, method, aug)


class LShift(BitwiseOp):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2,Constatant.LShift,)


class RShift(BitwiseOp):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2,Constatant.RShift,)


class BitAnd(BitwiseOp):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2,Constatant.BitAnd,)


class BitOr(BitwiseOp):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2,Constatant.BitOr,)


class BitXor(BitwiseOp):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2,Constatant.BitXor,)


class BitInvert(BitwiseOp):
    def __init__(self, obj1=None) -> None:
        super().__init__(obj1, obj2=None ,op=Constatant.BitInvert,)

if __name__ == "__main__":
    print(Not(And(4, 2)))
