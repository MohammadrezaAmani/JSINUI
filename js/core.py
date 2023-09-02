class Constant:
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
    Add = "+"
    Sub = "-"
    Mult = "*"
    Div = "/"
    FloorDiv = "Math.floor"
    Pow = "Math.pow"
    Mod = "%"
    BitAnd = "&"
    BitOr = "|"
    BitXor = "^"
    LShift = "<<"
    RShift = ">>"
    Negative = "-"
    Posetive = "+"
    BitInvert = "~"


class BuiltIn(object):
    def __init__(self, *args, **kwargs) -> None:
        self.args = args
        self.kwargs = kwargs

    @property
    def args(self):
        return self.__args

    @args.setter
    def args(self, obj):
        self.__args = convertType(obj)

    @property
    def kwargs(self):
        return self.__kwargs

    @kwargs.setter
    def kwargs(self, val: str):
        self.__kwargs = val

    def render(self):
        return self.renderClass()

    def renderClass(self):
        return str(self.args)

    def __str__(self) -> str:
        return self.render()

    def __repr__(self) -> str:
        return f"{str(self.__class__.__name__)}({self.__str__()})"


def convertType(obj):
    # Define the mapping of Python types to their corresponding JavaScript types
    convert = {
        str: Str,
        int: Int,
        float: Float,
        complex: Complex,
        list: List,  # Added List type
        tuple: Tuple,  # Added Tuple type
        range: Range,  # Added Range type
        bytes: Bytes,  # Added Bytes type
        bytearray: BytesArray,  # Added BytesArray type
        memoryview: MemoryView,  # Added MemoryView type
        set: Set,  # Added Set type
        frozenset: FrozenSet,  # Added FrozenSet type
        dict: Dict,  # Added Dict type
    }

    # Check if the type of obj is in the convert dictionary
    if type(obj) in convert:
        objtype = convert[type(obj)]
        return objtype(obj)

    # If the type is not in the dictionary, return the object as is
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
        super().__init__(obj1, obj2, Constant.And)


class Or(BoolOp):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(obj1, obj2, Constant.Or)


class Not(BoolOp):
    def __init__(self, obj1=None) -> None:
        super().__init__(obj1, op=Constant.Not)


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
    #! implement this class
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
    def op(self, val: str):
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
    def method(self, val: str):
        self.__method = val

    @property
    def aug(self):
        return self.__aug

    @aug.setter
    def aug(self, val: bool):
        self.__aug = val

    def renderClass(self):
        render_text = ""
        if self.obj2 == None:
            render_text = f"({self.op}{self.obj1})"
        elif self.aug:
            if self.method:
                render_text = f"{self.obj1} = {self.op}({self.obj1},{self.obj2})"
            else:
                render_text = f"{self.obj1} {self.op}= {self.obj2}"
        else:
            if self.method:
                render_text = f"{self.op}({self.obj1},{self.obj2})"
            else:
                render_text = f"({self.obj1} {self.op} {self.obj2})"

        return render_text


class Add(Op):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(
            obj1,
            obj2,
            Constant.Add,
        )


class Sub(Op):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(
            obj1,
            obj2,
            Constant.Sub,
        )


class Mult(Op):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(
            obj1,
            obj2,
            Constant.Mult,
        )


class Div(Op):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(
            obj1,
            obj2,
            Constant.Div,
        )


class FloorDiv(Op):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(
            obj1,
            obj2,
            Constant.FloorDiv,
        )


class Mod(Op):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(
            obj1,
            obj2,
            Constant.Mod,
        )


class Pow(Op):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(
            obj1,
            obj2,
            Constant.Pow,
        )


class Negative(Op):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(
            obj1,
            obj2,
            Constant.Negative,
        )


class Posetive(Op):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(
            obj1,
            obj2,
            Constant.Posetive,
        )


class BitwiseOp(Op):
    def __init__(self, obj1=None, obj2=None, op=None, method=None, aug=None) -> None:
        super().__init__(obj1, obj2, op, method, aug)


class LShift(BitwiseOp):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(
            obj1,
            obj2,
            Constant.LShift,
        )


class RShift(BitwiseOp):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(
            obj1,
            obj2,
            Constant.RShift,
        )


class BitAnd(BitwiseOp):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(
            obj1,
            obj2,
            Constant.BitAnd,
        )


class BitOr(BitwiseOp):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(
            obj1,
            obj2,
            Constant.BitOr,
        )


class BitXor(BitwiseOp):
    def __init__(self, obj1=None, obj2=None) -> None:
        super().__init__(
            obj1,
            obj2,
            Constant.BitXor,
        )


class BitInvert(BitwiseOp):
    def __init__(self, obj1=None) -> None:
        super().__init__(
            obj1,
            obj2=None,
            op=Constant.BitInvert,
        )


class Scope(BuiltIn):
    def __init__(self, childs=None, indent=4) -> None:
        self.childs = childs
        self.indent = int(indent)

    @property
    def childs(self):
        return self.__childs

    @childs.setter
    def childs(self, args):
        if args == None:
            args = ()

        elif type(args) not in [list, set, tuple]:
            args = tuple(args)
        self.__childs = args

    def renderClass(self):
        childs = ""
        for i in self.childs:
            childs += "\n" + (self.indent * " ") + str(convertType(i))
        return "{\n%s\n}" % (childs)


