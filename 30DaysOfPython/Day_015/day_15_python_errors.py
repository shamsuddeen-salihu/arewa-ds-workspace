Windows PowerShell
Copyright (C) 2015 Microsoft Corporation. All rights reserved.

PS C:\Users\PC\projects\arewa-ds-workspace> & "C:/Program Files (x86)/Python37-32/python.exe"
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print "shamsuddeen"
  File "<stdin>", line 1
    print "shamsuddeen"
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("shamsuddeen")?
o 'print'. Did you mean print("shamsuddeen
")?
>>> print(deenee)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'deenee' is not defined
>>> number = '10'
>>> add=number + 10
Traceback (most recent call last):        int") to str
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "
int") to str
>>> my_list=['apple','banana','orange']
>>> my_list[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> import randoms
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'rand
oms'
>>> import math
>>> math.sqrts
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attri
bute 'sqrts'
>>> my_data={'name':'Shamsu','age':'20'}
>>> my_data['ages']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'ages'
>>> 10 + '2'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for
 +: 'int' and 'str'
>>> from functools import reduces
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'reduces'
from 'functools' (C:\Program Files (x86)\P
ython37-32\lib\functools.py)
>>> number=int("abc")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with
 base 10: 'abc'
>>> result=5/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>