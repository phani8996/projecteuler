###Correct code
'''output
871198282

real	0m0.022s
user	0m0.020s
sys	0m0.000s'''


fo=open("PE22.txt","r")
string=map(str,fo.read().split(","))
for i in range(0,len(string)):
	string[i]=string[i][1:len(string[i])-1]
string.sort()
chars={}
i='A'
j=65
while j<91:
	i=chr(j)
	chars[i]=j-64
	j+=1
	
#print chars
value=[]
for i in range(0,len(string)):
	sums=0
	for j in str(string[i]):
		sums+=chars[j]
	value.append(sums*(i+1))
print sum(value)
