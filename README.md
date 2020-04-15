# Debugging

<badges>[![version](https://img.shields.io/pypi/v/debugging.svg)](https://pypi.org/project/debugging/)
[![license](https://img.shields.io/pypi/l/debugging.svg)](https://pypi.org/project/debugging/)
[![pyversions](https://img.shields.io/pypi/pyversions/debugging.svg)](https://pypi.org/project/debugging/)  
[![donate](https://img.shields.io/badge/Donate-Paypal-0070ba.svg)](https://paypal.me/foxe6)
[![powered](https://img.shields.io/badge/Powered%20by-UTF8-red.svg)](https://paypal.me/foxe6)
[![made](https://img.shields.io/badge/Made%20with-PyCharm-red.svg)](https://paypal.me/foxe6)
</badges>

<i>Grab debug and error information with ease.</i>

# Hierarchy

```
debugging
'---- debug_info()
```

# Example

## python
```python
from debugging import *
def main():
    # specify an indent level for formatting debug info
    print(debug_info(indent=2)[0])  # default is 0
#         [Debug]    Loaded    'main'@test3.py:4
# 
    try:
        # specify what debug info to dump from your own program
        print(debug_info(info=obj)[0])
        # NameError
    except:
        print(debug_info()[0])  # index 0 is formatted text
# [Debug]    Failed    'main'@test3.py:7
#     Traceback (most recent call last):
#       File "D:/foxe6/test3.py", line 7, in main
#         print(debug_info(info=obj)[0])
#     NameError: name 'obj' is not defined
# 
        print(debug_info()[1])  # index 1 is a tuple of stacks
# (('NameError', "'main'@test3.py:7", "name 'obj' is not defined\n"),)
# 
if __name__ == "__main__":
    main()
```

## shell
```shell script
rem debugging.exe
rem debug test
("[Debug]    Loaded    'main'@test.py:7", ())
('[Debug]    Failed    \'main\'@test.py:8\n    Traceback (most recent call last):\n      File "c:\\program files\\python38\\lib\\site-packages\\debugging\\test.py", line 8, in main\n        raise Exception("test Exception")\n    Exception: test Exception\n', (('Exception', "'main'@test.py:8", 'test Exception\n'),))
```
