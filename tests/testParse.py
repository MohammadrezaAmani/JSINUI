import ast
import unittest
import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir)
from js.parser import *

# import
# dict
not True
# no return
# return
python_code = """
import os
name = 'hi'
12
a + 4
1 is 2 + 9 - 6
not True
def hello(a,b=2):
    print(hello)
    return 12, 9.9
a = '''
salam 
man

'''
class B(Base):
    pass

"""

parsed_code = ast.parse(python_code)
# print(ast.dump(parsed_code, indent=4))
converter = PythonToJavaScriptConverter()
js_code = converter.visit(parsed_code)

print(js_code)
