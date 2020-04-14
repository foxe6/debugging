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
|---- debug_info()
|---- get_error_info()
'---- get_success_info()
```

# Example

## python
```python
import debugging.test
debugging.test.main()
# ("[Debug]\tLoaded\t'main'@test.py:7", [])
# # To get "'main'@test.py:7" instead, try:
# # get_success_info()
# # # call stacks may be disrupted by decorators
# (
#     '[Debug]    Failed    \'main\'@test.py:8\n    Traceback (most recent call last):\n      File "c:\\program files\\python38\\lib\\site-packages\\debugging\\test.py", line 8, in main\n        raise Exception("test Exception")\n    Exception: test Exception\n',
#     [('Exception', "'main'@test.py:8", 'test Exception\n')]
# )
# # To get a list of error stacks instead, try:
# # get_error_info()
# # # call stacks may be disrupted by decorators

from debugging import *
def main():
    # specify an indent level for formatting debug info
    print(debug_info(indent=2))  # default is 0
    # specify what debug info to dump from your own program
    print(debug_info(info=obj))
if __name__ == "__main__":
    main()
```

## shell
```shell script
rem debugging.exe
rem debug test
("[Debug]    Loaded    'main'@test.py:7", [])
('[Debug]    Failed    \'main\'@test.py:8\n    Traceback (most recent call last):\n      File "c:\\program files\\python38\\lib\\site-packages\\debugging\\test.py", line 8, in main\n        raise Exception("test Exception")\n    Exception: test Exception\n', [('Exception', "'main'@test.py:8", 'test Exception\n')])
```
