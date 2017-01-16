'''correct code
better convert number to string and treat as array of characters
now add each elemnt of array to count to get sum of digits
dont forget to convers str bavk ti int

output
1366

real	0m0.032s
user	0m0.024s
sys	0m0.008s'''


j=2**1000
string=str(j)
count=0

for i in range(0,len(string)):
	count+=int(string[i])
	
print count
