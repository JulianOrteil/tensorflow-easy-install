import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="tensorflow-easy-install",
    version="0.0.1",
    author="Julian_Orteil",
    description="Python module for stupidly easy Tensorflow installation.",
    long_description=long_description,
    long_description_conent_type="text/markdown",
    url="https://github.com/Julian_Orteil/tensorflow-easy-install",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows 10"
    ],
    python_requires=">=3.0"
)