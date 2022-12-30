#!/usr/bin/env python
from setuptools import dist
dist.Distribution().fetch_build_eggs(['setuptools_rust'])
from setuptools import setup
from setuptools_rust import Binding, RustExtension


setup(
    name="fib-crust",
    version="0.1",
    rust_extensions=[RustExtension(
        ".fib_crust.fib_crust",
        path="Cargo.toml", binding=Binding.PyO3)],
    packages=["fib_crust"],
    classifiers=[
            "License :: OSI Approved :: GNU General Public License v3",
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Programming Language :: Python",
            "Programming Language :: Rust",
            "Operating System :: POSIX",
            "Operating System :: MacOS :: MacOS X",
        ],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'fib-number = fib_crust.'
            'fib_number_command:'
            'fib_number_command',
        ],
    },
    # requirements=[
    #     "pyyaml>=3.13",
    #     "numpy"
    # ]
)
