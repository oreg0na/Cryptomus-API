from setuptools import setup, find_packages
from io import open


def read(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

setup()
