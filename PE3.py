###Correct code
'''output
Highest prime factor is  6857

real	0m0.030s
user	0m0.028s
sys	0m0.000s'''
#Better Code in short

n=600851475143

i = 2
while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1
print "Highest prime factor is ",n
