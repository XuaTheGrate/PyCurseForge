from setuptools import setup

version = "1.0.0-3"

import os

with open("requirements.txt") as f:
    requires = f.readlines()

with open("README.md") as f:
    readme = f.read()

setup(
    name='PyCurseForge',
    install_requires=requires,
    author='XuaTheGrate',
    url='https://github.com/XuaTheGrate/PyCurseForge',
    version=version,
    packages=['curseforge'],
    license='MIT',
    description='A python wrapper for the (hidden) CurseForge API',
    long_description=readme,
    long_description_content_type='text/markdown',
    python_requires='>=3.8.0',
    classifiers=[
        "Development Status :: 5 - Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Games/Entertainment",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed"
    ]
)
