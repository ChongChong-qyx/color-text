#-*- coding:utf-8 -*-#

from platform import system

if system() == 'Windows':
	del system

	from .color import *
	from .output import all_colors, computer_language

	def GetBlackInput(prompt=''):
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_BLACK | BACKGROUND_WHITE)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetBlueInput(prompt=''):
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_BLUE)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetGreenInput(prompt=''):
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_GREEN)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetLightGreenInput(prompt='', color_number=1):
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
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_RED)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetPurpleInput(prompt=''):
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_PURPLE)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetYellowInput(prompt=''):
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_YELLOW)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetWhiteInput(prompt=''):
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_WHITE)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetGreyInput(prompt=''):
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_GREY)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetGrayInput(prompt=''):
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_GREY)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetLightBlueInput(prompt=''):
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_LIGHT_BLUE)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetVeryLightGreenInput(prompt=''):
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_VERY_LIGHT_GREEN)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetLightRedInput(prompt=''):
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_LIGHT_RED)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetLightPurpleInput(prompt=''):
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_LIGHT_PURPLE)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetLightYellowInput(prompt=''):
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_LIGHT_YELLOW)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetGlossWhiteInput(prompt=''):
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(FOREGROUND_GLOSS_WHITE)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetOtherColorInput(prompt='', text_color=FOREGROUND_WHITE, background_color=BACKGROUND_BLACK):
		from .functions import set_cmd_text_color, resetColor
		import sys
		set_cmd_text_color(text_color | background_color)
		input_text = input(prompt)
		resetColor()
		del sys
		del set_cmd_text_color, resetColor
		return input_text

	def GetInput(prompt='', text_color=FOREGROUND_WHITE, background_color=BACKGROUND_BLACK):
		input_text = GetOtherColorInput(prompt, text_color = text_color, background_color = background_color)
		return input_text

else:
	del system