class Assign(BuiltIn):
    def __init__(self, variableName=None, value=None, assigntype="") -> None:
        self.variableName = variableName
        self.value = value
        self.assigntype = assigntype

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = convertType(val)

    @property
    def variableName(self):
        return self.__variableName

    @variableName.setter
    def variableName(self, name: str):
        name = str(name)
        name = name.strip()
        if len(name) == 0:
            raise BaseException("invalid name")
        self.__variableName = name

    def __str__(self) -> str:
        if self.value == None:
            return "%s %s;" % (self.assigntype, self.variableName)
        return "%s %s = %s;" % (self.assigntype, self.variableName, self.value)

    def __repr__(self):
        return self.__str__()


class Const(Assign):
    def __init__(self, variableName=None, value=None) -> None:
        super().__init__(variableName, value, "const")


class Let(Assign):
    def __init__(self, variableName=None, value=None):
        super().__init__(variableName, value, "let")


class Var(Assign):
    def __init__(self, variableName=None, value=None) -> None:
        super().__init__(variableName, value, "var")


class Iterator(Type):
    def __init__(self, iterable=None) -> None:
        self.iterable = iterable

    @property
    def iterable(self):
        return self.__iterable

    @iterable.setter
    def iterable(self, obj):
        self.__iterable = obj

    def renderClass(self):
        return f"{str(self.iterable)}[Symbol.iterator]()"


class Generator(Type):
    def __init__(self, func=None) -> None:
        self.func = func

    @property
    def func(self):
        return self.__func

    @func.setter
    def func(self, obj):
        self.__func = obj

    def renderClass(self):
        return f"function* () {{\n{str(self.func)}\n}}"


class Sequence(Iterator):
    def __init__(self, elements) -> None:
        super().__init__(True)
        self.elements = elements

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, obj):
        if obj == None:
            obj = []
        elements = []
        for i in list(obj):
            elements.append(convertType(i))
        self.__elements = elements


class List(Sequence):
    def __init__(self, elements) -> None:
        super().__init__(elements)

    def renderClass(self):
        elements = ", ".join(map(str, self.elements)) if self.elements else ""
        return f"[{elements}]"


class Tuple(Sequence):
    def __init__(self, elements=None) -> None:
        super().__init__(elements)

    def renderClass(self):
        elements = ", ".join(map(str, self.elements)) if self.elements else ""
        return f"[{elements}]"


class Range(Sequence):
    def __init__(self, start=None, stop=None, step=None) -> None:
        self.start = start
        self.stop = stop
        self.step = step

    def renderClass(self):
        start = self.start if self.start is not None else ""
        stop = self.stop if self.stop is not None else ""
        step = self.step if self.step is not None else ""
        return f"Array.from({start}, {stop}, {step})"


class ImmutableSequence(Type):
    def __init__(self, elements=None) -> None:
        self.elements = elements

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, obj):
        if obj is not None and not isinstance(obj, list):
            raise ValueError("ImmutableSequence elements must be a list")
        self.__elements = obj

    def renderClass(self):
        elements = ", ".join(map(str, self.elements)) if self.elements else ""
        return f"Object.freeze([{elements}])"


class BinarySequence(Type):
    def __init__(self, binary_str=None) -> None:
        self.binary_str = binary_str

    def renderClass(self):
        return f'parseInt("{self.binary_str}", 2)'


class Bytes(Type):
    def __init__(self, value=None) -> None:
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, obj):
        self.__value = obj

    def renderClass(self):
        return f"new Uint8Array({str(self.value).encode()})"


class BytesArray(Type):
    def __init__(self, elements=None) -> None:
        self.elements = elements

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, obj):
        if obj is not None and not isinstance(obj, list):
            raise ValueError("BytesArray elements must be a list")
        self.__elements = obj

    def renderClass(self):
        elements = ", ".join(map(str, self.elements)) if self.elements else ""
        return f"new Uint8Array([{elements}])"


class MemoryView(Type):
    def __init__(self, obj=None) -> None:
        self.obj = obj

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = obj

    def renderClass(self):
        return f"new DataView({str(self.obj)})"


class StringFormat:
    def __init__(self, format_string=None, args=None) -> None:
        self.format_string = format_string
        self.args = args

    @property
    def format_string(self):
        return self.__format_string

    @format_string.setter
    def format_string(self, value):
        if value is None or not isinstance(value, str):
            raise ValueError("Format string must be a valid string")
        self.__format_string = value

    @property
    def args(self):
        return self.__args

    @args.setter
    def args(self, value):
        if value is None or not isinstance(value, tuple):
            raise ValueError("Args must be a tuple")
        self.__args = value

    def renderClass(self):
        return f'`{self.format_string}`.format({", ".join(map(str, self.args))})'


class Set(Type):
    def __init__(self, elements=None) -> None:
        self.elements = elements

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, value):
        if value is not None and not isinstance(value, list):
            raise ValueError("Set elements must be a list")
        self.__elements = value

    def renderClass(self):
        elements = ", ".join(map(str, self.elements)) if self.elements else ""
        return f"new Set([{elements}])"


class FrozenSet(Set):
    def renderClass(self):
        elements = ", ".join(map(str, self.elements)) if self.elements else ""
        return f"new Set([{elements}])"


class Dict(Type):
    def __init__(self, key_value_pairs=None) -> None:
        self.key_value_pairs = key_value_pairs

    @property
    def key_value_pairs(self):
        return self.__key_value_pairs

    @key_value_pairs.setter
    def key_value_pairs(self, value):
        if value is not None and not isinstance(value, dict):
            raise ValueError("Dict key-value pairs must be a dictionary")
        self.__key_value_pairs = value

    def renderClass(self):
        pairs = (
            ", ".join(
                [f"{key}: {value}" for key, value in self.key_value_pairs.items()]
            )
            if self.key_value_pairs
            else ""
        )
        return f"{{{pairs}}}"


