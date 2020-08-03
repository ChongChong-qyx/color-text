import setuptools

with open("README.md", "r", encoding = "utf-8") as file_object:
	long_description = file_object.read()

setuptools.setup(
	name = "color_text",
	version = "4.0.1",
	author = "A Chinese that likes programming   一个热爱编程的中国人",
	author_email = "colortextpackage@yandex.com",
	description = "A library for printing colored text, getting colored input, changing Qt5 controls' colors.   一个用来打印彩色文字、获取彩色的输入、更改Qt5控件的颜色的库。",
	long_description = long_description,
	license = "MIT",
	long_description_content_type = "text/markdown",
	url = None,
	packages = ["color_text", "color_text/doc"],
	zip_safe = False,
	python_requires = ">=3.0, !=3.9.*, <4.0",
	data_files = [(
		"Lib/site-packages/color_text/doc",
		["color_text/doc/help.doc",
		"color_text/doc/help.docx",
		"color_text/doc/help.md",
		"color_text/doc/help.mhtml",
		"color_text/doc/help.odt",
		"color_text/doc/help.pdf",
		"color_text/doc/help.rtf",
		"color_text/doc/help.xml",
		"color_text/doc/help.xps"]
		)],
	classifiers = [
		"Intended Audience :: Developers",
		"Programming Language :: Python",
		"Programming Language :: Python :: Implementation :: CPython",
		"Programming Language :: Python :: 3.8",
		"Operating System :: Microsoft :: Windows",
		"License :: OSI Approved :: MIT License",
		"Environment :: Win32 (MS Windows)",
	],
	keywords = ["color_text", "color text", "colour_text", "colour text", "彩色文字", "有颜色的文字", "颜色文字",
		"彩色文本", "有颜色的文本", "颜色文本", "color_words", "color words", "colour_words", "colour words", "color_word",
		"color word", "colour_word", "colour word"],
	platforms = ["Windows"],
	scripts = [
		"color_text-examples.cmd",
		"color_text-examples.py",
		"color_text-examples.ps1"
	],
)
