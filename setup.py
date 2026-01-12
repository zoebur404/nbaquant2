from setuptools import setup, find_packages

setup(
    name="nba_quant",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "requests",
        "pydantic",
        "nba_api",
        "pyarrow"
    ],
)
