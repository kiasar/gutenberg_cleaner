from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name="gutenberg_cleaner",
    install_requires=['nltk'],
    version='0.1.3',
    description="cleans gutenberg dataset books",
    author_email='mohsenikiasari@ce.sharif.edu',
    packages=["_cleaning_options"],
    py_modules=["gutenberg_cleaner"],
    url="https://github.com/kiasar/gutenberg_cleaner",
    license='MIT',
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
)
