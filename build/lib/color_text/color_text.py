#-*- coding:utf-8 -*-#

# import ctypes, sys

# from color import *

# STD_INPUT_HANDLE = -10
# STD_OUTPUT_HANDLE = -11
# STD_ERROR_HANDLE = -12

from settings import *

from color import *

from functions import *

import ctypes
dll_h = ctypes.windll.kernel32
language = hex(dll_h.GetSystemDefaultUILanguage())

#green
def printGreen(mess):
	set_cmd_text_color(FOREGROUND_GREEN)
	sys.stdout.write(mess + '\n')
	resetColor()

#red
def printRed(mess):
	set_cmd_text_color(FOREGROUND_RED)
	sys.stdout.write(mess + '\n')
	resetColor()

#yellow
def printYellow(mess):
	set_cmd_text_color(FOREGROUND_YELLOW)
	sys.stdout.write(mess + '\n')
	resetColor()

#light_red
def printLightRed(mess):
	set_cmd_text_color(FOREGROUND_LIGHT_RED)
	sys.stdout.write(mess + '\n')
	resetColor()

#black
def printBlack(mess):
	set_cmd_text_color(FOREGROUND_BLACK | BACKGROUND_WHITE)
	sys.stdout.write(mess + '\n')
	resetColor()

#blue
def printBlue(mess):
	set_cmd_text_color(FOREGROUND_BLUE)
	sys.stdout.write(mess + '\n')
	resetColor()

#light_green
def printLightGreen(mess, number=1):
	if number == 1:
		set_cmd_text_color(FOREGROUND_LIGHT_GREEN)
		sys.stdout.write(mess + '\n')
		resetColor()
	elif number == 2:
		set_cmd_text_color(FOREGROUND_LIGHT_GREEN_TWO)
		sys.stdout.write(mess + '\n')
		resetColor()

#purple
def printPurple(mess):
	set_cmd_text_color(FOREGROUND_PURPLE)
	sys.stdout.write(mess + '\n')
	resetColor()

#white
def printWhite(mess):
	set_cmd_text_color(FOREGROUND_WHITE)
	sys.stdout.write(mess + '\n')
	resetColor()

#grey
def printGrey(mess):
	set_cmd_text_color(FOREGROUND_GREY)
	sys.stdout.write(mess + '\n')
	resetColor()

#gray
def printGray(mess):
	set_cmd_text_color(FOREGROUND_GREY)
	sys.stdout.write(mess + '\n')
	resetColor()

#light_blue
def printLightBlue(mess):
	set_cmd_text_color(FOREGROUND_LIGHT_BLUE)
	sys.stdout.write(mess + '\n')
	resetColor()

#very_light_green
def printVeryLightGreen(mess):
	set_cmd_text_color(FOREGROUND_VERY_LIGHT_GREEN)
	sys.stdout.write(mess + '\n')
	resetColor()

#light_purple
def printLightPurple(mess):
	set_cmd_text_color(FOREGROUND_LIGHT_PURPLE)
	sys.stdout.write(mess + '\n')
	resetColor()

#light_yellow
def printLightYellow(mess):
	set_cmd_text_color(FOREGROUND_LIGHT_YELLOW)
	sys.stdout.write(mess + '\n')
	resetColor()

#gloss_white
def printGlossWhite(mess):
	set_cmd_text_color(FOREGROUND_GLOSS_WHITE)
	sys.stdout.write(mess + '\n')
	resetColor()

#color_rectangle
def printRectangle(amount, color='white'):
	rectanglemess = ""
	if color == 'white':
		set_cmd_text_color(FOREGROUND_GLOSS_WHITE)
		sys.stdout.write(rectanglemess + '\n')
		resetColor()

class Print():
	def __init__(self, mess):
		self.mess = mess
		print(self.mess)

#example
def example(computer_language=language, time_to_sleep=1800):
	if computer_language == 0x409 or computer_language == '0x409' or computer_language == 'English' or computer_language == 'english' or computer_language == u'英文' or computer_language == u'英语':
		printLightRed("This is a light red text.")
		printYellow("This is a yellow text.")
		printRed("This is a red text.")
		printGreen("This is a green text.")
		printBlack("This is a black text.")
		printBlue("This is a blue text.")
		printPurple("This is a purple text.")
		printWhite("This is a white text.")
		printGrey("This is a grey text.")
		printGray("This is a grey text too.")
		printLightBlue("This is a light blue text.")
		printVeryLightGreen("This is a very light green text.")
		printLightPurple("This is a light purple text.")
		printLightYellow("This is a light yellow text.")
		printGlossWhite("This is a gloss white text.")
		printLightGreen("This is a light green text.")
		printLightGreen("This is a light green text too.", 2)
	elif computer_language == 0x804 or computer_language == '0x804' or computer_language == 'Chinese' or computer_language == 'chinese' or computer_language == u'中文' or computer_language == u'汉语' or computer_language == u'普通话':
		printLightRed("这是一段浅红色的文字。")
		printYellow("这是一段黄色的文字。")
		printRed("这是一段红色的文字。")
		printGreen("这是一段绿色的文字。")
		printBlack("这是一段黑色的文字。")
		printBlue("这是一段蓝色的文字。")
		printPurple("这是一段紫色的文字。")
		printWhite("这是一段白色的文字。")
		printGrey("这是一段灰色的文字。")
		printGray("这也是一段灰色的文字。")
		printLightBlue("这是一段浅蓝色的文字。")
		printVeryLightGreen("这是一段很浅的绿色的文字。")
		printLightPurple("这是一段浅紫色的文字。")
		printLightYellow("这是一段浅黄色的文字。")
		printGlossWhite("这是一段亮白色的文字。")
		printLightGreen("这是一段浅绿色的文字。")
		printLightGreen("这也是一段浅绿色的文字。", 2)
	import time as t
	t.sleep(int(time_to_sleep))
	del t

# example()
