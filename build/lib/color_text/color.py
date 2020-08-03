#-*- coding:utf-8 -*-#

from platform import system

if system() == 'Windows':
	del system

	# 字体颜色定义 text colors
	FOREGROUND_BLACK =             0x00 # black                   a
	FOREGROUND_BLUE =              0x01 # blue                    a
	FOREGROUND_GREEN =             0x02 # green                   a
	FOREGROUND_LIGHT_GREEN =       0x03 # light_green             a
	FOREGROUND_RED =               0x04 # red                     a
	FOREGROUND_PURPLE =            0x05 # purple                  a
	FOREGROUND_YELLOW =            0x06 # yellow                  a
	FOREGROUND_WHITE =             0x07 # white                   a
	FOREGROUND_GREY =              0x08 # grey                    a
	FOREGROUND_LIGHT_BLUE =        0x09 # light_blue              a
	FOREGROUND_LIGHT_GREEN_TWO =   0x0a # another_light_green     a
	FOREGROUND_VERY_LIGHT_GREEN =  0x0b # very_light_green        a
	FOREGROUND_LIGHT_RED =         0x0c # light_red               a
	FOREGROUND_LIGHT_PURPLE =      0x0d # light_purple            a
	FOREGROUND_LIGHT_YELLOW =      0x0e # light_yellow            a
	FOREGROUND_GLOSS_WHITE =       0x0f # gloss_white             a

	# 背景颜色定义 background colors
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

else:
	del system
