import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="superstructure-cli",
    version="0.0.1",
    author="MultifokalHirn",
    author_email="lennardwolf@live.de",
    description="a tool for dialectics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MultifokalHirn/superstructure",
    packages=setuptools.find_packages(),
    install_requires=["Click", "flexible-dotdict", "dill", "sortedcontainers"],
    py_modules=["superstructure"],
    classifiers=[
        # Classifiers: https://pypi.org/classifiers/
        "Development Status :: 1 - Planning",
        "Intended Audience :: Other Audience",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="hegel dialectics",
    python_requires=">=3.7",
    entry_points={"console_scripts": ["superstructure-cli=superstructure:cli",],},
)
