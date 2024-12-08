def process_input(filepath):
    with open(filepath) as f:
        return [list(s) for s in f.read().splitlines()]

def count_horizontal(arr, i):
    word = ['X', 'M', 'A', 'S']
    res = []
    for j in range(len(arr[i])):
        if j - 3 >= 0:
            res.append(arr[i][j - 3 : j + 1] == word[::-1])
        if j + 4 <= len(arr[i]):
            res.append(arr[i][j: j + 4] == word)
        else:
            res.append(False)
    return sum(res)

def count_vertical(arr, j):
    return count_horizontal(list(map(list, zip(*arr))), j)

def count_diagonal(arr):
    word = ['X', 'M', 'A', 'S']
    res = []
    m, n = len(arr), len(arr[0])
    for i in range(m):
        for j in range(n):
            if j - 3 >= 0 and i - 3 >= 0:
                check = [arr[i][j], arr[i - 1][j - 1], arr[i - 2][j - 2], arr[i - 3][j - 3]]
                res.append(check == word)
            if j + 3 < n and i + 3 < m:
                check = [arr[i][j], arr[i + 1][j + 1], arr[i + 2][j + 2], arr[i + 3][j + 3]]
                res.append(check == word)
    return sum(res)

def part_two(arr):
    word = ['M', 'A', 'S']
    res = []
    m, n = len(arr), len(arr[0])
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            check_one = [arr[i - 1][j - 1], arr[i][j], arr[i + 1][j + 1]]
            check_two = [arr[i - 1][j + 1], arr[i][j], arr[i + 1][j - 1]]
            res.append((check_one == word and (check_two == word or check_two == word[::-1])) or\
                (check_two == word and (check_one == word or check_one == word[::-1])) or\
                (check_one == word[::-1] and (check_two == word or check_two == word[::-1])) or\
                (check_two == word[::-1] and (check_one == word or check_one == word[::-1])))
    return sum(res)         
            
arr = process_input('./large.txt')

print(f"Part 1: {sum([count_horizontal(arr, i) for i in range(len(arr))]) +\
    sum([count_vertical(arr, j) for j in range(len(arr[0]))]) +\
        count_diagonal(arr) +\
            count_diagonal([row[::-1] for row in arr])}")

print(f"Part 2: {part_two(arr)}")