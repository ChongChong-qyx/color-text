"""
All functions for getting input.
所有用来获取输入的函数。
"""

from platform import system

if system() == 'Windows':
	del system

	from .color import *
	from .output import all_colors, computer_language

	def GetBlackInput(prompt=''):
		"""
		Get balck input.
		获取黑色的输入。
		"""
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_BLACK | BACKGROUND_WHITE)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetBlueInput(prompt=''):
		"""
		Get blue input.
		获取蓝色的输入。
		"""
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_BLUE)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetGreenInput(prompt=''):
		"""
		Get green input.
		获取绿色的输入。
		"""
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_GREEN)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetLightGreenInput(prompt='', color_number=1):
		"""
		Get light green input.
		获取浅绿色的输入。
		"""
		from .functions import set_cmd_text_color, resetColor
		import sys
		if color_number == 1:
			set_cmd_text_color(FOREGROUND_LIGHT_GREEN)
			input_text = input(prompt)
			resetColor()
		elif color_number == 2:
			set_cmd_text_color(FOREGROUND_LIGHT_GREEN_TWO)
			input_text = input(prompt)
			resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetRedInput(prompt=''):
		"""
		Get red input.
		获取红色的输入。
		"""
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_RED)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetPurpleInput(prompt=''):
		"""
		Get purple input.
		获取紫色的输入。
		"""
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_PURPLE)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetYellowInput(prompt=''):
		"""
		Get yellow input.
		获取黄色的输入。
		"""
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_YELLOW)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetWhiteInput(prompt=''):
		"""
		Get white input.
		获取白色的输入。
		"""
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_WHITE)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetGreyInput(prompt=''):
		"""
		Get grey input.
		获取灰色的输入。
		"""
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_GREY)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetGrayInput(prompt=''):
		"""
		Get gray input.
		获取灰色的输入。
		"""
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_GREY)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetLightBlueInput(prompt=''):
		"""
		Get light blue input.
		获取浅蓝色的输入。
		"""
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_LIGHT_BLUE)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetVeryLightGreenInput(prompt=''):
		"""
		Get very light green input.
		获取很浅的浅绿色的输入。
		"""
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_VERY_LIGHT_GREEN)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetLightRedInput(prompt=''):
		"""
		Get light red input.
		获取浅红色的输入。
		"""
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_LIGHT_RED)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetLightPurpleInput(prompt=''):
		"""
		Get light purple input.
		获取浅紫色的输入。
		"""
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_LIGHT_PURPLE)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetLightYellowInput(prompt=''):
		"""
		Get light yellow input.
		获取浅黄色的输入。
		"""
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_LIGHT_YELLOW)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetGlossWhiteInput(prompt=''):
		"""
		Get gloss white input.
		获取亮白色的输入。
		"""
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_GLOSS_WHITE)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetOtherColorInput(prompt='', text_color=FOREGROUND_WHITE, background_color=BACKGROUND_BLACK):
		"""
		Get other colors input.
		获取其他颜色的输入。
		"""
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(text_color | background_color)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetInput(prompt='', text_color=FOREGROUND_WHITE, background_color=BACKGROUND_BLACK):
		"""
		Get input.
		获取输入。
		"""
		input_text = GetOtherColorInput(prompt, text_color = text_color, background_color = background_color)
		return input_text

	def get_input_example(computer_language=computer_language, time_to_sleep=0):
		"""
		An Example of getting input.
		一个获取输入的例子。
		"""
		if computer_language == 0x409 or computer_language == '0x409' or computer_language == 'English' or computer_language == 'english' or computer_language == u'英文' or computer_language == u'英语' or computer_language == 1033 or computer_language == '1033':
			GetLightRedInput("Please enter some words: ")
			GetYellowInput("Please enter some words: ")
			GetRedInput("Please enter some words: ")
			GetGreenInput("Please enter some words: ")
			GetBlackInput("Please enter some words: ")
			GetBlueInput("Please enter some words: ")
			GetPurpleInput("Please enter some words: ")
			GetWhiteInput("Please enter some words: ")
			GetGreyInput("Please enter some words: ")
			GetGrayInput("Please enter some words: ")
			GetLightBlueInput("Please enter some words: ")
			GetVeryLightGreenInput("Please enter some words: ")
			GetLightPurpleInput("Please enter some words: ")
			GetLightYellowInput("Please enter some words: ")
			GetGlossWhiteInput("Please enter some words: ")
			GetLightGreenInput("Please enter some words: ")
			GetLightGreenInput("Please enter some words: ", color_number = 2)
		elif computer_language == 0x804 or computer_language == '0x804' or computer_language == 'Chinese' or computer_language == 'chinese' or computer_language == u'中文' or computer_language == u'汉语' or computer_language == u'普通话' or computer_language == 2052 or computer_language == '2052':
			GetLightRedInput("请输入一些字：")
			GetYellowInput("请输入一些字：")
			GetRedInput("请输入一些字：")
			GetGreenInput("请输入一些字：")
			GetBlackInput("请输入一些字：")
			GetBlueInput("请输入一些字：")
			GetPurpleInput("请输入一些字：")
			GetWhiteInput("请输入一些字：")
			GetGreyInput("请输入一些字：")
			GetGrayInput("请输入一些字：")
			GetLightBlueInput("请输入一些字：")
			GetVeryLightGreenInput("请输入一些字：")
			GetLightPurpleInput("请输入一些字：")
			GetLightYellowInput("请输入一些字：")
			GetGlossWhiteInput("请输入一些字：")
			GetLightGreenInput("请输入一些字：")
			GetLightGreenInput("请输入一些字：", color_number = 2)
		else:
			GetLightRedInput("Please enter some words: ")
			GetYellowInput("Please enter some words: ")
			GetRedInput("Please enter some words: ")
			GetGreenInput("Please enter some words: ")
			GetBlackInput("Please enter some words: ")
			GetBlueInput("Please enter some words: ")
			GetPurpleInput("Please enter some words: ")
			GetWhiteInput("Please enter some words: ")
			GetGreyInput("Please enter some words: ")
			GetGrayInput("Please enter some words: ")
			GetLightBlueInput("Please enter some words: ")
			GetVeryLightGreenInput("Please enter some words: ")
			GetLightPurpleInput("Please enter some words: ")
			GetLightYellowInput("Please enter some words: ")
			GetGlossWhiteInput("Please enter some words: ")
			GetLightGreenInput("Please enter some words: ")
			GetLightGreenInput("Please enter some words: ", color_number = 2)
		import time as t
		t.sleep(int(time_to_sleep))
		del t

	if __name__ == '__main__':
		get_input_example()

else:
	del system
