<div align="center">
  <img src="/logo.png" alt="Gutenberg books and dataset cleaner Python Package" width="250"/>
</div>

# gutenberg-cleaner
[![Downloads](https://static.pepy.tech/badge/gutenberg-cleaner)](https://pepy.tech/project/gutenberg-cleaner)
[![Downloads](https://static.pepy.tech/badge/gutenberg-cleaner/month)](https://pepy.tech/project/gutenberg-cleaner)

A Python package for cleaning Project Gutenberg books and datasets.

### Prerequisites
- nltk package

### Installing
```console
[sudo] pip install gutenberg-cleaner
```

## How to use it?

The package provides two main functions: "simple_cleaner" and "super_cleaner".
```python
from gutenberg_cleaner import simple_cleaner, super_cleaner
```
### simple_claner:
Removes lines that are part of the Project Gutenberg header or footer without altering the main text.
```python
simple_cleaner(book: str) -> str
```
### super_cleaner:
Performs a thorough cleaning of the book by removing titles, footnotes, images, book information, and other non-content elements. Note that it may happen to remove some valid content too (but rarely).
```python
super_cleaner(book: str, min_token: int = 5, max_token: int = 600) -> str
```
- `min_token`: The minimum number of tokens required for a non-dialog/non-quote paragraph to be retained. Set to -1 to skip tokenization (faster but less effective cleaning).
- `max_token`: The maximum number of tokens allowed for any paragraph.


Deleted paragraphs will be marked with: `[deleted]`


## Author

* **Peyman Mohseni kiasari**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
