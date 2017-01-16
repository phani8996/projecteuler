###correct code
'''output
9183

real	0m0.694s
user	0m0.689s
sys	0m0.004s'''


num=[]

for a in range(2,101):
	for b in range(2,101):
		i=a**b
		if i not in num:
			num.append(i)
		else:
			continue
		
		
print len(num)
