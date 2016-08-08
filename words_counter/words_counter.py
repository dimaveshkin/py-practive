#!/usr/bin/env python
from urllib.request import urlopen
import sys


def fetch_words(url):
    """
    Fetch a list of words from URL.
    :param url:
        The url of a UTF-8 document
    :return:
        A list of strings containing the words from the document
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode("utf8").split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == "__main__":
    url = sys.argv[1]
    main(url)
