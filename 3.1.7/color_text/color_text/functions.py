"""
All functions for setting CMD text color.
所有用来设置CMD（命令提示符）的文本颜色的函数。
"""

from platform import system

if system() == 'Windows':
	from .handles import STD_OUTPUT_HANDLE, STD_INPUT_HANDLE, STD_ERROR_HANDLE
	import ctypes
	del system

	std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
	std_error_handle = ctypes.windll.kernel32.GetStdHandle(STD_ERROR_HANDLE)
	std_input_handle = ctypes.windll.kernel32.GetStdHandle(STD_INPUT_HANDLE)
	
	del ctypes
	del STD_OUTPUT_HANDLE, STD_INPUT_HANDLE, STD_ERROR_HANDLE
	
	def set_cmd_text_color(color, handle = std_out_handle):
		"""
		Set the text color of CMD.
		设置CMD（命令提示符）的文本的颜色。
		"""
		import ctypes
		Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
		del ctypes
		return Bool
	
	def resetColor(handle = std_out_handle):
		"""
		Restore the text color of CMD to white.
		将CMD（命令提示符）的文本颜色恢复为白色。
		"""
		from .color import FOREGROUND_RED, FOREGROUND_GREEN, FOREGROUND_BLUE
		set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE, handle = handle)
		del FOREGROUND_RED, FOREGROUND_GREEN, FOREGROUND_BLUE

else:
	del system
