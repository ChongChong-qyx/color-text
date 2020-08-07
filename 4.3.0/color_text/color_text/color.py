"""
All color variables.
所有颜色变量。
"""

from platform import system

if system() == 'Windows':
	del system

	FOREGROUND_BLACK =             0x00 # black
	FOREGROUND_BLUE =              0x01 # blue
	FOREGROUND_GREEN =             0x02 # green
	FOREGROUND_LIGHT_GREEN =       0x03 # light_green
	FOREGROUND_RED =               0x04 # red
	FOREGROUND_PURPLE =            0x05 # purple
	FOREGROUND_YELLOW =            0x06 # yellow
	FOREGROUND_WHITE =             0x07 # white
	FOREGROUND_GREY =              0x08 # grey
	FOREGROUND_LIGHT_BLUE =        0x09 # light_blue
	FOREGROUND_LIGHT_GREEN_TWO =   0x0a # another_light_green
	FOREGROUND_VERY_LIGHT_GREEN =  0x0b # very_light_green
	FOREGROUND_LIGHT_RED =         0x0c # light_red
	FOREGROUND_LIGHT_PURPLE =      0x0d # light_purple
	FOREGROUND_LIGHT_YELLOW =      0x0e # light_yellow
	FOREGROUND_GLOSS_WHITE =       0x0f # gloss_white

	BACKGROUND_BLACK =             0x00 # balck
	BACKGROUND_BLUE =              0x10 # blue
	BACKGROUND_GREEN =             0x20 # green
	BACKGROUND_LIGHT_GREEN =       0x30 # light_green
	BACKGROUND_RED =               0x40 # red
	BACKGROUND_PURPLE =            0x50 # purple
	BACKGROUND_YELLOW =            0x60 # yellow
	BACKGROUND_WHITE =             0x70 # white
	BACKGROUND_GREY =              0x80 # grey
	BACKGROUND_LIGHT_BLUE =        0x90 # light_blue
	BACKGROUND_LIGHT_GREEN_TWO =   0xa0 # another_light_green
	BACKGROUND_VERY_LIGHT_GREEN =  0xb0 # very_light_green
	BACKGROUND_LIGHT_RED =         0xc0 # light_red
	BACKGROUND_LIGHT_PURPLE =      0xd0 # light_purple
	BACKGROUND_LIGHT_YELLOW =      0xe0 # light_yellow
	BACKGROUND_GLOSS_WHITE =       0xf0 # gloss_white

	ALL_TEXT_FOREGROUND_BLACK =            '0' # black
	ALL_TEXT_FOREGROUND_BLUE =             '1' # blue
	ALL_TEXT_FOREGROUND_GREEN =            '2' # green
	ALL_TEXT_FOREGROUND_LIGHT_GREEN =      '3' # light_green
	ALL_TEXT_FOREGROUND_RED =              '4' # red
	ALL_TEXT_FOREGROUND_PURPLE =           '5' # purple
	ALL_TEXT_FOREGROUND_YELLOW =           '6' # yellow
	ALL_TEXT_FOREGROUND_WHITE =            '7' # white
	ALL_TEXT_FOREGROUND_GREY =             '8' # grey
	ALL_TEXT_FOREGROUND_LIGHT_BLUE =       '9' # light_blue
	ALL_TEXT_FOREGROUND_LIGHT_GREEN_TWO =  'A' # another_light_green
	ALL_TEXT_FOREGROUND_VERY_LIGHT_GREEN = 'B' # very_light_green
	ALL_TEXT_FOREGROUND_LIGHT_RED =        'C' # light_red
	ALL_TEXT_FOREGROUND_LIGHT_PURPLE =     'D' # light_purple
	ALL_TEXT_FOREGROUND_LIGHT_YELLOW =     'E' # light_yellow
	ALL_TEXT_FOREGROUND_GLOSS_WHITE =      'F' # gloss_white

	ALL_TEXT_BACKGROUND_BLACK =            '0' # black
	ALL_TEXT_BACKGROUND_BLUE =             '1' # blue
	ALL_TEXT_BACKGROUND_GREEN =            '2' # green
	ALL_TEXT_BACKGROUND_LIGHT_GREEN =      '3' # light_green
	ALL_TEXT_BACKGROUND_RED =              '4' # red
	ALL_TEXT_BACKGROUND_PURPLE =           '5' # purple
	ALL_TEXT_BACKGROUND_YELLOW =           '6' # yellow
	ALL_TEXT_BACKGROUND_WHITE =            '7' # white
	ALL_TEXT_BACKGROUND_GREY =             '8' # grey
	ALL_TEXT_BACKGROUND_LIGHT_BLUE =       '9' # light_blue
	ALL_TEXT_BACKGROUND_LIGHT_GREEN_TWO =  'A' # another_light_green
	ALL_TEXT_BACKGROUND_VERY_LIGHT_GREEN = 'B' # very_light_green
	ALL_TEXT_BACKGROUND_LIGHT_RED =        'C' # light_red
	ALL_TEXT_BACKGROUND_LIGHT_PURPLE =     'D' # light_purple
	ALL_TEXT_BACKGROUND_LIGHT_YELLOW =     'E' # light_yellow
	ALL_TEXT_BACKGROUND_GLOSS_WHITE =      'F' # gloss_white

else:
	del system
