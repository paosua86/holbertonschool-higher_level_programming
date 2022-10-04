#!/usr/bin/python3
"""
This is the "5-text_indentation" module.

The module contains one function, text_identation(text)
"""


def text_indentation(text):
    """"Write a function that prints a text with 2
    new lines after: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    flag = 0
    for i in text:
        if flag == 0:
            if i == " ":
                continue
            else:
                flag = 1
        if flag == 1:
            if i == "?" or i == ":" or i == ".":
                print(i)
                print()
                flag = 0
            else:
                print(i, end="")
