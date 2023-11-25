#!/usr/bin/python3
"""Function that processes text and prints formatted lines"""


def text_indentation(text):
    """Process text and print formatted lines.

    Args:
        text: The input text.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    cp_str = ""
    for i in text:
        alert = 0
        cp_str += i
        if i == '\n':
            cp_str = cp_str.strip()
            print(cp_str)
            cp_str = ""

        if i in ".?:":
            print(f"{cp_str.strip()}\n")
            cp_str = ""
            alert = 1
    if alert == 0 and not all(l == ' ' for l in cp_str):
        print(cp_str.strip())
