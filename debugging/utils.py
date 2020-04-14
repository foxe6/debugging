import sys
import os
import inspect
import gc
from types import FrameType


__ALL__ = ["get_error_info", "get_success_info"]


def get_error_info() -> list:
    e = sys.exc_info()[1]
    tb = sys.exc_info()[2]
    stacks = []
    while True:
        try:
            lineno = tb.tb_lineno
            filename = os.path.basename(tb.tb_frame.f_code.co_filename)
            info = None
            try:
                info = ",".join(e.args)
            except:
                info = str(e)
            stacks.append((type(e).__name__, qualname(tb.tb_frame) + "@" + filename + ":" + str(lineno), info + "\n"))
            tb = tb.tb_next
        except:
            return stacks


def get_success_info(depth: int = 1) -> str:
    depth = int(depth)
    stack = inspect.stack()[depth]
    lineno = stack[2]
    filename = os.path.basename(stack[1])
    frame = stack[0]
    return qualname(frame) + "@" + filename + ":" + str(lineno)


def qualname(frame: FrameType) -> str:
    return f"'{where(frame).__qualname__}'"


def where(frame: FrameType) -> object:
    return [obj for obj in gc.get_referrers(frame.f_code) if inspect.isfunction(obj)][0]

