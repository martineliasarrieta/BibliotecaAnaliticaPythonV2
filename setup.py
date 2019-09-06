import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BibliotecaAnalitcaAlfa",
    version="0.2.0",
    author="martarto",
    author_email="mearrieta@sura.com.co",
    description="Contiene funciones para etl datalake y datawarehouse",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/martineliasarrieta/BibliotecaAnalitica_v2_alfa.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)