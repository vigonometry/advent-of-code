from collections import deque

stones = [int(x) for x in input().split(' ')]
cache = {}

def count(stone, iters):
    if iters == 0: #no more evolutions
        return 1
    if (stone, iters) in cache:
        return cache[(stone, iters)]
    
    if stone == 0: # 0 -> 1
        cache[(stone, iters)] = count(1, iters - 1)
        return cache[(stone, iters)]
    s = str(stone)
    l = len(s)
    if l % 2 == 0: #even length stone split in 2
        ls, rs = int(s[:l//2]), int(s[l//2:])
        cache[(stone, iters)] = count(ls, iters - 1) + count(rs, iters - 1)
        return cache[(stone, iters)]
    
    cache[(stone, iters)] = count(2024 * stone, iters - 1) #muiltiply by 2024
    return cache[(stone, iters)]

#cache from functools which memoizes the results for us once invoked (https://www.youtube.com/watch?v=layyhtQQuM0&ab_channel=HyperNeutrino)

print(f"Part 1: {sum([count(stone, 25) for stone in stones])}")
print(f"Part 2: {sum([count(stone, 75) for stone in stones])}")
