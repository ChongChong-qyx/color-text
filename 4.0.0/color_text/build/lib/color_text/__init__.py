r"""
This is a library for printing colored texts.
这是一个用来打印彩色文字的库。

教程见 https://pypi.org/project/color-text/ 或 Python 安装文件夹\Lib\site-packages\color_text\doc 中的教程。
Tutorial see https://pypi.org/project/color-text/ or tutorials in Python installation folder\Lib\site-packages\color_text\doc.
"""

from platform import system
import sys

class _Version(str):
	def __init__(self, version):
		pass

	def init_version_variable(self, number_1, number_2, number_3):
		self.version_str = number_1 + '.' + number_2 + '.' + number_3
		self.version_tuple = (int(number_1), int(number_2), int(number_3))
		self.version_str_tuple = (number_1, number_2, number_3)
		self.version_list = [int(number_1), int(number_2), int(number_3)]
		self.version_str_list = [number_1, number_2, number_3]
		self.version_dict = {'first_number' : int(number_1), 'second_number' : int(number_2), 'third_number' : int(number_3)}
		self.version_str_dict = {'first_number' : number_1, 'second_number' : number_2, 'third_number' : number_3}

if sys.version_info[:2] >= (3, 8):
	import importlib.metadata as importlib_metadata
else:
	import importlib_metadata

metadata = importlib_metadata.metadata("color_text")
__title__ = metadata["name"]
__summary__ = metadata["summary"]
__version__ = metadata["version"]
__author__ = metadata["author"]
__email__ = metadata["author-email"]
__license__ = metadata["license"]
__copyright__ = "Copyright 2020 齐奕翔"
__version__ = _Version(__version__)
__version__.init_version_variable('3', '1', '8')

del _Version
del sys

if system() == 'Windows':

	del system
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

	del system
