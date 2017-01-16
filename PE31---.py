'''Correct code
but i need to find a better code this gives output after 11 mins

Output:73681
real	11m1.838s
user	11m1.316s
sys	0m0.096s'''

count=0
s=0
l1=[]
for a in range(0,1):
	s=0
	s+=200*a
	if not(s-200):
		count+=1
		continue
	else:
		for b in range(0,3):
			s=200*a
			s+=100*b
			if not(s-200):
				count+=1
				continue
			else:
				for c in range(0,5):
					s=200*a+100*b
					s+=50*c
					if not(s-200):
						count+=1
						continue
					else:
						for d in range(0,11):
							s=200*a+100*b+50*c
							s+=20*d
							if not(s-200):
								count+=1
								continue
							else:
								for e in range(0,21):
									s=200*a+100*b+50*c+20*d
									s+=10*e
									if not(s-200):
										count+=1
										continue
									else:
										for f in range(0,41):
											s=200*a+100*b+50*c+20*d+10*e
											s+=5*f
											if not(s-200):
												count+=1
												continue
											else:
												for g in range(0,101):
													s=200*a+100*b+50*c+20*d+10*e+5*f
													s+=2*g
													if not(s-200):
														count+=1
														continue
													else:
														for h in range(0,201):
															s=200*a+100*b+50*c+20*d+10*e+5*f+2*g
															s+=h
															if not(s-200):
																count+=1
																continue
												
print s,count
