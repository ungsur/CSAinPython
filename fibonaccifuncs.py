from functools import lru_cache
from typing import Generator

def fib1(n):
    if n < 2:
        return n
    else:
        return fib1(n-2) + fib1(n-1)

def fib2(n):
    cache = {0:0,1:1}
    if n not in cache.keys():
       cache[n] = fib2(n-2) + fib2(n-1)
    return cache[n]

@lru_cache(maxsize=None)
def fib3(n):
    if n<2:
        return n
    return (fib3(n-2) + fib3(n-1))

def fib4(n):
    if n == 0:
        return 0
    last = 0
    next = 1
    for i in range(1,n):
        last, next = next, next + last
    return next

def fib5(n):
    yield 0
    if n > 0:
        yield 1
    last = 0
    next = 1
    for i in range(1,n):
        last, next = next, last + next
        yield next

def main():
    print(fib1(30))
    print(fib2(30))
    print(fib3(30))
    print(fib4(30))
    for i in (fib5(30)):
        print(i)
    
if __name__ == '__main__':
    main()