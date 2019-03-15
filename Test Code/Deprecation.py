def deprecated(func):
    """Print a deprecation warning once on first use of the function.

    >>> @deprecated                      # doctest: +SKIP
    ... def f():
    ...     pass
    >>> f()                              # doctest: +SKIP
    f is deprecated
    """
    count = [0]
    def wrapper(*args, **kwargs):
        count[0] += 1
        if count[0] == 1:
            print (func.__name__, 'is deprecated') 
        return func(*args, **kwargs)
    return wrapper

@deprecated
def test(a,b,test1=2,test2=5):
    print ("pass")

test(1,2,3,4)
test(2,3,4,5)