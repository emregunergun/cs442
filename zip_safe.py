"""
Illustrates how zip is stopping if one iterable is exhausted
without a warning and how to prevent it.
"""
import itertools


a = [1, 2, 3]
b = ["One", "Two"]

result1 = list(zip(a, b))
result2 = list(itertools.zip_longest(a, b))

print(result1)
print(result2)
