import time
from collections import deque
# from math import floor, log10

f = [*open(0)]
def soln(part):
        res = 0
        for line in f:
            
            target, nums = line.split(': ')
            target = int(target)
            
            nums = list(map(int, nums.split()))
            q = deque([(nums[0], 1)])
            while len(q) > 0:
                val, idx = q.popleft()
                if idx == len(nums):
                    if val == target:
                        res += target
                        break
                    continue
                q.append((val + nums[idx], idx + 1))
                q.append((val * nums[idx], idx + 1))
                if part:
                    # q.append((val * 10**(1 + floor(log10(nums[idx]))) + nums[idx], idx + 1))
                    q.append((int(f'{val}{nums[idx]}'), idx + 1))
        return res

t = time.time()
print(f"Part 1: {soln(0)}, {round(time.time() - t, 3) * 1000}ms")
t = time.time()
print(f"Part 2: {soln(1)}, {round(time.time() - t, 3) * 1000}ms")
        
                
                
