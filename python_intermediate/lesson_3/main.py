def floors(start, my_string):
    """
    >>> floors(0, '(())')
    0
    >>> floors(0, ')())())')
    -3

    :param my_string:
    :return:
    """
    for i in my_string:
        if i == '(':
            start += 1
        elif i == ')':
            start -= 1
    return start