class UnionType(Type):
    def __init__(self, types=None) -> None:
        self.types = types

    @property
    def types(self):
        return self.__types

    @types.setter
    def types(self, value):
        if value is not None and not isinstance(value, list):
            raise ValueError("UnionType types must be a list")
        self.__types = value

    def renderClass(self):
        types = " | ".join(map(str, self.types)) if self.types else ""
        return types


class BuiltInFunc(BuiltIn):
    pass


class Abs(BuiltInFunc):
    def __init__(self, value=None) -> None:
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, obj):
        self.__value = convertType(obj)

    def renderClass(self):
        return f"Math.abs({str(self.value)})"


class Aiter(BuiltInFunc):
    def __init__(self, iterable=None) -> None:
        self.iterable = iterable

    @property
    def iterable(self):
        return self.__iterable

    @iterable.setter
    def iterable(self, obj):
        self.__iterable = convertType(obj)

    def renderClass(self):
        return f"{str(self.iterable)}[Symbol.asyncIterator]()"


class All(BuiltInFunc):
    def __init__(self, iterable=None) -> None:
        self.iterable = iterable

    @property
    def iterable(self):
        return self.__iterable

    @iterable.setter
    def iterable(self, obj):
        self.__iterable = convertType(obj)

    def renderClass(self):
        return f"Array.from({str(self.iterable)}).every(Boolean)"


class Anext(BuiltInFunc):
    def __init__(self, async_iterator=None) -> None:
        self.async_iterator = async_iterator

    @property
    def async_iterator(self):
        return self.__async_iterator

    @async_iterator.setter
    def async_iterator(self, obj):
        self.__async_iterator = convertType(obj)

    def renderClass(self):
        return f"{str(self.async_iterator)}.next()"


class Any(BuiltInFunc):
    def __init__(self, iterable=None) -> None:
        self.iterable = iterable

    @property
    def iterable(self):
        return self.__iterable

    @iterable.setter
    def iterable(self, obj):
        self.__iterable = convertType(obj)

    def renderClass(self):
        return f"Array.from({str(self.iterable)}).some(Boolean)"


class Ascii(BuiltInFunc):
    def __init__(self, obj=None) -> None:
        self.obj = obj

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = convertType(obj)

    def renderClass(self):
        return f"{str(self.obj)}.charCodeAt(0)"


class Bin(BuiltInFunc):
    def __init__(self, obj=None) -> None:
        self.obj = obj

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = convertType(obj)

    def renderClass(self):
        return f"(parseInt({str(self.obj)}, 10)).toString(2)"


class BreackPoint(BuiltInFunc):
    def __init__(self) -> None:
        pass

    def renderClass(self):
        return "debugger"


class Callable(BuiltInFunc):
    def __init__(self, obj=None) -> None:
        self.obj = obj

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = convertType(obj)

    def renderClass(self):
        return f'typeof {str(self.obj)} === "function"'


class Chr(BuiltInFunc):
    def __init__(self, ascii_value=None) -> None:
        self.ascii_value = ascii_value

    @property
    def ascii_value(self):
        return self.__ascii_value

    @ascii_value.setter
    def ascii_value(self, obj):
        self.__ascii_value = convertType(obj)

    def renderClass(self):
        return f"String.fromCharCode({str(self.ascii_value)})"


class ClassMethod(BuiltInFunc):
    def __init__(self, method=None) -> None:
        self.method = method

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, obj):
        self.__method = convertType(obj)

    def renderClass(self):
        return f"{str(self.method)}.bind({str(self.method.__class__)})"


class Compile(BuiltInFunc):
    def __init__(self, source_code=None, filename=None, mode=None) -> None:
        self.source_code = source_code
        self.filename = filename
        self.mode = mode

    @property
    def source_code(self):
        return self.__source_code

    @source_code.setter
    def source_code(self, obj):
        self.__source_code = convertType(obj)

    @property
    def filename(self):
        return self.__filename

    @filename.setter
    def filename(self, obj):
        self.__filename = convertType(obj)

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, obj):
        self.__mode = convertType(obj)

    def renderClass(self):
        return f'new Function("{str(self.source_code)}")'


class DelAttr(BuiltInFunc):
    def __init__(self, obj=None, attr_name=None) -> None:
        self.obj = obj
        self.attr_name = attr_name

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = convertType(obj)

    @property
    def attr_name(self):
        return self.__attr_name

    @attr_name.setter
    def attr_name(self, obj):
        self.__attr_name = convertType(obj)

    def renderClass(self):
        return f"delete {str(self.obj)}.{str(self.attr_name)}"


class Dir(BuiltInFunc):
    def __init__(self, obj=None) -> None:
        self.obj = obj

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = convertType(obj)

    def renderClass(self):
        return f"Object.keys({str(self.obj)})"


class DivMod(BuiltInFunc):
    def __init__(self, x=None, y=None) -> None:
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, obj):
        self.__x = convertType(obj)

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, obj):
        self.__y = convertType(obj)

    def renderClass(self):
        return f"[{str(self.x)} / {str(self.y)}, {str(self.x)} % {str(self.y)}]"


