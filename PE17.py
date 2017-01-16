###correct code
'''output
21124

real	0m0.012s
user	0m0.012s
sys	0m0.000s'''

count={}
def counting(t):
	s=str(t)
	count['1']=3
	count['2']=3
	count['3']=5
	count['4']=4
	count['5']=4
	count['6']=3
	count['7']=5
	count['8']=5
	count['9']=4
	count['11']=6
	count['12']=6
	count['13']=8
	count['14']=8
	count['15']=7
	count['16']=7
	count['17']=8
	count['18']=9
	count['19']=8
	count['10']=3
	count['20']=6
	count['30']=6
	count['40']=5
	count['50']=5
	count['60']=5
	count['70']=7
	count['80']=6
	count['90']=6
	if len(s)==2:
		if count.has_key(s):
			return count[s]
		else:
			count[s]=count[str(int(s[0])*10)]+count[s[1]]
	elif len(s)==3:
		p=s[1:]
		if count.has_key(p):
			count[s]=count[p]+count[s[0]]+10
		elif p=='00':
			count[s]=count[s[0]]+7
		elif s[1]=='0':
			count[s]=count[s[2]]+count[s[0]]+10
		else:
			count[s]=count[str(int(s[1])*10)]+count[s[2]]+count[s[0]]+10
	elif len(s)==4:
		count[s]=11
	return count[s]

counts=0
for i in range(1,1001):
	counts+=counting(i)
	
print counts
