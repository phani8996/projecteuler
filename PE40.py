###Correct code
'''
Output::
210

real	0m0.076s
user	0m0.068s
sys	0m0.004s'''


s=''
for i in range(1,200000):
	s+=str(i)
product=1
for i in range(1,7):
	product*=int(s[10**i-1])
	
print product	
#print s,len(s)
