# JSinUI test results

Thid file contains results of last             last test of JSINUI module, we are trying to            fix them as soon as possible.

------

### Failures: 

``` python
test_And_constant (__main__.TestJs.test_And_constant)
Traceback (most recent call last):
  File "/home/bug/dev/jsinui/tests/test.py", line 20, in test_And_constant
    self.assertEqual(
AssertionError: '(me && you)' != '"me" && "you"'
- (me && you)
? ^         ^
+ "me" && "you"
? ^  +    +   ^
 : Should be: "me" && "you"

```
------------
``` python
test_And_variable (__main__.TestJs.test_And_variable)
Traceback (most recent call last):
  File "/home/bug/dev/jsinui/tests/test.py", line 27, in test_And_variable
    self.assertEqual(
AssertionError: '(me && you)' != '("me" && "you")'
- (me && you)
+ ("me" && "you")
?  +  +    +   +
 : Should be: ("me" && "you")

```
------------
``` python
test_Or_constant (__main__.TestJs.test_Or_constant)
Traceback (most recent call last):
  File "/home/bug/dev/jsinui/tests/test.py", line 32, in test_Or_constant
    self.assertEqual(
AssertionError: '(me && you)' != '("me" || "you")'
- (me && you)
+ ("me" || "you")
 : Should be: ("me" || "you")

```
------------
### Errors:

### ExpectedFailures: 

