# color_text

This is a library for printing colored texts.

这是一个用来打印彩色文字的库。

## Note  注意

> Best use in Python 3.8.

> 最好在 Python 3.8 上使用。

> Please use on Windows operating system.

> 请在 Windows 操作系统上使用。

## Install  安装

```bash
pip3 install color_text
```

## Usage  使用方法

### Output   输出

#### 1.Print with a function that prints colored text  用打印彩色文字的函数打印文字

```python
from color_text import *

printLightRedText("This is a light red text.")
printYellowText("This is a yellow text.")
printRedText("This is a red text.")
printGreenText("This is a green text.")
printBlackText("This is a black text.")
printBlueText("This is a blue text.")
printPurpleText("This is a purple text.")
printWhiteText("This is a white text.")
printGreyText("This is a grey text.")
printGrayText("This is a grey text too.")
printLightBlueText("This is a light blue text.")
printVeryLightGreenText("This is a very light green text.")
printLightPurpleText("This is a light purple text.")
printLightYellowText("This is a light yellow text.")
printGlossWhiteText("This is a gloss white text.")
printLightGreenText("This is a light green text.")
printLightGreenText("This is a light green text too.", 2)

# You can see the result of this example in the library's output_example() function or by typing "color_text-example.cmd" in CMD after installing the library.
# 你可以在这个库的 output_example() 函数中或安装这个库后在 CMD 中输入"color_text-example.cmd"看到这个例子的结果。（如果计算机默认语言是中文的就会看到中文结果，函数的顺序是一样的）
```

Parameters of all functions that print only one color text: values, end (default is '\n')

所有只打印某一种彩色文字的函数的参数：values, end （默认值为'\n'）

#### 2.Print text with custom colors   打印带有自定义颜色的文本

```python
from color_text import *
printOtherColorText(values, text_color=FOREGROUND_WHITE, background_color=BACKGROUND_BLACK, end='\n')

# Note: Put the text_color parameter and background_color parameter in the last command to program the color variables you want. Please see the end of the tutorial for all color variables.
# 注意：清把上一个命令中的 text_color 参数和 background_color 参数编程你想要的颜色变量，所有颜色变量请看教程最后，values 参数是要打印的内容，end 参数是结尾，默认值为 '\n'。
# You can also use the Print() function with the same arguments and default values.
# 还可以用 Print() 函数，参数和上面一样，默认值也一样。
```

### Get input   获取输入

#### 1.Get input with a function that gets color input   用获取彩色输入的函数获取输入

##### All functions   所有函数

GetBlackInput()

GetBlueInput()

GetGlossWhiteInput()

GetGrayInput()

GetGreenInput()

GetGreyInput()

GetLightBlueInput()

GetLightGreenInput()

GetLightPurpleInput()

GetLightRedInput()

GetLightYellowInput()

GetPurpleInput()

GetRedInput()

GetVeryLightGreenInput()

GetWhiteInput()

GetYellowInput()

##### Parameters   参数

prompt

##### Parameters explain    参数说明

Prompt: The content used for prompt

prompt: 用于提示的内容

#### 2.Get input with a custom color   获取自定义颜色的输入
```python
from color_text import *
GetOtherColorInput(prompt='', text_color=FOREGROUND_WHITE, background_color=BACKGROUND_BLACK)

# Note: Put the text_color parameter and background_color parameter in the last command to program the color variables you want. See the end of the tutorial for all color variables.
# 注意：清把上一个命令中的 text_color 参数和 background_color 参数编程你想要的颜色变量，所有颜色变量请看教程最后，prompt 参数是用于提示的内容。
# You can also use the GetInput() function with the same arguments and default values as above.
# 还可以用 GetInput() 函数，参数和上面一样，默认值也一样。
```

### Set color   设置颜色
```python
from color_text import *

set_cmd_text_color(color, handle = std_out_handle)
resetColor(handle = std_out_handle)
```

The set_cmd_text_color () function is used to set the color of the text, where the color parameter is the color to be set and the handle parameter is the handle to the color to be set (the default is std_out_handle).

set_cmd_text_color() 函数使用来设置文本颜色的，其中 color 参数是要设定的颜色，handle 参数是被设定颜色的句柄（默认值为 std_out_handle）。

The resetColor() function is used to restore the color to its default value, where the handle parameter is the handle to the restored color (the default is std_out_handle).

resetColor() 函数是用来将颜色恢复到默认值的，其中 handle 参数是被恢复颜色的句柄（默认值为 std_out_handle）。

See the end of the tutorial for all handle variables.

