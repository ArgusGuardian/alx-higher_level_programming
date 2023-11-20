#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        x = fct(*args)
        return x
    except Exception as e:
        print("Excepton: {}".format(e), file=sys.stderr)
        return None
