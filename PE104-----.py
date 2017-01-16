###correct bot not at all elegentits a mere guess of limits
"""output
329468

real	0m52.785s
user	0m52.597s
sys	0m0.052s"""



from sys import *
setrecursionlimit(1000000)

def is_pandigital(p):
	q=str(p)
	for j in range(1,10):
		s=str(j)
		z=1
		if q.count(s)!=1:
			return False
	
	return True

fibs={}
def fib(n):
	if fibs.has_key(n):
		return fibs[n]
	else:
		if not((n-1)*(n-2)):
			fibs[n]=1
			return 1
		elif n%2==0:
			k=n/2
			fibs[n]=fib(k)*(2*fib(k-1)+fib(k))
			return fibs[n]
		else:
			k=(n+1)/2
			fibs[n]=fib(k-1)**2+fib(k)**2
			return fibs[n]


			
for i in range(330001,0,-1):
	j=fib(i)
	s=str(j)
	p=s[:9]
	q=s[len(s)-9:]
	print i
	if is_pandigital(p) and is_pandigital(q):
		print j,i,len(s)
		break
