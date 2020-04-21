from os import path
from setuptools import setup


this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, "readme.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="nintendeals",
    version="0.1",
    url="https://github.com/federicocalendino/nintendeals",
    license="MIT",
    description="Scrapping tools for Nintendo games and prices on NA, EU and JP.",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Federico Calendino",
    author_email="federicocalendino@gmail.com",
    packages=["nintendeals"],
    install_requires=["unidecode"],
    keywords=[
        "nintendo",
        "eshop",
        "deals",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
