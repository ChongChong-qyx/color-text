import setuptools

with open("README.md", "r",  encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="color_text",
    version="1.1.3",
    author="None",
    author_email=None,
    description="A library for printing colored text.   这是一个用来打印彩色文字的库。",
    long_description=long_description,
    license='MIT',
    long_description_content_type="text/markdown",
    url=None,
    packages=['color_text', 'color_text/tests'],
    zip_safe=False,
    python_requires='==3.8.*',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "License :: OSI Approved :: MIT License"
    ],
    keywords=["color_text"]
)