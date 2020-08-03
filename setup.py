import setuptools

with open("README.md", "r",  encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="color_text",
    version="1.1.1",
    author="None",
    author_email=None,
    description="A library for printing colored text",
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
        "License :: OSI Approved :: MIT License",
    ],
)