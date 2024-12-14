import re

WIDTH, HEIGHT = 101, 103 #11, 7 for sample input
velocities = {}
bot_id = 0

#max_bots, min_iter, max_grid = -1, -1, None
min_pdt, min_iter, max_grid = (WIDTH * HEIGHT) ** 4, -1, None

for l in open(0).read().splitlines():
    x, y, dx, dy = list(map(int, re.findall(r'-*\d+', l)))
    velocities[bot_id] = (x, y, dx, dy)
    bot_id += 1

for i in range(1, WIDTH * HEIGHT + 1):
    grid = [['.' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    
    q1, q2, q3, q4 = 0, 0, 0, 0
    for bot_id in velocities:
        x, y, dx, dy = velocities[bot_id]
        x, y = x + dx, y + dy
        x = WIDTH + x if x < 0 else x - WIDTH if x >= WIDTH  else x
        y = HEIGHT + y if y < 0 else y - HEIGHT if y >= HEIGHT else y
        velocities[bot_id] = (x, y, dx, dy)
        grid[y][x] = '#'
        
        if x > WIDTH // 2 and y < HEIGHT // 2:
            q1 += 1
        elif x > WIDTH // 2 and y > HEIGHT // 2: 
            q2 += 1
        elif x < WIDTH // 2 and y > HEIGHT // 2:
            q3 += 1
        elif x < WIDTH // 2 and y < HEIGHT // 2:
            q4 += 1
    score = q1 * q2 * q3 * q4
    if i == 100:
        print(f"Part 1: {score}")
    #if max(q1, q2, q3, q4) > max_bots:
    #    max_bots, min_iter, max_grid = max(q1, q2, q3, q4), i, grid
    if score < min_pdt:
        min_pdt, min_iter, max_grid = score, i, grid
                
print(f"Part 2: {min_iter}")