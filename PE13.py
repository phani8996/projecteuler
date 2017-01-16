###Correct code
'''Output:
5537376230

real	0m0.017s
user	0m0.008s
sys	0m0.008s'''


f0=open("PE13.txt","r+")
count=0
num={}
for i in range(1,101):
	num[i]=f0.read(51)
	count+=int(num[i])

s=str(count)
print s[:10]
