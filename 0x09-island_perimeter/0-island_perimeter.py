#!/usr/bin/python3
from typing import List

""" Contains the island_perimeter function """


def island_perimeter(grid: List[List[int]]) -> int:
    """Calculates the perimeter of an island."""
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Assume the cell contributes 4 sides to the perimeter
                perimeter += 4

                # Check if there's a land cell to the right
                if j + 1 < cols and grid[i][j + 1] == 1:
                    perimeter -= 2

                # Check if there's a land cell below
                if i + 1 < rows and grid[i + 1][j] == 1:
                    perimeter -= 2

    return perimeter
