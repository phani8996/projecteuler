###Correct code
'''output
137846528820

real	0m0.034s
user	0m0.024s
sys	0m0.008s'''

def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)

print fact(40)/(fact(20)**2)#fact(2n)/(fact(n)*fact(n))
