from setuptools import find_packages
from setuptools import setup

setup(
    name="dc_utils",
    version="0.0.1",
    description="Some useful uils for running\
          tests and managing small projects",
    author="Kostiantyn Gurianov",
    author_email="kostiantyn.gurianov@gmail.com",
    url="https://github.com/thenin-dailycoding/p-daily-coding.git",
    packages=find_packages(exclude=("tests*", "testing*")),
)
