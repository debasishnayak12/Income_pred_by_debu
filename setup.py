from setuptools import find_packages,setup
from typing import List


setup(
    name="IncomePrediction",
    version="0.0.1",
    author="debasishnayak",
    author_email="nayakdebasish7205@gmail.com",
    install_requires=['scikit-learn',"pandas","numpy"],
    packages=find_packages()
)