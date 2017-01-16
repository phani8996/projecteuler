'''735481-aXXjcntdovZGtnIspGGKnTPQA0g5AraPqMAc0w2b recovery for projecter euler
gGdCmmOqp6xcUwHm
this is a correct and a elegent code.
In case of recursive use a dictionary to save time 
call function from j to i j>i since it reduces running time

output
Max no of steps occur for 837799,steps is 524

real	0m48.813s
user	0m48.616s
sys	0m0.164s'''


col={}

def collaz(n):
	if col.has_key(n):
		return col[n]
	else:
		if not(n-1):
			col[n]=1
			return 1
		elif not(n%2):
			col[n]=n/2
			return n/2
		else:
			col[n]=3*n+1
			return 3*n+1
			
steps={}
s={}

for i in range(1000001,1,-1):
	count=1
	j=collaz(i)
	while(j!=1):
		count+=1
		j=collaz(j)
	if(j==1):
		steps[i]=count
		
s = [(value, key) for key, value in steps.items()]  #changes key to value and value to key.Inversing the dictionary
print "Max no of steps occur for %d,steps is %d"% (max(s)[1],max(s)[0])
