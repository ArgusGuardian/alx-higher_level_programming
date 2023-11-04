#!/usr/bin/python3
def multiple_returns(sentence):
    char = None
    if sentence:
        char = sentence[0]
    return len(sentence), char
