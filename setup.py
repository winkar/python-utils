PACKAGE = "utils"
NAME = "winkar_utils"
DESCRIPTION = "Util functions for python"
AUTHOR = "WinKaR"
AUTHOR_EMAIL = "winkar@163.com"
VERSION = __import__(PACKAGE).__version__

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst',format="md")
except ImportError:
    print("warning: pypandoc module not found, could not convert Markdown to RST")
    read_md = lambda f: open(f, 'r').read()

from setuptools import *



setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read_md("README.md"),
    install_requires=[],
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    packages=find_packages(exclude=["tests.*", "test"]),
    zip_safe=False,
)
