# symmetric difference project

def symmetric_difference(*args):
    if len(args) <= 1:
        return args

    a = args[0]
    b = args[1]

    x = [i for i in a if i not in b]
    y = [j for j in b if j not in a]

    sym = x + y
    for i in range(2, len(args)):
        x = [j for j in args[i] if j not in sym]
        y = [k for k in sym if k not in args[i]]
        sym = x + y

    sym = list(dict.fromkeys(sym))
    sym.sort()

    return sym


if __name__ == '__main__':
    sym = symmetric_difference([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1])
    print(sym)


