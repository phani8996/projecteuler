
###function to check whether 1 to n pandigital
def is_pandigital(p,n):
	q=str(p)
	for j in range(1,n+1):
		s=str(j)
		z=1
		if q.count(s)!=1:
			return False
	
	return True


####function to return nth fibbnocci number    memoccion technique
fibs={}
def fib(n):
	if fibs.has_key(n):
		return fibs[n]
	else:
		if not((n-1)*(n-2)):
			fibs[n]=1
			return 1
		elif n%2==0:
			k=n/2
			fibs[n]=fib(k)*(2*fib(k-1)+fib(k))
			return fibs[n]
		else:
			k=(n+1)/2
			fibs[n]=fib(k-1)**2+fib(k)**2
			return fibs[n]


#####function to check whether a number prime or not
def is_prime(i):
	if i==2 or i==5:
		return True
	elif i==1:
		return False
	elif not(i%2 and i%5):
		return False
	else:
		z=1
		for j in range(2,int(i**0.5)+1):
			if not(i%j):
				z=0
				return False
				
		if z:
			return True


####return prime factors of number
fact={}
def factors(n):
	count=0
	while n%2==0:
		count+=1
		n/=2
	fact[2]=count
	p=3
	while p<=n:
		count=0
		while n%p==0:
			count+=1
			n/=p
		fact[p]=count
		p+=2
	for i in fact.keys():
		if not(fact[i]):
			del fact[i]
	return fact


####returns sum of prime divisors
def divisors_sum(j):
	factors(j)	
	product=1
	for i in fact.keys():
		product*=((i**(fact[i]+1)-1)/(i-1))
	sums=product-j
	return sums
	

####Sieve of Eratosthenes
def primes(b):
	prime=[]
	for i in range(2,b+1):
		if i==2 or i==5:
			prime.append(i)
		elif not(i%2 and i%5):
			continue
		else:
			n=i
			p=3
			count=0
			while p<n:
				while n%p==0:
					count+=1
					n/=p
				p+=2
			if not(count):
				prime.append(n)
	return prime

