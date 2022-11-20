def concatination(param):
    strings = ''
    for i in param:
        strings = strings + str(i)
    return strings


a = concatination([5, 7, 8, 9])
print(a)
