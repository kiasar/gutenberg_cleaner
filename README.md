<div align="center">
  <img src="/logo.png" alt="Gutenberg books and dataset cleaner Python Package" width="250"/>
</div>

# gutenberg-cleaner
[![Downloads](https://static.pepy.tech/badge/gutenberg-cleaner)](https://pepy.tech/project/gutenberg-cleaner)
[![Downloads](https://static.pepy.tech/badge/gutenberg-cleaner/month)](https://pepy.tech/project/gutenberg-cleaner)

A python package for cleaning Gutenberg books and dataset.

### Prerequisites
nltk package

### Installing
```
[sudo] pip install gutenberg-cleaner
```

## How to use it?

it has two methods called "simple_cleaner" and "super_cleaner".
```
from gutenberg_cleaner import simple_cleaner, super_cleaner
```
### simple_claner:
Just removes lines that are part of the Project Gutenberg header or footer.
Doesnt go deeply in the text to remove other things like titles or footnotes or etc...
```
simple_cleaner(book: str) -> str
```
### super_cleaner:
Super clean the book (titles, footnotes, images, book information, etc.). may delete some good lines too.
```
super_cleaner(book: str, min_token: int = 5, max_token: int = 600) -> str
```
min_token: The minimum tokens of a paragraph that is not "dialog" or "quote", -1 means don't tokenize the txt (so it will be faster, but less efficient cleaning).
max_token: The maximum tokens of a paragraph.

it will mark deleted paragraphs with: [deleted]


## Author

* **Peyman Mohseni kiasari**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