class Enumerate(BuiltInFunc):
    def __init__(self, iterable=None, start=None) -> None:
        self.iterable = iterable
        self.start = start

    @property
    def iterable(self):
        return self.__iterable

    @iterable.setter
    def iterable(self, obj):
        self.__iterable = convertType(obj)

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, obj):
        self.__start = convertType(obj)

    def renderClass(self):
        if self.start is not None:
            return f"Array.from({str(self.iterable)}).map((value, index) => [{str(self.start)} + index, value])"
        return f"Array.from({str(self.iterable)}).map((value, index) => [index, value])"


class Eval(BuiltInFunc):
    def __init__(self, code_string=None, global_vars=None, local_vars=None) -> None:
        self.code_string = code_string
        self.global_vars = global_vars
        self.local_vars = local_vars

    @property
    def code_string(self):
        return self.__code_string

    @code_string.setter
    def code_string(self, obj):
        self.__code_string = convertType(obj)

    @property
    def global_vars(self):
        return self.__global_vars

    @global_vars.setter
    def global_vars(self, obj):
        if obj is not None and not isinstance(obj, dict):
            raise ValueError("Global variables must be a dictionary")
        self.__global_vars = obj

    @property
    def local_vars(self):
        return self.__local_vars

    @local_vars.setter
    def local_vars(self, obj):
        if obj is not None and not isinstance(obj, dict):
            raise ValueError("Local variables must be a dictionary")
        self.__local_vars = obj

    def renderClass(self):
        if self.global_vars is not None and self.local_vars is not None:
            return f"eval({str(self.code_string)}, {str(self.global_vars)}, {str(self.local_vars)})"
        if self.global_vars is not None:
            return f"eval({str(self.code_string)}, {str(self.global_vars)})"
        if self.local_vars is not None:
            return f"eval({str(self.code_string)}, undefined, {str(self.local_vars)})"
        return f"eval({str(self.code_string)})"


class Exec(BuiltInFunc):
    def __init__(self, code_string=None, global_vars=None, local_vars=None) -> None:
        self.code_string = code_string
        self.global_vars = global_vars
        self.local_vars = local_vars

    @property
    def code_string(self):
        return self.__code_string

    @code_string.setter
    def code_string(self, obj):
        self.__code_string = convertType(obj)

    @property
    def global_vars(self):
        return self.__global_vars

    @global_vars.setter
    def global_vars(self, obj):
        if obj is not None and not isinstance(obj, dict):
            raise ValueError("Global variables must be a dictionary")
        self.__global_vars = obj

    @property
    def local_vars(self):
        return self.__local_vars

    @local_vars.setter
    def local_vars(self, obj):
        if obj is not None and not isinstance(obj, dict):
            raise ValueError("Local variables must be a dictionary")
        self.__local_vars = obj

    def renderClass(self):
        if self.global_vars is not None and self.local_vars is not None:
            return f"eval({str(self.code_string)}, {str(self.global_vars)}, {str(self.local_vars)})"
        if self.global_vars is not None:
            return f"eval({str(self.code_string)}, {str(self.global_vars)})"
        if self.local_vars is not None:
            return f"eval({str(self.code_string)}, undefined, {str(self.local_vars)})"
        return f"eval({str(self.code_string)})"


class Filter(BuiltInFunc):
    def __init__(self, function=None, iterable=None) -> None:
        self.function = function
        self.iterable = iterable

    @property
    def function(self):
        return self.__function

    @function.setter
    def function(self, obj):
        self.__function = convertType(obj)

    @property
    def iterable(self):
        return self.__iterable

    @iterable.setter
    def iterable(self, obj):
        self.__iterable = convertType(obj)

    def renderClass(self):
        return f"{str(self.iterable)}.filter({str(self.function)})"


class Format(BuiltInFunc):
    def __init__(self, value=None, format_spec=None) -> None:
        self.value = value
        self.format_spec = format_spec

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, obj):
        self.__value = convertType(obj)

    @property
    def format_spec(self):
        return self.__format_spec

    @format_spec.setter
    def format_spec(self, obj):
        self.__format_spec = convertType(obj)

    def renderClass(self):
        if self.format_spec is not None:
            return f"({str(self.value)}).toLocaleString(undefined, {str(self.format_spec)})"
        return f"({str(self.value)}).toLocaleString()"


class GetAttr(BuiltInFunc):
    def __init__(self, obj=None, attr_name=None, default=None) -> None:
        self.obj = obj
        self.attr_name = attr_name
        self.default = default

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = convertType(obj)

    @property
    def attr_name(self):
        return self.__attr_name

    @attr_name.setter
    def attr_name(self, obj):
        self.__attr_name = convertType(obj)

    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, obj):
        self.__default = convertType(obj)

    def renderClass(self):
        if self.default is not None:
            return f"{str(self.obj)}?.{str(self.attr_name)} ?? {str(self.default)}"
        return f"{str(self.obj)}?.{str(self.attr_name)}"


class Globals(BuiltInFunc):
    def __init__(self) -> None:
        pass

    def renderClass(self):
        return "this"


class HasAttr(BuiltInFunc):
    def __init__(self, obj=None, attr_name=None) -> None:
        self.obj = obj
        self.attr_name = attr_name

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = convertType(obj)

    @property
    def attr_name(self):
        return self.__attr_name

    @attr_name.setter
    def attr_name(self, obj):
        self.__attr_name = convertType(obj)

    def renderClass(self):
        return f"{str(self.attr_name)} in {str(self.obj)}"


