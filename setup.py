from setuptools import setup, find_packages
import sys

if sys.version_info[0] != 3:
    sys.exit("This is a python3 only package.")
  
setup(  
    name = "pic_dl",
    version = "0.2.0",
    keywords = ("picture", "download"),
    description = "A simple downloader for many sites.",
    license = "MIT License",
    install_requires = [],
    requires = ["requests"],

    author = "yk",
    author_email = "yk@archlinuxcn.org",

    packages = ["pic_dl", "pic_dl.extractor"],
    package_dir = {"pic_dl": "pic_dl"},
    platforms = "any",
    entry_points = {"console_scripts": ["pic-dl = pic_dl.main:main"]}
)  

