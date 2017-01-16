###Correct code
'''
Output
9110846700

real	0m0.024s
user	0m0.020s
sys	0m0.000s'''


sums=0
for i in range(1,1001):
	sums+=i**i
	
print str(sums)[len(str(sums))-10:]
