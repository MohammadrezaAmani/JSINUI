# JSinUI test results

Thid file contains results of last             last test of JSINUI module, we are trying to            fix them as soon as possible.

------

### Failures: 

``` python
test_scope_with_children (__main__.TestScope.test_scope_with_children)
Traceback (most recent call last):
  File "/home/bug/dev/jsinui/tests/test.py", line 140, in test_scope_with_children
    self.assertEqual(scope.render(), expected_result)
AssertionError: "{\n\n  ('Child1',)\n  ('Child2',)\n}" != '{\n  Child1\n  Child2\n}'
  {
- 
-   ('Child1',)
?   --      ---
+   Child1
-   ('Child2',)
?   --      ---
+   Child2
  }

```
------------
``` python
test_scope_with_different_indent (__main__.TestScope.test_scope_with_different_indent)
Traceback (most recent call last):
  File "/home/bug/dev/jsinui/tests/test.py", line 147, in test_scope_with_different_indent
    self.assertEqual(scope.render(), expected_result)
AssertionError: "{\n\n    ('Child1',)\n    ('Child2',)\n}" != '{\n    Child1\n    Child2\n}'
  {
- 
-     ('Child1',)
?     --      ---
+     Child1
-     ('Child2',)
?     --      ---
+     Child2
  }

```
------------
``` python
test_scope_with_mixed_children (__main__.TestScope.test_scope_with_mixed_children)
Traceback (most recent call last):
  File "/home/bug/dev/jsinui/tests/test.py", line 168, in test_scope_with_mixed_children
    self.assertEqual(scope.render(), expected_result)
AssertionError: "{\n\n  ('Child1',)\n  ('Child2',)\n}" != '{\n  Child1\n  Child2\n}'
  {
- 
-   ('Child1',)
?   --      ---
+   Child1
-   ('Child2',)
?   --      ---
+   Child2
  }

```
------------
``` python
test_scope_with_set_children (__main__.TestScope.test_scope_with_set_children)
Traceback (most recent call last):
  File "/home/bug/dev/jsinui/tests/test.py", line 161, in test_scope_with_set_children
    self.assertEqual(scope.render(), expected_result)
AssertionError: "{\n\n    ('Child1',)\n    ('Child2',)\n}" != '{\n  Child1\n  Child2\n}'
  {
+   Child1
+   Child2
- 
-     ('Child1',)
-     ('Child2',)
  }

```
------------
``` python
test_scope_with_tuple_children (__main__.TestScope.test_scope_with_tuple_children)
Traceback (most recent call last):
  File "/home/bug/dev/jsinui/tests/test.py", line 154, in test_scope_with_tuple_children
    self.assertEqual(scope.render(), expected_result)
AssertionError: "{\n\n    ('Child1',)\n    ('Child2',)\n}" != '{\n  Child1\n  Child2\n}'
  {
+   Child1
+   Child2
- 
-     ('Child1',)
-     ('Child2',)
  }

```
------------
### Errors:

### ExpectedFailures: 

