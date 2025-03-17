from setuptools import setup, find_packages

setup(
    name='charsay',
    version='0.1.32',
    packages=find_packages(),
    author='Kishan S',
    author_email='senthilkumarkishan@gmail.com',
    description='A simple Python package that generates ASCII art of characters saying a given string.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/kish-0/charsay',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
