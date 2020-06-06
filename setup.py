import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="superstructure-MultifokalHirn",  # Replace with your own username
    version="0.0.1",
    author="MultifokalHirn",
    author_email="MultifokalHirn@gmail.com",
    description="a tool for Erkenntnis through dialectical notetaking",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MultifokalHirn/superstructure",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
