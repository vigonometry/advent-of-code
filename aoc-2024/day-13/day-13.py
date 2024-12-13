import re
chunks = [*open(0).read().split("\n\n")]
def solve(p):
    total = 0
    for chunk in chunks:
        ax, ay, bx, by, px, py = list(map(int, re.findall(r'\d+', chunk)))
        px, py = px + p * 10**13, py + p * 10 ** 13
        if ax * by == ay * bx: #2 x 2 matrix determinant denom
            print("non-invertible")
            break
        ca = (by * px - bx * py) / (ax * by - ay * bx)
        cb = (-ay * px + ax * py) / (ax * by - ay * bx)
        if ca % 1 == 0 and cb % 1 == 0:
            total += int(3 * ca + cb)
    return total
print(f"Part 1: {solve(0)}, Part 2: {solve(1)}")

