from setuptools import setup, find_packages
import setuptools


    
VERSION = '0.3.0'
DESCRIPTION = 'Vinted API wrapper for python'

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="pyVinted",
    version=VERSION,
    author="Aimé Risson",
    author_email="aime.risson.1@gmail.fr",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    install_requires=['requests'], 
    keywords=['python', 'Vinted api', 'Vinted API wrapper', 'python vinted'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Education",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    url = "https://github.com/aime-risson/vinted-api-wrapper"
)