# Debugging Tool

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


    # specify an indent scale for indent spaces
    print(debug_info(indent_scale=1)[0])  # default is 4


    try:
        # specify what debug info to dump from your own program
        print(debug_info(info=obj)[0])
        # NameError
    except:
        print(debug_info()[0])  # index 0 is formatted text






        print(debug_info()[1])  # index 1 is a tuple of stacks


if __name__ == "__main__":
    main()
```
