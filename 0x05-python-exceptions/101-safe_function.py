#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        x = fct(*args)
        return x
    except Exception as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None