class Hash(BuiltInFunc):
    def __init__(self, obj=None) -> None:
        self.obj = obj

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = convertType(obj)

    def renderClass(self):
        return f"{str(self.obj)}.hashCode()"


class Help(BuiltInFunc):
    def __init__(self, obj=None) -> None:
        self.obj = obj

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = convertType(obj)

    def renderClass(self):
        return f"help({str(self.obj)})"


class Hex(BuiltInFunc):
    def __init__(self, obj=None) -> None:
        self.obj = obj

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = convertType(obj)

    def renderClass(self):
        return f"({str(self.obj)}).toString(16)"


class Id(BuiltInFunc):
    def __init__(self, obj=None) -> None:
        self.obj = obj

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = convertType(obj)

    def renderClass(self):
        return f"{str(self.obj)}"


class Input(BuiltInFunc):
    def __init__(self, prompt=None) -> None:
        self.prompt = prompt

    @property
    def prompt(self):
        return self.__prompt

    @prompt.setter
    def prompt(self, obj):
        self.__prompt = convertType(obj)

    def renderClass(self):
        return f"prompt({str(self.prompt)})"


class IsInstance(BuiltInFunc):
    def __init__(self, obj=None, classinfo=None) -> None:
        self.obj = obj
        self.classinfo = classinfo

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = convertType(obj)

    @property
    def classinfo(self):
        return self.__classinfo

    @classinfo.setter
    def classinfo(self, obj):
        self.__classinfo = convertType(obj)

    def renderClass(self):
        return f"isInstance({str(self.obj)}, {str(self.classinfo)})"


class IsSubclass(BuiltInFunc):
    def __init__(self, cls=None, classinfo=None) -> None:
        self.cls = cls
        self.classinfo = classinfo

    @property
    def cls(self):
        return self.__cls

    @cls.setter
    def cls(self, obj):
        self.__cls = convertType(obj)

    @property
    def classinfo(self):
        return self.__classinfo

    @classinfo.setter
    def classinfo(self, obj):
        self.__classinfo = convertType(obj)

    def renderClass(self):
        return f"isSubclass({str(self.cls)}, {str(self.classinfo)})"


class Iter(BuiltInFunc):
    def __init__(self, iterable=None) -> None:
        self.iterable = iterable

    @property
    def iterable(self):
        return self.__iterable

    @iterable.setter
    def iterable(self, obj):
        self.__iterable = convertType(obj)

    def renderClass(self):
        return f"{str(self.iterable)}[Symbol.iterator]()"


class Len(BuiltInFunc):
    def __init__(self, obj=None) -> None:
        self.obj = obj

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = convertType(obj)

    def renderClass(self):
        return f"{str(self.obj)}.length"


class Locals(BuiltInFunc):
    def __init__(self) -> None:
        pass

    def renderClass(self):
        return "this"


class Map(BuiltInFunc):
    def __init__(self, function=None, iterable=None) -> None:
        self.function = function
        self.iterable = iterable

    @property
    def function(self):
        return self.__function

    @function.setter
    def function(self, obj):
        self.__function = convertType(obj)

    @property
    def iterable(self):
        return self.__iterable

    @iterable.setter
    def iterable(self, obj):
        self.__iterable = convertType(obj)

    def renderClass(self):
        return f"Array.from({str(self.iterable)}).map({str(self.function)})"


class Max(BuiltInFunc):
    def __init__(self, iterable=None, *args) -> None:
        self.iterable = iterable
        self.args = args

    @property
    def iterable(self):
        return self.__iterable

    @iterable.setter
    def iterable(self, obj):
        self.__iterable = convertType(obj)

    @property
    def args(self):
        return self.__args

    @args.setter
    def args(self, args):
        self.__args = [convertType(arg) for arg in args]

    def renderClass(self):
        if self.args:
            return f'Math.max.apply(null, [0, ...{str(self.iterable)}, {", ".join(map(str, self.args))}])'
        return f"Math.max.apply(null, [0, ...{str(self.iterable)}])"


class Min(BuiltInFunc):
    def __init__(self, iterable=None, *args) -> None:
        self.iterable = iterable
        self.args = args

    @property
    def iterable(self):
        return self.__iterable

    @iterable.setter
    def iterable(self, obj):
        self.__iterable = convertType(obj)

    @property
    def args(self):
        return self.__args

    @args.setter
    def args(self, args):
        self.__args = [convertType(arg) for arg in args]

    def renderClass(self):
        if self.args:
            return f'Math.min.apply(null, [0, ...{str(self.iterable)}, {", ".join(map(str, self.args))}])'
        return f"Math.min.apply(null, [0, ...{str(self.iterable)}])"


class Next(BuiltInFunc):
    def __init__(self, iterator=None, default=None) -> None:
        self.iterator = iterator
        self.default = default

    @property
    def iterator(self):
        return self.__iterator

    @iterator.setter
    def iterator(self, obj):
        self.__iterator = convertType(obj)

    @property
    def default(self):
        return self.__default

    @default.setter
    def default(self, obj):
        self.__default = convertType(obj)

    def renderClass(self):
        if self.default is not None:
            return f"{str(self.iterator)}.next()?.value ?? {str(self.default)}"
        return f"{str(self.iterator)}.next()?.value"


class Object(BuiltInFunc):
    def __init__(self, value=None) -> None:
        self.value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, obj):
        self.__value = convertType(obj)

    def renderClass(self):
        return f"new Object({str(self.value)})"


