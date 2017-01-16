###Correct code
'''output
Sum of all even valued fib numbers is 4613732

real	0m3.695s
user	0m3.692s
sys	0m0.000s'''

def fib(n):
	if n==0:
		return 1;
	elif n==1:
		return 1;
	else:
		return fib(n-1)+fib(n-2)
count=0
for i in range(100):
	a=fib(i)
	if(a>4000000):
		break
	if(a%2==0):
		count+=a
print "Sum of all even valued fib numbers is %d" % count
