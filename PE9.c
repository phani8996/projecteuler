/*****************************************************
correct code
output
a,b,c are 200,375,425 and product is 31875000

real	0m0.004s
user	0m0.004s
sys	0m0.000s
******************************************************/


#include<stdio.h>

void main(){
	int a,b;
	for(b=1;b<=1000 && b>0;b++){
	for(a=1;a<=1000 && a<b && a>0;a++){
		int x=1000-a-b;
		int y=(a*a)+(b*b);
		int w=x*x;
		if(x>0 && b<x && a<x){
	//			printf("a is %d\tb is %d\tc is %d\t\t",a,b,x);
		//		printf("c^2 is %d\ta^2+b^2 is %d\n",w,y);
			if(y==w){
				int z=x*a*b;	
				printf("a,b,c are %d,%d,%d and product is %d\n",a,b,x,z);
		}
		}
	}
	}
}
