#-*- coding:utf-8 -*-#

import ctypes, sys

from .color import *

STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE = -11
STD_ERROR_HANDLE = -12

# get handle
# std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

# def set_cmd_text_color(color, handle=std_out_handle):
# 	Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
# 	return Bool

# #reset white
# def resetColor():
# 	set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
