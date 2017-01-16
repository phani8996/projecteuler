###Correct code
'''output:::
8739992577

real	0m0.227s
user	0m0.220s
sys	0m0.004s'''

p=2**30
i=1

for k in range(1,1+7830457/30):
	i=i*p
	i=int(str(i)[-10:])
i=i*(2**7)
i=int(str(i)[-10:])
i=i*28433
i+=1
i=int(str(i)[-10:])
print i
