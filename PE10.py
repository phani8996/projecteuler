###correct code but i need to find an elegant code.this code takes 30m59.148s to execute
###outpot:::::142913828922

from math import *

prime=[2,3,5,7]
l=[]
count=0

for i in range(10,2000000):
	if not(i%2):
		continue
	elif not(i%5):
		continue
	else:
		l.append(i)
		
#print l
for i in l:
	z=1
	for j in prime:
		if not(i%j):
			z=0
			break
	if z:
		prime.append(i)

for i in prime:
		count+=i
		
print len(l),len(prime)
print count

