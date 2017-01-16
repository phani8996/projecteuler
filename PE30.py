###correct code
'''output[4150, 4151, 54748, 92727, 93084, 194979]
443839

real	0m1.051s
user	0m1.048s
sys	0m0.000s'''


def sum_num(n):
	s=str(n)
	count=0
	for i in range(0,len(s)):
		count+=(int(s[i])**5)
	return count
	
num=[]
count2=0
for i in range(2,295246):
	count=sum_num(i)
	if count==i:
		num.append(i)
		count2+=i
		
print num
print count2

