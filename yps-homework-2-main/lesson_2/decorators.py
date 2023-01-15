#!usr/penv/python
import time


# prints time of function execution
def timeit(func):
    def timed(*args, **kwargs):
        ts = time.time()
        result = func(*args, **kwargs)
        te = time.time()
        print('%r  %2.2f ms' % (func.__name__, (te - ts) * 1000))
        return result
    return timed


# multiplies by n values of resulting dictionary if ii is string
def strange_deco(n: int = 1):
    def _strange_deco(func):
        def __strange_deco(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, dict):
                for k, v in result.items():
                    if isinstance(v, str):
                        result[k] = n * v
            return result
        return __strange_deco
    return _strange_deco


@timeit
def f1(x):
    import math
    y = math.sqrt(x)
    return y


@timeit
@strange_deco(3)
def f2():
    d = {"x": "a", "b": 2}
    return d


if __name__ == '__main__':
    print("decorators check")
    y = f1(2)
    d = f2()
    print(d)
