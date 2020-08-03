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

else:
	del system
