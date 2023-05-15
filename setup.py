#!/usr/bin/env python3

from setuptools import find_packages, setup

setup(
    name="simple-wer",
    version="0.1",
    py_modules=["simple_wer"],
    python_requires=">=3.6.0",
    description="A simple commandline tool to calculate WERs for ASR",
    author="Wei Kang",
    author_email="wkang.pku@gmail.com",
    license="Apache-2.0 License",
    url="https://github.com/pkufool/simple-wer",
    packages=find_packages(),
    install_requires=["kaldialign", "click>=6.7"],
    entry_points={
        "console_scripts": [
            "simple_wer = simple_wer.simple_wer_cli:cli",
        ],
    },
)
