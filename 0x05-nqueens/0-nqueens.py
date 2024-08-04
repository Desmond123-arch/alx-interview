#!/usr/bin/python3
""" Solve the nqueens problem """
from sys import argv
placedQueen = []
solution = []
N = argv[1]
if N is None:
    print("Usage: nqueens N")
    exit(1)
try:
    N = int(N)
except ValueError:
    print("N must be a Number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)


def solveNquens(row=0):
    if row == N:
        solution.append(placedQueen.copy())
    for col in range(N):
        if isSafe(row, col):
            placedQueen.append([row, col])
            solveNquens(row+1)
            placedQueen.pop()


def isSafe(row, col):
    for queen in placedQueen:
        if row == queen[0] or col == queen[1] or \
                row - col == queen[0] - queen[1] or\
                row + col == queen[0] + queen[1]:
            return False
    return True


solveNquens()
for i in solution:
    print(i)
