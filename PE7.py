###Correct code
'''output
104743

real	0m7.128s
user	0m7.028s
sys	0m0.096s'''


from math import *

prime=[2,3,5,7]
l=[]
#n=int(raw_input("Enter n"))
for i in range(10,10**7):
	if not(i%2):
		continue
	elif not(i%5):
		continue
	else:
		l.append(i)
		
#print l
for i in l:
	if len(prime)==10001:
		break
	z=1
	for j in prime:
		if not(i%j):
			z=0
			break
	if z:
		prime.append(i)
		
print len(prime)
print prime[10000]

