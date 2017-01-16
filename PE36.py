###correct code
'''output
872187

real	0m1.246s
user	0m1.213s
sys	0m0.032s'''


from math import *


def is_palindrome(n):
	s=str(n)
	z=1
	for i in range(0,int(floor(len(s)/2))):
		if s[i]!=s[len(s)-1-i]:
			z=0
		else:continue
	if z:
		return True
	else:
		return False

sums=0
for i in range(1,1000001):
	if is_palindrome(i):
		if is_palindrome(bin(i)[2:]):
			sums+=i
		else:continue
	else:continue
	
print sums
