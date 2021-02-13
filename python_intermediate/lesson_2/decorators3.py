"""
Noriu išsaugoti visus argumentus ir rezultatus kai įvyksta funkcija
"""
duomenys = {
    "funkcijos_pavadinimas": {
        "argumentai": "rezultatas"
    }
}
duomenys = {}


def log_arguments_and_results(f):
    def wrapper(*args, **kwargs):
        name = f.__name__
        r = f(*args, **kwargs)
        all_arguments = args + tuple(kwargs.items())
        if name in duomenys:
            duomenys[name][all_arguments] = r
        else:
            duomenys[name] = {all_arguments: r}
        return r

    return wrapper


@log_arguments_and_results
def suma(a, b, *args):
    return a + b + sum(args)


@log_arguments_and_results
def suma_su_daugikliu(a, b, *args, n=1):
    return (a + b + sum(args)) * n


@log_arguments_and_results
def add_lists(a, b):
    return a + b


if __name__ == '__main__':
    suma(1, 2)
    suma(1, 2)
    suma(5, 2, 48, 4, 5, 5, 6)
    suma_su_daugikliu(4, 8, 5)
    suma_su_daugikliu(4, 8, 5, n=2)
    add_lists([1, 2], [3, 4])
    print(duomenys)
