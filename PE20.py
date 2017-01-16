###correct code
'''648

real	0m0.035s
user	0m0.028s
sys	0m0.004s'''


def fact(n):

    if n==0 or n==1:

        return 1

    else:

        return n*fact(n-1)


f=str(fact(100))

num=0


for i in range(0,len(f)):

    num+=int(f[i])
    


print num
