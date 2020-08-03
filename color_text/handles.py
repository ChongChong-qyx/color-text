"""
All handles variables.
所有句柄变量。
"""

from platform import system

if system() == 'Windows':
	del system
	STD_INPUT_HANDLE = -10
	STD_OUTPUT_HANDLE = -11
	STD_ERROR_HANDLE = -12

else:
	del system

# get handle
# std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

# def set_cmd_text_color(color, handle=std_out_handle):
# 	Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
# 	return Bool

# #reset white
# def resetColor():
# 	set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
