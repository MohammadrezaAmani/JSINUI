from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


VERSION = "0.0.1"

PACKAGE_NAME = "JSINUI"
DESCRIPTION = ""
LONG_DESCRIPTION = "Python to Javascript Compiler"
AUTHOR_NAME = "Mohammadreza Amani"
AUTHOR_EMAIL = "more.amani@yahoo.com"
PROJECT_URL = "https://github.com/MohammadrezaAmani/JSINUI/"
REQUIRED_PACKAGES = []
PROJECT_KEYWORDS = ["ui", "python", "javascript", "framework", "frontend"]

CLASSIFIERS = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3",
]
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    url=PROJECT_URL,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    keywords=PROJECT_KEYWORDS,
    classifiers=CLASSIFIERS,
)
