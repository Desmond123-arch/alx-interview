#!/usr/bin/python3
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

def combination(n, r):
    return int((factorial(n)) /
               ((factorial(r)) * factorial(n - r)))


def pascal_triangle(rows):
    result = []
    for count in range(rows):
        row = []
        for element in range(count + 1):
            row.append(combination(count, element))
        result.append(row)
    return result
