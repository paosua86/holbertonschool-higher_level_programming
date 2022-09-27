#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        a = fct(*args)
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        a = None
    return a