class Oct(BuiltInFunc):
    def __init__(self, obj=None) -> None:
        self.obj = obj

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = convertType(obj)

    def renderClass(self):
        return f"({str(self.obj)}).toString(8)"


class Open(BuiltInFunc):
    def __init__(
        self,
        file=None,
        mode=None,
        buffering=None,
        encoding=None,
        errors=None,
        newline=None,
        closefd=None,
        opener=None,
    ) -> None:
        self.file = file
        self.mode = mode
        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, obj):
        self.__file = convertType(obj)

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, obj):
        self.__mode = convertType(obj)

    @property
    def buffering(self):
        return self.__buffering

    @buffering.setter
    def buffering(self, obj):
        self.__buffering = convertType(obj)

    @property
    def encoding(self):
        return self.__encoding

    @encoding.setter
    def encoding(self, obj):
        self.__encoding = convertType(obj)

    @property
    def errors(self):
        return self.__errors

    @errors.setter
    def errors(self, obj):
        self.__errors = convertType(obj)

    @property
    def newline(self):
        return self.__newline

    @newline.setter
    def newline(self, obj):
        self.__newline = convertType(obj)

    @property
    def closefd(self):
        return self.__closefd

    @closefd.setter
    def closefd(self, obj):
        self.__closefd = convertType(obj)

    @property
    def opener(self):
        return self.__opener

    @opener.setter
    def opener(self, obj):
        self.__opener = convertType(obj)

    def renderClass(self):
        args = [str(self.file)]
        if self.mode is not None:
            args.append(str(self.mode))
        if self.buffering is not None:
            args.append(str(self.buffering))
        if self.encoding is not None:
            args.append(f"encoding={str(self.encoding)}")
        if self.errors is not None:
            args.append(f"errors={str(self.errors)}")
        if self.newline is not None:
            args.append(f"newline={str(self.newline)}")
        if self.closefd is not None:
            args.append(f"closefd={str(self.closefd)}")
        if self.opener is not None:
            args.append(f"opener={str(self.opener)}")
        return f'open({", ".join(args)})'


class Ord(BuiltInFunc):
    def __init__(self, char=None) -> None:
        self.char = char

    @property
    def char(self):
        return self.__char

    @char.setter
    def char(self, obj):
        self.__char = convertType(obj)

    def renderClass(self):
        return f"({str(self.char)}).charCodeAt(0)"


class Print(BuiltInFunc):
    def __init__(self, *objects, sep=None, end=None, file=None, flush=None) -> None:
        self.objects = objects
        self.sep = sep
        self.end = end
        self.file = file
        self.flush = flush

    @property
    def objects(self):
        return self.__objects

    @objects.setter
    def objects(self, objs):
        self.__objects = [convertType(obj) for obj in objs]

    @property
    def sep(self):
        return self.__sep

    @sep.setter
    def sep(self, obj):
        self.__sep = convertType(obj)

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, obj):
        self.__end = convertType(obj)

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, obj):
        self.__file = convertType(obj)

    @property
    def flush(self):
        return self.__flush

    @flush.setter
    def flush(self, obj):
        self.__flush = convertType(obj)

    def renderClass(self):
        args = [f"{str(obj)}" for obj in self.objects]
        if self.sep is not None:
            args.append(f"sep={str(self.sep)}")
        if self.end is not None:
            args.append(f"end={str(self.end)}")
        if self.file is not None:
            args.append(f"file={str(self.file)}")
        if self.flush is not None:
            args.append(f"flush={str(self.flush)}")
        return f'console.log({", ".join(args)})'


class Property(BuiltInFunc):
    def __init__(self, fget=None, fset=None, fdel=None, doc=None) -> None:
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.doc = doc

    @property
    def fget(self):
        return self.__fget

    @fget.setter
    def fget(self, obj):
        self.__fget = convertType(obj)

    @property
    def fset(self):
        return self.__fset

    @fset.setter
    def fset(self, obj):
        self.__fset = convertType(obj)

    @property
    def fdel(self):
        return self.__fdel

    @fdel.setter
    def fdel(self, obj):
        self.__fdel = convertType(obj)

    @property
    def doc(self):
        return self.__doc

    @doc.setter
    def doc(self, obj):
        self.__doc = convertType(obj)

    def renderClass(self):
        args = []
        if self.fget is not None:
            args.append(f"fget={str(self.fget)}")
        if self.fset is not None:
            args.append(f"fset={str(self.fset)}")
        if self.fdel is not None:
            args.append(f"fdel={str(self.fdel)}")
        if self.doc is not None:
            args.append(f"doc={str(self.doc)}")
        return f'property({", ".join(args)})'


class Repr(BuiltInFunc):
    def __init__(self, obj=None) -> None:
        self.obj = obj

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = convertType(obj)

    def renderClass(self):
        return f"`${{str(self.obj)}}`"


class Reversed(BuiltInFunc):
    def __init__(self, iterable=None) -> None:
        self.iterable = iterable

    @property
    def iterable(self):
        return self.__iterable

    @iterable.setter
    def iterable(self, obj):
        self.__iterable = convertType(obj)

    def renderClass(self):
        return f"Array.from({str(self.iterable)}).reverse()"


class Round(BuiltInFunc):
    def __init__(self, number=None, ndigits=None) -> None:
        self.number = number
        self.ndigits = ndigits

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, obj):
        self.__number = convertType(obj)

    @property
    def ndigits(self):
        return self.__ndigits

    @ndigits.setter
    def ndigits(self, obj):
        self.__ndigits = convertType(obj)

    def renderClass(self):
        if self.ndigits is not None:
            return f"Math.round({str(self.number)} * 10**{str(self.ndigits)}) / 10**{str(self.ndigits)}"
        return f"Math.round({str(self.number)})"


