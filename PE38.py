###correct code
'''output
932718654

real	0m0.065s
user	0m0.061s
sys	0m0.008s'''


def is_pandigital(p):
	q=str(p)
	for j in range(1,10):
		s=str(j)
		z=1
		if q.count(s)!=1:
			return False
	
	return True
big=0
for i in range(1,10001):
	p=1
	s=''
	for j in range(1,10):		
		p=i*j
		s=s+str(p)
		if(len(s)==9):
			if is_pandigital(int(s)):
				big=int(s)
				continue
				
print big
