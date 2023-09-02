from typing import Any
from .core import *
import ast


class PythonToJavaScriptConverter(ast.NodeVisitor):
    def visit_Module(self, node):
        self.js_code = []
        for stmt in node.body:
            js_stmt = self.visit(stmt)
            if js_stmt is not None:
                self.js_code.append(str(js_stmt))
        return "\n".join(self.js_code)

    def visit_AsyncFunctionDef(self, node):
        defults = [self.visit(param) for param in node.args.defaults]
        js_params = [param.arg for param in node.args.args]
        kwarg = {}
        for i in range(len(defults)):
            kwarg[js_params[-i - 1]] = defults[-i - 1]
        js_params = js_params[: len(js_params) - len(defults)]
        js_code = []
        for stmt in node.body:
            js_stmt = self.visit(stmt)
            if js_stmt is not None:
                js_code.append(js_stmt)
        return AsyncDef(name=node.name, args=js_params, body=js_code, kwargs=kwarg)

    def visit_FunctionDef(self, node):
        defults = [self.visit(param) for param in node.args.defaults]
        js_params = [param.arg for param in node.args.args]
        kwarg = {}
        for i in range(len(defults)):
            kwarg[js_params[-i - 1]] = defults[-i - 1]
        js_params = js_params[: len(js_params) - len(defults)]
        js_code = []
        for stmt in node.body:
            js_stmt = self.visit(stmt)
            if js_stmt is not None:
                js_code.append(js_stmt)
        return Function(name=node.name, args=js_params, body=js_code, kwargs=kwarg)

    def visit_Return(self, node):
        return Return(self.visit(node.value))

    def visit_Await(self, node):
        value = self.visit(node.value)
        return Await(value)

    def visit_Assign(self, node: Assign):
        if isinstance(node.targets[0], ast.Name) and isinstance(
            node.targets[0].ctx, ast.Store
        ):
            target = self.visit(node.targets[0])
            value = self.visit(node.value) if node.value else ""
            return Let(target, value)
        elif isinstance(node.targets[0], ast.Attribute):
            target = self.visit(node.targets[0].value)
            if target == "self".strip():
                target = "this"
            target += "."
            attribute = node.targets[0].attr
            value = self.visit(node.value) if node.value else ""
            return Assign(target + attribute, value)
        else:
            # Handle other cases if needed
            return None

    def visit_Name(self, node):
        return node.id

    def visit_Constant(self, node: Constant) -> Any:
        if type(node.n) == bool:
            return Bool(node.n)
        if type(node.n) == int:
            return Int(node.n)
        if type(node.n) == str:
            return Str(node.n)
        if type(node.n) == float:
            return Float(node.n)
        if type(node.n) in [list, set, tuple]:
            return List(node.n)
        if type(node.n) == dict:
            return Dict(node.n)
        else:
            return str(node.n)

    def visit_Expr(self, node) -> Any:
        return self.visit(node.value)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            func = self.visit(node.func)
            if func == "print":
                func = "console.log"
        elif isinstance(node.func, ast.Attribute):
            attr = node.func.attr
            func = str(self.visit(node.func.value)) + "." + attr
        args = [self.visit(i) for i in node.args]
        kwargs = {}
        for i in node.keywords:
            kwargs[i.arg] = self.visit(i.value)
        return Call(func, args, kwargs)

    def visit_ClassDef(self, node):
        class_name = node.name
        bases = ", ".join([self.visit(base) for base in node.bases])
        js_code = []
        for stmt in node.body:
            js_stmt = self.visit(stmt)
            if js_stmt is not None:
                js_code.append(js_stmt)
        if bases:
            return Class(class_name, bases, js_code)
        else:
            return Class(class_name, body=js_code)

    def visit_Dict(self, node: Dict):
        items = []
        for i in range(len(node.keys)):
            key = self.visit(node.keys[i])
            value = self.visit(node.values[i])
            items.append(f"{key}: {value}")
        return Dict(items)

    def visit_Compare(self, node) -> Any:
        left = self.visit(node.left)
        right = self.visit(node.comparators[0])
        ops = {
            ast.Eq: Eq,
            ast.NotEq: NotEq,
            ast.Gt: GT,
            ast.GtE: GTE,
            ast.Lt: LT,
            ast.LtE: LTE,
            ast.Is: Is,
            ast.IsNot: IsNot,
        }
        return ops[type(node.ops[0])](left, right)

    def visit_For(self, node):
        target = self.visit(node.target)
        iterable = self.visit(node.iter)
        body = "\n".join([self.visit(stmt) for stmt in node.body])

        js_for_loop = f"for (let {target} of {iterable}) {{\n{body}\n}}"
        return js_for_loop

    def visit_While(self, node):
        test = self.visit(node.test)
        body = "\n".join([self.visit(stmt) for stmt in node.body])

        js_while_loop = f"while ({test}) {{\n{body}\n}}"
        return js_while_loop

    def visit_If(self, node):
        test = self.visit(node.test)
        body = "\n".join([self.visit(stmt) for stmt in node.body])
        js_if_statement = f"if ({test}) {{\n{body}\n}}"

        orelse = node.orelse
        if orelse:
            if isinstance(orelse[0], ast.If):
                js_if_statement += self.visit(orelse[0])  # Handle "elif"
            else:
                js_else_body = "\n".join([self.visit(stmt) for stmt in orelse])
                js_if_statement += f"else {{\n{js_else_body}\n}}"

        return js_if_statement

    def visit_AugAssign(self, node):
        target = self.visit(node.target)
        value = self.visit(node.value)
        operator = node.op

        if isinstance(operator, ast.Add):
            c = Add
        elif isinstance(operator, ast.Sub):
            c = Sub
        elif isinstance(operator, ast.Mult):
            c = Mult
        elif isinstance(operator, ast.Div):
            c = Div
        elif isinstance(operator, ast.FloorDiv):
            c = FloorDiv
        elif isinstance(operator, ast.Mod):
            c = Mod
        elif isinstance(operator, ast.Pow):
            c = Pow
        elif isinstance(operator, ast.LShift):
            c = LShift
        elif isinstance(operator, ast.RShift):
            c = RShift
        elif isinstance(operator, ast.BitAnd):
            c = BitAnd
        elif isinstance(operator, ast.BitOr):
            c = BitOr
        elif isinstance(operator, ast.BitXor):
            c = BitXor
        elif isinstance(operator, ast.And):
            c = And
        elif isinstance(operator, ast.Or):
            c = Or
        else:
            raise NotImplementedError(f"Unsupported AugAssign operator: {operator}")

        return c(target, value, Aug=True)

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        if isinstance(node.op, ast.Add):
            return Add(left, right)
        elif isinstance(node.op, ast.Sub):
            return Sub(left, right)
        elif isinstance(node.op, ast.Mult):
            return Mult(left, right)
        elif isinstance(node.op, ast.Div):
            return Div(left, right)
        elif isinstance(node.op, ast.FloorDiv):
            return FloorDiv(left, right)
        elif isinstance(node.op, ast.Mod):
            return Mod(left, right)
        elif isinstance(node.op, ast.Pow):
            return Pow(left, right)
        elif isinstance(node.op, ast.BitAnd):
            return BitAnd(left, right)
        elif isinstance(node.op, ast.BitOr):
            return BitOr(left, right)
        elif isinstance(node.op, ast.BitXor):
            return BitXor(left, right)
        elif isinstance(node.op, ast.LShift):
            return LShift(left, right)
        elif isinstance(node.op, ast.RShift):
            return RShift(left, right)
        elif isinstance(node.op, ast.And):
            return And(left, right)
        elif isinstance(node.op, ast.Or):
            return Or(left, right)
