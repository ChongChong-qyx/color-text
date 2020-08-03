import setuptools

with open("README.md", "r", encoding = "utf-8") as file_object:
	long_description = file_object.read()

setuptools.setup(
	name = "color_text",
	version = "3.1.7",
	author = "A Chinese working in FJA   一个在FJA工作的中国人",
	author_email = "colortextpackage@yandex.com",
	description = "A library for printing colored text.   一个用来打印彩色文字的库。",
	long_description = long_description,
	license = "MIT",
	long_description_content_type = "text/markdown",
	url = None,
	packages = ["color_text"],
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
		"License :: OSI Approved :: MIT License"
	],
	keywords = ["color_text", "color text", "colour_text", "colour text", "彩色文字", "有颜色的文字", "颜色文字",
		"彩色文本", "有颜色的文本", "颜色文本", "color_words", "color words", "colour_words", "colour words", "color_word",
		"color word", "colour_word", "colour word"],
	platforms = ["Windows"],
	scripts = ["color_text-example.cmd"]
)
