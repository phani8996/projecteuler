###Correct
'''output
31626

real	0m2.087s
user	0m2.077s
sys	0m0.008s'''

ambi=[]
fact={}
sums={}
def factors(n):
	count=0
	while n%2==0:
		count+=1
		n/=2
	fact[2]=count
	p=3
	while p<=n:
		count=0
		while n%p==0:
			count+=1
			n/=p
		fact[p]=count
		p+=2

for j in range(1,10001):
	factors(j)	
	product=1
	for i in fact.keys():
		product*=((i**(fact[i]+1)-1)/(i-1))
	fact={}
	sums[j]=product-j
	
for j in sums.keys():
	if sums.has_key(j):
		if sums.has_key(sums[j]):
			k=sums[j]
			if j==sums[k]:
				ambi.append(j)
				ambi.append(k)
				del sums[sums[j]]
				
			else:
				continue
		else:continue
	else:continue	
rep=[]
for i in ambi:
	if ambi.count(i)>1:
		ambi.remove(i)
		rep.append(i)
		
for i in rep:
	ambi.remove(i)
	
sum1=0
for j in ambi:
	sum1+=j

print sum1
