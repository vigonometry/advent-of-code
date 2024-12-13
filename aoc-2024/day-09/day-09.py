disk = []
fid, pos = 0, 0
locs, spaces = {}, [] #part 2

for i, char in enumerate(input()):
    b_len = int(char)
    if i % 2 == 0: #even numbers are files
        disk.extend([fid] * b_len)
        locs[fid] = (pos, b_len)
        fid += 1
    else: #odd numbers are free spaces
        disk.extend([-1] * b_len)
        spaces.append((pos, b_len))
    pos += b_len
        

free = [i for i, fid in enumerate(disk) if fid == -1]
p = len(disk) - 1

for idx in free:
    if p <= idx:
        break
    while disk[p] == -1:
        p -= 1
    disk[idx], disk[p] = disk[p], -1
    p -= 1

while fid > 0:
    fid -= 1
    pos, f_len = locs[fid]
    for i, (s, b_len) in enumerate(spaces):
        if s >= pos: #if space is after current position, skip
            break
        if f_len <= b_len:
            locs[fid]= (s, f_len)
            r_len = b_len - f_len #remaining length
            if not r_len:
                spaces.pop(i)
            else:
                spaces[i] = (s + f_len, r_len)
            break

print(f"Part 1: {sum([i * val for i, val in enumerate(disk) if val != -1])}")
print(f"Part 2: {sum([fid * i for fid, (pos, f_len) in locs.items() for i in range(pos, pos + f_len)])}")