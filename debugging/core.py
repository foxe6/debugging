import os
import sys
import traceback
import textwrap
from omnitools import dumpobj, jd, successstacks, errorstacks
from typing import *


__ALL__ = ["debug_info"]


def debug_info(info: Any = None, indent: int = 0, indent_scale: int = 4) -> tuple:
    indent = int(indent)+1
    indent_size = indent*indent_scale
    indent = " "*indent_size
    try:
        stack = (None, None, None)
        failed = sys.exc_info() != stack
        status = "Failed" if failed else "Loaded"
        what = " "*(indent_size-indent_scale)+f"[Debug]    {status}    "
        stack = ()
        if failed:
            stack = errorstacks()
            what += stack[0][1]
        else:
            what += successstacks()[2]
        if info:
            try:
                columns = os.get_terminal_size().columns
            except:
                columns = 80
            tw = textwrap.TextWrapper(
                width=columns-indent_size,
                initial_indent=indent,
                subsequent_indent=indent
            )
            try:
                _info = jd(info, indent=indent_scale)
                serializer = jd
            except:
                _info = dumpobj(info, indent_scale=indent_scale)
                serializer = dumpobj
            if len(_info) > 2500:
                _info = tw.fill(serializer(info))
            elif any([s for s in ("\r", "\n") if s in _info]):
                _info = textwrap.indent(_info, indent)
            else:
                _info = tw.fill(_info)
            what += "\n"+_info
        if failed:
            what += "\n"+textwrap.indent(traceback.format_exc(), indent)
        return what, stack
    except:
        return\
            " "*(indent_size-indent_scale)+\
            "Debug information is not available due to:\n"+\
            textwrap.indent(traceback.format_exc(), indent),\
            errorstacks()


