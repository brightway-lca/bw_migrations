from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

requirements = ["stats_arrays", "bw2data", "pandas"]
test_requirements = ["pytest"]

v_temp = {}
with open("bw_migrations/version.py") as fp:
    exec(fp.read(), v_temp)
version = ".".join((str(x) for x in v_temp["version"]))


setup(
    name="bw_migrations",
    version=version,
    description="Migration data and utilities for Brightway IO and LCA in general",
    long_description=open(path.join(here, "README.md")).read(),
    long_description_content_type="text/markdown",
    url="https://github.com/brightway-lca/bw_migrations",
    author="Chris Mutel",
    author_email="cmutel@gmail.com",
    license="NewBSD 3-clause; LICENSE",
    package_data={'bw_migrations': ["data/*.json"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    packages=find_packages(exclude=["tests"]),
    install_requires=requirements,
    tests_require=requirements + test_requirements,
)
