from collections import deque
grid = [[int(c) for c in l.strip()] for l in open(0)]
rows, cols = len(grid), len(grid[0])
zeros = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]

#implement bfs
#for part 1 uncomment the seen portion

def solve(r, c):
    q = deque([(r, c)])
    # seen = set()
    s = 0
    while q:
        i, j = q.popleft()
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            ni, nj = i + dx, j + dy
            if rows > ni > -1 < nj < cols and\
                grid[ni][nj] == grid[i][j] + 1:
                # (ni, nj) not in seen and\:
                        # seen.add((ni, nj))
                        if grid[ni][nj] == 9:
                            s += 1
                        else:
                            q.append((ni, nj))           
    return s

print(sum([solve(r, c) for r, c in zeros]))
                        