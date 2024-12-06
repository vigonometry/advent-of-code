import re
with open('./large.txt') as f:
    inputs = ('do()' + f.read().strip()).split("don't()")
    #str.find() returns -1 if do() is not found in the string, allows us to slice the string as well
    soln = lambda pt: sum([int(i) * int(j) for l in inputs 
                           for i, j in re.findall(r'mul\((\d+),(\d+)\)', l[l.find('do()') * pt:])])
    print(f"Part 1: {soln(0)}")
    print(f"Part 2: {soln(1)}")
