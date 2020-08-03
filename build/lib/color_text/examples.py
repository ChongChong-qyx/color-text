"""
Examples.
例子。
"""

import os
import sys

from color_text import output_example
from color_text import get_input_example
from color_text.PyQt5_util import SetControlTextColor

print("color_text output example")
output_example('0x409')

print("\n")

print("color_text 输出示例")
output_example('0x804')

print("\n")

print("color_text get input example")
get_input_example('0x409')

print("\n")

print("color_text 获取输入示例")
get_input_example('0x804')

def check_qt():
	try:
		import PyQt5
		del PyQt5

		return [True, 'PyQt5']

	except ModuleNotFoundError:

		try:
			import PySide2
			del PySide2

			return [True, 'PySide2']

		except ModuleNotFoundError:
			error_text = ['如果要使用关于Qt5功能，请先在CMD（命令提示符）输入命令 “python -m pip install PyQt5 pyqt5-tools PyQt5-sip click python-dotenv” 以安装PyQt5、pyqt5-tools、PyQt5-sip、click和python-dotenv。',
				'To use this functions for Qt5, enter the command "Python-m pip install PyQt5 pyqt5-tools pyqt5-sip click python-dotenv" in CMD (command prompt) to install PyQt5, pyqt5-tools, PyQt5-sip, click, and python-dotenv.']
			print(error_text[1] + '\n' + '              ' + error_text[0])

			return [False, None]

print("\n")

qt = check_qt()
if qt[0]:
	exec('from ' + qt[1] + '.QtWidgets import *')
	exec('from ' + qt[1] + '.QtGui import *')
	exec('from ' + qt[1] + '.QtCore import *')
	example_app = QApplication(sys.argv)
	example_window = QWidget()
	example_window.resize(300,40)
	example_window.setWindowTitle("Example    例子")

	example_label = QLabel(example_window)
	example_label.setText("A red label\n一个红色的标签")
	SetControlTextColor(example_label, "red")

	example_window.show()
	example_app.exec_()

os.system('pause')
