###Correct code
'''output
Highest palindrome formed by product of two 3-digit numbers 995,911 is 906609

real	0m0.846s
user	0m0.832s
sys	0m0.012s'''


n=3
palindrome=[]

for i in range(10**(n-1),10**(n)):
	for j in range(10**(n-1),10**(n)):
		temp=str(i*j)
		z=0
		for k in range(0,len(temp)/2):
			if(temp[k]!=temp[len(temp)-k-1]):
				z=1
				break
		if z==0:
			t=int(temp)
			palindrome.append(t)
			pal=i

print "Highest palindrome formed by product of two %d-digit numbers %d,%d is %d"% (n,pal,max(palindrome)/pal,max(palindrome))
