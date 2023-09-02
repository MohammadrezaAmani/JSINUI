# JSinUI test results

Thid file contains results of last             last test of JSINUI module, we are trying to            fix them as soon as possible.

------

### Failures: 

``` python
test_bytes (__main__.TestPythonToJavaScriptConversion.test_bytes)
Traceback (most recent call last):
  File "/home/bug/dev/jsinui/tests/test.py", line 284, in test_bytes
    self.assertEqual(js_code, expected_js)
AssertionError: 'new Uint8Array(b"b\'Hello, World!\'")' != 'new Uint8Array([72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33])'
- new Uint8Array(b"b'Hello, World!'")
+ new Uint8Array([72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33])


```
------------
``` python
test_dict (__main__.TestPythonToJavaScriptConversion.test_dict)
Traceback (most recent call last):
  File "/home/bug/dev/jsinui/tests/test.py", line 327, in test_dict
    self.assertEqual(js_code, expected_js)
AssertionError: '{a: 1, b: 2, c: 3}' != '{"a": 1, "b": 2, "c": 3}'
- {a: 1, b: 2, c: 3}
+ {"a": 1, "b": 2, "c": 3}
?  + +     + +     + +


```
------------
``` python
test_string_format (__main__.TestPythonToJavaScriptConversion.test_string_format)
Traceback (most recent call last):
  File "/home/bug/dev/jsinui/tests/test.py", line 306, in test_string_format
    self.assertEqual(js_code, expected_js)
AssertionError: '`Hello, {}!`.format(world)' != '`Hello, ${"world"}!`.format(world)'
- `Hello, {}!`.format(world)
+ `Hello, ${"world"}!`.format(world)
?         + +++++++


```
------------
``` python
test_scope_with_children (__main__.TestScope.test_scope_with_children)
Traceback (most recent call last):
  File "/home/bug/dev/jsinui/tests/test.py", line 139, in test_scope_with_children
    self.assertEqual(scope.render(), expected_result)
AssertionError: '{\n\n  ["Child1"]\n  ["Child2"]\n}' != '{\n  Child1\n  Child2\n}'
  {
- 
-   ["Child1"]
?   --      --
+   Child1
-   ["Child2"]
?   --      --
+   Child2
  }

```
------------
``` python
test_scope_with_different_indent (__main__.TestScope.test_scope_with_different_indent)
Traceback (most recent call last):
  File "/home/bug/dev/jsinui/tests/test.py", line 146, in test_scope_with_different_indent
    self.assertEqual(scope.render(), expected_result)
AssertionError: '{\n\n    ["Child1"]\n    ["Child2"]\n}' != '{\n    Child1\n    Child2\n}'
  {
- 
-     ["Child1"]
?     --      --
+     Child1
-     ["Child2"]
?     --      --
+     Child2
  }

```
------------
``` python
test_scope_with_mixed_children (__main__.TestScope.test_scope_with_mixed_children)
Traceback (most recent call last):
  File "/home/bug/dev/jsinui/tests/test.py", line 167, in test_scope_with_mixed_children
    self.assertEqual(scope.render(), expected_result)
AssertionError: '{\n\n  ["Child1"]\n  ["Child2"]\n}' != '{\n  Child1\n  Child2\n}'
  {
- 
-   ["Child1"]
?   --      --
+   Child1
-   ["Child2"]
?   --      --
+   Child2
  }

```
------------
``` python
test_scope_with_set_children (__main__.TestScope.test_scope_with_set_children)
Traceback (most recent call last):
  File "/home/bug/dev/jsinui/tests/test.py", line 160, in test_scope_with_set_children
    self.assertEqual(scope.render(), expected_result)
AssertionError: '{\n\n    ["Child2"]\n    ["Child1"]\n}' != '{\n  Child1\n  Child2\n}'
  {
- 
-     ["Child2"]
-     ["Child1"]
?   ----      --
+   Child1
+   Child2
  }

```
------------
``` python
test_scope_with_tuple_children (__main__.TestScope.test_scope_with_tuple_children)
Traceback (most recent call last):
  File "/home/bug/dev/jsinui/tests/test.py", line 153, in test_scope_with_tuple_children
    self.assertEqual(scope.render(), expected_result)
AssertionError: '{\n\n    ["Child1"]\n    ["Child2"]\n}' != '{\n  Child1\n  Child2\n}'
  {
- 
-     ["Child1"]
?   ----      --
+   Child1
-     ["Child2"]
?   ----      --
+   Child2
  }

```
------------
``` python
test_zip_render (__main__.TestZip.test_zip_render)
Traceback (most recent call last):
  File "/home/bug/dev/jsinui/tests/test.py", line 354, in test_zip_render
    self.assertEqual(rendered_code, expected_code)
AssertionError: 'Array.from([List([1, 2, 3]), List(["a", "b", "c"]), T[62 chars]]`])' != 'Array.from([1, 2, 3, "a", "b", "c", [10, 20, 30]]).ma[28 chars]6]])'
- Array.from([List([1, 2, 3]), List(["a", "b", "c"]), Tuple([10, 20, 30])]).map((_,i)=>[`_[${i}]`, `_[${i}]`, `_[${i}]`])
?             ------       --  ------             --  ------            -               -  -- - -  -  -- ^ -  -  -- ^ -
+ Array.from([1, 2, 3, "a", "b", "c", [10, 20, 30]]).map((_,i)=>[_[i], _[i+3], _[i+6]])
?                                                                         ^^      ^^


```
------------
### Errors:

### ExpectedFailures: 

