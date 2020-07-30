"""
All functions for output.
所有用来输出的函数。
"""

from platform import system

if system() == 'Windows':

	all_colors = ['BACKGROUND_BLACK', 'BACKGROUND_BLUE', 'BACKGROUND_GLOSS_WHITE', 'BACKGROUND_GREEN', 'BACKGROUND_GREY',
		'BACKGROUND_LIGHT_BLUE', 'BACKGROUND_LIGHT_GREEN', 'BACKGROUND_LIGHT_GREEN_TWO', 'BACKGROUND_LIGHT_PURPLE',
		'BACKGROUND_LIGHT_RED', 'BACKGROUND_LIGHT_YELLOW', 'BACKGROUND_PURPLE', 'BACKGROUND_RED',
		'BACKGROUND_VERY_LIGHT_GREEN', 'BACKGROUND_WHITE', 'BACKGROUND_YELLOW', 'FOREGROUND_BLACK',
		'FOREGROUND_BLUE', 'FOREGROUND_GLOSS_WHITE', 'FOREGROUND_GREEN', 'FOREGROUND_GREY', 'FOREGROUND_LIGHT_BLUE',
		'FOREGROUND_LIGHT_GREEN', 'FOREGROUND_LIGHT_GREEN_TWO', 'FOREGROUND_LIGHT_PURPLE', 'FOREGROUND_LIGHT_RED',
		'FOREGROUND_LIGHT_YELLOW', 'FOREGROUND_PURPLE', 'FOREGROUND_RED', 'FOREGROUND_VERY_LIGHT_GREEN',
		'FOREGROUND_WHITE', 'FOREGROUND_YELLOW']

	from .color import *

	import ctypes
	try:
		_dll_h = ctypes.windll.kernel32
		computer_language = hex(_dll_h.GetSystemDefaultUILanguage())
		del _dll_h
	except:
		computer_language = None

	del ctypes
	del system

	def PrintGreenText(*values, end='\n'):
		"""
		Print green text.
		打印绿色的文字。
		"""
		times = 0
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_GREEN)
		for mess in values:
			times += 1
			if times < len(values):
				sys.stdout.write(str(mess) + ' ')
			else:
				sys.stdout.write(str(mess))
		try:
			sys.stdout.write(end)
		except:
			raise TypeError("end must be None or a string, not int")
		resetColor()
		del sys
		del set_cmd_text_color, resetColor

	def PrintRedText(*values, end='\n'):
		"""
		Print red text.
		打印红色的文字。
		"""
		times = 0
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_RED)
		for mess in values:
			times += 1
			if times < len(values):
				sys.stdout.write(str(mess) + ' ')
			else:
				sys.stdout.write(str(mess))
		try:
			sys.stdout.write(end)
		except:
			raise TypeError("end must be None or a string, not int")
		resetColor()
		del sys
		del set_cmd_text_color, resetColor

	def PrintYellowText(*values, end='\n'):
		"""
		Print yellow text.
		打印黄色的文字。
		"""
		times = 0
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_YELLOW)
		for mess in values:
			times += 1
			if times < len(values):
				sys.stdout.write(str(mess) + ' ')
			else:
				sys.stdout.write(str(mess))
		try:
			sys.stdout.write(end)
		except:
			raise TypeError("end must be None or a string, not int")
		resetColor()
		del sys
		del set_cmd_text_color, resetColor

	def PrintLightRedText(*values, end='\n'):
		"""
		Print light red text.
		打印浅红色的文字。
		"""
		times = 0
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_LIGHT_RED)
		for mess in values:
			times += 1
			if times < len(values):
				sys.stdout.write(str(mess) + ' ')
			else:
				sys.stdout.write(str(mess))
		try:
			sys.stdout.write(end)
		except:
			raise TypeError("end must be None or a string, not int")
		resetColor()
		del sys
		del set_cmd_text_color, resetColor

	def PrintBlackText(*values, end='\n'):
		"""
		Print black text.
		打印黑色的文字。
		"""
		times = 0
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_BLACK | BACKGROUND_WHITE)
		for mess in values:
			times += 1
			if times < len(values):
				sys.stdout.write(str(mess) + ' ')
			else:
				sys.stdout.write(str(mess))
		try:
			sys.stdout.write(end)
		except:
			raise TypeError("end must be None or a string, not int")
		resetColor()
		del sys
		del set_cmd_text_color, resetColor

	def PrintBlueText(*values, end='\n'):
		"""
		Print blue text.
		打印蓝色的文字。
		"""
		times = 0
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_BLUE)
		for mess in values:
			times += 1
			if times < len(values):
				sys.stdout.write(str(mess) + ' ')
			else:
				sys.stdout.write(str(mess))
		try:
			sys.stdout.write(end)
		except:
			raise TypeError("end must be None or a string, not int")
		resetColor()
		del sys
		del set_cmd_text_color, resetColor

	def PrintLightGreenText(*values, color_number=1, end='\n'):
		"""
		Print light green text.
		打印浅绿色的文字。
		"""
		times = 0
		from .functions import set_cmd_text_color, resetColor
		import sys
		if color_number == 1:
			set_cmd_text_color(FOREGROUND_LIGHT_GREEN)
			for mess in values:
				times += 1
				if times < len(values):
					sys.stdout.write(str(mess) + ' ')
				else:
					sys.stdout.write(str(mess))
			try:
				sys.stdout.write(end)
			except:
				raise TypeError("end must be None or a string, not int")
			resetColor()
		elif color_number == 2:
			set_cmd_text_color(FOREGROUND_LIGHT_GREEN_TWO)
			for mess in values:
				times += 1
				if times < len(values):
					sys.stdout.write(str(mess) + ' ')
				else:
					sys.stdout.write(str(mess))
			try:
				sys.stdout.write(end)
			except:
				raise TypeError("end must be None or a string, not int")
			resetColor()
		del sys
		del set_cmd_text_color, resetColor

	def PrintPurpleText(*values, end='\n'):
		"""
		Print purple text.
		打印紫色的文字。
		"""
		times = 0
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_PURPLE)
		for mess in values:
			times += 1
			if times < len(values):
				sys.stdout.write(str(mess) + ' ')
			else:
				sys.stdout.write(str(mess))
		try:
			sys.stdout.write(end)
		except:
			raise TypeError("end must be None or a string, not int")
		resetColor()
		del sys
		del set_cmd_text_color, resetColor

	def PrintWhiteText(*values, end='\n'):
		"""
		Print white text.
		打印白色的文字。
		"""
		times = 0
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_WHITE)
		for mess in values:
			times += 1
			if times < len(values):
				sys.stdout.write(str(mess) + ' ')
			else:
				sys.stdout.write(str(mess))
		try:
			sys.stdout.write(end)
		except:
			raise TypeError("end must be None or a string, not int")
		resetColor()
		del sys
		del set_cmd_text_color, resetColor

	def PrintGreyText(*values, end='\n'):
		"""
		Print grey text.
		打印灰色的文字。
		"""
		times = 0
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_GREY)
		for mess in values:
			times += 1
			if times < len(values):
				sys.stdout.write(str(mess) + ' ')
			else:
				sys.stdout.write(str(mess))
		try:
			sys.stdout.write(end)
		except:
			raise TypeError("end must be None or a string, not int")
		resetColor()
		del sys
		del set_cmd_text_color, resetColor

	def PrintGrayText(*values, end='\n'):
		"""
		Print gray text.
		打印灰色的文字。
		"""
		times = 0
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_GREY)
		for mess in values:
			times += 1
			if times < len(values):
				sys.stdout.write(str(mess) + ' ')
			else:
				sys.stdout.write(str(mess))
		try:
			sys.stdout.write(end)
		except:
			raise TypeError("end must be None or a string, not int")
		resetColor()
		del sys
		del set_cmd_text_color, resetColor

	def PrintLightBlueText(*values, end='\n'):
		"""
		Print light blue text.
		打印浅蓝色的文字。
		"""
		times = 0
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_LIGHT_BLUE)
		for mess in values:
			times += 1
			if times < len(values):
				sys.stdout.write(str(mess) + ' ')
			else:
				sys.stdout.write(str(mess))
		try:
			sys.stdout.write(end)
		except:
			raise TypeError("end must be None or a string, not int")
		resetColor()
		del sys
		del set_cmd_text_color, resetColor

	def PrintVeryLightGreenText(*values, end='\n'):
		"""
		Print very light green text.
		打印很浅的浅绿色的文字。
		"""
		times = 0
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_VERY_LIGHT_GREEN)
		for mess in values:
			times += 1
			if times < len(values):
				sys.stdout.write(str(mess) + ' ')
			else:
				sys.stdout.write(str(mess))
		try:
			sys.stdout.write(end)
		except:
			raise TypeError("end must be None or a string, not int")
		resetColor()
		del sys
		del set_cmd_text_color, resetColor

	def PrintLightPurpleText(*values, end='\n'):
		"""
		Print light purple text.
		打印浅紫色的文字。
		"""
		times = 0
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_LIGHT_PURPLE)
		for mess in values:
			times += 1
			if times < len(values):
				sys.stdout.write(str(mess) + ' ')
			else:
				sys.stdout.write(str(mess))
		try:
			sys.stdout.write(end)
		except:
			raise TypeError("end must be None or a string, not int")
		resetColor()
		del sys
		del set_cmd_text_color, resetColor

	def PrintLightYellowText(*values, end='\n'):
		"""
		Print light yellow text.
		打印浅黄色的文字。
		"""
		times = 0
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_LIGHT_YELLOW)
		for mess in values:
			times += 1
			if times < len(values):
				sys.stdout.write(str(mess) + ' ')
			else:
				sys.stdout.write(str(mess))
		try:
			sys.stdout.write(end)
		except:
			raise TypeError("end must be None or a string, not int")
		resetColor()
		del sys
		del set_cmd_text_color, resetColor

	def PrintGlossWhiteText(*values, end='\n'):
		"""
		Print gloss white text.
		打印亮白色的文字。
		"""
		times = 0
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_GLOSS_WHITE)
		for mess in values:
			times += 1
			if times < len(values):
				sys.stdout.write(str(mess) + ' ')
			else:
				sys.stdout.write(str(mess))
		try:
			sys.stdout.write(end)
		except:
			raise TypeError("end must be None or a string, not int")
		resetColor()
		del sys
		del set_cmd_text_color, resetColor

	def Print(*values, text_color=FOREGROUND_WHITE, background_color=BACKGROUND_BLACK, end='\n'):
		"""
		Print text.
		打印文字。
		"""
		times = 0
		for value in values:
			times += 1
			if times < len(values):
				PrintOtherColorText(value, text_color = text_color, background_color = background_color, end = ' ')
			else:
				PrintOtherColorText(value, text_color = text_color, background_color = background_color, end = '')
		PrintOtherColorText('', text_color = text_color, background_color = background_color, end = end)

	def PrintOtherColorText(*values, text_color=FOREGROUND_WHITE, background_color=BACKGROUND_BLACK, end='\n'):
		"""
		Print other colors text.
		打印其他颜色的文字。
		"""
		times = 0
		from .functions import set_cmd_text_color, resetColor
		import sys
		for value in values:
			set_cmd_text_color(text_color | background_color)
			times += 1
			if times < len(values):
				sys.stdout.write(str(value) + ' ')
			else:
				sys.stdout.write(str(value))
			resetColor()
		set_cmd_text_color(text_color | background_color)
		try:
			sys.stdout.write(end)
		except:
			raise TypeError("end must be None or a string, not int")
		resetColor()
		del sys
		del set_cmd_text_color, resetColor

	def output_example(computer_language=computer_language, time_to_sleep=0):
		"""
		A Example of output.
		一个输出的例子。
		"""
		if computer_language == 0x409 or computer_language == '0x409' or computer_language == 'English' or computer_language == 'english' or computer_language == u'英文' or computer_language == u'英语' or computer_language == 1033 or computer_language == '1033':
			PrintLightRedText("This is a light red text.")
			PrintYellowText("This is a yellow text.")
			PrintRedText("This is a red text.")
			PrintGreenText("This is a green text.")
			PrintBlackText("This is a black text.")
			PrintBlueText("This is a blue text.")
			PrintPurpleText("This is a purple text.")
			PrintWhiteText("This is a white text.")
			PrintGreyText("This is a grey text.")
			PrintGrayText("This is a grey text too.")
			PrintLightBlueText("This is a light blue text.")
			PrintVeryLightGreenText("This is a very light green text.")
			PrintLightPurpleText("This is a light purple text.")
			PrintLightYellowText("This is a light yellow text.")
			PrintGlossWhiteText("This is a gloss white text.")
			PrintLightGreenText("This is a light green text.")
			PrintLightGreenText("This is a light green text too.", color_number = 2)
		elif computer_language == 0x804 or computer_language == '0x804' or computer_language == 'Chinese' or computer_language == 'chinese' or computer_language == u'中文' or computer_language == u'汉语' or computer_language == u'普通话' or computer_language == 2052 or computer_language == '2052':
			PrintLightRedText("这是一段浅红色的文字。")
			PrintYellowText("这是一段黄色的文字。")
			PrintRedText("这是一段红色的文字。")
			PrintGreenText("这是一段绿色的文字。")
			PrintBlackText("这是一段黑色的文字。")
			PrintBlueText("这是一段蓝色的文字。")
			PrintPurpleText("这是一段紫色的文字。")
			PrintWhiteText("这是一段白色的文字。")
			PrintGreyText("这是一段灰色的文字。")
			PrintGrayText("这也是一段灰色的文字。")
			PrintLightBlueText("这是一段浅蓝色的文字。")
			PrintVeryLightGreenText("这是一段很浅的绿色的文字。")
			PrintLightPurpleText("这是一段浅紫色的文字。")
			PrintLightYellowText("这是一段浅黄色的文字。")
			PrintGlossWhiteText("这是一段亮白色的文字。")
			PrintLightGreenText("这是一段浅绿色的文字。")
			PrintLightGreenText("这也是一段浅绿色的文字。", color_number = 2)
		else:
			PrintLightRedText("This is a light red text.")
			PrintYellowText("This is a yellow text.")
			PrintRedText("This is a red text.")
			PrintGreenText("This is a green text.")
			PrintBlackText("This is a black text.")
			PrintBlueText("This is a blue text.")
			PrintPurpleText("This is a purple text.")
			PrintWhiteText("This is a white text.")
			PrintGreyText("This is a grey text.")
			PrintGrayText("This is a grey text too.")
			PrintLightBlueText("This is a light blue text.")
			PrintVeryLightGreenText("This is a very light green text.")
			PrintLightPurpleText("This is a light purple text.")
			PrintLightYellowText("This is a light yellow text.")
			PrintGlossWhiteText("This is a gloss white text.")
			PrintLightGreenText("This is a light green text.")
			PrintLightGreenText("This is a light green text too.", color_number = 2)
		import time as t
		t.sleep(int(time_to_sleep))
		del t

else:
	del system

if __name__ == '__main__':
	output_example()
