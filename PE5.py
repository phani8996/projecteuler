###Correct code
'''output
232792560

real	0m0.029s
user	0m0.020s
sys	0m0.008s'''


n=20L

def gcd(a,b):
	if(a>=b):
		if(a%b==0):
			return b
		else:
			return gcd(b,a%b)
	else:
		return gcd(b,a)
		
def lcm(a,b):
	return a*b/gcd(a,b)


a=1L
b=1L
for i in range(1,n+1):
	a=lcm(i,b)
	b=a

print a
