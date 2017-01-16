###Correct code
'''output
40730

real	0m1.743s
user	0m1.728s
sys	0m0.012s'''

f={
	1:1,
	2:2,
	3:6,
	4:24,
	5:120,
	6:720,
	7:7040,
	8:40320,
	9:362880,
	0:1}


def fact_sum(n):
	s=str(n)
	count=0
	for i in s:
		j=int(i)	
		count+=f[j]
	return count
		
	
f1=[]
count2=0
i=2
while i>=2 and i<=564481:
	i+=1
	j=fact_sum(i)
	if(i==j):
		count2+=i
		f1.append(i)
		
print count2
