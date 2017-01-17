#correct code
'''
output:26241

real    0m4.817s
user    0m4.812s
sys     0m0.000s
'''

def isprime(n):
    n=int(n)
    if n==2:
        return True
    if n>2:
        if n%2==0:
            return False
        nrange=range(3,int(n**0.5+1),2)
        for i in nrange:
            if not(n%i):
                return False
    else:
        return False
    return True

if __name__=='__main__':
    N=100000
    nrange=range(1,N)
    pcount=0
    for i in nrange:
        p=2*i+1
        num=p*p-p+1
        for j in range(0,3):
            if isprime(num):
                pcount+=1
            num-=(p-1)
        length=4*i+1.0
        if pcount/length < 0.1:
            print p
            break