class SetAttr(BuiltInFunc):
    def __init__(self, obj=None, attr_name=None, value=None) -> None:
        self.obj = obj
        self.attr_name = attr_name
        self.value = value

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = convertType(obj)

    @property
    def attr_name(self):
        return self.__attr_name

    @attr_name.setter
    def attr_name(self, obj):
        self.__attr_name = convertType(obj)

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, obj):
        self.__value = convertType(obj)

    def renderClass(self):
        return f"{str(self.obj)}.{str(self.attr_name)} = {str(self.value)}"


class Slice(BuiltInFunc):
    def __init__(self, iterable=None, start=None, stop=None, step=None) -> None:
        self.iterable = iterable
        self.start = start
        self.stop = stop
        self.step = step

    @property
    def iterable(self):
        return self.__iterable

    @iterable.setter
    def iterable(self, obj):
        self.__iterable = convertType(obj)

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, obj):
        self.__start = convertType(obj)

    @property
    def stop(self):
        return self.__stop

    @stop.setter
    def stop(self, obj):
        self.__stop = convertType(obj)

    @property
    def step(self):
        return self.__step

    @step.setter
    def step(self, obj):
        self.__step = convertType(obj)

    def renderClass(self):
        args = [str(self.iterable)]
        if self.start is not None:
            args.append(str(self.start))
        if self.stop is not None:
            args.append(str(self.stop))
        if self.step is not None:
            args.append(str(self.step))
        return f'{args[0]}.slice({", ".join(args[1:])})'


class Sorted(BuiltInFunc):
    def __init__(self, iterable=None, key=None, reverse=None) -> None:
        self.iterable = iterable
        self.key = key
        self.reverse = reverse

    @property
    def iterable(self):
        return self.__iterable

    @iterable.setter
    def iterable(self, obj):
        self.__iterable = convertType(obj)

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, obj):
        self.__key = convertType(obj)

    @property
    def reverse(self):
        return self.__reverse

    @reverse.setter
    def reverse(self, obj):
        self.__reverse = convertType(obj)

    def renderClass(self):
        args = [str(self.iterable)]
        if self.key is not None:
            args.append(f"key={str(self.key)}")
        if self.reverse is not None:
            args.append(f"reverse={str(self.reverse)}")
        return f'{str(self.iterable)}.sort({", ".join(args)})'


class StaticMethod(BuiltInFunc):
    def __init__(self, method=None) -> None:
        self.method = method

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, obj):
        self.__method = convertType(obj)

    def renderClass(self):
        return f"StaticMethod({str(self.method)})"


class Sum(BuiltInFunc):
    def __init__(self, iterable=None, start=None) -> None:
        self.iterable = iterable
        self.start = start

    @property
    def iterable(self):
        return self.__iterable

    @iterable.setter
    def iterable(self, obj):
        self.__iterable = convertType(obj)

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, obj):
        self.__start = convertType(obj)

    def renderClass(self):
        if self.start is not None:
            return (
                f"{str(self.start)} + {str(self.iterable)}.reduce((a, b) => a + b, 0)"
            )
        return f"{str(self.iterable)}.reduce((a, b) => a + b, 0)"


class Supper(BuiltInFunc):
    def __init__(self) -> None:
        pass

    def renderClass(self):
        return "super()"


class Vars(BuiltInFunc):
    def __init__(self, obj=None) -> None:
        self.obj = obj

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = convertType(obj)

    def renderClass(self):
        return f"Object.keys({str(self.obj)})"


class Zip(BuiltInFunc):
    def __init__(self, *iterables) -> None:
        self.iterables = iterables

    @property
    def iterables(self):
        return self.__iterables

    @iterables.setter
    def iterables(self, objs):
        self.__iterables = [convertType(obj) for obj in objs]

    def renderClass(self):
        return f'Array.from({str(self.iterables)}).map((_,i)=>[{", ".join(["`_[${i}]`" for i in range(len(self.iterables))])}])'


class Import(BuiltInFunc):
    def __init__(self, name=None) -> None:
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, obj):
        self.__name = convertType(obj)

    def renderClass(self):
        return f"import {str(self.name)}"


class Quit(BuiltInFunc):
    def __init__(self, code=None) -> None:
        self.code = code

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, obj):
        self.__code = convertType(obj)

    def renderClass(self):
        return f"quit({str(self.code)})"


class Exit(BuiltInFunc):
    def __init__(self, code=None) -> None:
        self.code = code

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, obj):
        self.__code = convertType(obj)

    def renderClass(self):
        return f"exit({str(self.code)})"


class Try(BuiltIn):
    def __init__(self, body=None, except_blocks=None, final_block=None):
        self.body = body
        self.except_blocks = except_blocks
        self.final_block = final_block

    def renderClass(self):
        body_code = str(self.body) if self.body else ""
        except_blocks_code = (
            "\n".join(str(block) for block in self.except_blocks)
            if self.except_blocks
            else ""
        )
        final_block_code = str(self.final_block) if self.final_block else ""
        return f"try {{\n{body_code}\n}}{except_blocks_code}\n{final_block_code}"


