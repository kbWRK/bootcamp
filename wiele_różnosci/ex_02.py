def my_enumerate(s):
    index = 0
    for lmt in s:
        yield (index, lmt)
        index += 1


