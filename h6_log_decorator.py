def logger(func):
    def wrapper(*args, **kwargs):
        print(f'Name of function is {func.__name__}')
        if args or kwargs:
            if args:
                print(f'Arguments are {", ".join(str(arg) for arg in args)}')
            if kwargs:
                print(f'Keyword arguments are: {", ".join(str(key)+"="+str(value) for key, value in kwargs.items())}')
        else:
            print('There are no arguments')
    return wrapper


@logger
def test_func(*args, **kwargs):
    pass


if __name__ == '__main__':
    test_func(1, 4, 7, 'a', d=34, g=56)