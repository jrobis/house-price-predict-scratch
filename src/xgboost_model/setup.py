import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # name="xgboost-model-pkg-jarsushi", # Replace with your own username
    name="xgboost_model",
    version="0.1.0",
    author="Joshua Robison",
    author_email="joshua.robison.a@gmail.com",
    description="A small xgboost model package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jarsushi/house-price-predict-scratch/tree/master/src/xgboost_model",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
