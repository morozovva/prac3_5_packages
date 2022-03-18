import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prac3_5_packages",
    version="0.0.1",
    author="morozovva",
    author_email="morozovva6@mail.ru",
    description="My package",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/morozovva/prac3_5_packages",
    classifiers=[
     "Programming Language :: Python :: 3"
    ]
)