from collections import defaultdict
from itertools import combinations
from math import gcd

grid = open(0).read().splitlines()

def solve(part):
    char_dict = defaultdict(list)
    m, n = len(grid), len(grid[0])
    for x in range(m):
        for y in range(n):
            c = grid[x][y]
            if c != '.':
                char_dict[c].append((x, y))

    antinodes = set()
    #manhattan distance = (x2 - x1) + (y2 - y1)
    #x1 - (x2 - x1) = 2x1 - x2, x2 + (x2 - x1) = 2x2 - x1 (same for y)
    for pts in char_dict.values():
        pairs = combinations(pts, 2)
        for (x1, y1), (x2, y2) in pairs:
            dx, dy = x2 - x1, y2 - y1
            if not part:
                nx, ny = x1 - dx, y1 - dy
                mx, my = x2 + dx, y2 + dy
                if m > nx > -1 < ny < n:
                    antinodes.add((nx, ny))
                if m > mx > -1 < my < n:
                    antinodes.add((mx, my))
            if part:
                #the antennas can also be considered antinodes
                #dx, dy are divided by gcd to find minimum step length in each dir
                div = gcd(dx, dy)
                dx, dy = dx // div, dy // div
                x, y = x1, y1
                while m > x >= 0 <= y < n:
                    antinodes.add((x, y))
                    x -= dx
                    y -= dy
                x, y = x1, y1
                while m > x >= 0 <= y < n:
                    antinodes.add((x, y))
                    x += dx
                    y += dy
    return len(antinodes)

print(f"Part 1: {solve(0)}")
print(f"Part 2: {solve(1)}")