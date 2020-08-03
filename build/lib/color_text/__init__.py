"""
This is a library for printing colored texts.
这是一个用来打印彩色文字的库。

教程见 https://pypi.org/project/color-text/3.1.3/
Tutorial see https://pypi.org/project/color-text/3.1.3/
"""

from platform import system

class _Version(str):
	def __init__(self, version):
		pass

	def init_variable(self, number_1, number_2, number_3):
		self.version_str = number_1 + '.' + number_2 + '.' + number_3
		self.version_tuple = (int(number_1), int(number_2), int(number_3))
		self.version_str_tuple = (number_1, number_2, number_3)
		self.version_list = [int(number_1), int(number_2), int(number_3)]
		self.version_str_list = [number_1, number_2, number_3]
		self.version_dict = {'first_number' : int(number_1), 'second_number' : int(number_2), 'third_number' : int(number_3)}
		self.version_str_dict = {'first_number' : number_1, 'second_number' : number_2, 'third_number' : number_3}

__version__ = '3.1.3'
version = _Version(__version__)
version.init_variable('3', '1', '3')

del _Version

if system() == 'Windows':

	from .output import PrintLightRedText, PrintYellowText, PrintRedText, PrintGreenText, PrintBlackText, PrintBlueText
	from .output import PrintGreyText, PrintGrayText, PrintLightBlueText, PrintVeryLightGreenText, PrintLightPurpleText
	from .output import PrintGlossWhiteText, PrintLightGreenText, output_example, Print, PrintOtherColorText, all_colors 
	from .output import computer_language, PrintPurpleText, PrintWhiteText, PrintLightYellowText
	from .get_input import GetBlackInput, GetBlueInput, GetGlossWhiteInput, GetGrayInput, GetGreenInput, GetGreyInput
	from .get_input import GetLightBlueInput, GetLightGreenInput, GetLightPurpleInput, GetLightRedInput, GetLightYellowInput
	from .get_input import GetPurpleInput, GetRedInput, GetVeryLightGreenInput, GetWhiteInput, GetYellowInput
	from .get_input import GetOtherColorInput, GetInput
	from .color import *
	from .functions import *
	from .handles import *

else:

	ErrorText = "This library is temporarily unavailable on the operating system you are using.\n         这个库暂时不能在你使用的操作系统上运行。"
	Error = OSError(ErrorText)
	raise Error
	del Error
	del ErrorText
