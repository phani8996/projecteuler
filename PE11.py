#correct code
'''
output 70600674

real	0m0.041s
user	0m0.024s
sys	0m0.000s
'''

if __name__=='__main__':
    f1=open('PE11.txt','r')
    data=f1.read().splitlines()
    lines=[]
    for line in data:
        lines.append(map(int,line.split()))
    r,c=len(lines),len(lines[0])
    maxp=1
    rrange=range(0,r)
    crange=range(0,c)
    for i in rrange:
        for j in crange:
            p3=1
            if i>r-4:
                p1=0
                p3=0
            else:
                p1=lines[i][j]*lines[i+1][j]*lines[i+2][j]*lines[i+3][j]
            if j>c-4:
                p2=0
                p3=0
            else:
                p2=lines[i][j]*lines[i][j+1]*lines[i][j+2]*lines[i][j+3]
            if p3:
                p3=lines[i][j]*lines[i+1][j+1]*lines[i+2][j+2]*lines[i+3][j+3]
            if i<4 or j>c-4:
                p4=0
            else:
                p3 = lines[i][j] * lines[i - 1][j + 1] * lines[i - 2][j + 2] * lines[i - 3][j + 3]
            maxp=max(maxp,p1,p2,p3)
    print maxp




