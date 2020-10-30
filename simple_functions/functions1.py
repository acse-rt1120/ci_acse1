from functools import lru_cache

__all__ = ['my_sum']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        from IPython import embed; embed()
        tot += i.data
    return tot
