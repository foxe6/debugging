from . import *
from omnitools import *


def main():
    try:
        p(debug_info())
        raise Exception("test Exception")
    except:
        p(debug_info())


if __name__ == "__main__":
    main()

