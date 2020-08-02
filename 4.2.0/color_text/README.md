# color_text

A library for printing colored text, getting colored input, changing Qt5 controls' colors.

一个用来打印彩色文字、获取彩色的输入、更改Qt5控件的颜色的库。

## Note  注意

> Best use in Python 3.8.

> 最好在 Python 3.8 上使用。

> If you want to use all functions in this package, please use on Windows operating system.

> 如果你想要使用这个库的所有功能，请在 Windows 操作系统上使用。

## Install  安装

### Linux

First execute the following command.

先执行以下命令：

```bash
pip3 --version
```

If there are no errors, pip has been installed.

如果没有错误，说明已经安装了 pip。

If there is an error, please execute the following command.

如果有错误，请输入以下命令以安装 pip：

```bash
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
```

If pip is already installed, execute the following command.

如果已经安装了 pip，请输入以下命令：

```bash
pip3 install color_text
```

If you want to use the features related to Qt5, execute the following command.

如果想使用有关 Qt5 的功能，请输入以下命令：

```bash
pip3 install PyQt5 PySide2
```

### Mac OS

First execute the following command.

先执行以下命令：

```bash
pip3 --version
```

If there are no errors, pip has been installed.

如果没有错误，说明已经安装了 pip。

If there is an error, please execute the following command.

如果有错误，请输入以下命令以安装 pip：

```bash
sudo easy_install pip
```

If pip is already installed, execute the following command.

如果已经安装了 pip，请输入以下命令：

```bash
pip3 install color_text
```

If you want to use the features related to Qt5, execute the following command.

如果想使用有关 Qt5 的功能，请输入以下命令：

```bash
pip3 install PyQt5 PySide2
```

### Windows

First execute the following command.

先执行以下命令：

```command prompt
pip3 --version
```

If there are no errors, pip has been installed.

如果没有错误，说明已经安装了 pip

If there is an error, please execute the following command.

如果有错误，请输入以下命令以安装 pip：

```command prompt
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
del /F /S /Q get-pip.py
```

If pip is already installed, execute the following command.

如果已经安装了 pip，请输入以下命令：

```command prompt
pip3 install color_text
```

If you want to use the features related to Qt5, execute the following command.

如果想使用有关 Qt5 的功能，请输入以下命令：

```command prompt
pip3 install PyQt5 PySide2
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
# 你可以在这个库的 output_example() 函数中看到这个例子的结果。（如果计算机默认语言是中文的就会看到中文结果，函数的顺序是一样的）
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

prompt: The content used for prompt

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

### 3.Set Consoles color   设置控制台颜色
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

### 4.Change the color of text of PyQt5 and PySide2 controls   更改 PyQt5 和 PySide2 的控件的文字的颜色

```python
from color_text.PyQt5_util import *

