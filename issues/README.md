# JSinUI test results

Thid file contains results of last             last test of JSINUI module, we are trying to            fix them as soon as possible.

------

### Failures: 

``` python
test_and_constant (__main__.TestJs.test_and_constant)
Traceback (most recent call last):
  File "/home/bug/dev/jsinui/test.py", line 16, in test_and_constant
    self.assertEqual(
AssertionError: 'me && you' != '"me" && "you"'
- me && you
+ "me" && "you"
? +  +    +   +
 : Should be: "me" && "you"

```
------------
``` python
test_and_variable (__main__.TestJs.test_and_variable)
Traceback (most recent call last):
  File "/home/bug/dev/jsinui/test.py", line 23, in test_and_variable
    self.assertEqual(
AssertionError: 'me && you' != '"me" && "you"'
- me && you
+ "me" && "you"
? +  +    +   +
 : Should be: "me" && "you"

```
------------
### Errors:

### ExpectedFailures: 

