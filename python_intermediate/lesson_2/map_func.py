# map() function

listofnames = ['erikas', 'sigita', 'karolina']
listofnums = [1, 2, 3, 4, 5]


def capitalize(item):
    return item.capitalize()


def multiplyby2(num):
    return num * 2


print(list(map(capitalize, listofnames)))
print('================================')
print(list(map(multiplyby2, listofnums)))
print('================================')
print(list(map(lambda x: x * 2, listofnums)))
