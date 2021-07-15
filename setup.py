from setuptools import setup

print("-"*20, "This package is a W.I.P and currently does nothing. See the source here: https://github.com/XuaTheGrate/PyCurseForge", "-"*20, sep='\n')

#with open("requirements.txt") as f:
#    requirements = f.readlines()

version = "1.0.0a0"

with open("README.md") as f:
    readme = f.read()

setup(
    name='PyCurseForge',
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
        "Development Status :: 2 - Pre-Alpha",
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
