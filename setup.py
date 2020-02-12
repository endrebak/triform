import sys
from setuptools import setup, find_packages


__version__ = open("triform2/version.py").readline().split(" = ")[1].replace(
    '"', '').strip()

install_requires = ["pyranges"]

setup(
    name="triform2",
    packages=find_packages(),
    # package_dir=find_packages(),
    # package_data={"triform2": ["scripts/chromsizes/*.chromsizes"]},
    scripts=["bin/triform2"],
    version=__version__,
    description=
    "Improved sensitivity, specificity and control of false discovery rates in ChIP-Seq peak finding.",
    author="Endre Bakken Stovner",
    author_email="endrebak85@gmail.com",
    url="http://github.com/endrebak/triform2",
    keywords=["ChIP-Seq"],
    license=["MIT"],
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Other Environment", "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Topic :: Scientific/Engineering"
    ],
    long_description=
    "Improved sensitivity, specificity and control of false discovery rates in ChIP-Seq peak finding.")
