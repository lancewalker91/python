def square(x):
    '''
    >>> square(2)
    4
    >>> square(4)
    16
    '''
    return x**2
if __name__ == '__main__':
    import doctest,doctest_my_path
    doctest.testmod(doctest_my_path)

