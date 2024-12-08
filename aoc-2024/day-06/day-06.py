import numpy as np
import time
from tqdm import tqdm

t = time.time()
with open(0) as f:
    maze = np.array([list(line) for line in f.read().splitlines()])
    m, n = len(maze), len(maze[0])
    x, y = (c[0] for c in np.where(maze == '^'))
    
    #part 1
    visited = set()
    def simulate(maze, x, y):
        dx, dy = -1, 0
        while m > x >= 0 <= y < n:
            if maze[x][y] == '#' or maze[x][y] == 'O':
                x, y = x - dx, y - dy
                dx, dy = dy, -dx
            else:
                visited.add((x, y, dx, dy))
                # maze[x][y] = 'X'
            x, y = x + dx, y + dy
            
            if (x, y, dx, dy) in visited: #cycle detection including direction
                return True
        return False
        # print('\n'.join(map(lambda s: ''.join(s), maze)))
    
    simulate(maze, x, y)
    print(f"Part 1: {len(visited)}, {round(time.time() - t, 2)}s")
    
    x, y = (c[0] for c in np.where(maze == '^'))
    #part 2
    t = time.time()
    res = 0
    for i in range(m):
        for j in tqdm(range(n)):
            visited.clear()
            if maze[i][j] == '.':
                tmp, maze[i][j] = maze[i][j], 'O'
                res += simulate(maze, x, y)
                maze[i][j] = tmp
                    
    print(f"Part 2: {res}, {round(time.time() - t, 2)}s")