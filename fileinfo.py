#!/usr/bin/env python
import sys


def fileinfo(filepath, whitespace=" \t\v\f\r"):
    """
    Function counting lines, words and characters in a file with given path.
    :param filepath: path to the file, which contents are to be counted
    :param whitespace: set of whitespace characters
    :return: tuple containing number of lines, words and characters in file (in this order)
    """
    with open(filepath, "rt") as file:
        lines, words, chars = 0, 0, 0
        white = True
        while char := file.read(1):
            chars += 1                  # assuming we're counting all characters in file, not only non-whitespace ones
            if char == "\n":
                lines += 1
                if not white:
                    words += 1
                white = True
            elif char in whitespace:
                if not white:
                    words += 1
                white = True
            else:
                white = False
    return lines, words, chars


def file_count(path):
    """
    Function counting lines, words and characters in a file with given path.
    :param path: path to the file, which contents are to be counted
    :return: tuple containing number of lines, words and characters in file (in this order)
    """
    file = open(path, "rt", encoding="utf8")

    lines, words, chars = 0, 0, 0
    for line in file:
        lines += 1
        words += len(line.split())
        chars += len(line)

    file.close()
    return lines, words, chars


def main():
    assert len(sys.argv) == 2, f"USAGE: {sys.argv[0]} filepath"
    lines, words, chars = file_count(sys.argv[1])
    print(f"{sys.argv[1]}:\n\tLines: {lines}\n\tWords: {words}\n\tCharacters: {chars}")
    lines, words, chars = fileinfo(sys.argv[1])
    print(f"{sys.argv[1]}:\n\tLines: {lines}\n\tWords: {words}\n\tCharacters: {chars}")


if __name__ == "__main__":
    main()
