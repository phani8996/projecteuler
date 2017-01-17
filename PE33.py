#correct code
'''
output:100

real    0m0.025s
user    0m0.028s
sys     0m0.000s

'''
from fractions import Fraction as frac
f=1
for c in range(1,10):
    for a in range(1,c):
        b=(9*a*c)/float(10*a-c)
        if b-int(b)==0 and b<10 and a!=int(b):
            b=int(b)
            f*=frac(a,c)

print f.denominator