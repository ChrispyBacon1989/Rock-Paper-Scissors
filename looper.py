# Looper module
def loop_print(arg1, arg2):
# print series between arg1 and arg2
    """Print a series of numbers."""
    while arg1 < arg2:
        print(arg1, end=' ')
        arg1 +=1

def loop_store(arg1, arg2):
# return series between arg1 and arg2
    """Return a series of numbers"""
    result = []
    while arg1 < arg2:
        result.append(arg1)
        # see below
        arg1 +=1
    return result