SetControlTextColor(control, color, controls="*)
```

In the above example, replace the control parameter with your control ,the color parameter with the color you want and replae the controls parameter with controls that you want to change color (Default value is "*").

在上面的例子中，请把 control 参数替换成你的控件，把 color 参数替换成你想要的颜色，把 controls 参数替换成你要更改颜色的控件（默认值为“*”）。

#### Method of writing color parameters   颜色参数的写法

##### 1.Use English words   使用英文单词

##### 2.Control the amount of primary colors   控制三原色的量

###### Method   写法

```python
rgb(red, green, blue)

# 注意：清把上面的 red、green、blue 参数替换成红色的量、绿色的量、蓝色的量
# Note: Replace the red, green and blue parameters with red, green and blue parameters.
```

#### How to write the "controls" parameter   controls 参数的写法

If you have many controls, use ", "to separate each control; if you have only one, write that control; if you want to change the text color of all controls, use" * ".

如果有很多控件，用“, ”把每一个控件分开，如果只有一个控件，那就写那个控件，如果要更改全部控件的文字颜色，用“*”。


### 5.Add image and text watermark to video   给视频添加图片、文字水印

#### Add a image watermark   添加图片水印

```python
from color_text import *

AddPhotoWatermarkToVideoFile(video_file, ouput_file, pos, photo_file, show_informations=False)
```

##### Parameters description 参数说明

###### video_file

The file to be watermarked.

要被添加水印的文件。

###### output_file

Output file.

输出文件。

###### pos

The watermark position.

水印方位

How to write it: (x-coordinate, y-coordinate)

写法：(x坐标, y坐标)

###### photo_file

Image file.

图片文件。

###### show_informations

Whether to display the information given by FFmpeg, default value is False.

是否显示由 FFmpeg 给出的信息，默认值为 False。

#### Add a text watermark   添加文字水印

```python
from color_text import *

AddTextWatermarkToVideoFile(video_file, output_file, pos, font_file, text, font_size, font_color, shadowy, show_informations=False)
```

##### Parameters description 参数说明

###### video_file

The file to be watermarked.

要被添加水印的文件。

###### output_file

Output file.

输出文件。

###### pos

The watermark position.

水印方位

How to write it: (x-coordinate, y-coordinate)

写法：(x坐标, y坐标)

###### font_file

Font file.

字体文件。

###### text

Text in watermarks.

水印中的文字。

###### font_size

Font size.

文字大小。

###### font_color

Font color.

文字颜色。

###### shadowy

Shadow portion size.

阴影部分大小。

###### show_informations

Whether to display the information given by FFmpeg, default value is False.

是否显示由 FFmpeg 给出的信息，默认值为 False。

#### Add many watermarks   添加大量水印

```python
from color_text import *

AddWatermarksToVideoFile(video_file, output_file, show_informations=False, *args)
```

Replace video_file in the above code with your video file, output_file with the output file, show_informations with True (you want FFmpeg for the information) or False (you don't want FFmpeg for the information, which is also the default), and args with multiple dictionaries (separated by ", ").

请将上面代码中的 video_file 替换成你的视频文件，将 output_file 替换输出文件，show_informations 替换成 True（你想要 FFmpeg 提供的信息）或 False（你不想要 FFmpeg 提供的信息，也是默认值），将 args 替换为多个字典（用“, ” 分隔）。

##### args 参数的写法

###### Text watermark   文字水印

{type: "photo", parameter: parameter}

{type: "text", 参数: 参数}

Note: please replace the above "parameter" with your parameters. See the article above for all parameters.

注意：清把上面的“参数”替换成你的参数，所有参数见上面的文章。

###### Image watermark   图片水印

{type: "photo", parameter: parameter}

{type: "photo", 参数: 参数}

Note: please replace the above "parameter" with your parameters. See the article above for all parameters.

注意：清把上面的“参数”替换成你的参数，所有参数见上面的文章。

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

## Examples 示例

### Note 注意

> Examples of this library can only run on Windows systems.

> 这个库的示例只能在 Windows 系统中运行。

If you want to run a print text example of this library, install the library and enter the following command at CMD.

如果要运行这个库的打印文字的示例，请安装本库，并在 CMD 输入以下命令：

```command prompt
color_text-output_example
```

If you want to run a get input example of this library, install the library and enter the following command at CMD.

如果要运行这个库的获取输入的示例，请安装本库，并在 CMD 输入以下命令：

```command prompt
color_text-get_input_example
```

If you want to run all the examples of this library, install the library and enter the following command at CMD.

如果要运行这个库的所有示例，请安装本库，并在 CMD 输入以下命令：

```command prompt
color_text-examples
```

## What's new in this version   这个版本中的新功能

- Added functions for adding image and text watermarks to videos.

- 增加了给视频添加图片、文字水印的功能。

## Repaired problems 问题修复

- Fixed an issue where the example could not run in some cases.

- 修复了在某些情况下无法运行示例的问题。

- Fixed some bugs.

- 修复了若干个 bug。

- Fixed an issue where the modules could not import in some cases.

- 修复了在某些情况下无法导入模块的问题。

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

- 增加了 example() 函数和 Print() 函数。

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

#### Repaired problems 问题修复

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

#### Repaired problems   问题修复

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

### v3.1.7

#### What's new in this version   这个版本中的新功能

- The help Markdown file, help HTML file, and help Word file have been added to the package.

- 在包中增加了帮助 Markdown 文件、帮助 HTML 文件和帮助 Word 文件。

### v3.1.8

#### What's new in this version   这个版本中的新功能

- Improved HTML tutorials in the package.

- 改进了包中的 HTML 教程。

- Added function to open tutorials directly in package.

- 增加了直接打开包中的教程的函数。

### v4.0.0

#### What's new in this version   这个版本中的新功能

- Functions that change controls of PyQt5 and PySide2 had been added.

- 增加了更改 PyQt5 和 Pyside2 的控件的函数。

### 4.0.1

#### What's new in this version   这个版本中的新功能

- Optimized the part of the installation library in the tutorial.

- 优化了教程中安装库的部分。

- Added a large number of examples.

- 增加了大量示例。

- Optimized the project description in PyPI.

- 优化了 PyPI 中的项目描述。

#### Repaired problems 问题修复

- Fixed several bugs in this tutorial.

- 修复了教程中的若干个 bug。

- Fixed a number of bugs encountered on Linux.

- 修复了在 Linux 系统中会遇到的若干个 bug。

### 4.1.0

#### What's new in this version   这个版本中的新功能

- Added the ability to select some small Qt5 control to change the text color when changing the text color of a large Qt5 control.

- 增加了更改大 Qt5 控件的文字颜色时，选择要更改文字颜色的小 Qt5 控件的功能。

- Added 3 EXE examples.

- 增加了 3 个 EXE 示例。

#### Repaired problems 问题修复

- Fixed a syntax error in the tutorial.

- 修复了教程中的一个语法错误。

- Fixed an issue where modules related to Qt5 could not be imported in some cases.

- 修复了在某些情况下无法导入有关 Qt5 的模块的问题。

- Fixed a problem that is other QSS failures after changing the text color of the Qt5 control.

- 修复了更改 Qt5 控件的文字颜色后，其它 QSS 失效的问题。

### 4.2.0

#### What's new in this version   这个版本中的新功能

- Added functions for adding image and text watermarks to videos.

- 增加了给视频添加图片、文字水印的功能。

#### Repaired problems 问题修复

- Fixed an issue where the example could not run in some cases.

- 修复了在某些情况下无法运行示例的问题。

- Fixed some bugs.

- 修复了若干个 bug。

- Fixed an issue where the modules could not import in some cases.

- 修复了在某些情况下无法导入模块的问题。
