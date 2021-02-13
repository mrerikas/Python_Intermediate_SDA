tipai = [int, bool, str, float, list, tuple, set, dict]
immuatable = [int, bool, str, float, tuple]
mutable = [list, set, dict]


def recursive_replace(item):
    """
    >>> recursive_replace(1)
    1
    >>> recursive_replace(True)
    True
    >>> recursive_replace("abc")
    'abc'
    >>> recursive_replace(10.1)
    10.1
    >>> recursive_replace((1,2,3))
    (1, 2, 3)
    >>> recursive_replace([1,2,3])
    (1, 2, 3)
    >>> recursive_replace({1,2,3})
    (1, 2, 3)
    >>> recursive_replace({"a":1,"b":2})
    (('a', 1), ('b', 2))
    >>> recursive_replace([1,2,[3,4]])
    (1, 2, (3, 4))
    >>> recursive_replace({"a":1,"b":[1,2]})
    (('a', 1), ('b', (1, 2)))
    >>> recursive_replace((1,2,[2,3]))
    (1, 2, (2, 3))

    :param item:
    :return:
    """
    if isinstance(item, (list, set, tuple)):
        return tuple(recursive_replace(it) for it in item)
    elif isinstance(item, dict):
        return tuple(zip(item.keys(), map(recursive_replace, item.values())))
    return item

