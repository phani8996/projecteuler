#correct code
'''
output:153

real    1m23.007s
user    1m22.928s
sys     0m0.068s

'''
from fractions import Fraction as frac
from sys import setrecursionlimit as limit
limit(10000)
def calculate(val,d):
    d-=1
    if d<=0:
        return 1+frac(1,val)
    val=2+frac(1,val)
    return calculate(val,d)

count=0
for i in range(1,1000):
    number=calculate(2,i)
    if len(str(number.numerator))>len(str(number.denominator)):
        count+=1
print count