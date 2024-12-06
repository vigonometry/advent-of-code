import re
from collections import Counter

def process_inputs(filepath):
    with open(filepath) as f:
        return list(map(lambda lst: sorted(lst),
            zip(*map(lambda ln: map(int, re.split(r'\s+', ln.strip())), f.read().splitlines()))))
       
def solve_part_one(filepath):
    return sum(map(lambda x: abs(x[1] - x[0]), zip(*process_inputs(filepath))))

def solve_part_two(filepath):
    lhs, rhs = process_inputs(filepath)
    cr = Counter(rhs)
    return sum(map(lambda e: e * cr.get(e, 0), lhs))

print(f"Part 1: {solve_part_one('./large.txt')}")
print(f"Part 2: {solve_part_two('./large.txt')}")