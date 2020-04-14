from .utils import *
import traceback
import textwrap
from omnitools import *


__ALL__ = ["debug_info"]


def debug_info(info: Any = None, indent: int = 0) -> tuple:
    indent = int(indent)+1
    indent_scale = 4
    indent_size = indent*indent_scale
    indent = " "*indent_size
    try:
        stack = (None, None, None)
        failed = sys.exc_info() != stack
        status = "Failed" if failed else "Loaded"
        what = " "*(indent_size-indent_scale)+f"[Debug]    {status}    "
        stack = []
        if failed:
            stack = get_error_info()
            what += stack[0][1]
        else:
            what += get_success_info(depth=2)
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
                _info = dumpobj(info, indent=0, indent_scale=indent_scale)
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
            get_error_info()


