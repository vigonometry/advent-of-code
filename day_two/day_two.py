from itertools import pairwise

def part2(arr):
  return any(part1(arr[:i] + arr[i + 1:]) for i in range(len(arr)))

#pairwise is faster than zip(arr, arr[1:])
def part1(arr):
  diffs = [i - j for i, j in pairwise(arr)]
  signs = [k > 0 for k in diffs]
  return (not any(signs) or all(signs)) and all(1 <= abs(k) <= 3 for k in diffs)

with open("large.txt", "r") as f:
  print(sum([part1([int(i) for i in line.split()]) for line in f]))
