#!/usr/bin/env python
import pathlib
from setuptools import setup
# from scriptforge_stubs import __version__
PKG_NAME = 'types-uno-script'
VERSION = "0.1.1"

# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
with open(HERE / "README.rst") as fh:
    README = fh.read()

setup(
    name=PKG_NAME,
    version=VERSION,
    url="https://github.com/Amourspirit/python-types-uno-script",
    packages=["uno", "unohelper"],
    package_data={
        "uno":["py.typed","__init__.pyi"],
        "unohelper":["py.typed","__init__.pyi"]
        },
    author=":Barry-Thomas-Paul: Moss",
    author_email='bigbytetech@gmail.com',
    license="Apache Software License",
    python_requires='>=3.7.0',
    keywords=['libreoffice', 'openoffice', 'typings', 'uno', 'ooouno', 'pyuno'],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Office/Business",
        "Typing :: Typed",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=[
        'typing_extensions>=3.7.4.3;python_version<"3.7"'
    ],
    description="Type annotations for LibreOffice UNO Script",
    long_description_content_type="text/x-rst",
    long_description=README
)