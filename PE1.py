###Correct code
'''output
sum is 233168

real	0m0.064s
user	0m0.028s
sys	0m0.000s'''


count=0
for i in range(1000):
	if(i%3==0 or i%5==0):
		count+=i
print "sum is %d" % count
