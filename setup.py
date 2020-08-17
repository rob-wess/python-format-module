import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="format-pkg-ROB-WESS",
    version="0.0.1",
    author="Robert E. Wessinger III",
    author_email="robert.wessinger@outlook.com",
    description="A small package to help with formatting and error handling",
    url="https://github.com/rob-wess/python-format-module.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
