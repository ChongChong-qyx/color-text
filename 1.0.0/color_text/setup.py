import setuptools

with open("README.md", "r",  encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="color_text",
    version="1.0.0",
    author="None",
    author_email=None,
    description="A package for printing colored text",
    long_description=long_description,
    license='MIT',
    long_description_content_type="text/markdown",
    url=None,
    packages=['color_text'],
    zip_safe=False,
    python_requires='==3.8.*',
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
)