所有句柄变量见教程最后。

## What's new in this version   这个版本中的新功能

- A Chinese example has been added in color_text-example.cmd.

- 在 color_text-example.cmd 中增加了中文例子。

## All color variables   所有颜色变量

### Text colors   文字颜色

FOREGROUND_BLACK

FOREGROUND_BLUE

FOREGROUND_GREEN

FOREGROUND_LIGHT_GREEN

FOREGROUND_RED

FOREGROUND_PURPLE

FOREGROUND_YELLOW

FOREGROUND_WHITE

FOREGROUND_GREY

FOREGROUND_LIGHT_BLUE

FOREGROUND_LIGHT_GREEN_TWO

FOREGROUND_VERY_LIGHT_GREEN

FOREGROUND_LIGHT_RED

FOREGROUND_LIGHT_PURPLE

FOREGROUND_LIGHT_YELLOW

FOREGROUND_GLOSS_WHITE

### Background colors   背景颜色

BACKGROUND_BLACK

BACKGROUND_BLUE

BACKGROUND_GREEN

BACKGROUND_LIGHT_GREEN

BACKGROUND_RED

BACKGROUND_PURPLE

BACKGROUND_YELLOW

BACKGROUND_WHITE

BACKGROUND_GREY

BACKGROUND_LIGHT_BLUE

BACKGROUND_LIGHT_GREEN_TWO

BACKGROUND_VERY_LIGHT_GREEN

BACKGROUND_LIGHT_RED

BACKGROUND_LIGHT_PURPLE

BACKGROUND_LIGHT_YELLOW

BACKGROUND_GLOSS_WHITE

## All handle variables   所有句柄变量

std_out_handle

std_error_handle

std_input_handle

## Update log   更新日志

### v1.0.0

First version.

第一个版本。

### v1.1.0

#### What's new in this version   这个版本中的新功能

- The tutorial is refined.

- 细化了教程。

### v1.1.1

#### What's new in this version   这个版本中的新功能

- The example() and Print() functions have been added.

- 增加了example() 函数和 Print() 函数。

### v1.1.2

#### What's new in this version   这个版本中的新功能

- Added version information.

- 增加了版本信息。

### v1.1.3

#### What's new in this version   这个版本中的新功能

- Added tutorials in built-in function help().

- 增加了内置函数 help() 中的教程。

### v3.1.2

#### What's new in this version 这个版本中的新功能

- Added the PrintOtherColorText() function for printing custom color text.

- 增加了用来打印自定义颜色的文字的 PrintOtherColorText() 函数。

- Added the ability to Print custom colored text to Print().

- 给 Print() 函数增加了打印自定义颜色的文字的功能。

- Error messages are printed when an incompatible operating system is encountered.

- 在遇到不兼容的操作系统时会打印错误信息。

- All functions that print colored text can be separated by commas like the built-in function print().

- 让所有打印有颜色的文字的函数都可以像内置函数 print() 一样将要打印的文字用逗号分开。

- Added a function to get input.

- 添加了获取输入的函数。

- Added detailed version information.

- 增加了详细的版本信息。

- Added the error screen buffer handle variable and the input screen buffer handle variable.

- 增加了错误屏幕缓冲区句柄的变量和输入屏幕缓冲区的句柄变量。

- The handle argument is added to the set_cmd_text_color() function and the resetColor() function.

- 在 set_cmd_text_color() 函数和 resetColor() 函数中添加了句柄参数。

- Added all_color variable to view all colors.

- 增加了用来查看所有颜色的 all_color 变量。

#### The problem to repair 问题修复

- Fixed a problem where the example() function had no output at some point.

- 解决了某些时候 example() 函数没有输出的问题。

- Fixed the problem of importing other libraries in some cases.

- 解决了某些情况下会导入一些其它库的问题。

- Fixed a problem in the tutorial.

- 修复了教程中的一个问题。

### v3.1.3

#### What's new in this version   这个版本中的新功能

- Added tutorials for each function in the built-in help() function.

- 增加了内置函数 help() 中每个函数的教程。

- Added update log.

- 增加了更新日志。

#### The problem to repair   问题修复

- Fixed a problem in the tutorial.

- 修复了教程中的一个问题。

### v3.1.4

#### What's new in this version   这个版本中的新功能

- Added refined information variables.

- 增加了细化的信息变量。

### v3.1.6

#### What's new in this version   这个版本中的新功能

- A Chinese example has been added in color_text-example.cmd.

- 在 color_text-example.cmd 中增加了中文例子。
