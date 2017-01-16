###Correct code
'''
Output::
162

real	0m0.022s
user	0m0.020s
sys	0m0.000s'''


fo=open("PE42.txt","r")
string=map(str,fo.read().split(","))
for i in range(0,len(string)):
	string[i]=string[i][1:len(string[i])-1]
string.sort()
j=65
chars={}
while j<91:
	i=chr(j)
	chars[i]=j-64
	j+=1
	
tri=[]
for i in range(1,26):
	tri.append(i*(i+1)/2)
count=0
for i in range(0,len(string)):
	sums=0
	for j in str(string[i]):
		sums+=chars[j]
	if sums in tri:
		count+=1
	
print count
