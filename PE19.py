###Correct code
'''output
171

real	0m0.037s
user	0m0.020s
sys	0m0.016s'''


#rem=0+year+(year/4)+month+1
m1={
    1:1,
    2:4,
    3:4,
    4:0,
    5:2,
    6:5,
    7:0,
    8:3,
    9:6,
    10:1,
    11:4,
    12:6
    }
m2={
    1:0,
    2:3,
    3:4,
    4:0,
    5:2,
    6:5,
    7:0,
    8:3,
    9:6,
    10:1,
    11:4,
    12:6
    }
count=0
i=1901
while i>=1901 and i<2000:
    year=i%100
    for month in range(1,13):
        if(i%4==0):
            rem=(year+(year/4)+m2[month])%7
            if rem==0:
                count+=1
        else:
            rem=(year+(year/4)+m1[month])%7
            if rem==0:
                count+=1
    i+=1
i=2000
for month in range(1,13):
    year=i%100
    if(i%4==0):
        rem=(6+year+(year/4)+m2[month])%7
        if rem==0:
            count+=1
    else:
        rem=(6+year+(year/4)+m1[month])%7
        if rem==0:
            count+=1
            
print count
