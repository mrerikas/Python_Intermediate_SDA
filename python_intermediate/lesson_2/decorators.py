def multiply_by(f=None, n=2):
    print(f, n)

    def wrapper():
        return f() * n

    def two_level(f):
        def wrapper():
            return f() * n

        return wrapper

    if f is None:
        return two_level
    return wrapper


@multiply_by(n=3)
def foo():
    return 2


foo()


@multiply_by
def foo():
    return 2


foo()


@multiply_by(n=10)
def foo():
    return 2


foo()


def foo():
    return 2


foo()

default = multiply_by(n=6)(foo)

default()
