###Correct code
'''
Output:
2783915460

real	0m1.373s
user	0m1.324s
sys	0m0.044s'''

from itertools import permutations
p = [''.join(i) for i in permutations('0123456789')]
p.sort()
print p[1000000-1]
