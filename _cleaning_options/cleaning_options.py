import string
import re
from nltk import word_tokenize

email_regex = re.compile("[\w.-]+@[\w.-]+\.\w+")  # Regex to find Emails.
footnote_notation_regex = re.compile("^\{.+\}|^\[.+\]")  # Regex to find start of footnotes.
number_of_copies_regex = re.compile("[0-9]* copies|copyright")  # Regex to find copy mentioning.
starts_with_regex = re.compile('^[%_<>*]')  # If the text is started with these, it is not a good one.
image_formats_regex = re.compile("\.png|\.jpg|\.jpeg|\.gif|picture:")  # Regex to find images.


def _is_title_or_etc(text: str, min_token: int = 5, max_token: int = 600) -> bool:
    """
    determining if a paragraph is title or information of the book.
    IMPORTANT: if you don't want the text to be tokenize, just put min_token = -1.
    :rtype: bool
    :param text: Raw paragraph.
    :param min_token: The minimum tokens of a paragraph that is not "dialog" or "quote",
     -1 means don't tokenize the txt (so it will be faster).
    :param max_token: The maximum tokens of a paragraph.
    :return: Boolean, True if it is title or information of the book or a bad paragraph.
    """
    txt = text.strip()
    num_token = len(word_tokenize(txt)) if min_token >= 0 else -1
    if num_token > max_token:
        return True
    if len(txt) == 0 or num_token < min_token and not (txt.count('"') == 2 or txt.count('\'') == 2 or txt[-1] == ":"):
        return True  # Length is short but not "dialog" or "quote"
    if sum(1 for c in txt if c.isupper() or c.isdigit() or c in string.punctuation.replace("\"", "")) \
            / len(txt.replace(" ", "")) > 0.6:
        return True  # More than 60% of chars are UPPER or digits or punctuations so it might be title or etc.
    if txt.lower().startswith("appendix") or bool(re.search(starts_with_regex, txt)):
        return True
    if txt.count(":") > 3 and 2 * txt.count(":") - txt.count("\"") > 3:
        return True  # mostly information about the book.
    if ("@" in txt and len(txt) < 100) or ('printed in' in txt.lower() and len(txt) < 200) or "inc." in txt.lower() \
            or ('original title' in txt.lower() and len(txt) < 200):
        return True
    return False


def _is_table(text: str) -> bool:
    """
    determining if a paragraph is a table or catalog.
    :rtype: bool
    :param text: Raw paragraph.
    :return:  Boolean, True if it is a table or catalog.
    """
    txt = text.strip()
    if txt.count("   ") > 3 or txt.count("\t") > 2:
        txt = " ".join([line.strip() for line in txt.split("\n")])
        if txt.count("   ") > 3 or txt.count("\t") > 2:
            return True  # mostly tables.
    if txt.count("*") > 3 or txt.count("=") > 2:
        return True  # mostly catalogs and etc.


def _is_image(text: str) -> bool:
    """
    determining if a paragraph is for mentioning an image.
    :param text: Raw paragraph.
    :return: Boolean, True if it is for mentioning an image.
    """
    return bool(re.search(image_formats_regex, text.lower()))


def _is_footnote(text: str) -> bool:
    """
    determining if a paragraph is the footnote of the book.
    :rtype: bool
    :param text: Raw paragraph.
    :return: Boolean, True if it is the footnote of the book.
    """
    txt = text.strip()
    if "footnote" in txt.lower() and len(txt.replace(" ", "")) < 50:
        return True
    return bool(re.search(footnote_notation_regex, txt))  # if a line starts with {...} it might be a footnote.


def _is_books_copy(text: str) -> bool:
    """
    determining if a paragraph indicates the number of copies of this book.
    :rtype: bool
    :param text: text: Raw paragraph.
    :return: Boolean, True if it is indicating the copy of book or copyrights.
    """
    if bool(re.search(number_of_copies_regex, text)) and len(text.replace(" ", "")) < 500:
        return True
    return False


def _is_email_init(text: str) -> bool:
    """
    determining if a paragraph includes an Email.
    :rtype: bool
    :param text: Raw paragraph.
    :return: Boolean, True if it includes an Email.
    """
    return bool(re.search(email_regex, text))
