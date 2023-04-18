def decorator(func):

    def warp(*args):
        a = 0
        for i in args:
            a += i
        a = a / len(args)
        print(a)
        func(*args)
    return warp


@decorator
def dz(*args):
    b = 0
    for i in args:
        b += i
    print(b)


dz(2, 2, 2)