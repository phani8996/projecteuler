#correct code
'''
output:272

real    0m0.035s
user    0m0.028s
sys     0m0.004s

'''
from fractions import Fraction as frac

def calculate(val,d):
    d-=1
    if d<=0:
        return 2+frac(1,val)
    if d%3==1 or d%3==0:
        val=1+frac(1,val)
    else:
        val=2*(d/3+1)+frac(1,val)
    return calculate(val,d)

num=calculate(1,99)
numerator=str(num.numerator)
s=0
for i in numerator:
    s+=int(i)
print s