import time
from collections import deque
from multiprocessing import Pool
from functools import partial

def solve(line, part):
    target, nums = line.split(': ')
    target = int(target)
    
    nums = list(map(int, nums.split()))
    q = deque([(nums[0], 1)])
    while len(q) > 0:
        val, idx = q.popleft()
        if idx == len(nums):
            if val == target:
                return target
            continue
        q.append((val + nums[idx], idx + 1))
        q.append((val * nums[idx], idx + 1))
        if part:
            q.append((int(f'{val}{nums[idx]}'), idx + 1))
    
    return 0
    
if __name__ == "__main__":   
    f = [*open(0)]  
    with Pool() as pool:
        t = time.time()
        print(f"Part 1: {sum(pool.map(partial(solve, part=0), f))}, {round((time.time() - t) * 1000)}ms")
        t = time.time()
        print(f"Part 2: {sum(pool.map(partial(solve, part=1), f))}, {round((time.time() - t) * 1000)}ms")
    pool.close()