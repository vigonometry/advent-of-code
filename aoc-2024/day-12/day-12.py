from collections import deque
grid = [list(l) for l in open(0).read().splitlines()]
rows, cols = len(grid), len(grid[0])
plots, seen = [], set()

#flood fill
for r in range(rows):
    for c in range(cols):
        if (r, c) in seen:
            continue
        seen.add((r, c))
        plot = {(r, c)}
        q = deque([(r, c)])
        while q:
            i, j = q.popleft()
            for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                nr, nc = i + dx, j + dy
                if rows > nr > -1 < nc < cols and\
                    (nr, nc) not in seen:
                        if grid[nr][nc] == grid[r][c]:
                            seen.add((nr, nc))
                            plot.add((nr, nc))
                            q.append((nr, nc))
        plots.append(plot)

#each region can be composed of unit length squares
def perimeter(plot):
    res = 0
    for i, j in plot:
        res += 4
        for dx, dy in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            if (i + dx, j + dy) in plot: #crop is planted -> no fence there
                res -= 1
    return res

                
print(f"Part 1: {sum([len(plot) * perimeter(plot) for plot in plots])}")