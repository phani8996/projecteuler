###Correct code
'''
Output::
7652413

real	9m56.835s
user	9m55.732s
sys	0m0.636s'''


from func1 import *
from itertools import permutations
number=''
max_prime=[]
pan={}
for x in range(1,10):
	number+=str(x)
	p = [''.join(l) for l in permutations(number)]
	for i in p:
		pan[i]=is_prime(int(i))
	#print len(pan),len(p)	
	for i in pan.keys():
		if not(pan[i]):
			del pan[i]
			p.remove(i)
	if len(p):
		max_prime.append(max(p))
		
print max(max_prime)
