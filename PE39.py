###correct code
'''Output
840

real	0m52.301s
user	0m52.245s
sys	0m0.000s'''



big=0
for p in range(1,1001):
	count=0
	for a in range(1,p):
		for b in range(a,p):
			c=p-a-b
			d=(a*a)+(b*b)
			e=c*c
			if(e==d):
				count+=1
	if count>=big:
		big=count
		t=p
		
print t
