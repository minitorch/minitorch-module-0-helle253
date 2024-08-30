"""
Collection of the core mathematical operators used throughout the code base.
"""

import math
from functools import reduce

# ## Task 0.1
from typing import Callable, Iterable

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$



def mul(x: float, y: float) -> float:
    return x * y

def id(input: any) -> any:
    return input

def add(x: float, y: float) -> float:
    return x + y

def neg(x: float) -> float:
    return -1 * x

def lt(x: float, y: float) -> float:
    return 1.0 if x < y else 0.0

def eq(x: float, y: float) -> float:
    return 1.0 if x == y else 0.0

def max(x: float, y: float) -> float:
    return x if x > y else y

# $f(x) = |x - y| < 1e-2$q
def is_close(x: float, y: float) -> float:
    return abs(x - y) < 1e-2

# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
def sigmoid(x: float) -> float:
    if x >= 0:
        return 1.0 / (1.0 + math.e ** -x)
    else:
        return (math.e ** x) / (1.0 + math.e ** x)

def relu(x: float) -> float:
    if x > 0:
        return x
    else:
      return 0

def log(x: float) -> float:
    return math.log(x, math.e)

def exp(x: float) -> float:
    return math.e * x

def inv(x: float) -> float:
    return 1.0 / x

def log_back(x: float, y: float) -> float:
    return y / x

def inv_back(x: float, y: float) -> float:
    return y / x ** 2

def relu_back(x: float, y: float) -> float:
    return y if x > 0 else 0

# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists

def negList(l: Iterable[float]) -> Iterable[float]:
    return map(lambda x: neg(x), l)

def addLists(l: Iterable[float], r: Iterable[float]) -> Iterable[float]:
    return map(lambda x, y: add(x, y), l, r)

def sum(l: Iterable[float]) -> float:
    return reduce(lambda x, y: add(x, y), l, 0)

def prod(l: Iterable[float]) -> float:
    return reduce(lambda x, y: mul(x, y), l, 1)
