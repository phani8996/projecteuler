###Correct code
'''Output::
4075

real	0m0.016s
user	0m0.012s
sys	0m0.004s'''


from func1 import *

def comb(n,r):
	return factorial(n)/(factorial(r)*factorial(n-r))
	
count=0
for n in range(22,101):
	for r in range(3,n-3):
		if comb(n,r)>=1000000:
			count+=1
			
print count
