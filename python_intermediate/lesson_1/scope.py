PI = 3.14
from dis import dis


def area(r):
    global PI
    PI = 4

    def again():
        a = 5
        b = 8
        print(locals())

    print(locals(), "area")
    again()
    return PI * r ** 2


print(dis(area))
