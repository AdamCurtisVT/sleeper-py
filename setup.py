import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sleeper_py",
    version="0.0.1-beta12",
    author="Adam Curtis",
    author_email="adamcurtisvt@gmail.com",
    description="A python implementation of the Sleeper.app API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AdamCurtisVT/sleeper-py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)