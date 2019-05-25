from gutenberg_cleaning_options.cleaning_options import is_title_or_etc, is_books_copy, is_email_init, is_footnote, \
    is_image, is_table
from gutenberg_cleaning_options.strip_headers import strip_headers


def simple_cleaner(book: str) -> str:
    """
    Just removes lines that are part of the Project Gutenberg header or footer.
    Doesnt go deeply in the text to remove other things like titles or footnotes or etc...
    :rtype: str
    :param book: str of a gutenberg's book
    :return: str of the book without the lines that are part of the Project Gutenberg header or footer.
    """
    return strip_headers(book)


def super_cleaner(book: str, min_token: int = 5, max_token: int = 600) -> str:
    """
    Super clean the book (titles, footnotes, images, book information, etc.). may delete some good lines too.
    ^_^ Do you have a comment to make it better? Email to mohsenikiasari@ce.sharif.edu ^_^.
    IMPORTANT: if you don't want the text to be tokenize, just put min_token = -1.
    :rtype: str
    :param book: str of a gutenberg's book.
    :param min_token: The minimum tokens of a paragraph that is not "dialog" or "quote",
     -1 means don't tokenize the txt (so it will be faster).
    :param max_token: The maximum tokens of a paragraph.
    :return: str of the book with paragraphs that have been deleted are shown with "[deleted]" in it.
    you can split the book to paragraphs by "\n\n".
    """
    headless_book = strip_headers(book)
    paragraphs = headless_book.split("\n\n")  # split the book to paragraphs.

    paragraphs_after_cleaning = []
    for par in paragraphs:
        if is_image(par) or is_footnote(par) or is_email_init(par) or \
                is_books_copy(par) or is_table(par) or is_title_or_etc(par, min_token, max_token):
            paragraphs_after_cleaning.append("[deleted]")  # if the paragraph is not good , replace it with [deleted]
        else:
            paragraphs_after_cleaning.append(par)

    cleaned_book = "\n\n".join(paragraphs_after_cleaning)  # joining the list of paragraphs into one string
    return cleaned_book
