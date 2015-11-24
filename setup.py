PACKAGE = "utils"
NAME = "winkar_utils"
DESCRIPTION = "Util functions for python"
AUTHOR = "WinKaR"
AUTHOR_EMAIL = "winkar@163.com"
VERSION = __import__(PACKAGE).__version__

from setuptools import *

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=open("README.md").read(),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="BSD",
    packages=find_packages(exclude=["tests.*", "test"]),
    zip_safe=False,
)
