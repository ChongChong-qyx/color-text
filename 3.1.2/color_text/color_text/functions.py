#-*- coding:utf-8 -*-#

from platform import system

if system() == 'Windows':
	from .handles import STD_OUTPUT_HANDLE, STD_INPUT_HANDLE, STD_ERROR_HANDLE
	import ctypes
	del system
	# get handle
	std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
	std_error_handle = ctypes.windll.kernel32.GetStdHandle(STD_ERROR_HANDLE)
	std_input_handle = ctypes.windll.kernel32.GetStdHandle(STD_INPUT_HANDLE)
	del ctypes
	del STD_OUTPUT_HANDLE, STD_INPUT_HANDLE, STD_ERROR_HANDLE
	
	def set_cmd_text_color(color, handle = std_out_handle):
		import ctypes
		Bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
		del ctypes
		return Bool
	
	# reset color to white
	def resetColor(handle = std_out_handle):
		from .color import FOREGROUND_RED, FOREGROUND_GREEN, FOREGROUND_BLUE
		set_cmd_text_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE, handle = handle)
		del FOREGROUND_RED, FOREGROUND_GREEN, FOREGROUND_BLUE

else:
	del system
