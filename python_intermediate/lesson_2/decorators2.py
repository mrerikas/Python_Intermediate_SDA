from time import time


def measure_time(f):
    def wrapper(*args, **kwargs):
        start = time()
        r = f(*args, **kwargs)
        print("Took time:", (time() - start))
        return r

    return wrapper


@measure_time
def suma(a, b, *args):
    return a + b + sum(args)


if __name__ == '__main__':
    print(suma(1, 4, 5, 8, 6, 6))
