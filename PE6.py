###Correct code
'''output
25164150

real	0m0.033s
user	0m0.028s
sys	0m0.004s'''


s1=0
s2=0
for i in range(0,101):
	s1+=(i**2)
for i in range(0,101):
	s2+=i
	
print (s2**2)-s1
