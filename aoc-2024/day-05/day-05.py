from functools import cmp_to_key
from itertools import filterfalse
import re

with open(0) as f:
    orderings, sequences = map(str.splitlines, re.split(r'\s{2,}', f.read()))
    orderings = [tuple(map(int, line.split('|'))) for line in orderings]
    sequences = [list(map(int, line.strip().split(','))) for line in sequences]
    
    valid = {}
    #ideally shouldn't have cycle of length 1
    for node, nei in orderings:
        valid[(node, nei)], valid[(nei, node)] = -1, 1
    
    def is_ordered(seq):
        m = len(seq)
        return all([valid.get((seq[i], seq[j]), -1) == -1 for i in range(m) for j in range(i + 1, m)])
    
    ordered_seqs = filter(is_ordered, sequences)
    print(f"Part 1: {sum([s[len(s) // 2] for s in ordered_seqs])}")
    
    unordered_seqs = [sorted(s, key=cmp_to_key(lambda x, y: valid.get((x, y), 0))) for s in filterfalse(is_ordered, sequences)]
    print(f"Part 2: {sum([s[len(s) // 2] for s in unordered_seqs])}")
    