class Except(BuiltIn):
    def __init__(self, exception=None, as_variable=None, body=None):
        self.exception = exception
        self.as_variable = as_variable
        self.body = body

    def renderClass(self):
        exception_code = f" {self.as_variable}" if self.as_variable else ""
        body_code = str(self.body) if self.body else ""
        return f"catch ({str(self.exception)}{exception_code}) {{\n{body_code}\n}}"


class Finally(BuiltIn):
    def __init__(self, body=None):
        self.body = body

    def renderClass(self):
        body_code = str(self.body) if self.body else ""
        return f"finally {{\n{body_code}\n}}"


class With(BuiltIn):
    def __init__(self, context_manager=None, as_variable=None, body=None):
        self.context_manager = context_manager
        self.as_variable = as_variable
        self.body = body

    def renderClass(self):
        as_variable_code = f" {self.as_variable}" if self.as_variable else ""
        body_code = str(self.body) if self.body else ""
        return (
            f"with ({str(self.context_manager)}{as_variable_code}) {{\n{body_code}\n}}"
        )


class As(BuiltIn):
    def __init__(self, obj=None, variable=None):
        self.obj = obj
        self.variable = variable

    def renderClass(self):
        return f"{str(self.obj)} as {str(self.variable)}"


class Async(BuiltIn):
    def __init__(self, body=None):
        self.body = body

    def renderClass(self):
        body_code = str(self.body) if self.body else ""
        return f"async {{\n{body_code}\n}}"


class Await(BuiltIn):
    def __init__(self, obj=None):
        self.obj = obj

    def renderClass(self):
        return f"await {str(self.obj)}"


class AsyncDef(Async):
    def __init__(self, name=None, args=None, body=None):
        self.name = name
        self.args = args
        self.body = body

    def renderClass(self):
        name_code = f" {str(self.name)}" if self.name else ""
        args_code = f'({", ".join(str(arg) for arg in self.args)})' if self.args else ""
        body_code = str(self.body) if self.body else ""
        return f"async function{name_code}{args_code} {{\n{body_code}\n}}"


class AsyncFor(Async):
    def __init__(self, variable=None, iterable=None, body=None):
        self.variable = variable
        self.iterable = iterable
        self.body = body

    def renderClass(self):
        variable_code = str(self.variable) if self.variable else ""
        iterable_code = str(self.iterable) if self.iterable else ""
        body_code = str(self.body) if self.body else ""
        return f"for ({variable_code} of {iterable_code}) {{\n{body_code}\n}}"


class Assert(BuiltIn):
    def __init__(self, condition=None, message=None):
        self.condition = condition
        self.message = message

    def renderClass(self):
        condition_code = str(self.condition) if self.condition else ""
        message_code = f", {str(self.message)}" if self.message else ""
        return f"assert({condition_code}{message_code});"


class Error(BuiltIn):
    def __init__(self, message=None):
        self.message = message

    def renderClass(self):
        message_code = f"{str(self.message)}" if self.message else ""
        return f"Error({message_code});"


class Raise(Error):
    def renderClass(self):
        return f"throw {super().renderClass()}"


class Exception(Error):
    def renderClass(self):
        return f"throw {super().renderClass()}"


class Module(BuiltIn):
    def __init__(self, name=None, body=None):
        self.name = name
        self.body = body

    def renderClass(self):
        name_code = f"{str(self.name)}" if self.name else ""
        body_code = str(self.body) if self.body else ""
        return f"module {name_code} {{\n{body_code}\n}}"


class Class(BuiltIn):
    def __init__(self, name=None, bases=None, body=None):
        self.name = name
        self.bases = bases
        self.body = body

    def renderClass(self):
        name_code = f"{str(self.name)}" if self.name else ""
        bases_code = (
            f'({", ".join(str(base) for base in self.bases)})' if self.bases else ""
        )
        body_code = str(self.body) if self.body else ""
        return f"class {name_code}{bases_code} {{\n{body_code}\n}}"


class ClassInstance(Class):
    def renderClass(self):
        return f"new {super().renderClass()}"


class Function(BuiltIn):
    def __init__(self, name=None, args=None, body=None):
        self.name = name
        self.args = args
        self.body = body

    def renderClass(self):
        name_code = f"{str(self.name)}" if self.name else ""
        args_code = f'({", ".join(str(arg) for arg in self.args)})' if self.args else ""
        body_code = str(self.body) if self.body else ""
        return f"function {name_code}{args_code} {{\n{body_code}\n}}"


class Method(BuiltIn):
    def __init__(self, name=None, args=None, body=None):
        self.name = name
        self.args = args
        self.body = body

    def renderClass(self):
        name_code = f"{str(self.name)}" if self.name else ""
        args_code = f'({", ".join(str(arg) for arg in self.args)})' if self.args else ""
        body_code = str(self.body) if self.body else ""
        return f"{name_code}{args_code} {{\n{body_code}\n}}"


class Code(BuiltIn):
    def __init__(self, code=None):
        self.code = code

    def renderClass(self):
        return str(self.code)


class TypeOf(BuiltIn):
    def __init__(self, obj=None):
        self.obj = obj

    def renderClass(self):
        return f"typeof {str(self.obj)}"


class Null(BuiltIn):
    def renderClass(self):
        return "null"


class Ellipsis(BuiltIn):
    def renderClass(self):
        return "..."


class NotImplemented(BuiltIn):
    def renderClass(self):
        return "NotImplemented"


class Bool(Type):
    def __init__(self, value=False):
        self.value = value

    def renderClass(self):
        return "true" if self.value else "false"
