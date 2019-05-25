from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name="gutenberg_cleaner",
    install_requires=['nltk'],
    version='0.0.1',
    description="cleans gutenberg dataset books",
    author_email='mohsenikiasari@ce.sharif.edu',
    py_modules=["gutenbergـcleaner"],
    license='MIT',
    long_description=long_description,
    classifiers=[
        "Programming language :: Python :: 3",
        "Programming language :: Python :: 3.6",
        "Programming language :: Python :: 3.7",
        "Operation System :: OS Independent"
    ]
)
